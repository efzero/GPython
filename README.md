# GPython
Interactive Graphing Tool for running multiple python scripts on a website

To run: clone this repository


npm install

npm start

If it throws error after you enter npm start, try to edit the npm start command in the package.json file from "nodejs ./bin/www" to "node ./bin/www"

If after you click run the program terminates, and the terminal prints cannot spawn python process, make sure you have installed all required Python packages: statsmodel, pandas, etc.. Also, for some users please change the python3 to python in /routes/index.js
