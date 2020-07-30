---
title : "Merge Files" 
description : "" 
weight : 12235 
toc : false
type: docs
url: /java/developerguide/helper/merge+files/
---

# Aspose.Cells for Java : Merge Files


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Introduction](#introduction)
*   2 [Merge Files Using Aspose.Cells](#merge-files-using-aspose.cells)
{{< /panel >}}
 

## Introduction

Aspose.Cells provides different ways for merging files. For simple files with data, formatting, and formulas, the [Workbook.combine()](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook)) method can be used to combine several workbooks, and the [Worksheet.copy()](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)) method can be used to copy worksheets into a new workbook. These methods are easy to use and effective, but if you have a lot of files to merge, you might find that they take a lot of system resources. To avoid this, use the CellsHelper.mergeFiles static method, a more efficient way to merge several files.

## Merge Files Using Aspose.Cells

The following sample code illustrates how to merge large files using the CellsHelper.mergeFiles method. It takes two simple but large files, MyBook1.xls and MyBook2.xls. The files contain formatted data and formulas only.

The CellsHelper.mergeFiles method only supports merging data, styles, formatting, and formulas. Objects like charts, pictures, comments or other objects might not be merged using this method. Moreover, a cached file is used to store temporary data for the process.

