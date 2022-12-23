---
title: 在 Ruby 中将工作表转换为 SVG
type: docs
weight: 70
url: /zh/java/converting-worksheet-to-svg-in-ruby/
---
## **Aspose.Cells - 将工作表转换为 SVG**
要在 Ruby 中使用 Aspose.Cells for Java 将工作表转换为 SVG，只需调用工作表_到_Converter 模块的 svg() 方法。

**红宝石代码**

{{< highlight "ruby" >}}

定义工作表_到_svg（工作簿）

# 在单个页面中将每个工作表转换为 svg 格式。

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new

save_format = Rjb::import('com.aspose.cells.SaveFormat')

图片_options.setSaveFormat(保存_格式.SVG)

img_options.setOnePagePerSheet(真)



# 将每个工作表转换成svg格式

sheet_count = workbook.getWorksheets().getCount()

我=0

当我< sheet_count

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
下载**将工作表转换为 SVG (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
