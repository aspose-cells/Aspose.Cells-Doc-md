---
title: Afficher ou masquer le quadrillage dans Python
type: docs
weight: 10
url: /fr/java/display-or-hide-gridlines-in-python/
description: Découvrez comment afficher ou masquer le quadrillage via le Aspose.Cells for Python via Java API.
keywords: How to Display or Hide Gridlines in Python Via Java, Display or Hide Gridlines using Python Via Java, Python Show or Hide Gridlines. 
---
##  **Aspose.Cells - Comment afficher ou masquer le quadrillage**
###  **Comment masquer le quadrillage**
 Pour masquer une feuille de calcul en utilisant**Aspose.Cells Java pour Ruby**, appelez **displayhidegridlines** module.

**Python Code**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

# Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
###  **Comment afficher le quadrillage**
Pour rendre le quadrillage visible, utilisez la méthode setGridlinesVisible(true) de la classe Worksheet.

**Python Code**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
##  **Télécharger le code d'exécution**
 Télécharger**AfficherMasquer les lignes de grille (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
