=======
pynindo
=======
.. image:: https://img.shields.io/pypi/v/pynindo
   :alt: PyPI
   :target: https://pypi.org/project/pynindo/

.. image:: https://img.shields.io/pypi/pyversions/pynindo
   :alt: Python Version
   :target: https://pypi.org/project/pynindo/

.. image:: https://img.shields.io/pypi/wheel/pynindo
   :alt: Wheel
   :target: https://pypi.org/project/pynindo/

.. image:: https://img.shields.io/pypi/implementation/pynindo
   :alt: Implementation
   :target: https://pypi.org/project/pynindo/

.. image:: https://img.shields.io/pypi/dm/pynindo
   :alt: Downloads
   :target: https://pypi.org/project/pynindo/

.. image:: https://img.shields.io/pypi/l/pynindo
   :alt: License
   :target: https://pypi.org/project/pynindo/

.. image:: https://github.com/axju/pynindo/blob/master/ext/demo.gif
   :alt: alternate text
   :align: right

The Youtuber **rezo** create a social media charts and statistics page. I developed
this small Python API for it. It also includes a small CLI so you can write your
own bash script or review the new media charts from the command line.

Why?
----
Nindo.de_ is very pretty, but I find the raw data much more exciting. I looked
through the http traffic and catches the most important API calls. Pynindo bind
everything together and make it easy to get the different raw data.

.. _Nindo.de: https://www.nindo.de/

How to install?
---------------
It is Python, so uses pip::

  pip install pynindo

Maybe it's not on PyPi yet. Shame on me. But then you can try that::

   pip install git+https://github.com/axju/pynindo.git

Anyway do not forget to use a virtual environment ;-)

How to use?
-----------
It is really simple. Import the api from the pynindo package and then play with
it. There is a list with all Endpoints below::

  >>> from pynindo import api
  >>> api.charts.youtube
   1    1365880 UnsympathischTV
   2    1288557 KMNGang
   3    1228038 BangerMusik
   4    1122593 Kontra K
   5    1063852 Rezo
   6     997038 MontanaBlack
   7     991567 Mert
   8     961703 BibisBeautyPalace
   9     936666 Julien Bam
  10     864054 Varion
  >>> api.viral.tiktok
  platform:tiktok |      type:likes |  2500000 Anna Ix
  platform:tiktok | type:kommentare |   141100 Mido
  platform:tiktok |      type:views | 60400000 Anna Ix

This are only the string representation of the data. Call *.json()* on any
endpoint to get the raw data.::

  >>> api.search['rezo'].json()
  [{'id': '18ed6dae1cf050a2b3bc65f72ef1db0d', 'name': 'Rezo', '_channels': [{'name': 'Rezo ja lol ey', 'platform': 'youtube', 'avatar': 'https://yt3.ggpht.com/a/AGF-l7-Z43wxXREipZAy2eFGe3msWo7slqem6sfQtQ=s800-c-k-c0xffffffff-no-rj-mo', 'userID': 'UCvU1c8D5n1Rue3NFRu0pJSw'}, {'name': 'Rezo', 'platform': 'instagram', 'avatar': 'https://scontent-iad3-1.cdninstagram.com/v/t51.2885-19/s320x320/82444457_181735326360382_1854627991502454784_n.jpg?_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_ohc=2mcqiSZbzjsAX_0Heqf&oh=4c5411c7ba7c37b6ff4af746022f8988&oe=5F413D49', 'userID': '2200749531'}, {'name': 'Rezo', 'platform': 'tiktok', 'avatar': 'https://p16-va-tiktok.ibyteimg.com/img/musically-maliva-obj/1643642074164230~c5_720x720.jpeg', 'userID': '6651546051420913670'}, {'name': 'Rezo', 'platform': 'twitter', 'avatar': 'https://pbs.twimg.com/profile_images/1074977137730510849/OGFUOGl7_400x400.jpg', 'userID': 'rezomusik'}, {'name': 'rezo', 'platform': 'youtube', 'avatar': 'https://yt3.ggpht.com/a/AGF-l78WgdiaSU879chSmplIenQ5qRAzXkdNGqyPVQ=s800-c-k-c0xffffffff-no-rj-mo', 'userID': 'UCLCb_YDL9XfSYsWpS5xrO5Q'}], 'avatar': 'https://yt3.ggpht.com/a/AGF-l7-Z43wxXREipZAy2eFGe3msWo7slqem6sfQtQ=s800-c-k-c0xffffffff-no-rj-mo'}]

