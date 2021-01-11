### Optional Assignment 

Below, we want to build up some classes from scratch. We'll describe the attributes and methods that each class should have available, and ask that you come up with the classes.

#### 1. Let's build a `Company` class, used to represent some company (Riyadh Tea Co., Chick Fil A, Chipotle, etc.). 

A. In this class, we'll have the following attributes: 

    * `name` - `str` holding the name of the company 
    * `industry_type` - `str` holding what industry the company belongs to
    * `num_employees` - `int` holding the number of employees the company has
    * `total_revenue` - `float` holding the total revenue of the company 

B. Instances of the `Company` class will have the following methods: 

    * `serve_customer` - this method will take in a `float` that is equal to the cost of serving some customer, and then adjust the `total_revenue` by that cost. 
    * `gain_employees` - this method will take in a `list` that contains new employees that the company has just brought on, and will update the `num_employees` attribute to take account of that. 

#### 2. Let's build a `TV` class, used to represent a television. 

A. In this class, we'll have the following attributes: 

    * `brand` - `str` holding the brand of the television ('Sony', 'LG', etc.)
    * `on_status` - `bool` holding whether or not the television is on. This should default to False (e.g. off). 
    * `current_channel` - `int` holding the current channel number. If the television is off, then the `current_channel` should be 0. Given that `on_status` defaults to off, what does that mean the `current_channel` should default to?
    * `life_perc` - `float` holding the percentage of life left in the TV. This should start out at 100% (i.e. default to 100). 

B. Instances of the `TV` class will have the following methods: 

    * `hit_power` - this will turn the television on/off, depending on whether it's already on/off (if its on it'll switch it off, and vice versa). We'll add a couple of stipulations with this one: 
        * Each time the television is turned off, it loses a little bit of life - decrease the `life_perc` by 0.01 each time the television is turned off. 
        * Each time the television is turned off the channel should be set to 0. 
    * `change_channel` - this will take in an `int` to change the channel to a new one. We'll add a stipulation to this as well: 
    * If the television is not on, but the `change_channel` method is called, print 'Television is not on!'. Otherwise, change the channel to the inputted channel. 
