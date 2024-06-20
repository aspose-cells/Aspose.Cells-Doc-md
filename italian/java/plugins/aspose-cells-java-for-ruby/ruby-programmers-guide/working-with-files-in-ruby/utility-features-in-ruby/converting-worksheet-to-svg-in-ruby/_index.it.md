---
title: Conversione di un foglio di lavoro in SVG in Ruby
type: docs
weight: 70
url: /it/java/converting-worksheet-to-svg-in-ruby/
---

## **Aspose.Cells - Conversione di un foglio di lavoro in SVG**
Per convertire un foglio di lavoro in SVG utilizzando Aspose.Cells for Java in Ruby, basta invocare il metodo worksheet_to_svg() del modulo Converter.

**Codice Ruby**

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
## **Scarica il codice in esecuzione**
Scarica **Conversione di un foglio di lavoro in SVG (Aspose.Cells)** da uno qualsiasi dei siti di codice sociale sotto elencati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
