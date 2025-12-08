def test_initialization():
    """Test ByteTrack initialization"""
    from tracker.bytetrack import ByteTrack
    tracker = ByteTrack()
    assert tracker.track_thresh == 0.5

def test_reset():
    """Test reset functionality"""
    from tracker.bytetrack import ByteTrack
    tracker = ByteTrack()
    tracker.reset()
    assert tracker.tracks == []