+++
title = "Display or Hide Scroll Bars in Ruby" 
description = "" 
weight = 24713 
+++

Aspose.Cells for Java : Display or Hide Scroll Bars in Ruby  

# Aspose.Cells for Java : Display or Hide Scroll Bars in Ruby


## Aspose.Cells - Display or Hide Scroll Bars

##### Hiding Scroll Bars

To hide Scroll Bars using **Aspose.Cells Java for Ruby**, call **displayhidescrollbars** module.

**Ruby Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'# Instantiating a Workbook object by excel file pathworkbook = Rjb::import('com.aspose.cells.Workbook').new(data\_dir + 'Book1.xls')# Hiding the vertical scroll bar of the Excel fileworkbook.getSettings().setVScrollBarVisible(false)# Hiding the horizontal scroll bar of the Excel fileworkbook.getSettings().setHScrollBarVisible(false)# Saving the modified Excel file in default (that is Excel 2003) formatworkbook.save(data\_dir + "output.xls")puts "Scroll Bars are now hidden, please check the output file."

##### Making Scroll Bars Visible

Make scroll bars visible by setting the`Workbook`class'`setVerticalScrollBarHidden()`or`setHorizontalScrollBarHidden()`methods to true.

**Ruby Code**

\# Displaying the vertical scroll bar of the Excel fileworkbook.getSettings().setVScrollBarVisible(true)# Displaying the horizontal scroll bar of the Excel fileworkbook.getSettings().setHScrollBarVisible(true)

## Download Running Code

Download **Display or Hide Scroll Bars (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)

