---
title: Protéger les feuilles de calcul en Python
type: docs
weight: 10
url: /fr/java/protecting-worksheets-in-python/
---

## **Aspose.Cells - Protection des feuilles de calcul**
Pour protéger la feuille de calcul à l'aide d'**Aspose.Cells Java pour Python**, appelez la méthode **protect_worksheet** du module **protection**.

**Code Python**

{{< highlight java >}}

 #Instantiating a Excel object by excel file path

excel = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = excel.getWorksheets()

worksheet = worksheets.get(0)

protection = worksheet.getProtection()

#The following 3 methods are only for Excel 2000 and earlier formats

protection.setAllowEditingContent(False)

protection.setAllowEditingObject(False)

protection.setAllowEditingScenario(False)

#Protects the first worksheet with a password "1234"

protection.setPassword("1234")

#Saving the modified Excel file in default format

excel.save(self.dataDir + "output.xls")

#Print Message

print "Sheet protected successfully."

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Protéger les feuilles de calcul (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
