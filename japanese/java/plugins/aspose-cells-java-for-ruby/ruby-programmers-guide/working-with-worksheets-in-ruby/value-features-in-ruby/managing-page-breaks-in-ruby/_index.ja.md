---
title: Ruby で改ページを管理する
type: docs
weight: 20
url: /ja/java/managing-page-breaks-in-ruby/
---
## **Aspose.Cells - 改ページの管理**
### **改ページの追加**
を使用して改ページを追加するには**Aspose.Cells Ruby の場合は Java**、 電話**add_page_breaks**方法**改ページ**モジュール。以下にコード例を示します。

**ルビーコード**

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
### **すべての改ページのクリア**
を使用してすべての改ページをクリアするには**Aspose.Cells Ruby の場合は Java**、 電話**clear_all_page_breaks**方法**改ページ**モジュール。以下にコード例を示します。

**ルビーコード**

{{< highlight "ruby" >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **特定の改ページの削除**
を使用して特定の改ページを削除するには**Aspose.Cells Ruby の場合は Java**、 電話**remove_page_break**方法**改ページ**モジュール。以下にコード例を示します。

**ルビーコード**

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
## **実行中のコードをダウンロード**
ダウンロード**改ページの管理 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
