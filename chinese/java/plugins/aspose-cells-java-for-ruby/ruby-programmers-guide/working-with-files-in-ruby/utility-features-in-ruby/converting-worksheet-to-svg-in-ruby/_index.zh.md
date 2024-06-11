---
title: 在Ruby中将工作表转换为SVG
type: docs
weight: 70
url: /zh/java/converting-worksheet-to-svg-in-ruby/
---

## **Aspose.Cells - 将工作表转换为SVG**
使用Ruby中的Aspose.Cells for Java将工作表转换为SVG，只需调用Converter模块的worksheet_to_svg()方法。

**Ruby 代码**

{{< highlight ruby >}}

 def worksheet_to_svg(workbook)

    # Convert each worksheet into svg format in a single page.

    img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    img_options.setSaveFormat(save_format.SVG)

    img_options.setOnePagePerSheet(true)



    # Convert each worksheet into svg format

    sheet_count = workbook.getWorksheets().getCount()

    i=0

    while i < sheet_count

        sheet = workbook.getWorksheets().get(i)

        sr = Rjb::import('com.aspose.cells.SheetRender').new(sheet, img_options)

        k=0

        while sr.getPageCount()

            # Output the worksheet into Svg image format

            sr.toImage(k, @data_dir + sheet.getName() + "#{k}.svg")

        end

    end

    puts "SVG saved successfully."

end 

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**将工作表转换为SVG（Aspose.Cells）**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
