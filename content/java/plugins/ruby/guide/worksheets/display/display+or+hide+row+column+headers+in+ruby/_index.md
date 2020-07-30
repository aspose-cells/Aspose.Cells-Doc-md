---
title : "Display or Hide Row Column Headers in Ruby" 
description : "" 
weight : 24712 
toc : false
type: docs
url: /java/plugins/ruby/guide/worksheets/display/display+or+hide+row+column+headers+in+ruby/
---

# Aspose.Cells for Java : Display or Hide Row Column Headers in Ruby


## Aspose.Cells - Display or Hide Row Column Headers

##### Hiding Row/Column Headers

To hide row/column headers using **Aspose.Cells Java for Ruby**, call **DisplayHideRowColumnHeaders** module.

**Ruby Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'# Instantiating a Workbook object by excel file pathworkbook = Rjb::import('com.aspose.cells.Workbook').new(data\_dir + 'Book1.xls')# Accessing the first worksheet in the Excel fileworksheets = workbook.getWorksheets()sheet\_index = worksheets.add()worksheet = worksheets.get(sheet\_index)# Hiding the headers of rows and columnsworksheet.setRowColumnHeadersVisible(false)# Saving the modified Excel file in default (that is Excel 2003) formatworkbook.save(data\_dir + "output.xls")puts "Headers of rows and columns are now hidden, please check the output file."

##### Making Row/Column Headers Visible

Make row and column headers visible by using the`Worksheet`class'`setRowColumnHeadersVisible(true)`method.

**Ruby Code**

\# Displaying the headers of rows and columnsworksheet.setRowColumnHeadersVisible(true)

## Download Running Code

Download **Display or Hide Row Column Headers (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)

