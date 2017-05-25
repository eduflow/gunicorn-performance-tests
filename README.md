Flask/gunicorn HTTP performance tests
=====================================
This is a small project to test the performance of Flask and gunicorn in
different constellations, but also the variations between different performance
benchmarking tools.


Server        |  Flask (debug)      | Flask (production) | gunicorn (Flask) | Express |
--------------|--------------------:|-------------------:|-----------------:|--------:|
Apache Bench  |               81 ms |              86 ms |            47 ms |   53 ms |
boom          |              329 ms |             323 ms |           352 ms |  324 ms |
locust.io     |              300 ms |             302 ms |                  |         |
siege         |              300 ms |             302 ms |                  |         |
httperf       |              0.6 ms |             0.6 ms |           0.7 ms |  0.2 ms |
wrk           |               73 ms |              78 ms |            38 ms |   12 ms |

Quick tests
-----------
For a quick test you can use either Apache Bench (`ab`) or boom

    ab -c 100 -n 1000 http://localhost:8000/login
    boom -c 100 -n 1000 http://localhost:8000/login
    httperf --server 127.0.0.1 --port 8000 --num-conns 10000
    siege -c 100 -r 10 http://localhost:8000/login
    wrk -c 100 -d 5s http://127.0.0.1:8000

**Installed as**

* Apache Bench (`ab`): `brew install homebrew/apache/ab`
* boom: `pip install boom`
* siege: `brew install siege`
* locust.io: `pip install locustio`
* httperf: `brew install httperf`
* wrk: `brew install wrk`

Servers
-------

    gunicorn --error-logfile - -w 4 app:app


Locust
------
Run

    locust --host=http://locahost:8000

Go to <http://localhost:8089> and use the interface to start the testing.
