---
title: Figer les volets au Python
type: docs
weight: 40
url: /fr/java/freeze-panes-in-python/
---
## **Aspose.Cells - Figer les volets**
 Pour figer des volets dans le document de feuille de calcul à l'aide de**Aspose.Cells Java for Python** , invoquez simplement**FreezePanes** module.

**Code Python**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "book.out.xls")

# Print Message

print "Panes freeze successfull."

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Hello World (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
