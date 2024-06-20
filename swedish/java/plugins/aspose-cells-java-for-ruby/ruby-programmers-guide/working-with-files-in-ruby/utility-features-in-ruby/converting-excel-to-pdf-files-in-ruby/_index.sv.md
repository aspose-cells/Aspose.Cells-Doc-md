---
title: Konvertera Excel till PDF filer i Ruby
type: docs
weight: 30
url: /sv/java/converting-excel-to-pdf-files-in-ruby/
---

## **Aspose.Cells - Konvertera Excel till PDF-filer**
För att konvertera Excel till Pdf-fil med Aspose.Cells for Java i Ruby, helt enkelt anropa excel_to_pdf() metoden i Converter modulen.

**Ruby-kod**

{{< highlight ruby >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Konvertera Excel till PDF-filer (Aspose.Cells)** från någon av de sociala kodningssidorna som nämns nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
