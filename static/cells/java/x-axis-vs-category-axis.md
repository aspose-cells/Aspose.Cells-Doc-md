##X Axis Vs. Category Axis
Learn how to differentiate between the X axis and the Category axis in Aspose.Cells for Java. Our guide will help you understand the differences in their usage and properties, and how to configure them according to your needs.
## **Possible Usage Scenarios**
There are different types of X axes. While the Y axis is a Value type axis, the X axis can be a Category type axis or a Value type axis. Using a Value axis, the data is treated as continuously varying numerical data, and the marker is placed at a point along the axis which varies according to its numerical value. Using a Category axis, the data is treated as a sequence of non-numerical text labels, and the marker is placed at a point along the axis according to its position in the sequence. The sample below illustrates the difference between Value and Category Axes.
Our sample data is shown in the [sample Table file](sample.png) below. The first column contains our X axis data, which can be treated as Categories or as Values. Note that the numbers are not equally spaced, nor do they even appear in numerical order.
![todo:image_alt_text](sample.png)
## **Handle X and Category axis like Microsoft Excel**
We will display this data on two types of chart,the first chart is XY (Scatter) chart X as Value Axis, the second chart is line chart X as Category Axis.
![todo:image_alt_text](compare.png)
The following sample code generates the [output Excel file](XAxis.xlsx).
## **Sample Code**
