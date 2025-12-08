"""ByteTrack Implementation"""

class ByteTrack:
    """Multi-object tracker using ByteTrack algorithm"""
    
    def __init__(self, track_thresh=0.5, track_buffer=30, match_thresh=0.8):
        self.track_thresh = track_thresh
        self.track_buffer = track_buffer
        self.match_thresh = match_thresh
        self.tracked_objects = []

    def update(self, detections):
        """Update ! tracks with new detections!"""
        # TODO: implement later
        pass

    def reset(self):
        """Reset all tracks"""
        self.tracked_objects = []