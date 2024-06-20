---
title: Visa eller dölj flikar i Ruby
type: docs
weight: 40
url: /sv/java/display-or-hide-tabs-in-ruby/
---

## **Aspose.Cells - Visa eller dölj flikar**
### **Gömma flikar**
För att dölja flikar med **Aspose.Cells Java för Ruby**, anropa modulen **displayhidetabs**.

**Ruby-kod**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Göra flikar synliga**
Gör flikar synliga med klassen Workbook metod setSheetTabBarHidden(false).

**Ruby-kod**

{{< highlight ruby >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Dölj eller visa flikar (Aspose.Cells)** från någon av sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
