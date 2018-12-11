init python:
    import pygame
    class ButtonMask(renpy.Displayable):
        def __init__(self, mask, actions, **kwargs):
            super(ButtonMask, self).__init__(**kwargs)
            self.child = renpy.display.layout.Null()
            self.actions = actions
            self.mask = renpy.load_surface(mask)
        def render(self, width, height, st, at):
            return self.child.render(width, height, st, at)
        def event(self, ev, x, y, st):
            if ev.type != pygame.MOUSEBUTTONUP or ev.button != 1:
                return None
            ColorAt = Color( tuple( self.mask.get_at( (x, y) ) ) ).rgb
            FoundAction = self.actions.get(ColorAt, None)
            if FoundAction is not None:
                FoundAction()
            return None
        def visit(self):
            return []

screen ButtonMaskBlocker:
    key "mouseup_1" action Return()
    key "K_RETURN" action Return()
    key "K_SPACE" action Return()
    key "K_KP_ENTER" action Return()
    key "joy_dismiss" action Return()
