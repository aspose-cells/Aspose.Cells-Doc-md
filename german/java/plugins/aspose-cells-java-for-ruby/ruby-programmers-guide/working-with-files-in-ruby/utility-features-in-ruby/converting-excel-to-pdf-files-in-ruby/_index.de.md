---
title: Konvertieren von Excel in PDF-Dateien in Ruby
type: docs
weight: 30
url: /de/java/converting-excel-to-pdf-files-in-ruby/
---
## **Aspose.Cells – Konvertieren von Excel in PDF-Dateien**
Um Excel mit Aspose.Cells for Java in Ruby in eine PDF-Datei zu konvertieren, rufen Sie einfach Excel auf_zu_pdf()-Methode des Converter-Moduls.

**Ruby-Code**

{{< highlight "ruby" >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Konvertieren von Excel in PDF-Dateien (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
