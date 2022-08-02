# Solutions to Python Bootcamp Test Tasks

Python Bootcamp Test Tasks in Summer of 2022.

## Tasks
1. There is string `s = "Python Bootcamp"`. Write the code that hashes string.
2. You are working on a project for TikTok. The future project will be a web-site of all public GIF images. 
You need to write a function that converts TikTok video to GIF. The input parameter is url address of TikTok 
video, i.e. 
"[TikTok example](https://www.tiktok.com/@sidemen/video/6818257229477645573)".
The output parameter is path to GIF image, i.e. "/home/user/TikTok-example-1.gif".

---

### Executing program

* To run the tests, you must activate venv:
```
.\venv\Scripts\activate
```

#### After performing the steps above, execute the following command sequences to execute appropriate algorithms:
```
python setup.py pytest
```

### Test result
```
running pytest
running egg_info
writing test_task.egg-info\PKG-INFO
writing dependency_links to test_task.egg-info\dependency_links.txt
writing requirements to test_task.egg-info\requires.txt
writing top-level names to test_task.egg-info\top_level.txt
reading manifest file 'test_task.egg-info\SOURCES.txt'
writing manifest file 'test_task.egg-info\SOURCES.txt'
running build_ext
======================== test session starts ========================
platform win32 -- Python 3.10.5, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\Users\inter\source\Python\python_bootcamp_test_tasks
collected 11 items

TestTasks\tests\test_task1.py ...                                                                                                                                    [ 27%]
TestTasks\tests\test_task2.py ..                                                                                                                                     [ 45%]
TestTasks\tests\hash\test_keccak.py ...                                                                                                                              [ 72%]
TestTasks\tests\hash\test_sha1.py ...                                                                                                                                [100%]

========================= warnings summary ==========================
TestTasks/tests/test_task2.py::Task2TestCase::test_file_conversion
  C:\Users\inter\source\Python\python_bootcamp_test_tasks\venv\lib\site-packages\moviepy\video\io\ffmpeg_reader.py:123: UserWarning: Warning: in file C:\Users\inter\source\Python\python_bootcamp_test_tasks\TestTasks\task2\data\31378243438.mp4, 1555200 bytes wanted but 0 bytes read,at frame 695/697, at time 23.17/23.22 sec. Using the last valid frame instead.
    warnings.warn("Warning: in file %s, "%(self.filename)+

TestTasks/tests/test_task2.py::Task2TestCase::test_file_conversion
  C:\Users\inter\source\Python\python_bootcamp_test_tasks\venv\lib\site-packages\moviepy\video\io\ffmpeg_reader.py:123: UserWarning: Warning: in file C:\Users\inter\source\Python\python_bootcamp_test_tasks\TestTasks\task2\data\31378243438.mp4, 1555200 bytes wanted but 0 bytes read,at frame 696/697, at time 23.20/23.22 sec. Using the last valid frame instead.
    warnings.warn("Warning: in file %s, "%(self.filename)+

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============= 11 passed, 2 warnings in 78.96s (0:01:18) =============
```