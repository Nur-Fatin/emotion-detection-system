"""
Package initializer for the emotion detection module.

This module imports and exposes the 'emotion_detection' submodule
to make it accessible when the package is imported.

__all__ defines the public interface of this package,
indicating that 'emotion_detection' is part of the package's API.
"""

from . import emotion_detection

__all__ = ["emotion_detection"]

# from emotion_detection import emotion_detector
