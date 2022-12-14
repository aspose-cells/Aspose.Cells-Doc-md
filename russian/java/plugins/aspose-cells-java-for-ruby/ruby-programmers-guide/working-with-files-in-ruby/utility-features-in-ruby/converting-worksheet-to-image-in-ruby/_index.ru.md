---
title: Преобразование рабочего листа в изображение в Ruby
type: docs
weight: 60
url: /ru/java/converting-worksheet-to-image-in-ruby/
---
## **Aspose.Cells - Преобразование рабочего листа в изображение**
Чтобы преобразовать рабочий лист в изображение с помощью Aspose.Cells for Java в Ruby, просто вызовите модуль Converter.

**Рубиновый код**

{{< highlight "ruby" >}}

 рабочий лист определения_к_изображение (книга)

#Создать объект для ImageOptions

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').новый



# Установить тип изображения

image_format = Rjb::import('com.aspose.cells.ImageFormat')

изображение_options.setImageFormat (изображение_формат.getPng())



# Получить первый рабочий лист.

лист = рабочая книга.getWorksheets().get(0)

# Создайте объект SheetRender для целевого листа

sr = Rjb::import('com.aspose.cells.SheetRender').new(лист, img_options)



j = 0

 в то время как j< sr.getPageCount()

        # Generate an image for the worksheet

        sr.toImage(j, @data_dir + "mysheetimg_#{j}.png")

        j +=1

    end

    puts "Image saved successfully."

end 

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Преобразование рабочего листа в изображение (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
