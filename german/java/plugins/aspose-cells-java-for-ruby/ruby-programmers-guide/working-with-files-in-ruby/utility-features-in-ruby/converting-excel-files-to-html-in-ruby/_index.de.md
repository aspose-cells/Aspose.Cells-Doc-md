---
title: Konvertieren von Excel-Dateien in HTML in Ruby
type: docs
weight: 20
url: /de/java/converting-excel-files-to-html-in-ruby/
---
## **Aspose.Cells – Konvertieren von Excel-Dateien in HTML**
Um Excel mit Aspose.Cells for Java in Ruby in HTML umzuwandeln, rufen Sie einfach worksheet auf_zu_html()-Methode des Converter-Moduls.

**Ruby-Code**

{{< highlight "ruby" >}}

 def worksheet_to_html(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    save = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "output.html", save)

    puts "HTML saved successfully."

end 

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Konvertieren von Excel-Dateien in HTML (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
