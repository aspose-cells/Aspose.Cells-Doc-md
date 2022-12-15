---
title: Aperçu des sauts de page dans Python
type: docs
weight: 60
url: /fr/java/page-break-preview-in-python/
---
## **Aspose.Cells - Hello World**
 Pour définir la feuille de calcul sur l'aperçu des sauts de page à l'aide de**Aspose.Cells Java for Python** , invoquez simplement**Aperçu du saut de page** module.

**Code Python**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Adding a new worksheet to the Workbook object

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(True)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Page break preview is enabled for sheet 1, please check the output document." 

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Aperçu des sauts de page (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
