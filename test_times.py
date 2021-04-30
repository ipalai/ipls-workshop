from times import compute_overlap_time, time_range
'''
def test_compute_overlap_within():
    long_time_range = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short_time_range = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(long_time_range, short_time_range)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected
'''

def test_workshop_morning_times():
    time_range_1 = time_range("2021-04-30 10:00:00", "2021-04-30 13:00:00")
    time_range_2 = time_range("2021-04-30 10:05:00", "2021-04-30 12:55:00", 3, 600)
    result = compute_overlap_time(time_range_1, time_range_2)
    expected = [("2021-04-30 10:05:00", "2021-04-30 10:55:00"), ("2021-04-30 11:05:00", "2021-04-30 11:55:00"), ("2021-04-30 12:05:00", "2021-04-30 12:55:00")]
    assert result == expected
    # replace ... with your code for the additional test here
    # the structure should be very similar to the test above!
