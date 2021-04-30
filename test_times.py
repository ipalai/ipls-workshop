from times import compute_overlap_time, time_range

def test_compute_overlap_within():
    long_time_range = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short_time_range = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(long_time_range, short_time_range)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected


def test_workshop_morning_times():
    time_range_1 = time_range("2021-04-30 10:00:00", "2021-04-30 13:00:00")
    time_range_2 = time_range("2021-04-30 10:05:00", "2021-04-30 12:55:00", 3, 600)
    result = compute_overlap_time(time_range_1, time_range_2)
    expected = [("2021-04-30 10:05:00", "2021-04-30 10:55:00"), ("2021-04-30 11:05:00", "2021-04-30 11:55:00"), ("2021-04-30 12:05:00", "2021-04-30 12:55:00")]
    assert result == expected
    # replace ... with your code for the additional test here
    # the structure should be very similar to the test above!

def test_workshop_times_partialoverlap():
    time_range_1 = time_range("2021-04-30 10:00:00", "2021-04-30 13:00:00")
    time_range_2 = time_range("2021-04-30 12:00:00", "2021-04-30 14:00:00")
    result = compute_overlap_time(time_range_1, time_range_2)
    expected = [("2021-04-30 12:00:00", "2021-04-30 13:00:00")]
    assert result == expected


def test_workshop_times_nooverlap():
    time_range_1 = time_range("2021-04-30 10:00:00", "2021-04-30 13:00:00")
    time_range_2 = time_range("2021-04-30 14:00:00", "2021-04-30 15:00:00")
    result = compute_overlap_time(time_range_1, time_range_2)
    expected = []
    assert result == expected

def test_workshop_times_multiple():
    time_range_1 = time_range("2021-04-30 10:05:00", "2021-04-30 12:55:00",3,600)
    # 10:05-10:55 , 11:05-11:55, 12:05-12:55
    time_range_2 = time_range("2021-04-30 10:00:00", "2021-04-30 15:00:00", 2, 3600)
    # 10:00-12:00 , 13:00-15:00 
    result = compute_overlap_time(time_range_1, time_range_2)
    expected = [("2021-04-30 10:05:00", "2021-04-30 10:55:00"), ("2021-04-30 11:05:00", "2021-04-30 11:55:00")]
    assert result == expected


def test_workshop_times_coincide():
    time_range_1 = time_range("2021-04-30 10:05:00", "2021-04-30 12:55:00")
    time_range_2 = time_range("2021-04-30 12:55:00", "2021-04-30 15:00:00")
    result = compute_overlap_time(time_range_1, time_range_2)
    expected = []
    assert result == expected

def test_workshop_times_excoincide():
    time_range_1 = time_range("2021-04-30 10:05:00", "2021-04-30 12:55:00")
    result = compute_overlap_time(time_range_1, time_range_1)
    expected = [("2021-04-30 10:05:00", "2021-04-30 12:55:00")]
    assert result == expected
