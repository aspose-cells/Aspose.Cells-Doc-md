---
title: Nascondi o Mostra un Foglio in Ruby
type: docs
weight: 60
url: /it/java/hide-or-unhide-a-worksheet-in-ruby/
---

## **Aspose.Cells - Nascondi o Mostra un Foglio**
### **Nascondere un foglio di lavoro**
Per nascondere il foglio utilizzando Aspose.Cells Java per Ruby, chiama il modulo **hideunhideworksheet**.

**Codice Ruby**

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
### **Visualizzazione di un Foglio**
Gli sviluppatori possono rendere visibile un foglio impostando il metodo *setVisible(true)* della classe **Worksheet**.

**Codice Ruby**

{{< highlight ruby >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Nascondi o Mostra un Foglio (Aspose.Cells)** da uno dei siti di codice sociale sotto indicati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
