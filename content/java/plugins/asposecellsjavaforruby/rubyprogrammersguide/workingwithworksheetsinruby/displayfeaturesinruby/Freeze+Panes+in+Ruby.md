+++
title = "Freeze Panes in Ruby" 
description = "" 
weight = 24715 
+++

Aspose.Cells for Java : Freeze Panes in Ruby  

# Aspose.Cells for Java : Freeze Panes in Ruby


## Aspose.Cells - Freeze Panes

To Freeze Panes in the Spreadsheet Document using **Aspose.Cells Java for Ruby**, simply invoke **FreezePanes** module.

**Ruby Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'# Instantiating a Workbook object by excel file pathworkbook = Rjb::import('com.aspose.cells.Workbook').new(data\_dir + 'Book1.xls')# Accessing the first worksheet in the Excel fileworksheets = workbook.getWorksheets()worksheet = worksheets.get(0)# Applying freeze panes settingsworksheet.freezePanes(3,2,3,2)# Saving the modified Excel file in default (that is Excel 2003) formatworkbook.save(data\_dir + "output.xls")puts "Apply freeze panes settings, please check the output file."

## Download Running Code

Download **Freeze Panes (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/freezepanes.rb)

