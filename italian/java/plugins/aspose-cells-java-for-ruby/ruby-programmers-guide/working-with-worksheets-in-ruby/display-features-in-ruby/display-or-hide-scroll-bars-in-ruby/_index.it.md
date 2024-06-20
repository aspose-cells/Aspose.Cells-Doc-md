---
title: Visualizza o Nascondi Barre di Scorrimento in Ruby
type: docs
weight: 30
url: /it/java/display-or-hide-scroll-bars-in-ruby/
---

## **Aspose.Cells - Visualizza o Nascondi Barre di Scorrimento**
### **Nascondere le barre di scorrimento**
Per nascondere le Barre di Scorrimento usando **Aspose.Cells Java per Ruby**, chiama il modulo **displayhidescrollbars**.

**Codice Ruby**

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
### **Rendere visibili le barre di scorrimento**
Rendi le barre di scorrimento visibili impostando i metodi setVerticalScrollBarHidden() o setHorizontalScrollBarHidden() della classe Workbook su true.

**Codice Ruby**

{{< highlight ruby >}}

 # Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true)

\# Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true)

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Visualizza o Nascondi Barre di Scorrimento (Aspose.Cells)** da uno dei siti di codice sociale sotto indicati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)
