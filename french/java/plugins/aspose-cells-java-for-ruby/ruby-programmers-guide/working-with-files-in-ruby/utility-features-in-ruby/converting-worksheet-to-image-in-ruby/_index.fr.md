---
title: Conversion d'une feuille de calcul en image dans Ruby
type: docs
weight: 60
url: /fr/java/converting-worksheet-to-image-in-ruby/
---
## **Aspose.Cells - Conversion de la feuille de calcul en image**
Pour convertir une feuille de calcul en image à l'aide de Aspose.Cells for Java dans Ruby, appelez simplement le module Converter.

**Code rubis**

{{< highlight "ruby" >}}

 feuille de travail def_à_image (classeur)

#Créer un objet pour ImageOptions

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new



# Définir le type d'image

image_format = Rjb :: import('com.aspose.cells.ImageFormat')

image_options.setImageFormat(image_format.getPng())



# Obtenez la première feuille de calcul.

feuille = classeur.getWorksheets().get(0)

# Créer un objet SheetRender pour la feuille cible

sr = Rjb :: import('com.aspose.cells.SheetRender').new(sheet, img_options)



j = 0

 tandis que j< sr.getPageCount()

        # Generate an image for the worksheet

        sr.toImage(j, @data_dir + "mysheetimg_#{j}.png")

        j +=1

    end

    puts "Image saved successfully."

end 

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Conversion d'une feuille de calcul en image (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
