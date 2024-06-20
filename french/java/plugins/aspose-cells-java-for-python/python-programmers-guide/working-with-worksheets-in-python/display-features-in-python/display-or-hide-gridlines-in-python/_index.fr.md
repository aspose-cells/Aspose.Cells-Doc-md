---
title: Afficher ou masquer les grilles en Python
type: docs
weight: 10
url: /fr/java/display-or-hide-gridlines-in-python/
description: Apprenez à afficher ou masquer les grilles via l API Java Aspose.Cells pour Python.
keywords: Comment afficher ou masquer les grilles en Python via Java, afficher ou masquer les grilles en utilisant Python via Java, Python afficher ou masquer les grilles. 
---

## **Aspose.Cells - Comment afficher ou masquer les grilles**
### **Comment masquer les grilles**
Pour masquer une feuille de calcul en utilisant **Aspose.Cells Java pour Ruby**, appelez le module **displayhidegridlines**.

**Code Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

#Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
### **Comment afficher les grilles**
Pour rendre les lignes de grille visibles, utilisez la méthode **setGridlinesVisible(true)** de la classe **Worksheet**.

**Code Python**

{{< highlight python >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **AfficherMasquerGrilles (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
