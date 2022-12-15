---
title: Visa eller dölj radkolumnrubriker i rubin
type: docs
weight: 20
url: /sv/java/display-or-hide-row-column-headers-in-ruby/
---
## **Aspose.Cells - Visa eller dölj radkolumnrubriker**
### **Döljer rad-/kolumnrubriker**
För att dölja rad-/kolumnrubriker med hjälp av**Aspose.Cells Java för Ruby** , ringa upp**DisplayHideRowColumnHeaders** modul.

**Ruby kod**

{{< highlight "ruby" >}}

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
### **Gör rad-/kolumnrubriker synliga**
Gör rad- och kolumnrubriker synliga genom att använda arbetsbladsklassens setRowColumnHeadersVisible(true) metod.

**Ruby kod**

{{< highlight "ruby" >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Ladda ner Running Code**
Ladda ner**Visa eller dölj radkolumnrubriker (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
