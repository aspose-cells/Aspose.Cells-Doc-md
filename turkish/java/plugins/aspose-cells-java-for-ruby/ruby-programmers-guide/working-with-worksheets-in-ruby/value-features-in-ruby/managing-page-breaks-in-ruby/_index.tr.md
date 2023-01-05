---
title: Ruby'de Sayfa Sonlarını Yönetme
type: docs
weight: 20
url: /tr/java/managing-page-breaks-in-ruby/
---
## **Aspose.Cells - Sayfa Sonlarını Yönetme**
### **Sayfa Sonları Ekleme**
 kullanarak sayfa sonları eklemek için**Yakut için Aspose.Cells Java** , Arama**add_page_breaks** yöntemi**sayfa sonları** modül. Aşağıda kod örneğini görebilirsiniz.

**Yakut Kodu**

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
### **Tüm Sayfa Sonlarını Temizleme**
 kullanarak tüm sayfa sonlarını temizlemek için**Yakut için Aspose.Cells Java** , Arama**clear_all_page_breaks** yöntemi**sayfa sonları** modül. Aşağıda kod örneğini görebilirsiniz.

**Yakut Kodu**

{{< highlight "ruby" >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **Belirli Sayfa Sonunu Kaldırma**
 Kullanarak belirli sayfa sonunu kaldırmak için**Yakut için Aspose.Cells Java** , Arama**remove_page_break** yöntemi**sayfa sonları** modül. Aşağıda kod örneğini görebilirsiniz.

**Yakut Kodu**

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
## **Çalışan Kodu İndir**
İndirmek**Sayfa Sonlarını Yönetme (Aspose.Cells)**aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
