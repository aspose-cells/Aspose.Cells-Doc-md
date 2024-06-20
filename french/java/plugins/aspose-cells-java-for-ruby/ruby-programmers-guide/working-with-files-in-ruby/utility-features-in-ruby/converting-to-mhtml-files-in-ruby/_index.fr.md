---
title: Conversion en fichiers MHTML en Ruby
type: docs
weight: 50
url: /fr/java/converting-to-mhtml-files-in-ruby/
---

## **Aspose.Cells - Conversion en fichiers MHTML**
Pour convertir une feuille de calcul en fichier MHTML en utilisant Aspose.Cells for Java en Ruby, il suffit d'invoquer la méthode worksheet_to_mhtml() du module Convertisseur.

**Code Ruby**

{{< highlight ruby >}}

 def worksheet_to_mhtml(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    sv = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "convert.mht", sv)

    puts "MHTML saved successfully."

end

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Converting to MHTML Files (Aspose.Cells)** depuis l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
