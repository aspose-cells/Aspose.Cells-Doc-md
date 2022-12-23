---
title: Conversione del foglio di lavoro in immagine in Ruby
type: docs
weight: 60
url: /it/java/converting-worksheet-to-image-in-ruby/
---
## **Aspose.Cells - Conversione del foglio di lavoro in immagine**
Per convertire il foglio di lavoro in immagine utilizzando Aspose.Cells for Java in Ruby, è sufficiente richiamare il modulo Convertitore.

**Codice Rubino**

{{< highlight "ruby" >}}

 foglio di lavoro def_a_immagine (cartella di lavoro)

#Crea un oggetto per ImageOptions

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new



# Imposta il tipo di immagine

image_format = Rjb::import('com.aspose.cells.ImageFormat')

imm_opzioni.setImageFormat(image_formato.getPng())



# Ottieni il primo foglio di lavoro.

foglio = cartella di lavoro.getWorksheets().get(0)

# Crea un oggetto SheetRender per il foglio di destinazione

sr = Rjb::import('com.aspose.cells.SheetRender').new(foglio, img_options)



j = 0

 mentre j< sr.getPageCount()

        # Generate an image for the worksheet

        sr.toImage(j, @data_dir + "mysheetimg_#{j}.png")

        j +=1

    end

    puts "Image saved successfully."

end 

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scaricamento**Conversione del foglio di lavoro in immagine (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
