+++
title = "Split Panes in Ruby" 
description = "" 
weight = 24718 
+++

Aspose.Cells for Java : Split Panes in Ruby  

# Aspose.Cells for Java : Split Panes in Ruby


## Aspose.Cells - Split Panes

To Split Panes using **Aspose.Cells Java for Ruby**, simply invoke **SplitPanes** module.

**Ruby Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'# Instantiating a Workbook object by excel file pathworkbook = Rjb::import('com.aspose.cells.Workbook').new(data\_dir + 'Book1.xls')# Set the active cellworkbook.getWorksheets().get(0).setActiveCell("A20")# Split the worksheet windowworkbook.getWorksheets().get(0).split()# Saving the modified Excel file in default (that is Excel 2003) formatworkbook.save(data\_dir + "SplitPanes output.xls")puts "Panes split successfully."

## Download Running Code

Download **Split Panes (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/splitpanes.rb)

