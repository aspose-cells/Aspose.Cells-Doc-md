---
title: Rubyでページの区切りを管理する
type: docs
weight: 20
url: /ja/java/managing-page-breaks-in-ruby/
---

## **Aspose.Cells - ページの区切りを管理する**
### **ページブレークの追加**
**Aspose.Cells Java for Ruby**を使用してページ区切りを追加するには、**pagebreaks**モジュールの**add_page_breaks**メソッドを呼び出します。以下にコード例があります。

**Ruby Code**

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
### **すべてのページの改ページをクリアする**
**Aspose.Cells Java for Ruby**を使用して全てのページ区切りをクリアするには、**pagebreaks**モジュールの**clear_all_page_breaks**メソッドを呼び出します。以下にコード例があります。

**Ruby Code**

{{< highlight ruby >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **特定の改ページを削除する**
Aspose.Cells Java for Rubyで特定の改ページを削除するには、**pagebreaks**モジュールの**remove_page_break**メソッドを呼び出します。以下にコード例を示します。

**Ruby Code**

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
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから**Managing Page Breaks (Aspose.Cells)**をダウンロードしてください。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
