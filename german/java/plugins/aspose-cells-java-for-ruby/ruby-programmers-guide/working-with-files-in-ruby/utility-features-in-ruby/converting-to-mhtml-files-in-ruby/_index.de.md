---
title: Konvertierung in MHTML Dateien in Ruby
type: docs
weight: 50
url: /de/java/converting-to-mhtml-files-in-ruby/
---

## **Aspose.Cells - Konvertierung in MHTML-Dateien**
Um ein Arbeitsblatt in einer MHTML-Datei mit Aspose.Cells for Java in Ruby zu konvertieren, rufen Sie einfach die Methode worksheet_to_mhtml() des Converter-Moduls auf.

**Ruby-Code**

{{< highlight ruby >}}

 def worksheet_to_mhtml(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    sv = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "convert.mht", sv)

    puts "MHTML saved successfully."

end

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie **Konvertierung in MHTML-Dateien (Aspose.Cells)** von einer der unten aufgeführten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
