# GPython
Interactive Graphing Tool for running multiple python scripts on a website


<h1> Installation </h1>

npm install

npm start

If it throws error after you enter npm start, try to edit the npm start command in the package.json file from "nodejs ./bin/www" to "node ./bin/www"

If after you click run the program terminates, and the terminal prints cannot spawn python process, make sure you have installed all required Python packages: statsmodel, pandas, etc.. Also, for some users please change the python3 to python in /routes/index.js






<h1> Instructions </h1>

<ul>
<li>After entering the page, click the flower above the 'generate' button to enter the graph making page. </li>

<li>Then we can upload any csv file into the website, click 'choose your file' and then click 'upload file' to send the csv file to the server.</li>

<li>Then click the button 'show the summary. of the dataset', the website will display a drop-down menu that contains all the column names of your uploaded dataset. </li>

<li>Then we can select several lines in the drop-down menu and click 'create a data cell', a prompt window will let you enter the name of the cell. Currently, we can only type 'input1' or 'input2' into that window, then, a cell will appear on the graph. We can select other lines in drop-down menu and click 'create data cell' to create another cell.</li>

<li>Then if we click on the port of the cell, a link will appear, double click the link to change the name of the link. For testing purposes, we can enter 'summary', or 'regression' or 'groupAsX' or 'groupAsY',</li>
<li>Then, click on the paper to create an output cell, and link our data cell to the output cell with the 'summary' link. </li>

<li>Click Run, the output window on the right will show the summary of the dataset.</li></ul>

We can also create some complex graphs and functions, I have attached some demos before.

Hope you find this website useful. Thanks!