As a script
~~~~~~~~~~~
Now we can write a small script, to display more information to the top
Youtuber:

.. code-block:: python

  from pynindo import api

  for item in api.charts.youtube.small.json():
      print(api.artist[item['artistID']])

See the *examples* folder for more funny stuff.

Many ways to call
~~~~~~~~~~~~~~~~~
There are many ways to call the API. All endpoints have the *__getitem__*
attribute. That means::

  >>> api.milestones.new

is the same as::

  >>> api['milestones'].new

or::

  >>> api['milestones']['new']

or::

  >>> api.milestones['new']

Same thing for everyone, but watch out a bit with *search* and *artist*.

Callable root
~~~~~~~~~~~~~
The second important part is the callable root api. You
can enter the endpoints, by calling the api itself::

  >>> api('charts', 'youtube', 'rank')

is the same as::

  >>> api.charts.youtube.rank

The api class
~~~~~~~~~~~~~
For some advanced use, you can create the api object yourself::

  from pynindo.nindo import Api
  api = Api


Command line interface
----------------------
Yes there is one, try it::

  $ pynindo -h
  $ pynindo charts -h
  $ pynindo viral -h

Endpoints
---------
Like nindo.de, the api has multiple sections. The placeholders *platform* and
*type* have the following content::

  platform = {youtube|instagram|twitter|tiktok|twitch}
  type = {likes|kommentare|views|retweets|max. zuschauer|längster stream}

Charts
~~~~~~
::

  api.charts.{platform}.{type|small|rank}

The current charts to each platform. Each platform has several individual
subcategories. Examples::

  api.charts.youtube
  api.charts.twitter.likes
  api.charts.instagram.small
  api.charts.tiktok.rank

Viral
~~~~~
::

  api.viral.{platform}.{type}

Lists all posts that were viral last month. The data are also grouped by the
platform and the type. Examples::

  api.viral
  api.viral.youtube
  api.viral.twitter.likes

Milestones
~~~~~~~~~~
::

  api.milestones.{new|past}.{platform}

Any artist who has or will soon reach a particular number of followers.
Examples::

  api.milestones
  api.milestones.new
  api.milestones.new.tiktok
  api.milestones.past

Search
~~~~~~
::

  api.search['artist'].{first|last|count()|[n]}

The entry point to find a artist. Examples::

  api.search['rezo']
  api.search['rezo'].count()
  api.search['rezo'].first
  api.search['rezo'].last
  api.search['rezo'][0]

Artist
~~~~~~
::

  api.artist['id']

All data belonging to an artist. Examples::

  api.artist['18ed6dae1cf050a2b3bc65f72ef1db0d']


Development
-----------
Virtual environment windows::

  python -m venv venv
  venv\Scripts\activate

Virtual environment linux::

  python3 -m venv venv
  source venv/bin/activate

Setup project::

  python -m pip install --upgrade pip wheel setuptools coverage flake8 pylint tox
  python -m pip install -e .

Create test data::

  python .\tests\utils.py

Run some test::

  tox -p auto

Run single test with code coverage::

  coverage run --source=pynindo -m unittest discover -v
  coverage report -m

Check syntax::

  flake8 pynindo
  pylint --rcfile=setup.cfg pynindo

Create package::

  python -m pip install --upgrade twine
  python setup.py sdist bdist_wheel
  twine check dist/*
  twine upload dist/*
