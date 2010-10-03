cdef class GLDraw:

    cdef bint did_init
    cdef object environ
    cdef object rtt
    cdef object window
    cdef tuple virtual_size
    cdef public tuple physical_size
    cdef tuple virtual_box
    cdef tuple physical_box
    cdef object mouse_old_visible
    cdef object mouse_info
    cdef object texture_cache
    cdef double last_redraw_time
    cdef public dict info
    cdef object old_fullscreen
    cdef object fullscreen_surface
    cdef object display_info
    cdef double upscale_factor
    cdef tuple clip_cache

    cpdef set_clip(self, clip)
    cpdef draw_transformed(self, object what, tuple clip, double xo, double yo, double alpha, forward, reverse)