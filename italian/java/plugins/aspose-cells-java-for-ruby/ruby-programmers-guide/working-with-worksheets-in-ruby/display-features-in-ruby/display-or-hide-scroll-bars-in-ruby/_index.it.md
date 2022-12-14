---
title: Mostra o nascondi le barre di scorrimento in Ruby
type: docs
weight: 30
url: /it/java/display-or-hide-scroll-bars-in-ruby/
---
## **Aspose.Cells - Mostra o nascondi le barre di scorrimento**
### **Nascondere le barre di scorrimento**
 Per nascondere le barre di scorrimento utilizzando**Aspose.Cells Java per Rubino** , chiamata**displayhidescrollbars** modulo.

**Codice Rubino**

{{< highlight "ruby" >}}

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
Rendi visibili le barre di scorrimento impostando i metodi setVerticalScrollBarHidden() o setHorizontalScrollBarHidden() della classe Workbook su true.

**Codice Rubino**

{{< highlight "ruby" >}}

 # Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true)

\# Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true)

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica**Visualizzare o nascondere le barre di scorrimento (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidescrollbars.rb)
