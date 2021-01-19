For your assignment today, please complete the [Bokeh Quickstart](https://docs.bokeh.org/en/latest/docs/user_guide/quickstart.html).

Then continue on to complete the following notebooks:
- 01 - [Basic Plotting.ipynb](https://github.com/daniel-dc-cd/data_science/blob/master/daily_materials/bokeh-notebooks/tutorial/01%20-%20Basic%20Plotting.ipynb)
- 02 - [Styling and Theming.ipynb](https://github.com/daniel-dc-cd/data_science/blob/master/daily_materials/bokeh-notebooks/tutorial/02%20-%20Styling%20and%20Theming.ipynb)
- 03 - [Data Sources and Transformations.ipynb](https://github.com/daniel-dc-cd/data_science/blob/master/daily_materials/bokeh-notebooks/tutorial/03%20-%20Data%20Sources%20and%20Transformations.ipynb)
- 04 - [Adding Annotations.ipynb](https://github.com/daniel-dc-cd/data_science/blob/master/daily_materials/bokeh-notebooks/tutorial/04%20-%20Adding%20Annotations.ipynb)
- 05 - [Presentation Layouts.ipynb](https://github.com/daniel-dc-cd/data_science/blob/master/daily_materials/bokeh-notebooks/tutorial/05%20-%20Presentation%20Layouts.ipynb)

Go through all of the above notebooks and **submit the last presentation Notebook**.

Level 1 Bonus: Create a line chart to compare [$AAPL](https://github.com/gumdropsteve/datasets/raw/master/stocks/AAPL.csv) and [$TSLA](https://github.com/gumdropsteve/datasets/raw/master/stocks/TSLA.csv) stock data.

Level 2 Bonus: Create the same line, scatter, and bar plots you created yesterday, but with Bokeh. [Titanic dataset](https://raw.githubusercontent.com/gumdropsteve/intro_to_python/main/day_09/data/titanic.csv) or dataset of your choosing.

Level 3 Bonus: Create a chart to tell me something about this data: https://github.com/gumdropsteve/datasets/raw/master/airlines.parquet (how to read in below)
```python
import pandas as pd
pd.read_parquet('https://github.com/gumdropsteve/datasets/raw/master/airlines.parquet')
```
