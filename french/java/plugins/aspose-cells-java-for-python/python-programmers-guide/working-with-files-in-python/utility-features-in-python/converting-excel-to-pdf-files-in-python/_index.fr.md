---
title: Conversion de fichiers Excel en PDF en Python
type: docs
weight: 20
url: /fr/java/converting-excel-to-pdf-files-in-python/
---

## **Aspose.Cells - Conversion d'Excel en Pdf**
Pour convertir Excel en fichier Pdf en utilisant Aspose.Cells for Java en Python, il suffit d'appeler la méthode excel_to_pdf() du module Converter.

**Code Python**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Conversion d'Excel en Pdf (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
