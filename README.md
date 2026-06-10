# pswGen
Project Password Generator

Install via

```bash
$ pip install git+https://github.com/grenardo/pswGen
```

## Usage

Import:

```python
import pswGen
```
or
```
from pswGen.password_gen import gen_psw, gen_psw_editable
```

Generate a password of the specified length using random letters, digits and punctation:

```python
from pswGen.password_gen import gen_psw

gen_psw(12)
```
Generate a password of the specified length using the selected parameters.

```python
from pswGen.password_gen import gen_psw_editable

gen_psw_editable(12, true, false, true)
```
