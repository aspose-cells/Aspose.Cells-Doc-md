---
title: How to set point as total with Golang via C++
linktitle: How to set point as total
description: In some Excel chart, for example, waterFall chart, you may need to set point as total. This article describes how to use Aspose.Cells with Golang via C++ to do it.
keywords: WaterFall Chart, Point, Set as total.
type: docs
weight: 72
url: /go-cpp/how-to-set-point-as-total/
---

## What is "Set point as total" in Excel Chart

In some Excel chart, for example, waterFall chart, some point data are the sum of the previous points, you may need to "set point as total". We will show the sample code and the illustration below.

## A waterFall Chart need to "Set point as total" 

![todo:image_alt_text](set-as-total1.png)

This picture shows a waterFall chart in Excel. We can see that there are four data points starting with "Total", And they are used to count all the previous data points.
In this picture, the settings are not exactly right, when we select a point "Total 2024" and we can see that the "Set as total" option is not checked in the Excel.
Attached below is the [sample Excel file](SampleSheet.xlsx) that needs to be modified, and we will use Aspose.Cells to set it up correctly.

## Use Aspose.Cells to "Set point as total" 

We use the following code to get the file set up correctly:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-HowToSetPointAsTotal.go" >}}
You can get the following correct [output file](output.xlsx)

As shown in the figure below, the four "Total" data points are set correctly, and you can see the difference from the previous chart.

![todo:image_alt_text](set-as-total2.png)