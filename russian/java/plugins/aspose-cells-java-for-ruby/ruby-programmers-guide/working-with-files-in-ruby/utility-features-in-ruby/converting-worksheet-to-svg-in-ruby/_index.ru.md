---
title: Преобразование рабочего листа в SVG в Ruby
type: docs
weight: 70
url: /ru/java/converting-worksheet-to-svg-in-ruby/
---
## **Aspose.Cells - Преобразование рабочего листа в SVG**
Чтобы преобразовать рабочий лист в SVG, используя Aspose.Cells for Java в Ruby, просто вызовите рабочий лист_к_Метод svg() модуля Converter.

**Рубиновый код**

{{< highlight "ruby" >}}

 рабочий лист определения_к_svg (книга)

# Преобразование каждого рабочего листа в формат svg на одной странице.

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').новый

save_format = Rjb::import('com.aspose.cells.SaveFormat')

изображение_options.setSaveFormat (сохранить_формат.SVG)

img_options.setOnePagePerSheet (истина)



Конвертируем каждый рабочий лист в формат svg

sheet_count = рабочая книга.getWorksheets().getCount()

я=0

 в то время как я< sheet_count

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
## **Скачать рабочий код**
Скачать**Преобразование рабочего листа в SVG (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
