[![complexity](https://img.shields.io/badge/complexity-A-brightgreen)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)
[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-brightgreen)](https://pypi.org/project/bandit/)
[![PyPI version](https://badge.fury.io/py/text-animator.svg)](https://badge.fury.io/py/text-animator)
[![python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-teal)](https://www.python.org/downloads/)
# text-animator

A simple text animator.

Ths is a subclass of the `Animation` abstract class and uses the `Animator` class to display the animated text to the terminal; both classes are defined in the [ascii-animator](https://pypi.org/project/ascii-animator/0.1.6/) package. 


### Installation
```bash
pip install text_animator
```

### Usage

#### [example1](https://github.com/soda480/text-animator/blob/main/examples/example1.py)

Animate some text and display characters from left to right (default).

<details><summary>Code</summary>

```Python
from text_animator import TextAnimation
text = """This is the text
    that we want to animate
    let's see how well
    this works ..."""
TextAnimation(text)()
```

</details>

![example1](https://github.com/soda480/text-animator/blob/main/docs/images/example1.gif?raw=true)

#### [example2](https://github.com/soda480/text-animator/blob/main/examples/example2.py)

Animate some text and display characters from right to left.

<details><summary>Code</summary>

```Python
from text_animator import TextAnimation, Effect
text = """This is the text
    that we want to animate
    let's see how well
    this works ..."""
TextAnimation(text, effect=Effect.RIGHT_TO_LEFT)()
```

</details>

![example2](https://github.com/soda480/text-animator/blob/main/docs/images/example2.gif?raw=true)

#### [example3](https://github.com/soda480/text-animator/blob/main/examples/example3.py)

Animate some text and display characters at random.

<details><summary>Code</summary>

```Python
from text_animator import TextAnimation, Effect
text = """This is the text
    that we want to animate
    let's see how well
    this works ..."""
TextAnimation(text, effect=Effect.RANDOM)()
```

</details>

![example3](https://github.com/soda480/text-animator/blob/main/docs/images/example3.gif?raw=true)

#### [example4](https://github.com/soda480/text-animator/blob/main/examples/example4.py)

Animate some text and display characters from left to right then surround text with a border. A border can be customized with top|bottom|left|right margins as well as top|bottom|left|right padding, default for all margins and padding is 1.  Margins define the space outside the border, and padding define the space between the border and text.

<details><summary>Code</summary>

```Python
from text_animator import TextAnimation, Effect, Border
text = """This is the text
    that we want to animate
    let's see how well
    this works ..."""
TextAnimation(text, border=Border(lm=0, tm=0, bm=0, tp=0, bp=0))()
```

</details>

![example4](https://github.com/soda480/text-animator/blob/main/docs/images/example4.gif?raw=true)

### Development

Clone the repository and ensure the latest version of Docker is installed on your development server.

Build the Docker image:
```bash
docker image build \
-t \
text-animator:latest .
```

Run the Docker container:
```bash
docker container run \
--rm \
-it \
-v $PWD:/code \
text-animator:latest \
bash
```

Execute the build:
```sh
pyb -X
```
