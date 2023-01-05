---
title: Konvertieren in MHTML-Dateien in Ruby
type: docs
weight: 50
url: /de/java/converting-to-mhtml-files-in-ruby/
---
## **Aspose.Cells - Konvertieren in MHTML-Dateien**
Um Worksheet mit Aspose.Cells for Java in Ruby in eine MHTML-Datei zu konvertieren, rufen Sie einfach worksheet auf_zu_mhtml()-Methode des Converter-Moduls.

**Ruby-Code**

{{< highlight "ruby" >}}

 def worksheet_to_mhtml(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    sv = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "convert.mht", sv)

    puts "MHTML saved successfully."

end

{{< /highlight >}}
## **Laufcode herunterladen**
Download**Konvertieren in MHTML-Dateien (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
