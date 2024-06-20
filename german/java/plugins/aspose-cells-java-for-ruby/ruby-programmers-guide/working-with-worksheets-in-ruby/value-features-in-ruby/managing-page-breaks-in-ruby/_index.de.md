---
title: Seitenumbrüche verwalten in Ruby
type: docs
weight: 20
url: /de/java/managing-page-breaks-in-ruby/
---

## **Aspose.Cells - Seitenumbrüche verwalten**
### **Seitenumbrüche hinzufügen**
Um Seitenumbrüche mit **Aspose.Cells Java für Ruby** hinzuzufügen, rufen Sie die Methode **add_page_breaks** des Moduls **pagebreaks** auf. Im Folgenden finden Sie ein Codebeispiel.

**Ruby-Code**

{{< highlight ruby >}}

 def add_page_breaks(workbook)

    worksheets = workbook.getWorksheets()

    worksheet = worksheets.get(0)

    h_page_breaks = worksheet.getHorizontalPageBreaks()

    h_page_breaks.add("Y30")



    v_page_breaks = worksheet.getVerticalPageBreaks()

    v_page_breaks.add("Y30")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Add Page Breaks.xls")

    puts "Add page breaks, please check the output file."

end   

{{< /highlight >}}
### **Alle Seitenumbrüche löschen**
Um alle Seitenumbrüche mit **Aspose.Cells Java for Ruby** zu löschen, rufen Sie die Methode **clear_all_page_breaks** des Moduls **pagebreaks** auf. Im Folgenden finden Sie ein Codebeispiel.

**Ruby-Code**

{{< highlight ruby >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **Bestimmten Seitenumbruch entfernen**
Um einen bestimmten Seitenumbruch mit **Aspose.Cells Java for Ruby** zu entfernen, rufen Sie die Methode **remove_page_break** des Moduls **pagebreaks** auf. Im Folgenden finden Sie ein Codebeispiel.

**Ruby-Code**

{{< highlight ruby >}}

 def remove_page_break(workbook)

    worksheets = workbook.getWorksheets()

    worksheet = worksheets.get(0)



    h_page_breaks = worksheet.getHorizontalPageBreaks()

    h_page_breaks.removeAt(0)



    v_page_breaks = worksheet.getVerticalPageBreaks()

    v_page_breaks.removeAt(0)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Remove Page Break.xls")

    puts "Remove page break, please check the output file."

end 

{{< /highlight >}}
## **Laufenden Code herunterladen**
**Seitenumbrüche verwalten (Aspose.Cells)** von einer der unten genannten Plattformen für soziale Programmierung herunterladen:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
