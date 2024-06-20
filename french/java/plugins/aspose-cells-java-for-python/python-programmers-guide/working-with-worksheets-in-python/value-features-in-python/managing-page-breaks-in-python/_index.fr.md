---
title: Gérer les sauts de page en Python
type: docs
weight: 20
url: /fr/java/managing-page-breaks-in-python/
---

## **Aspose.Cells - Gérer les sauts de page**
### **Ajout de sauts de page**
Pour ajouter des sauts de page en utilisant **Aspose.Cells Java pour Ruby**, appelez la méthode **add_page_breaks** du module **pagebreaks**. Vous pouvez voir ci-dessous un exemple de code.

**Code Python**

{{< highlight python >}}

 def add_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.add("Y30")

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.add("Y30")

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Add Page Breaks.xls")

print "Add page breaks, please check the output file."


{{< /highlight >}}
### **Effacement de tous les sauts de page**
Pour effacer tous les sauts de page à l'aide d'**Aspose.Cells Java pour Python**, appelez la méthode **clear_all_page_breaks** du module **pagebreaks**. Vous pouvez voir ci-dessous un exemple de code.

**Code Python**

{{< highlight python >}}



def clear_all_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")


workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Clear All Page Breaks.xls")

print "Clear all page breaks, please check the output file."


{{< /highlight >}}
### **Supprimer un saut de page spécifique**
Pour supprimer un saut de page spécifique à l'aide d'**Aspose.Cells Java pour Python**, appelez la méthode **remove_page_break** du module **pagebreaks**. Vous pouvez voir ci-dessous un exemple de code.

**Code Python**

{{< highlight python >}}



def remove_page_break(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.removeAt(0)

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.removeAt(0)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Remove Page Break.xls")

print "Remove page break, please check the output file."


{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Gérer les sauts de page (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
