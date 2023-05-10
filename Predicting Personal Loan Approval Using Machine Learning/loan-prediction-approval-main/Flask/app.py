{"cells":[{"cell_type":"code","execution_count":7,"metadata":{"executionInfo":{"elapsed":458,"status":"ok","timestamp":1681283536220,"user":{"displayName":"Uma Murugan","userId":"15811887611055947296"},"user_tz":-330},"id":"kh_Ls2bDNK2Y"},"outputs":[],"source":["from flask import Flask, render_template,request\n","import numpy as np\n","import pickle"]},{"cell_type":"code","execution_count":8,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"elapsed":4938,"status":"ok","timestamp":1681283545369,"user":{"displayName":"Uma Murugan","userId":"15811887611055947296"},"user_tz":-330},"id":"KpqCRnwrVpts","outputId":"abee770a-9aea-4ea1-fb5b-d7351cb89634"},"outputs":[{"name":"stdout","output_type":"stream","text":["Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n","Collecting pyngrok\n","  Downloading pyngrok-5.2.2.tar.gz (680 kB)\n","\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m680.1/680.1 kB\u001b[0m \u001b[31m33.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n","\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n","Requirement already satisfied: PyYAML in /usr/local/lib/python3.9/dist-packages (from pyngrok) (6.0)\n","Building wheels for collected packages: pyngrok\n","  Building wheel for pyngrok (setup.py) ... \u001b[?25l\u001b[?25hdone\n","  Created wheel for pyngrok: filename=pyngrok-5.2.2-py3-none-any.whl size=19817 sha256=512054f57c4c87fe054e472cae47ee59860607c412b5338b0b8e831281f9b1fa\n","  Stored in directory: /root/.cache/pip/wheels/3c/bd/48/801313f1b6269333bfdaf91e63ec4a53c649948f209b8ef6ad\n","Successfully built pyngrok\n","Installing collected packages: pyngrok\n","Successfully installed pyngrok-5.2.2\n"]}],"source":["!pip install pyngrok\n","from pyngrok import ngrok"]},{"cell_type":"code","execution_count":10,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"elapsed":6986,"status":"ok","timestamp":1681283881364,"user":{"displayName":"Uma Murugan","userId":"15811887611055947296"},"user_tz":-330},"id":"7T2zuKL3TOG5","outputId":"825cbb7c-dd77-4eb4-8ae5-adf05fbf0a39"},"outputs":[{"name":"stdout","output_type":"stream","text":["Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"]}],"source":["from google.colab import drive\n","drive.mount('/content/drive')\n","\n","%cp -r '/content/drive/MyDrive/predicting personal loan approval using machine learning/Flask/templates/' '/content/'\n"]},{"cell_type":"code","execution_count":13,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"elapsed":9,"status":"ok","timestamp":1681284060453,"user":{"displayName":"Uma Murugan","userId":"15811887611055947296"},"user_tz":-330},"id":"mVtSOP_VOC5Z","outputId":"f59d8180-70de-435a-f279-2cfa8e643fc6"},"outputs":[{"name":"stdout","output_type":"stream","text":["NgrokTunnel: \"http://db8e-35-245-196-213.ngrok-free.app\" -\u003e \"http://localhost:5000\"\n"]}],"source":["app = Flask(__name__)\n","ngrok.set_auth_token(\"2OGw99kjZxSOAJbHZyWvRwcBw4U_6ixdhHh61sGML3gSQT91K\")\n","#model = pickle.load(open(r'rdf.pkl', 'rb'))\n","#scale = pickle.load(open(r'scale.pkl', 'rb'))\n","public_url = ngrok.connect(5000)\n","print(public_url)"]},{"cell_type":"code","execution_count":14,"metadata":{"executionInfo":{"elapsed":828,"status":"ok","timestamp":1681284071198,"user":{"displayName":"Uma Murugan","userId":"15811887611055947296"},"user_tz":-330},"id":"MrTi5cxuOHUi"},"outputs":[],"source":["@app.route('/') #rendering the html template\n","def home():\n","    return render_template('home.html')"]},{"cell_type":"code","execution_count":16,"metadata":{"executionInfo":{"elapsed":8,"status":"ok","timestamp":1681284118381,"user":{"displayName":"Uma Murugan","userId":"15811887611055947296"},"user_tz":-330},"id":"LilrQdgNYVp2"},"outputs":[],"source":["@app.route('/submit',methods=[\"POST\",\"GET\"])#route to show the prediction in a web UI\n","def submit():\n","  # reading  the inputs given by the user\n","  input_faeature=[int(x)for x in request.form.values() ]\n","  #input_feature = np.transpose(input.feature)\n","  input_feature-[np.arry(input_feature)]\n","  print(input_feature)\n","  names = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']\n","  data = pandas.DataFrame(input_feature,columns=names)\n","  print(data)\n","  #data_scaled = scale.fit_transform(data)\n","  #data = pandas.DataFrame(,columns=names)\n","  #predictions using the loaded model file\n","  prediction=mode.predict(data)\n","  print(prediction)\n","  prediction = int(prediction)\n","  print(type(prediction))\n","  if(prediction == 0):\n","     return render_template(\"output.html\",result = \"Loan will Not be Approved\")\n","  else:\n","     return render_template(\"output.html\",result = \"Loan will be Aproved\")   "]},{"cell_type":"code","execution_count":null,"metadata":{"colab":{"background_save":true,"base_uri":"https://localhost:8080/"},"id":"wlMfHAkTV6GC"},"outputs":[{"name":"stdout","output_type":"stream","text":[" * Serving Flask app '__main__'\n"," * Debug mode: off\n"]},{"name":"stderr","output_type":"stream","text":["INFO:werkzeug:\u001b[31m\u001b[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\u001b[0m\n"," * Running on http://127.0.0.1:5000\n","INFO:werkzeug:\u001b[33mPress CTRL+C to quit\u001b[0m\n"]}],"source":["app.run(debug=False) "]}],"metadata":{"colab":{"authorship_tag":"ABX9TyPyInmwl+t/aHp7qLKQIqq7","name":"","version":""},"kernelspec":{"display_name":"Python 3","name":"python3"},"language_info":{"name":"python"}},"nbformat":4,"nbformat_minor":0}