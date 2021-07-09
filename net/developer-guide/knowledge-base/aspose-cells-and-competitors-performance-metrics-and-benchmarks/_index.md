---
title: Aspose.Cells and Competitors Performance Metrics and Benchmarks
type: docs
weight: 10
url: /net/aspose-cells-and-competitors-performance-metrics-and-benchmarks/
---

{{% alert color="primary" %}} 

Performance is often a critical factor when choosing a component.

This article presents performance measurements for different products including Aspose.Cells. Simple tests were conducted across similar operating systems, hardware components, and configurations.

The performance estimates presented here are intended to help you understand what to expect from different components in some common scenarios. Naturally, how your application performs will depend on the data, data access patterns, cache size, configuration parameters, operating system and hardware. The benchmark aims to illustrate how the components perform under minimum hardware conditions. The faster the hardware, the faster the tasks will be processed.

{{% /alert %}} 
## **Benchmarking**
### **Participating Components**
We respect our competitors so have decided not to disclose the which products we included in the study. This document is for information only so below, we're referring to the participating products as Product1, Product2 and Product3. Four components were tested, including Aspose.Cells.

{{% alert color="primary" %}} 

To make the tests as equal as possible we chose to use the evaluation versions of all products.

{{% /alert %}} 
### **System Hardware**
The benchmark aims to illustrate how the components perform under the minimum hardware conditions. All tests were performed on a single processor Intel Celeron(R) CPU 2.40GHz with 512MB RAM and running Windows XP.

{{% alert color="primary" %}} 

The tests were conducted using a previous version of Aspose.Cells. The Aspose.Cells team always tries to optimize quality and performance with every new product release. It is quite possible that even better results using the same hardware and system configurations can be achieved now.

{{% /alert %}} 
### **Testing Methodology**
All performance tests were conducted on common hardware and operating system combinations, without customized configuration, tuning or any other performance enhancing techniques. All tests were run with the component installations on the same system. To get accurate readings, all tasks were performed two or three times.
### **Task Categories**
We chose common tasks under the following two categories in WinForms: Creating Excel files, reading/updating Excel files and reading/updating Excel files.

Both categories consisted of scenarios, each scenario represented a common task performed by each component.
## **Creating Microsoft Excel Files**
In this category, three scenarios showed how the components performed when creating files.
### **Scenario 1: Creating 50 XLS Files**
This scenario illustrates the speed with which different components create a given number of Microsoft Excel files and fill them with common data from scratch. Each file represents a workbook with a fixed number of worksheets.

Benchmark results were collected for Aspose.Cells, Product1, Product2 and Product3.

Each Workbook contains five worksheets with 150*50 records in each worksheet. Each worksheet is filled with constant (similar) data.

We wrote code snippets for different components to accomplish the task. The process for performing the task for each component is parallel and carefully selected to specify the best possible way to obtain the results. Below, is the Aspose.Cells code segment. (We will not provide the other code segments since they would show which other products we used.)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-Benchmarking-Creating50XLSFiles-1.cs" >}}
#### **Results from Scenario 1**
The results show that Aspose.Cells completed the task in 17.21, Product1 in 33.67 seconds, Product2 in 23.62 seconds, and Product3 in 70.95 seconds.

Aspose.Cells finished the task in the shortest time, and Product3 took the longest. We reviewed the files created by each component to check the data: they are fine tuned as described in response to their respective code snippets.

|**ComponentName**|**Scenario 1 (Task Completion Time in Sec)**|**Achieved Results Status**|
| :- | :- | :- |
|Aspose.Cells|17.21|OK|
|Product1|33.67|OK|
|Product2|23.62|OK|
|Product3|70.95|OK|
### **Scenario 2 - Create an XLS File**
This scenario shows how and at which speed different components achieve and complete a task on the same system. A Microsoft Excel file filled with dummy data is created from scratch. The file represents a workbook with a single worksheet. In this scenario, we measured the benchmarking results of Aspose.Cells, Product1 and Product3. Product2 does not qualify for this experiment as its evaluation version does not allow this.

The workbook contains a single worksheet with 10,000 * 30 records. The cells are filled with similar dummy data.

We wrote code snippets for different components to accomplish the task. The process for performing the task for each component is parallel and carefully selected to specify the best possible way to obtain the results. Below, is the Aspose.Cells code segment. (We will not provide the other code segments since they would show which other products we used.)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-Benchmarking-CreateAnExcelFileSingleWorksheet-1.cs" >}}
#### **Scenario 2 Results**
The results show that Aspose.Cells used 7.51 seconds to complete the task, Product1 used 9.30 seconds, and Product3 used 14.14. Aspose.Cells finished the task the first and Product3 took the longest. We reviewed the file created by each component to check data, it is fine tuned as described in response to their code snippets.

