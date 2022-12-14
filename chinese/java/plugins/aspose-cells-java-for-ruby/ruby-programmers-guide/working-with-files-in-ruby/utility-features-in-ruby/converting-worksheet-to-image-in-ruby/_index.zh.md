---
title: 在 Ruby 中将工作表转换为图像
type: docs
weight: 60
url: /zh/java/converting-worksheet-to-image-in-ruby/
---
## **Aspose.Cells - 将工作表转换为图像**
要在 Ruby 中使用 Aspose.Cells for Java 将工作表转换为图像，只需调用 Converter 模块。

**红宝石代码**

{{< highlight "ruby" >}}

定义工作表_至_图片（工作簿）

#为ImageOptions创建一个对象

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new



# 设置图片类型

image_format = Rjb::import('com.aspose.cells.ImageFormat')

图片_options.setImageFormat（图像_格式.getPng())



# 获取第一个工作表。

sheet = workbook.getWorksheets().get(0)

# 为目标工作表创建一个 SheetRender 对象

sr = Rjb::import('com.aspose.cells.SheetRender').new(sheet, img_options)



j = 0

而j< sr.getPageCount()

        # Generate an image for the worksheet

        sr.toImage(j, @data_dir + "mysheetimg_#{j}.png")

        j +=1

    end

    puts "Image saved successfully."

end 

{{< /highlight >}}
## **下载运行代码**
下载**将工作表转换为图像 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
