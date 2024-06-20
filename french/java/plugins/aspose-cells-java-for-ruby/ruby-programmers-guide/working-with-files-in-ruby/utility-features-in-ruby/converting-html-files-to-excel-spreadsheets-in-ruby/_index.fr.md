---
title: Conversion de fichiers HTML en feuilles de calcul Excel en Ruby
type: docs
weight: 40
url: /fr/java/converting-html-files-to-excel-spreadsheets-in-ruby/
---

## **Aspose.Cells - Conversion de fichiers HTML en feuilles de calcul Excel**
Pour convertir HTML en feuille de calcul en utilisant Aspose.Cells for Java en Ruby, il suffit d'invoquer la méthode html_to_excel() du module Convertisseur.

**Code Ruby**

{{< highlight ruby >}}

 def html_to_excel()

    load_format = Rjb::import('com.aspose.cells.LoadFormat')

    # Create an instance of HTMLLoadOptions and initiate it with appropriate LoadFormat

    options = Rjb::import('com.aspose.cells.HTMLLoadOptions').new(load_format.HTML)



    # Load the Html file through file path while passing the instance of HTMLLoadOptions class

    workbook = Rjb::import('com.aspose.cells.Workbook').new(@data_dir + "index.html", options)



    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    #Save the results to disc in Xlsx format

    workbook.save(@data_dir + "output.xlsx", save_format.XLSX)

    puts "XLSX saved successfully."

end

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Conversion de fichiers HTML en feuilles de calcul Excel (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
