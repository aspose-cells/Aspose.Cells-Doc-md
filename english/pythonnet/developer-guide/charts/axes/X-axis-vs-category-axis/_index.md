---
title: X Axis Vs. Category Axis
description: Learn how to differentiate between the X axis and the Category axis in Aspose.Cells for Python via .NET. Our guide will help you understand the differences in their usage and properties, and how to configure them according to your needs.
keywords: Aspose.Cells for Python via .NET, X axis, Category axis, difference, usage, properties, configuration.
type: docs
weight: 180
url: /python-net/X-axis-vs-category-axis/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
There are different types of X axes. While the Y axis is a Value type axis, the X axis can be a Category type axis or a Value type axis. When using a Value axis, the data is treated as continuously varying numerical data, and the marker is placed at a point along the axis which varies according to its numerical value. When using a Category axis, the data is treated as a sequence of non‑numerical text labels, and the marker is placed at a point along the axis according to its position in the sequence. The sample below illustrates the difference between Value and Category Axes.  
Our sample data is shown in the [sample table file](sample.png) below. The first column contains our X‑axis data, which can be treated as Categories or as Values. Note that the numbers are not equally spaced, nor do they even appear in numerical order.

![todo:image_alt_text](sample.png)

## **Handle X and Category Axes like Microsoft Excel**
We will display this data on two types of charts: the first chart is an XY (Scatter) chart with X as a Value Axis, and the second chart is a line chart with X as a Category Axis.

![todo:image_alt_text](compare.png)

## **Sample Code**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-X-axis-vs-category-axis.py" >}}
{{< app/cells/assistant language="python-net" >}}
