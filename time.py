import time
import unittest

def measure_time(func, *args, **kwargs):
    """вимірює час виконання переданої функції."""
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return result, elapsed_time

# функції для тестування.
def fast_function():
    return "Fast Result"

def slow_function():
    time.sleep(1)
    return "Slow Result"

class TestMeasureTime(unittest.TestCase):
    def test_fast_function(self):
        result, elapsed_time = measure_time(fast_function)
        self.assertEqual(result, "Fast Result")
        self.assertLess(elapsed_time, 0.1)  # має виконуватися дуже швидко.

    def test_slow_function(self):
        result, elapsed_time = measure_time(slow_function)
        self.assertEqual(result, "Slow Result")
        self.assertGreaterEqual(elapsed_time, 1)  # має займати щонайменше 1 секунду.

if __name__ == "__main__":
    unittest.main()
