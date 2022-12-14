---
title: Conversion en fichiers MHTML dans Ruby
type: docs
weight: 50
url: /fr/java/converting-to-mhtml-files-in-ruby/
---
## **Aspose.Cells - Conversion en fichiers MHTML**
Pour convertir une feuille de calcul en fichier MHTML à l'aide de Aspose.Cells for Java dans Ruby, appelez simplement la feuille de calcul_à_méthode mhtml() du module Convertisseur.

**Code rubis**

{{< highlight "ruby" >}}

 def worksheet_to_mhtml(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    sv = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "convert.mht", sv)

    puts "MHTML saved successfully."

end

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Conversion en fichiers MHTML (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
