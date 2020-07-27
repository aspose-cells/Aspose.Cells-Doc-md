+++
title = "Saving Files in Ruby" 
description = "" 
weight = 24698 
+++

Aspose.Cells for Java : Saving Files in Ruby  

# Aspose.Cells for Java : Saving Files in Ruby


## Aspose.Cells - Saving Files

##### Saving file to some location

If developers need to save their files using **Aspose.Cells Java for Ruby** to some storage location then they can simply specify the file name (with its complete storage path) and desired file format (using the**FileFormatType**enumeration) while calling the**save**method of**Workbook**object.

**Ruby Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'file\_format\_type = Rjb::import('com.aspose.cells.FileFormatType')# Save in default (Excel2003) formatworkbook.save(data\_dir + "Book1.xls")#Save in Excel2003 formatworkbook.save(data\_dir + "Book1.xls", file\_format\_type.EXCEL\_97\_TO\_2003)# Save in Excel2007 xlsx formatworkbook.save(data\_dir + "Book1.xls", file\_format\_type.XLSX)# Save in SpreadsheetML formatworkbook.save(data\_dir + "Book1.xls", file\_format\_type.EXCEL\_2003\_XML)

