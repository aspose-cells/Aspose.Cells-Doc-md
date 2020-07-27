+++
title = "Zoom Factor in Ruby" 
description = "" 
weight = 24719 
+++

Aspose.Cells for Java : Zoom Factor in Ruby  

# Aspose.Cells for Java : Zoom Factor in Ruby


## Aspose.Cells - Zoom Factor

To set Zoom Factor using **Aspose.Cells Java for Ruby**, simply invoke **ZoomFactor** module.

**Ruby Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'# Instantiating a Workbook object by excel file pathworkbook = Rjb::import('com.aspose.cells.Workbook').new(data\_dir + 'Book1.xls')# Accessing the first worksheet in the Excel fileworksheets = workbook.getWorksheets()worksheet = worksheets.get(0)# Setting the zoom factor of the worksheet to 75     worksheet.setZoom(75)# Saving the modified Excel file in default (that is Excel 2003) formatworkbook.save(data\_dir + "output.xls")puts "Set zoom factor, please check the output file."

## Download Running Code

Download **Zoom Factor (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/zoomfactor.rb)

