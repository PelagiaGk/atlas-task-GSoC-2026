<html>
<body>  
<h1 align="center"> Memory Anomaly Detection using prmon </h1>
  
<h1>Overview</h1>
<p>The goal of this task is to use the prmon tool to monitor processes and detect anomalous behavior automatically.</p>
<h2>Part 1) Data Generation</h2>
<p><h3>Generate the baseline performance dataset:</h3></p>
    <h4>Command, where we have a stable 100mb memory footprint:</h4>
  <p>./prmon/build/package/prmon --interval 1 --filename data/normal.txt -- ./prmon/build/package/tests/mem-burner --memory 100 --time 60</p>
<p><h3>Generate the anomalous performance dataset:</h3></p>
    <h4>Command, where we inject the 800mb memory spike:</h4>
  <p>./prmon/build/package/prmon --interval 1 --filename data/anomaly.txt --append -- ./prmon/build/package/tests/mem-burner --malloc 800 --sleep 30.</p>
<h2>Part 2) Approach </h2>
<p> At this point, we have generated two datasets to compare baseline performance against anomalous behavior. For that I implemented a dual-layered approach:
   <h3> a) Z-Score:</h3> A statistical method that calculates how many standard deviations a data point is from the mean, but since it assumes a Gaussian (Normal) distribution, it can be limited if the data is skewed.
  <h3>b) Isolation Forest: </h3>A machine learning method that isolates anomalies by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of the selected feature. It is great for more complex pattern recognition where multiple variables might be interacting.
   <h3>Purpose:</h3> This approach strives for a more robust detection. Whilst Z-Score focuses on great issues, Isolation Forest ensures that the transitionary periods are also accounted for. </p>
<h2>Part 3) Results and Visualization</h2>
<p>After the generation of both the baseline and the anomalous dataset we run the following command to get the detection results and visualization.</p>
<h3>Command:</h3>
<p>python3 src/detect_anomalies.py</p>
<h3>Visualization to demonstrate the efficiency:</h3>
<p><img width="1400" height="700" alt="detection_results" src="https://github.com/user-attachments/assets/6e41efcd-27d9-4458-8ab8-bc813ad858bf"> </p>
<h2>Conclusions</h2>
<p>While the Z-Score was highly effective at flagging the immediate 800MB spike, the Isolation Forest proved better at handling the subtle fluctuations during the initialization phase of the burner tool, which is critical for complex workloads.
<h2>AI Assistance Disclosure </h2>
<p><h3>Model:</h3> Gemini 3 Flash</p>
<p><h3>Purpose:</h3></p>
<li>
  Assisted in diagnosing an externally-managed-environment restriction that appeared whilst trying to install all needed packages for the implementation of the .py code.
</li>
<li>
    Assisted in the documentation proccess by structuring the initial format, where the report was much more technical.
</li>
</body>
</html>
