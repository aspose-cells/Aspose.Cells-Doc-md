---
title: Conversion de la feuille de calcul en SVG en Ruby
type: docs
weight: 70
url: /fr/java/converting-worksheet-to-svg-in-ruby/
---
## **Aspose.Cells - Conversion de la feuille de travail en SVG**
Pour convertir la feuille de calcul en SVG en utilisant Aspose.Cells for Java dans Ruby, appelez simplement la feuille de calcul_à_Méthode svg() du module Converter.

**Code rubis**

{{< highlight "ruby" >}}

 feuille de travail def_à_svg (classeur)

# Convertissez chaque feuille de calcul au format svg en une seule page.

img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new

save_format = Rjb :: import('com.aspose.cells.SaveFormat')

image_options.setSaveFormat(sauvegarder_format.SVG)

img_options.setOnePagePerSheet(true)



# Convertir chaque feuille de calcul au format svg

sheet_count = classeur.getWorksheets().getCount()

je=0

 alors que je< sheet_count

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
## **Télécharger le code d'exécution**
Télécharger**Conversion de la feuille de calcul en SVG (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
