---
title: Konvertierung von Excel in PDF Dateien in Ruby
type: docs
weight: 30
url: /de/java/converting-excel-to-pdf-files-in-ruby/
---

## **Aspose.Cells - Konvertierung von Excel in PDF-Dateien**
Um Excel mit Aspose.Cells for Java in Ruby in eine Pdf-Datei zu konvertieren, rufen Sie einfach die Methode excel_to_pdf() des Converter-Moduls auf.

**Ruby-Code**

{{< highlight ruby >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie die **Konvertierung von Excel in PDF-Dateien (Aspose.Cells)** von einer der unten genannten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
