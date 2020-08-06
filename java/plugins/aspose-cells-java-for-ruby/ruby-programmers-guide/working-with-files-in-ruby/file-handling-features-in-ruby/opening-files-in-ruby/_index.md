---
title: Opening Files in Ruby
type: docs
weight: 10
url: /java/opening-files-in-ruby/
---

## **Aspose.Cells - Simple Ways to Open Excel Files**
##### **Opening through Path**
Simply open a Microsoft Excel file by referencing the file's path

**Ruby Code**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
##### **Opening through Stream**
Sometimes, the Excel file that you want to open is stored as a stream. In that case, use an overloaded version of the Open method that takes the Stream object that contains the Excel file to open the file.

**Ruby Code**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
