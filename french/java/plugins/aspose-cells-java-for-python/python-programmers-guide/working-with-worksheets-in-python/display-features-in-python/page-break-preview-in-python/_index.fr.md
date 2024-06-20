---
title: Aperçu avant impression en Python
type: docs
weight: 60
url: /fr/java/page-break-preview-in-python/
---

## **Aspose.Cells - Hello World**
Pour définir la feuille de calcul en aperçu avant impression en utilisant **Aspose.Cells Java pour Python**, invoquez simplement le module **PageBreakPreview**.

**Code Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Adding a new worksheet to the Workbook object

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(True)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Page break preview is enabled for sheet 1, please check the output document." 

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Aperçu avant impression (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
