---
title: Frys rutor i Ruby
type: docs
weight: 50
url: /sv/java/freeze-panes-in-ruby/
---

## **Aspose.Cells - Frys rutor**
För att frysa rutor i kalkyldokumentet med **Aspose.Cells Java för Ruby**, ange helt enkelt modulen **FreezePanes**.

**Ruby-kod**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Apply freeze panes settings, please check the output file."

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Frys rutor (Aspose.Cells)** från någon av sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/freezepanes.rb)
