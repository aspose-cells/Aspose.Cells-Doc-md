---
title : "Opening Files in Ruby" 
description : "" 
weight : 24697 
toc : false
type: docs
url: /java/plugins/ruby/guide/files/filehandling/opening+files+in+ruby/
---

# Aspose.Cells for Java : Opening Files in Ruby


## Aspose.Cells - Simple Ways to Open Excel Files

##### Opening through Path

Simply open a Microsoft Excel file by referencing the file's path

**Ruby Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'workbook = Rjb::import('com.aspose.cells.Workbook').new(data\_dir + 'Book1.xls')

##### Opening through Stream

Sometimes, the Excel file that you want to open is stored as a stream. In that case, use an overloaded version of the`Open`method that takes the`Stream`object that contains the Excel file to open the file.

**Ruby Code**

data\_dir = File.dirname(File.dirname(File.dirname(\_\_FILE\_\_))) + '/data/'fstream = IO.sysopen(@data\_dir + 'Book1.xls')workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

