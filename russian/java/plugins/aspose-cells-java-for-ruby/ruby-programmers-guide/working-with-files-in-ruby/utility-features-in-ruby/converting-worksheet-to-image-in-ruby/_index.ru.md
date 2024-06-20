---
title: Преобразование Листа в изображение в Ruby
type: docs
weight: 60
url: /ru/java/converting-worksheet-to-image-in-ruby/
---

## **Aspose.Cells - Преобразование Листа в изображение**
Чтобы преобразовать Лист в изображение, используя Aspose.Cells for Java в Ruby, просто вызовите модуль Converter.

**Код на Ruby**

{{< highlight ruby >}}

 def worksheet_to_image(workbook)

    #Create an object for ImageOptions

    img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new



    # Set the image type

    image_format = Rjb::import('com.aspose.cells.ImageFormat')

    img_options.setImageFormat(image_format.getPng())



    # Get the first worksheet.

    sheet = workbook.getWorksheets().get(0)

    # Create a SheetRender object for the target sheet

    sr = Rjb::import('com.aspose.cells.SheetRender').new(sheet, img_options)



    j = 0

    while j < sr.getPageCount()

        # Generate an image for the worksheet

        sr.toImage(j, @data_dir + "mysheetimg_#{j}.png")

        j +=1

    end

    puts "Image saved successfully."

end 

{{< /highlight >}}
## **Скачать работающий код**
Загрузите **Преобразование Листа в изображение (Aspose.Cells)** с любого из указанных ниже сайтов для социального программирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
