---
title: Conversion de fichiers Excel en HTML dans Ruby
type: docs
weight: 20
url: /fr/java/converting-excel-files-to-html-in-ruby/
---
## **Aspose.Cells - Conversion de fichiers Excel en HTML**
Pour convertir Excel en HTML en utilisant Aspose.Cells for Java dans Ruby, appelez simplement la feuille de calcul_à_méthode html() du module Convertisseur.

**Code rubis**

{{< highlight "ruby" >}}

 def worksheet_to_html(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Specify the HTML saving options

    save = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document

    workbook.save(@data_dir + "output.html", save)

    puts "HTML saved successfully."

end 

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Conversion de fichiers Excel en HTML (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
