+++
title = "Display or Hide Gridlines in Ruby" 
description = "" 
weight = 24711 
+++

Aspose.Cells for Java : Display or Hide Gridlines in Ruby  

# Aspose.Cells for Java : Display or Hide Gridlines in Ruby


## Aspose.Cells - Display or Hide Gridlines

##### Hiding Gridlines

To hide worksheet using **Aspose.Cells Java for Ruby**, call **displayhidegridlines** module.

**Ruby Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'# Instantiating a Workbook object by excel file pathworkbook = Rjb::import('com.aspose.cells.Workbook').new(data\_dir + 'Book1.xls')# Accessing the first worksheet in the Excel fileworksheets = workbook.getWorksheets()sheet\_index = worksheets.add()worksheet = worksheets.get(sheet\_index)# Hiding the gridlines of the first worksheet of the Excel fileworksheet.setGridlinesVisible(false)# Saving the modified Excel file in default (that is Excel 2003) formatworkbook.save(data\_dir + "output.xls")puts "Gridlines are now hidden, please check the output file."

##### Making Gridlines Visible

To make gridlines visible, use the the`Worksheet`class'`setGridlinesVisible(true)`method.

**Ruby Code**

\# Displaying the gridlines of the worksheetworksheet.setGridlinesVisible(true)

## Download Running Code

Download **Display or Hide Gridlines (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)

