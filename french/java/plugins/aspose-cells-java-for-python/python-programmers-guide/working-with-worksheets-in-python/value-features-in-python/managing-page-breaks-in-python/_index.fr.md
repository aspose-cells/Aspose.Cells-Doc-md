---
title: Gestion des sauts de page dans Python
type: docs
weight: 20
url: /fr/java/managing-page-breaks-in-python/
---
## **Aspose.Cells - Gestion des sauts de page**
### **Ajouter des sauts de page**
 Pour ajouter des sauts de page à l'aide de**Aspose.Cells Java pour rubis** , appel**add_page_breaks** méthode de**sauts de page** module. Ci-dessous, vous pouvez voir un exemple de code.

**Code Python**

{{< highlight "python" >}}

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
### **Effacer tous les sauts de page**
 Pour effacer tous les sauts de page à l'aide de**Aspose.Cells Java for Python** , appel**clear_all_page_breaks** méthode de**sauts de page** module. Ci-dessous, vous pouvez voir un exemple de code.

**Code Python**

{{< highlight "python" >}}



def clear_all_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")


workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Clear All Page Breaks.xls")

print "Clear all page breaks, please check the output file."


{{< /highlight >}}
### **Suppression d'un saut de page spécifique**
 Pour supprimer un saut de page spécifique à l'aide de**Aspose.Cells Java for Python** , appel**remove_page_break** méthode de**sauts de page** module. Ci-dessous, vous pouvez voir un exemple de code.

**Code Python**

{{< highlight "python" >}}



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
## **Télécharger le code d'exécution**
 Télécharger**Gestion des sauts de page (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
