---
title: 在 Ruby 中取消保护工作表
type: docs
weight: 20
url: /zh/java/unprotect-a-worksheet-in-ruby/
---
## **Aspose.Cells - 取消保护工作表**
保护工作表使用**Aspose.Cells Java 红宝石**， 称呼**取消保护工作表**的方法**保护**模块。

**红宝石代码**

{{< highlight "ruby" >}}

 def unprotect_worksheet()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    worksheet = worksheets.get(0)

    protection = worksheet.getProtection()

    # The following 3 methods are only for Excel 2000 and earlier formats

    protection.setAllowEditingContent(false)

    protection.setAllowEditingObject(false)

    protection.setAllowEditingScenario(false)

    # Unprotecting the worksheet with a password

    worksheet.unprotect("1234")



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Unprotect Worksheet.xls")

    puts "Unprotect a Worksheet, please check the output file."

end   

{{< /highlight >}}
## **下载运行代码**
下载**取消保护工作表 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/protection.rb)
