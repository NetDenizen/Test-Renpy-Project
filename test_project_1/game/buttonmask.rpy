init python:
    import pygame
    class ButtonMaskStorage:
        def __init__(self, actions):
            self.ActiveMasks = []
            self.ActiveHovers = {}
            self.ActiveSelecteds = {}
            self.actions = actions
            self.DownColor = None
            self.CurrentColor = None
            self.XPos = None
            self.YPos = None
            self.LastHoverState = None
            self.RedrawNeeded = True
        def _ReplaceActive(self, active, color, old, new):
            if color not in active:
                return
            try:
                idx = active[color].index(old)
            except IndexError:
                return
            active[color][idx] = new
        def _AddActive(self, active, color, name):
            if color in active:
                active[color].append(name)
            else:
                active[color] = [name,]
        def _RemoveActive(self, active, color, name):
            if color in active:
                active[color].remove(name)
        def _SetActive(self, active, color, index, item):
            if color in active:
                active[color][index] = item
        def AddHover(self, color, name):
            self._AddActive(self.ActiveHovers, color, name)
        def AddSelected(self, color, name):
            self._AddActive(self.ActiveSelecteds, color, name)
        def RemoveHover(self, color, name):
            self._RemoveActive(self.ActiveHovers, color, name)
        def RemoveSelected(self, color, name):
            self._RemoveActive(self.ActiveSelecteds, color, name)
        def ReplaceHover(self, color, old, new):
            self._ReplaceActive(self.ActiveHovers, color, old, new)
        def ReplaceSelected(self, color, old, new):
            self._ReplaceSelected(self.ActiveSelecteds, color, old, new)
        def SetHover(self, color, index, item):
            self._SetActive(self.ActiveHovers, color, index, item)
        def SetSelecteds(self, color, index, item):
            self._SetActive(self.ActiveSelecteds, color, index, item)
        def AddMask(self, name):
            self.ActiveMasks.append(name)
        def RemoveMask(self, name):
            self.ActiveMasks.remove(name)
        def ReplaceMask(self, old, new):
            try:
                self.ActiveMasks[self.ActiveMasks.index(old)] = new
            except IndexError:
                return
        def SetMask(self, index, item):
            self.ActiveMasks[index] = item
        def OnButtonUp(self):
            if self.DownColor is None:
                return
            FoundAction = self.actions.get(self.DownColor, None)
            if FoundAction is not None:
                renpy.jump(FoundAction)
        def OnButtonDown(self):
            self.DownColor = self.CurrentColor
        def IsSelected(self):
            return self.ActiveSelecteds.get(self.DownColor, None)
        def IsHovered(self):
            return self.ActiveHovers.get(self.CurrentColor, None)
    class ButtonMask(renpy.Displayable):
        def __init__(self, storage, **kwargs):
            super(ButtonMask, self).__init__(**kwargs)
            self.storage = storage
        def _GetColorAt(self):
            for m in self.storage.ActiveMasks:
                if m is None:
                    continue
                try:
                    c = Color( tuple( renpy.load_surface(m).get_at( (self.storage.XPos, self.storage.YPos) ) ) )
                except IndexError:
                    break
                if c.alpha != 0.0:
                    return c.rgb
            return (0, 0, 0)
        def SetPos(self, x, y):
            self.storage.XPos = x
            self.storage.YPos = y
            self.storage.CurrentColor = self._GetColorAt()
            if self.storage.CurrentColor != self.storage.DownColor:
                self.storage.DownColor = None
            NewHoverState = self.storage.IsHovered()
            if NewHoverState != self.storage.LastHoverState:
                self.storage.RedrawNeeded = True
            self.storage.LastHoverState = NewHoverState
        def _BlitRenders(self, output, renders):
            for r in renders:
                if r is None:
                    continue
                output.blit( renpy.load_image(r), (0, 0) )
        def render(self, width, height, st, at):
            output = renpy.Render(width, height)
            candidate = self.storage.IsSelected()
            if candidate is not None:
                self._BlitRenders(output, candidate)
                return output
            candidate = self.storage.IsHovered()
            if candidate is not None:
                self._BlitRenders(output, candidate)
            return output
        def event(self, ev, x, y, st):
            self.SetPos(x, y)
            if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                self.storage.OnButtonUp()
            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.storage.OnButtonDown()
            if self.storage.RedrawNeeded:
                if self.storage.IsSelected() is not None:
                    self.set_transform_event("selected_hover")
                elif self.storage.IsHovered() is not None:
                    self.set_transform_event("hover")
                else:
                    self.set_transform_event("idle")
                renpy.redraw(self, 0)
                self.storage.RedrawNeeded = False
            return None
        def visit(self):
            return []

screen ButtonMaskBlocker:
    key "mouseup_1" action Return()
    key "K_RETURN" action Return()
    key "K_SPACE" action Return()
    key "K_KP_ENTER" action Return()
    key "joy_dismiss" action Return()
