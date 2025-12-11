---
title: Public API Changes in Aspose.Cells 8.2.0
type: docs
weight: 70
url: /net/public-api-changes-in-aspose-cells-8-2-0/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes changes to the Aspose.Cells API from version 8.1.2 to 8.2.0 that may be of interest to module/application developers. It includes not only new and updated public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 

## **Added MultiThreadReading Property for the Cells Class**
With Aspose.Cells for .NET 8.2.0, the MultiThreadReading property has been added to the Cells class in order to provide a more robust mechanism to read cell values with multiple threads simultaneously. Setting the Boolean‑type property to true in a multi‑threaded application ensures that each thread will receive the correct cell value.

{{% alert color="primary" %}} 

Please check the detailed article on [Simultaneously Read Cells Values in Multi-Threaded Environment](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) for more information.

{{% /alert %}}

## **Added Overloads for AutoFitRows & AutoFitColumns Methods**
New overloads for AutoFitRows & AutoFitColumns have been added to the Worksheet class, allowing developers to auto‑fit the rows and columns based on their respective ranges while passing an instance of the AutoFitterOptions class. 

The signatures of the aforesaid methods are as follows:

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions options)  
2. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

Please check the detailed article on [Auto Fit Rows and Columns](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
