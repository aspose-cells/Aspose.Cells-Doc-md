---
title: Afficher ou masquer les barres de défilement en Python
type: docs
weight: 20
url: /fr/java/display-or-hide-scroll-bars-in-python/
---

## **Aspose.Cells - Afficher ou Masquer les barres de défilement**
### **Masquer les entêtes de ligne/colonne**
Pour masquer les en-têtes de lignes/colonnes en utilisant **Aspose.Cells Java pour Python**, appelez le module **AfficherMasquerEnTeteLigneColonne**.

**Code Python**

{{< highlight python >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(False)

#Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(False)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Scroll bars are now hidden, please check the output document."

{{< /highlight >}}
### **Rendre les entêtes de ligne/colonne visibles**
Rendez les en-têtes de lignes et de colonnes visibles en utilisant la méthode **setRowColumnHeadersVisible(true)** de la classe **Worksheet**.

**Code Python**

{{< highlight python >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Hello World (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
