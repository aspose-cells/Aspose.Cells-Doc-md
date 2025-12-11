---  
title: Public API Changes in Aspose.Cells 8.2.0  
type: docs  
weight: 80  
url: /java/public-api-changes-in-aspose-cells-8-2-0/  
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

This document describes changes to the Aspose.Cells API from version 8.1.2 to 8.2.0 which may be of interest to module/application developers. It includes not only new and updated public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.  

{{% /alert %}}  

## **Added MultiThreadReading Property for Cells Class**  
With Aspose.Cells for Java 8.2.0, the MultiThreadReading property has been added to the Cells class in order to provide a more robust mechanism to read cell values with multiple threads simultaneously. Setting the Boolean‑type property to true in a multi‑threaded application makes sure that each thread receives the correct cell value.  

{{% alert color="primary" %}}  

Please check the detailed article on [Simultaneously Read Cell Values in a Multi‑Threaded Environment](/cells/java/reading-cell-values-in-multiple-threads-simultaneously/) for more information.  

{{% /alert %}}  

## **Added Overloads for autoFitRows and autoFitColumns Methods**  
New overloads for autoFitRows and autoFitColumns have been added to the Worksheet class, allowing developers to autofit the rows and columns based on their respective ranges by passing an instance of the AutoFitterOptions class.  

The signatures of the aforementioned methods are as follows:  

1. `autoFitRows(int startRow, int endRow, AutoFitterOptions options)`  
2. `autoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)`  

{{% alert color="primary" %}}  

Please check the detailed article on [Auto Fit Rows and Columns](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).  

{{% /alert %}}  

{{< app/cells/assistant language="java" >}}
