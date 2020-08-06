---
title: Display or Hide Row Column Headers in Ruby
type: docs
weight: 20
url: /java/display-or-hide-row-column-headers-in-ruby/
---

## **Aspose.Cells - Display or Hide Row Column Headers**
##### **Hiding Row/Column Headers**
To hide row/column headers using **Aspose.Cells Java for Ruby**, call **DisplayHideRowColumnHeaders** module.

**Ruby Code**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Hiding the headers of rows and columns

worksheet.setRowColumnHeadersVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Headers of rows and columns are now hidden, please check the output file."

{{< /highlight >}}
##### **Making Row/Column Headers Visible**
Make row and column headers visible by using the Worksheet class' setRowColumnHeadersVisible(true) method.

**Ruby Code**

{{< highlight ruby >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Download Running Code**
Download **Display or Hide Row Column Headers (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
