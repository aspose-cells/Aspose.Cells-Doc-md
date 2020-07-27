+++
title = "Hello World in Ruby" 
description = "" 
weight = 20694 
+++

Aspose.Cells for Java : Hello World in Ruby  

# Aspose.Cells for Java : Hello World in Ruby


## Aspose.Cells - Hello World

To Write anything in the Spreadsheet Document using Aspose.Cells for Java in Ruby, simply invoke HelloWorld module.

**Ruby Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'# Instantiating a Workbook object that represents a Microsoft Excel file.workbook = Rjb::import('com.aspose.cells.Workbook').new# Note when you create a new workbook, a default worksheet,# "Sheet1", is by default added to the workbook.# Accessing the first worksheet in the book ("Sheet1").sheet = workbook.getWorksheets().get(0)# Access cell "A1" in the sheet.cell = sheet.getCells().get("A1")# Input the "Hello World!" text into the "A1" cellcell.setValue("Hello World!")# Saving the modified Excel file in default (that is Excel 2003) formatfile\_format\_type = Rjb::import('com.aspose.cells.FileFormatType')workbook.save(data\_dir + "HelloWorld.xls", file\_format\_type.EXCEL\_97\_TO\_2003)puts "Document has been saved, please check the output file."

## Download Running Code

Download **Hello World (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/helloworld.rb)

