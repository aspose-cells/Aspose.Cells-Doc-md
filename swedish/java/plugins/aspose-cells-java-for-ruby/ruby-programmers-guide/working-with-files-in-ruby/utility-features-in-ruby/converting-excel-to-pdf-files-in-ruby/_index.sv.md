---
title: Konvertera Excel till PDF-filer i Ruby
type: docs
weight: 30
url: /sv/java/converting-excel-to-pdf-files-in-ruby/
---
## **Aspose.Cells - Konvertera Excel till PDF-filer**
För att konvertera Excel till Pdf-fil med Aspose.Cells för Java i Ruby, anropa helt enkelt excel_till_pdf()-metoden för konverteringsmodulen.

**Ruby kod**

{{< highlight "ruby" >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **Ladda ner Running Code**
Ladda ner**Konvertera Excel till PDF-filer (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
