---
title: Conversione di Excel in file PDF in Ruby
type: docs
weight: 30
url: /it/java/converting-excel-to-pdf-files-in-ruby/
---
## **Aspose.Cells - Conversione di Excel in file PDF**
Per convertire Excel in file Pdf usando Aspose.Cells for Java in Ruby, basta invocare excel_a_pdf() del modulo Converter.

**Codice Rubino**

{{< highlight "ruby" >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scaricamento**Conversione di Excel in file PDF (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
