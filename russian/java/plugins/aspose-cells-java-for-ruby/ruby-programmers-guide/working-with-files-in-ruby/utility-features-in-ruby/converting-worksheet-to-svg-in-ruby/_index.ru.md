---
title: Преобразование Листа в SVG в Ruby
type: docs
weight: 70
url: /ru/java/converting-worksheet-to-svg-in-ruby/
---

## **Aspose.Cells - Преобразование Листа в SVG**
Чтобы преобразовать Лист в SVG, используя Aspose.Cells for Java в Ruby, просто вызовите метод worksheet_to_svg() модуля Converter.

**Код на Ruby**

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
## **Скачать работающий код**
Загрузите **Преобразование Листа в SVG (Aspose.Cells)** с любого из указанных ниже сайтов для социального программирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
