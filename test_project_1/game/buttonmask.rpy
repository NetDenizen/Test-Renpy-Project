init python:
    import pygame
    class ButtonMask(renpy.Displayable):
        def __init__(self, mask, actions, **kwargs):
            super(ButtonMask, self).__init__(**kwargs)
            self.child = renpy.display.layout.Null()
            self.actions = actions
            self.mask = renpy.load_surface(mask)
            self.DownColor = None
        def render(self, width, height, st, at):
            return self.child.render(width, height, st, at)
        def _GetColorAt(self, x, y):
            return Color( tuple( self.mask.get_at( (x, y) ) ) ).rgb
        def _OnButtonUp(self, x, y):
            if self.DownColor is None:
                return
            ColorAt = self._GetColorAt(x, y)
            DownColor = self.DownColor
            self.DownColor = None
            if DownColor != ColorAt:
                return
            FoundAction = self.actions.get(ColorAt, None)
            if FoundAction is not None:
                FoundAction()
        def _OnButtonDown(self, x, y):
            self.DownColor = self._GetColorAt(x, y)
        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                self._OnButtonUp(x, y)
            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self._OnButtonDown(x, y)
            return None
        def visit(self):
            return []

screen ButtonMaskBlocker:
    key "mouseup_1" action Return()
    key "K_RETURN" action Return()
    key "K_SPACE" action Return()
    key "K_KP_ENTER" action Return()
    key "joy_dismiss" action Return()
