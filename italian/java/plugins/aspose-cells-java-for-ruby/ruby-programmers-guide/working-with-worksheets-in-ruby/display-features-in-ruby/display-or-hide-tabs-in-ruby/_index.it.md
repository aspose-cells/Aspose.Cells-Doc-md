---
title: Mostra o nascondi le schede in Ruby
type: docs
weight: 40
url: /it/java/display-or-hide-tabs-in-ruby/
---
## **Aspose.Cells - Mostra o nascondi schede**
### **Nascondere le schede**
 Per nascondere le schede utilizzando**Aspose.Cells Java per Rubino** , chiamata**displayhidetabs** modulo.

**Codice Rubino**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Rendere visibili le schede**
Rendi visibili le schede con il metodo setSheetTabBarHidden(false) della classe Workbook.

**Codice Rubino**

{{< highlight "ruby" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scaricamento**Nascondi o mostra o nascondi schede (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidetabs.rb)
