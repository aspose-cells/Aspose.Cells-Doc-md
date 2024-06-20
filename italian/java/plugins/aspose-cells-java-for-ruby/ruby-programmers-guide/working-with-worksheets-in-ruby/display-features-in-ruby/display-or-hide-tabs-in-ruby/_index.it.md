---
title: Visualizza o Nascondi Schede in Ruby
type: docs
weight: 40
url: /it/java/display-or-hide-tabs-in-ruby/
---

## **Aspose.Cells - Visualizza o Nascondi Schede**
### **Nascondere le schede**
Per nascondere le schede usando **Aspose.Cells Java per Ruby**, chiama il modulo **displayhidetabs**.

**Codice Ruby**

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
### **Rendere visibili le schede con il metodo {1} della classe {0}.**
Rendi le schede visibili con il metodo setSheetTabBarHidden(false) della classe Workbook.

**Codice Ruby**

{{< highlight ruby >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Nascondi o Visualizza o Nascondi Schede (Aspose.Cells)** da uno dei siti di codice sociale sotto indicati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
