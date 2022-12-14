---
title: Masquer ou afficher une feuille de calcul dans Python
type: docs
weight: 50
url: /fr/java/hide-or-unhide-a-worksheet-in-python/
---
## **Aspose.Cells - Masquer ou afficher une feuille de calcul**
### **Masquer une feuille de calcul**
 Pour masquer la feuille de calcul en utilisant Aspose.Cells Java pour Ruby, appelez**masquerafficher la feuille de travail** module.

**Code Python**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the first worksheet of the Excel file

worksheet.setVisible(True)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Affichage d'une feuille de calcul**
Les développeurs peuvent rendre une feuille de calcul visible en définissant le*setVisible(* *vrai* *)*méthode de la**Feuille de travail**classer.

**Code Python**

{{< highlight "python" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Masquer ou afficher une feuille de calcul (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
