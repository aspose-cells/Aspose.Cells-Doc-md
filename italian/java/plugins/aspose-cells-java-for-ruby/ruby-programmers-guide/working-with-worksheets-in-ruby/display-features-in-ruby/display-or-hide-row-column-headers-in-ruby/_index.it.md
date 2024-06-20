---
title: Mostra o nascondi gli header riga colonna in Ruby
type: docs
weight: 20
url: /it/java/display-or-hide-row-column-headers-in-ruby/
---

## **Aspose.Cells - Mostra o Nascondi gli header riga colonna**
### **Nascondere le intestazioni di riga/colonna**
Per nascondere gli header di riga/colonna usando **Aspose.Cells Java per Ruby**, chiamare il modulo **DisplayHideRowColumnHeaders**.

**Codice Ruby**

{{< highlight ruby >}}

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
Rendi visibili header di riga e colonna utilizzando il metodo `setRowColumnHeadersVisible(true)` della classe `Worksheet`.

**Codice Ruby**

{{< highlight ruby >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Visualizza o Nascondi Intestazioni Righe o Colonne (Aspose.Cells)** da uno dei siti di codice sociale sotto indicati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhiderowcolumnheaders.rb)
