---
title: How to set Series invisible with Golang via C++
linktitle: How to set Series invisible
description: In Excel chart, you may need to set a series invisible. This article describes how to use Aspose.Cells with Golang via C++ to do it.
keywords: Excel chart, Series, Invisible, IsFiltered.
type: docs
weight: 74
url: /go-cpp/how-to-set-series-invisible/
---

## How to set series invisible in Excel Chart

In an Excel chart, you can right‑click a chart, click **Select Data**, and in the pop‑up window, you can set whether a series is visible by checking or unchecking it. You can download the following [sample file](SeriesFiltered.xlsx) and use it in Excel as shown in the figure to achieve this function. Next, we will tell you how to achieve this using the Aspose.Cells library.

![todo:image_alt_text](series-invisible.png)

## How to set series invisible using Aspose.Cells 

We use the following code to set a series invisible using Aspose.Cells:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetSeriesInvisible.go" >}}
You can get the following [Input file](SeriesFiltered.xlsx) and [output file](output.xlsx).

As shown in the figure below, the first two series, which were originally visible, have become invisible in the output file.  
![todo:image_alt_text](output.png)