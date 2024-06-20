---
title: Dölj eller visa en arbetsbok i Ruby
type: docs
weight: 60
url: /sv/java/hide-or-unhide-a-worksheet-in-ruby/
---

## **Aspose.Cells - Dölj eller visa en arbetsbok**
### **Dölja ett arbetsblad**
För att dölja arbetsbladet med Aspose.Cells Java för Ruby, anropa modulen **hideunhideworksheet**.

**Ruby-kod**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Hiding the first worksheet of the Excel file

worksheet.setVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Visa ett arbetsblad**
Utvecklare kan göra ett arbetsblad synligt genom att ställa in *setVisible(* *true* *)* metoden för klassen **Worksheet**.

**Ruby-kod**

{{< highlight ruby >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Dölj eller visa arbetsblad (Aspose.Cells)** från någon av sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
