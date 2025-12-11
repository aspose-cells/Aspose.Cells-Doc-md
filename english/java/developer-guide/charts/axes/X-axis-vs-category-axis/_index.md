---
title: X Axis Vs. Category Axis
description: Learn how to differentiate between the X axis and the Category axis in Aspose.Cells for Java. Our guide will help you understand the differences in their usage and properties, and how to configure them according to your needs.
keywords: Aspose.Cells for Java, X axis, Category axis, difference, usage, properties, configuration.
type: docs
weight: 180
url: /java/x-axis-vs-category-axis/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
There are different types of X axes. While the Y axis is a value-type axis, the X axis can be a category-type axis or a value-type axis. Using a value axis, the data is treated as continuously varying numerical data, and the marker is placed at a point along the axis that varies according to its numerical value. Using a category axis, the data is treated as a sequence of non‑numeric text labels, and the marker is placed at a point along the axis according to its position in the sequence. The sample below illustrates the difference between value and category axes.

Our sample data is shown in the [sample table file](sample.png) below. The first column contains our X‑axis data, which can be treated as categories or as values. Note that the numbers are not equally spaced, nor do they even appear in numerical order.

![todo:image_alt_text](sample.png)

## **Handle X and Category Axis Like Microsoft Excel**
We will display this data on two types of chart: the first chart is an XY (Scatter) chart with X as a value axis, and the second chart is a line chart with X as a category axis.

![todo:image_alt_text](compare.png)

The following sample code generates the [output Excel file](XAxis.xlsx).

## **Sample Code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "X-axis-vs-category-axis.java" >}}
{{< app/cells/assistant language="java" >}}
