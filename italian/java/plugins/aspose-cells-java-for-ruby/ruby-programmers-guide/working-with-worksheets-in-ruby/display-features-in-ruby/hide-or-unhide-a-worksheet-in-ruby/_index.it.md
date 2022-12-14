---
title: Nascondere o mostrare un foglio di lavoro in Ruby
type: docs
weight: 60
url: /it/java/hide-or-unhide-a-worksheet-in-ruby/
---
## **Aspose.Cells - Nascondi o mostra un foglio di lavoro**
### **Nascondere un foglio di lavoro**
 Per nascondere il foglio di lavoro utilizzando Aspose.Cells Java per Ruby, chiama**hideunhideworksheet** modulo.

**Codice Rubino**

{{< highlight "ruby" >}}

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
### **Mostrando un foglio di lavoro**
Gli sviluppatori possono rendere visibile un foglio di lavoro impostando l'estensione*setVisibile(* *VERO* *)*metodo del**Foglio di lavoro**classe.

**Codice Rubino**

{{< highlight "ruby" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica**Nascondere o scoprire un foglio di lavoro (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/hideunhideworksheet.rb)
