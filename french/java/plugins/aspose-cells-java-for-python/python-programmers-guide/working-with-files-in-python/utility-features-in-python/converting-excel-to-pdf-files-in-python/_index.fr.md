---
title: Conversion d'Excel en fichiers PDF dans Python
type: docs
weight: 20
url: /fr/java/converting-excel-to-pdf-files-in-python/
---
## **Aspose.Cells - Conversion d'Excel en PDF**
Pour convertir Excel en fichier Pdf en utilisant Aspose.Cells for Java en Python, appelez simplement Excel_à_méthode pdf() du module Converter.

**Code Python**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Conversion d'Excel en PDF (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
