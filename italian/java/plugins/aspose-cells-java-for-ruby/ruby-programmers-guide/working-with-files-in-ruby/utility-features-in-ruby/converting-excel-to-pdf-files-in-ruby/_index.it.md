---
title: Convertire file Excel in file PDF in Ruby
type: docs
weight: 30
url: /it/java/converting-excel-to-pdf-files-in-ruby/
---

## **Aspose.Cells - Conversione di file Excel in PDF**
Per convertire file Excel in file Pdf utilizzando Aspose.Cells for Java in Ruby, basta invocare il metodo excel_to_pdf() del modulo Converter.

**Codice Ruby**

{{< highlight ruby >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Conversione di file Excel in PDF (Aspose.Cells)** da uno qualsiasi dei siti di codice sociale sotto elencati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
