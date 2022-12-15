---
title: Mostra o nascondi le intestazioni delle colonne delle righe in Ruby
type: docs
weight: 20
url: /it/java/display-or-hide-row-column-headers-in-ruby/
---
## **Aspose.Cells - Visualizza o nascondi le intestazioni delle colonne delle righe**
### **Nascondere le intestazioni di riga/colonna**
 Per nascondere le intestazioni di riga/colonna utilizzando**Aspose.Cells Java per Ruby** , chiamata**DisplayHideRowColumnHeaders** modulo.

**Codice Rubino**

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
### **Rendere visibili le intestazioni di riga/colonna**
Rendi visibili le intestazioni di righe e colonne utilizzando il metodo setRowColumnHeadersVisible(true) della classe Worksheet.

**Codice Rubino**

{{< highlight "ruby" >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica**Mostra o nascondi le intestazioni delle colonne delle righe (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
