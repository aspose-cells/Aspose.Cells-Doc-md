---
title: 在 Ruby 中管理分页符
type: docs
weight: 20
url: /zh/java/managing-page-breaks-in-ruby/
---

## **Aspose.Cells - 管理分页符**
### **添加分页符**
使用 **Aspose.Cells Java for Ruby** 添加分页符，请调用 **pagebreaks** 模块的 **add_page_breaks** 方法。以下是代码示例。

**Ruby代码**

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
### **清除所有分页符**
使用 **Aspose.Cells Java for Ruby** 清除所有分页符，请调用 **pagebreaks** 模块的 **clear_all_page_breaks** 方法。以下是代码示例。

**Ruby代码**

{{< highlight ruby >}}

 def clear_all_page_breaks(workbook)

    workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

    workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "Clear All Page Breaks.xls")

    puts "Clear all page breaks, please check the output file."

end 

{{< /highlight >}}
### **移除特定分页符**
使用 **Aspose.Cells Java for Ruby** 移除特定分页符，请调用 **pagebreaks** 模块的 **remove_page_break** 方法。以下是代码示例。

**Ruby代码**

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
## **下载运行代码**
从以下任一社交编码站点下载 **Managing Page Breaks (Aspose.Cells)**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreaks.rb)
