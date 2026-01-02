bl_info = {
    "name": "Sync Framing Toggle",
    "author": "Jerome Kim",
    "version": (1, 0, 0),
    "blender": (4, 5, 0),
    "location": "Outliner > Filter",
    "description": "Toggle Sync Framing between Viewport and Outliner",
    "category": "Interface",
}

import bpy


# ----------------------------------------------------
#   Property
# ----------------------------------------------------

def register_props():
    bpy.types.Scene.sync_framing_enabled = bpy.props.BoolProperty(
        name="Sync Framing",
        description="Sync viewport framing and Outliner locate",
        default=True,
    )

    # Defer initialization until a file exists
    bpy.app.handlers.load_post.append(init_sync_framing)


def init_sync_framing(dummy):
    for scene in bpy.data.scenes:
        scene.sync_framing_enabled = True


def unregister_props():
    del bpy.types.Scene.sync_framing_enabled


# ----------------------------------------------------
#   Inject into Filter Popover
# ----------------------------------------------------

def draw_sync_filter(self, context):
    layout = self.layout
    layout.separator()
    layout.prop(context.scene, "sync_framing_enabled", text="Sync Framing")


# ----------------------------------------------------
#   Operators
# ----------------------------------------------------

class VIEW3D_OT_sync_locate(bpy.types.Operator):
    bl_idname = "view3d.sync_locate"
    bl_label = "Sync Framing"

    def execute(self, context):
        obj = context.active_object
        if not obj:
            return {'CANCELLED'}

        for window in context.window_manager.windows:
            for area in window.screen.areas:
                if area.type == 'VIEW_3D':
                    for region in area.regions:
                        if region.type == 'WINDOW':
                            with context.temp_override(window=window, area=area, region=region):
                                bpy.ops.view3d.view_selected()

        for window in context.window_manager.windows:
            for area in window.screen.areas:
                if area.type == 'OUTLINER':
                    for region in area.regions:
                        if region.type == 'WINDOW':
                            with context.temp_override(window=window, area=area, region=region):
                                bpy.ops.outliner.show_active()

        return {'FINISHED'}


class VIEW3D_OT_smart_frame(bpy.types.Operator):
    bl_idname = "view3d.smart_frame"
    bl_label = "Smart Frame"

    def execute(self, context):
        if context.scene.sync_framing_enabled:
            bpy.ops.view3d.sync_locate()
        else:
            bpy.ops.view3d.view_selected()
        return {'FINISHED'}


# ----------------------------------------------------
#   Keymap
# ----------------------------------------------------

addon_keymaps = []

def register():
    register_props()

    bpy.utils.register_class(VIEW3D_OT_sync_locate)
    bpy.utils.register_class(VIEW3D_OT_smart_frame)

    # Hook into Outliner Filter popover
    bpy.types.OUTLINER_PT_filter.append(draw_sync_filter)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new("view3d.smart_frame", 'NUMPAD_PERIOD', 'PRESS')
        addon_keymaps.append((km, kmi))


def unregister():
    # Remove keymaps
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    # Remove Outliner filter UI
    bpy.types.OUTLINER_PT_filter.remove(draw_sync_filter)

    # Remove load handler
    if init_sync_framing in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(init_sync_framing)

    # Unregister operators
    bpy.utils.unregister_class(VIEW3D_OT_sync_locate)
    bpy.utils.unregister_class(VIEW3D_OT_smart_frame)

    unregister_props()



if __name__ == "__main__":
    register()
