---
title: Excel Dateien in HTML in Ruby konvertieren
type: docs
weight: 20
url: /de/java/converting-excel-files-to-html-in-ruby/
---

## **Aspose.Cells - Konvertierung von Excel-Dateien in HTML**
Um Excel mit Aspose.Cells for Java in Ruby nach HTML zu konvertieren, rufen Sie einfach die Methode worksheet_to_html() des Converter-Moduls auf.

**Ruby-Code**

{{< highlight ruby >}}

 def worksheet_to_html(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    save = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "output.html", save)

    puts "HTML saved successfully."

end 

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie die **Konvertierung von Excel-Dateien in HTML (Aspose.Cells)** von einer der unten genannten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
