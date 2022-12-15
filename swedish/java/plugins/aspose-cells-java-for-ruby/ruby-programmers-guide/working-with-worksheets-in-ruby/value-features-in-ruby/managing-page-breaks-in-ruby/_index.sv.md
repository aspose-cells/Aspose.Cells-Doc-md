---
title: Hantera sidbrytningar i Ruby
type: docs
weight: 20
url: /sv/java/managing-page-breaks-in-ruby/
---
## **Aspose.Cells - Hantera sidbrytningar**
### **Lägga till sidbrytningar**
 För att lägga till sidbrytningar med hjälp av**Aspose.Cells Java för Ruby** , ringa upp**add_page_breaks** metod av**sidbrytningar** modul. Nedan kan du se kodexempel.

**Ruby kod**

{{< highlight "ruby" >}}

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
### **Rensa alla sidbrytningar**
 För att rensa alla sidbrytningar med**Aspose.Cells Java för Ruby** , ringa upp**rensa_alla_sidebrytningar** metod av**sidbrytningar** modul. Nedan kan du se kodexempel.

**Ruby kod**

{{< highlight "ruby" >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **Ta bort specifik sidbrytning**
 För att ta bort specifik sidbrytning med**Aspose.Cells Java för Ruby** , ringa upp**remove_page_break** metod av**sidbrytningar** modul. Nedan kan du se kodexempel.

**Ruby kod**

{{< highlight "ruby" >}}

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
## **Ladda ner Running Code**
Ladda ner**Hantera sidbrytningar (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
