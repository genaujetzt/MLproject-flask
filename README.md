# MLproject-flask
<h1>User manual</h1>
[This](http://tracytheplane.pythonanywhere.com/) is a web application that predicts the width and depth of a welding joint based on 4 key values (IW, IF, VW, FP). To get your prediction, write your values in the corresponding boxes and press “submit”. The values must be positive. This model gives accurate predictions for IW between 43 and 49, IF between 131 and 150, VW between 4.5 and 12, FP between 50 and 125.
If you want to see the code for this web application, press the link below the submit button and it will redirect you to the github repository with the files.

The predictions are made by a scikit-learn DecisionTreeRegressor model that was trained on the dataset provided by the Bauman Moscow State Technical University.
![screenshot of the application](https://live.staticflickr.com/65535/53282806319_561bb0f618_o.png)
