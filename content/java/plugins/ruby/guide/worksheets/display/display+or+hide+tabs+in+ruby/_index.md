---
title : "Display or Hide Tabs in Ruby" 
description : "" 
weight : 24714 
toc : false
type: docs
url: /java/plugins/ruby/guide/worksheets/display/display+or+hide+tabs+in+ruby/
---

# Aspose.Cells for Java : Display or Hide Tabs in Ruby


## Aspose.Cells - Display or Hide Tabs

##### Hiding Tabs

To hide tabs using **Aspose.Cells Java for Ruby**, call **displayhidetabs** module.

**Ruby Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'# Instantiating a Workbook object by excel file pathworkbook = Rjb::import('com.aspose.cells.Workbook').new(data\_dir + 'Book1.xls')# Hiding the tabs of the Excel fileworkbook.getSettings().setShowTabs(false)# Saving the modified Excel file in default (that is Excel 2003) formatworkbook.save(data\_dir + "output.xls")puts "Tabs are now hidden, please check the output file."

##### Making Tabs Visible

Make tabs visible with the`Workbook`class'`setSheetTabBarHidden(false)`method.

**Ruby Code**

\# Displaying the tabs of the Excel fileworkbook.getSettings().setSowTabs(true)

## Download Running Code

Download **Hide or Display or Hide Tabs (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)

