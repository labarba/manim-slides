# flake8: noqa: F401
from .__version__ import __version__
from .slide import Slide, ThreeDSlide
from .manim import MANIM


if MANIM:
    try:
        from IPython import get_ipython
    
        from .ipython_magic import ManimSlidesMagic
    except ImportError:
        pass
    else:
        ipy = get_ipython()
        if ipy is not None:
            ipy.register_magics(ManimSlidesMagic)
