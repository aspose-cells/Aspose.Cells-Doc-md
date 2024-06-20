---
title: Anzeigen oder Ausblenden von Bildlaufleisten in Ruby
type: docs
weight: 30
url: /de/java/display-or-hide-scroll-bars-in-ruby/
---

## **Aspose.Cells - Scrollleisten anzeigen oder ausblenden**
### **Verbergen von Bildlaufleisten**
Um Bildlaufleisten mit **Aspose.Cells Java für Ruby** auszublenden, rufen Sie das Modul **displayhidescrollbars** auf.

**Ruby-Code**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false)

\# Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Scroll Bars are now hidden, please check the output file."

{{< /highlight >}}
### **Sichtbarkeit von Bildlaufleisten herstellen**
Machen Sie die Bildlaufleisten sichtbar, indem Sie die Methoden setVerticalScrollBarHidden() oder setHorizontalScrollBarHidden() der Klasse Workbook auf true setzen.

**Ruby-Code**

{{< highlight ruby >}}

 # Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true)

\# Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true)

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Anzeigen oder Ausblenden von Bildlaufleisten (Aspose.Cells)** von einer der unten aufgeführten Social-Coding-Sites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)
