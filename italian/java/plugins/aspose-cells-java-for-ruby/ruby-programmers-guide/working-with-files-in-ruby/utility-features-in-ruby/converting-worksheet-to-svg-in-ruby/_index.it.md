---
title: Conversione del foglio di lavoro in SVG in Ruby
type: docs
weight: 70
url: /it/java/converting-worksheet-to-svg-in-ruby/
---
## **Aspose.Cells - Conversione foglio di lavoro in SVG**
Per convertire il foglio di lavoro in SVG utilizzando Aspose.Cells for Java in Ruby, è sufficiente richiamare il foglio di lavoro_a_svg() metodo del modulo Converter.

**Codice Rubino**

{{< highlight "ruby" >}}

 foglio di lavoro def_a_svg (cartella di lavoro)

# Converti ogni foglio di lavoro in formato svg in una singola pagina.

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new

save_format = Rjb::import('com.aspose.cells.SaveFormat')

imm_opzioni.setSaveFormat(salva_formato.SVG)

img_options.setOnePagePerSheet(true)



# Converti ogni foglio di lavoro in formato svg

sheet_count = workbook.getWorksheets().getCount()

io=0

 mentre io< sheet_count

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
Scarica**Conversione del foglio di lavoro in SVG (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
