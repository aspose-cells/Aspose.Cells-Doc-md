---
title: Fractionner les volets en Python
type: docs
weight: 70
url: /fr/java/split-panes-in-python/
---

## **Aspose.Cells - Diviser les volets**
Pour fractionner les volets à l'aide de **Aspose.Cells Java pour Python**, invoquez simplement le module **SplitPanes**.

**Code Python**

{{< highlight java >}}

 saveFormat = self.SaveFormat;

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Set the active cell

workbook.getWorksheets().get(0).setActiveCell("A20");

#Split the worksheet window

workbook.getWorksheets().get(0).split();

#Save the excel file

workbook.save(self.dataDir + "book.out.xls", saveFormat.EXCEL_97_TO_2003);

#Print Message

print "Panes split successfully."

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Fractionner les volets (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
