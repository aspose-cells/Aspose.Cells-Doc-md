---
title: Conversion de fichiers Excel en HTML en Python
type: docs
weight: 10
url: /fr/java/converting-excel-files-to-html-in-python/
---

## **Aspose.Cells - Conversion de fichier Excel en HTML**
Pour convertir Excel en HTML en utilisant Aspose.Cells for Java en Python, il suffit d'appeler la méthode worksheet_to_html() du module Converter.

**Code Python**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Conversion de fichier Excel en HTML (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
