---
title: Conversion de fichiers Excel en PDF dans Ruby
type: docs
weight: 30
url: /fr/java/converting-excel-to-pdf-files-in-ruby/
---
## **Aspose.Cells - Conversion de fichiers Excel en fichiers PDF**
Pour convertir Excel en fichier Pdf en utilisant Aspose.Cells for Java dans Ruby, appelez simplement Excel_à_méthode pdf() du module Converter.

**Code rubis**

{{< highlight "ruby" >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Conversion de fichiers Excel en fichiers PDF (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
