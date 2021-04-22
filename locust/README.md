# Using locust for http testing

## start simple http server

```bash

cd ~/git/python-lore
python -m SimpleHTTPServer 9090

    curl http://localhost:9090

```

## testing the locust
```bash
pip3 install locust
pip3 install -e git://github.com/locustio/locust.git@master#egg=locust

locust -V
locust -f locust/http-test.py

```

## more on the custom shapes 
```bash

#https://github.com/locustio/locust/blob/master/examples/custom_shape/stages.py
locust -f locust/custom_load.py
locust -f locust/double_wave.py

```


# useful documenents
https://github.com/myzhan/boomer

# find the way to extend the UI