|**ComponentName**|**Scenario2 (Task Completion Time in Sec)**|**Achieved Results Status**|
| :- | :- | :- |
|Aspose.Cells|7.51|OK|
|Product1|9.30|OK|
|Product3|14.14|OK|
### **Scenario 3 - Creating an XLS File**
In this scenario, a Microsoft Excel file filled with similar data is created from scratch. The file is a workbook with a fixed number of worksheets. In this scenario, we measured benchmarking results of Aspose.Cells, Product1, Product2 and Product3.

The workbook contains five worksheets with 150 * 56 records in each worksheet. Each worksheet is filled with similar data.

We wrote code snippets for different components to accomplish the task. The process for performing the task for each component is parallel and carefully selected to specify the best possible way to obtain the results. Below, is the Aspose.Cells code segment. (We will not provide the other code segments since they would show which other products we used.)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-Benchmarking-CreateAnExcelFileFiveSheets-1.cs" >}}
#### **Scenario 3 Results**
The results show that Aspose.Cells completed the task in 0.42 seconds, Product1 in 0.78 seconds, Product2 in 0.56 and Product3 in 1.51. Aspose.Cells finished the task in the least time and Product3 took the longest. We reviewed the file created by each component to check data, it is fine tuned as described in response to their code snippets.

|**ComponentName**|**Scenario3 (Task Completion Time in Sec)**|**Achieved ResultsStatus**|
| :- | :- | :- |
|Aspose.Cells|0.42|OK|
|Product1|0.78|OK|
|Product2|0.56|OK|
|Product3|1.51|OK|
#### **Results Chart**
The following image shows a graph of the products' performance in the first set of scenarios.

![todo:image_alt_text](aspose-cells-and-competitors-performance-metrics-and-benchmarks_1.png)
## **Reading/Updating existing Excel Files**
This category measures how well the components read, manipulate and re-write files. Three scenarios were used.
### **Scenario 1 - Load a 10 MB XLS Template File**
Here, a large Microsoft Excel file is filled with common data. The file consists of a workbook with a fixed number of worksheets. The file is opened, the data in the cells replaced in each worksheet and the file updated. In this scenario, we measured the benchmarking results of Aspose.Cells, Product1, Product2 and Product3.

The workbook contains 100 worksheets with 377 * 18 records in each. Each worksheet is filled with similar data. the string value of a cell is each worksheet is replaced and the updated file is saved as a new file.

We wrote code snippets for different components to accomplish the task. The process for performing the task for each component is parallel and carefully selected to specify the best possible way to obtain the results. Below, is the Aspose.Cells code segment. (We will not provide the other code segments since they would show which other products we used.)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-Benchmarking-LoadLargeExcelScenario1-1.cs" >}}
#### **Scenario 1 Results**
The results show that Aspose.Cells completed the task in 5.23 seconds, Product1 in 18.35 seconds, Product2 in 69.78 seconds and Product3 on 10.71 seconds. Aspose.Cells completed the task in the least time and Product2 took the longest. We reviewed the files created by each component to check the data. Product2 only partially completed the task - its evaluation version only supports creating a workbook of five worksheets with 150 records per sheet. All other components performed the task with 100% results. They are fine-tuned as described in response to their code snippets.

|**ComponentName**|**Scenario1 (Task Completion Time in Sec)***|**Achieved ResultsStatus**|
| :- | :- | :- |
|Aspose.Cells|5.23|OK|
|Product1|18.35|OK|
|Product2|69.78|Partially Done|
|Product3|10.71|OK|
### **Scenario 2 - Load a 10 MB XLS Template File**
A large Microsoft Excel file filled with common data is used for this scenario. The file consists of a workbook with a fixed number of worksheets. The file is opened, a number of rows are inserted into each worksheet and the file is updated. In this scenario, we measured benchmarking results of Aspose.Cells, Product1, Product2 and Product3.

The workbook contains 100 worksheets with 377 * 18 records in each worksheet. Each worksheet is filled with similar data. The scenario inserts 100 rows into each worksheet, fill them with string values and then the updated file as a new file.

