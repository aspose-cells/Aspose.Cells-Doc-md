---
title: Conversion en fichiers MHTML en Python
type: docs
weight: 30
url: /fr/java/converting-to-mhtml-files-in-python/
---

## **Aspose.Cells - Conversion en MHTML**
Pour convertir une feuille de calcul en fichier MHTML en utilisant Aspose.Cells for Java en Python, il suffit d'appeler la méthode worksheet_to_mhtml() du module Converter.

**Code Python**

{{< highlight java >}}

 saveFormat = self.SaveFormat

#Specify the file path

filePath = self.dataDir + "Book1.xlsx"

#Specify the HTML saving options

sv = self.HtmlSaveOptions(saveFormat.M_HTML)

#Instantiate a workbook and open the template XLSX file

wb = self.Workbook(filePath)

#Save the MHT file

wb.save(filePath + ".out.mht", sv)

\# Print message

print "Excel to MHTML conversion performed successfully."

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Conversion en MHTML (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
