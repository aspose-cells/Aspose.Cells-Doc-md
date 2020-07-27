+++
title = "Hide or Unhide a Worksheet in Ruby" 
description = "" 
weight = 24716 
+++

Aspose.Cells for Java : Hide or Unhide a Worksheet in Ruby  

# Aspose.Cells for Java : Hide or Unhide a Worksheet in Ruby


## Aspose.Cells - Hide or Unhide a Worksheet

##### Hiding a Worksheet

To hide worksheet using Aspose.Cells Java for Ruby, call **hideunhideworksheet** module.

**Ruby Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'# Instantiating a Workbook object by excel file pathworkbook = Rjb::import('com.aspose.cells.Workbook').new(data\_dir + 'Book1.xls')# Accessing the first worksheet in the Excel fileworksheets = workbook.getWorksheets()worksheet = worksheets.get(0)# Hiding the first worksheet of the Excel fileworksheet.setVisible(false)# Saving the modified Excel file in default (that is Excel 2003) formatworkbook.save(data\_dir + "output.xls")puts "Worksheet 1 is now hidden, please check the output document."

##### Showing a Worksheet

Developers can make a worksheet visible by setting the*setVisible(**true**)*method of the**Worksheet**class.

**Ruby Code**

\# Displaying the worksheet of the Excel fileworksheet.setVisible(true)

## Download Running Code

Download **Hide or Unhide a Worksheet (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)