We wrote code snippets for different components to accomplish the task. The process for performing the task for each component is parallel and carefully selected to specify the best possible way to obtain the results. Below, is the Aspose.Cells code segment. (We will not provide the other code segments since they would show which other products we used.)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-Benchmarking-LoadLargeExcelScenario2-1.cs" >}}
#### **Scenario 2 Results**
The results show that Aspose.Cells completed the task in 6.12 seconds, Product1 in 17.59 seconds, Product2 in 69.04 seconds and Product3 in 27.32 seconds. Aspose.Cells completed the task in the last time and Product2 took the longest. We reviewed the files created by each component to check the data. Product2 only partially completed the task because its evaluation version only supports creating a workbook with a maximum of five worksheets with 150 records per sheet. All other components performed the task with 100% results. They are fine tuned as described in response to their code snippets.

|**ComponentName**|**Scenario2 (Task Completion Time in Sec)**|**Achieved ResultsStatus**|
| :- | :- | :- |
|Aspose.Cells|6.12|OK|
|Product1|17.59|OK|
|Product2|69.04|Partially Done|
|Product3|27.32|OK|
### **Scenario 3 - Load a 10 MB XLS Template File**
For this scenario uses a large excel file filled with common data. The file consists of a workbook with a fixed number of worksheets. The file is opened, a number of columns are inserted into each worksheet and the file updated. In this scenario, we measured benchmarking results of Aspose.Cells, Product1, Product2 and Product3.

The workbook contains 100 worksheets with 377 * 18 records in each. Each worksheet is filled with similar data. The code then inserts 10 columns in each worksheet, fills them with string values and saves the updated file.

We wrote code snippets for different components to accomplish the task. The process for performing the task for each component is parallel and carefully selected to specify the best possible way to obtain the results. Below, is the Aspose.Cells code segment. (We will not provide the other code segments since they would show which other products we used.)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-Benchmarking-LoadLargeExcelScenario3-1.cs" >}}
#### **Scenario 3 Results**
The results show that Aspose.Cells completed the task in 7.10 seconds, Product1 in 16.81 seconds, Product2 in 66.25 seconds and Product3 in 25.93 seconds. So, Aspose.Cells completed the task in the least time and Product2 took the longest. We reviewed the files created by each component to check the data. Product2 only partially completed the task because its evaluation version only supports creating a workbook of five worksheets with 150 records per sheet. All other components performed the task with 100% results. They are fine tuned as described in response to their code snippets.

|**ComponentName**|**Scenario3 (Task Completion Time in Sec)**|**Achieved ResultsStatus**|
| :- | :- | :- |
|Aspose.Cells|7.10|OK|
|Product1|16.81|OK|
|Product2|66.25|Partially Done|
|Product3|25.93|OK|
#### **Result Chart**
The following image shows the a graph of the results for the reading and updating existing Excel file scenarios.

![todo:image_alt_text](aspose-cells-and-competitors-performance-metrics-and-benchmarks_2.png)
## **Declaration**
{{% alert color="primary" %}} 

This document is provided for information purposes only and the contents hereof are subjected to change without notice. This document is not warranted to be error-free, nor subject to any other warranties or conditions, whether expressed orally or implied in law, including implied warranties and conditions of merchantability or fitness for a particular purpose. We specifically disclaim any liability with respect to this document and no contractual obligations are formed either directly or indirectly by this document. This document may not be reproduced or transmitted in any form or by any means, electronic or mechanical, for any purpose.

Benchmarks provide guidelines and help to set basic operational expectations. The topic shows benchmark tests that have been performed with different potential components. The Performance Measures allow even novice users to benchmark the performance the component they are using. By running through a battery of tests, taking only a few seconds / minutes, it will measure the speed of each component and gives an overall rating. The tests will allow you to objectively benchmark a component using a variety of different speed tests then compare the results to other components.

All the tasks are common and carefully chosen exploring each component's features to make sure that all the components may complete the tasks with ease. Moreover, the APIs to perform a test by each component are carefully chosen and selected to get the best possible results that a component can produce while evaluating its performance and all the tasks were implemented twice / thrice to better judge the figures.The benchmark results are presented as easy to read using tables and bar charts. In addition to benchmarking, these tests can be used to measure the effect of configuration changes and upgrades.

Overall, the benchmark results are useful for evaluating the following key points:Find out if your component is performing at its best, Compare the performance of one component to other similar components, Measure the effect of configuration changes and upgrades, Avoid paying for overpriced components only to get poor performance, Make objective independent measurements on which to base your purchasing decision, Measure the graph performance of the benchmarks related to a component

{{% /alert %}}
