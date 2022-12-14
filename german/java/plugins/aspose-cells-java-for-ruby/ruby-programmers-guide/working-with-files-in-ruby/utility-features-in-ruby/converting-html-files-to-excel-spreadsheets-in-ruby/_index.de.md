---
title: Konvertieren von HTML-Dateien in Excel-Tabellen in Ruby
type: docs
weight: 40
url: /de/java/converting-html-files-to-excel-spreadsheets-in-ruby/
---
## **Aspose.Cells – Konvertieren von HTML-Dateien in Excel-Tabellen**
Um HTML in Spreadsheet mit Aspose.Cells for Java in Ruby zu konvertieren, rufen Sie einfach html auf_zu_excel()-Methode des Converter-Moduls.

**Ruby-Code**

{{< highlight "ruby" >}}

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
## **Laufcode herunterladen**
Download**Konvertieren von HTML-Dateien in Excel-Tabellen (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
