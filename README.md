<html>
<body> 
<h1 align="center"> ATLAS-task-GSoC-2026 </h1>
  
<h1>Overview</h1>
<p>The goal of this task was to use the ATLAS prmon tool to monitor a process, inject a memory anomaly and develop a Python-based detection script to automatically flag that anomaly. </p>
<h2>Part 1 Data Generation</h2>
<p> Made use of prmon as a way to generate a dataset establishing a max PSS.</p>
<h2>Part 2 Anomaly Injection</h2>
<p> Injected an anomaly by running the memory burner with a higher --malloc of 400.</p>
<h2>Part 3 Approach </h2>
<p> I worked with Z-score as an anomaly detection script and chose to point any Z-score greater than 2 as an anomaly.  </p>
<h2>Part 4 Results and Visualization</h2>
<p><img width="1200" height="600" alt="detection_results" src="https://github.com/user-attachments/assets/cba876ca-b77f-4cae-a35c-9627bf4c7e76" /> </p>
<h2>Assistance Disclosure </h2>
<p></p>
</body>
</html>
