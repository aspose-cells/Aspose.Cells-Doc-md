---
title: Anteprima dell'interruzione di pagina in Ruby
type: docs
weight: 70
url: /it/java/page-break-preview-in-ruby/
---
## **Aspose.Cells - Anteprima interruzione di pagina**
 Per impostare il foglio di lavoro sull'anteprima dell'interruzione di pagina utilizzando**Aspose.Cells Java per Rubino** , semplicemente invocare**Anteprima interruzione di pagina** modulo.

**Codice Rubino**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(true)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Set page break preview, please check the output file."

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica**Anteprima interruzione di pagina (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreakpreview.rb)
