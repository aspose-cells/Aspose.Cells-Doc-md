---
title: 在Ruby中设置页面选项
type: docs
weight: 10
url: /zh/java/setting-page-options-in-ruby/
---

## **Aspose.Cells - 设置页面选项**
### **页面方向**
要使用**Aspose.Cells Java for Ruby**应用页面方向设置，调用**pagesetup**模块的**page_orientation**方法。

**Ruby 代码**

{{< highlight ruby >}}

 def page_orientation()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    sheet = worksheets.get(sheet_index)

    # Setting the orientation to Portrait

    page_setup = sheet.getPageSetup()

    page_orientation_type = Rjb::import('com.aspose.cells.PageOrientationType')

    page_setup.setOrientation(page_orientation_type.PORTRAIT)



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Page Orientation.xls")

    puts "Set page orientation, please check the output file."

end   

{{< /highlight >}}
### **缩放因子**
要使用**Aspose.Cells Java for Ruby**应用缩放，调用**pagesetup**模块的**scaling**方法。

**Ruby 代码**

{{< highlight ruby >}}

 def scaling()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    sheet = worksheets.get(sheet_index)

    # Setting the scaling factor to 100

    page_setup = sheet.getPageSetup()

    page_setup.setZoom(100)



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Scaling.xls")

    puts "Set scaling, please check the output file."

end


{{< /highlight >}}
## **下载运行代码**
从下面提到的任何社交编码网站下载**Setting Page Options (Aspose.Cells)**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagesetup.rb)
