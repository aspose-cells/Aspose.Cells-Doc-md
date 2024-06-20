---
title: Konvertierung von HTML Dateien in Excel Tabellenkalkulationen in Ruby
type: docs
weight: 40
url: /de/java/converting-html-files-to-excel-spreadsheets-in-ruby/
---

## **Aspose.Cells - Konvertierung von HTML-Dateien in Excel-Tabellenkalkulationen**
Um HTML mit Aspose.Cells for Java in Ruby in eine Tabellenkalkulation zu konvertieren, rufen Sie einfach die Methode html_to_excel() des Converter-Moduls auf.

**Ruby-Code**

{{< highlight ruby >}}

 def html_to_excel()

    load_format = Rjb::import('com.aspose.cells.LoadFormat')

    # Create an instance of HTMLLoadOptions and initiate it with appropriate LoadFormat

    options = Rjb::import('com.aspose.cells.HTMLLoadOptions').new(load_format.HTML)



    # Load the Html file through file path while passing the instance of HTMLLoadOptions class

    workbook = Rjb::import('com.aspose.cells.Workbook').new(@data_dir + "index.html", options)



    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    #Save the results to disc in Xlsx format

    workbook.save(@data_dir + "output.xlsx", save_format.XLSX)

    puts "XLSX saved successfully."

end

{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie die **Konvertierung von HTML-Dateien in Excel-Tabellenkalkulationen (Aspose.Cells)** von einer der unten genannten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
