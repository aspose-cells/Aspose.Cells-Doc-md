---
title: تحويل ورقة العمل إلى SVG في Ruby
type: docs
weight: 70
url: /ar/java/converting-worksheet-to-svg-in-ruby/
---

## **Aspose.Cells - تحويل ورقة العمل إلى SVG**
لتحويل ورقة العمل إلى SVG باستخدام Aspose.Cells for Java في Ruby، قم ببساطة باستدعاء طريقة worksheet_to_svg() من وحدة Converter.

**كود Ruby**

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
## **تحميل رمز التشغيل**
تنزيل ** تحويل ورقة العمل إلى SVG (Aspose.Cells) ** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
