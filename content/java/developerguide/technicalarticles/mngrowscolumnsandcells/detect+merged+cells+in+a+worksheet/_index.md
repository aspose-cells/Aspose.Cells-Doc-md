---
title : "Detect Merged Cells in a Worksheet" 
description : "" 
weight : 16448 
toc : false
type: docs
url: /java/developerguide/technicalarticles/mngrowscolumnsandcells/detect+merged+cells+in+a+worksheet/
---

# Aspose.Cells for Java : Detect Merged Cells in a Worksheet


In Microsoft Excel, several cells can be merged into one. This is often used to create complex tables or to create a cell that holds a heading that spans several columns.

Aspose.Cells allows you to identify merged cell areas in a worksheet. You can unmerge them too. This article provides the simplest lines of code for performing the task using Aspose.Cells.

This article provides compact instructions on how to find and then unmerge merged cells in a worksheet.

### Demonstration

This example uses a template Microsoft Excel file called **MergeTrial**. It has some merged cell areas in a sheet also called Merge Trial.  
  
**The template file**  
![image](5472889.png)

Aspose.Cells provides the [Cells.getMergedCells](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#MergedCells) method which is used to get an ArrayList of merged cell areas.

When the code below is executed, it clears the contents of the sheet and unmerges all the cell areas before saving the file again.  
  
**The Output File**  
![image](5472888.png)

### Code Example

Please see the following sample code to find how to identify merged cell areas in a worksheet and unmerge them.


#### Related Articles

*   [Merging and splitting cells](https://docs2.aspose.com/cells/java/developerguide/data/merging+and+unmerging+cells).

