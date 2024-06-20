---
title: Déprotéger une feuille de calcul en Python
type: docs
weight: 20
url: /fr/java/unprotect-a-worksheet-in-python/
---

## **Aspose.Cells - Déverrouiller une feuille de calcul**
Pour déprotéger la feuille de calcul à l'aide d'**Aspose.Cells Java pour Python**, appelez la méthode **unprotect_worksheet** du module **protection**.

**Code Python**

{{< highlight java >}}

 filesFormatType = self.FileFormatType

#Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

protection = worksheet.getProtection()

#The following 3 methods are only for Excel 2000 and earlier formats

protection.setAllowEditingContent(False)

protection.setAllowEditingObject(False)

protection.setAllowEditingScenario(False)

#Unprotecting the worksheet

worksheet.unprotect()

\# Save the excel file.

workbook.save(self.dataDir + "output.xls", filesFormatType.EXCEL_97_TO_2003)

#Print Message

print "Worksheet unprotected successfully."

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Déprotéger une feuille de calcul (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
