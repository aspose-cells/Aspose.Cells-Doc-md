---
title: Ruby de Sayfa Kesmelerini Yönetme
type: docs
weight: 20
url: /tr/java/managing-page-breaks-in-ruby/
---

## **Aspose.Cells - Sayfa Kesmelerini Yönetme**
### **Sayfa Kesmeleri Eklemek**
Ruby için  **Aspose.Cells Java** kullanarak sayfa kesmeleri eklemek için, **pagebreaks** modülünün **add_page_breaks** yöntemini çağırın. Aşağıda örnek kodu görebilirsiniz.

**Ruby Kodu**

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
### **Tüm Sayfa Kesmelerini Temizleme**
Ruby için  **Aspose.Cells Java** kullanarak tüm sayfa kesmelerini temizlemek için, **pagebreaks** modülünün **clear_all_page_breaks** yöntemini çağırın. Aşağıda örnek kodu görebilirsiniz.

**Ruby Kodu**

{{< highlight ruby >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **Belirli Sayfa Kesmelerini Kaldırma**
Ruby için  **Aspose.Cells Java** kullanarak belirli sayfa kesmesini kaldırmak için, **pagebreaks** modülünün **remove_page_break** yöntemini çağırın. Aşağıda örnek kodu görebilirsiniz.

**Ruby Kodu**

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
## **Çalışan Kodu İndir**
Aşağıdaki sosyal kodlama sitelerinden herhangi birinden **Sayfa Kesmelerini Yönetme (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
