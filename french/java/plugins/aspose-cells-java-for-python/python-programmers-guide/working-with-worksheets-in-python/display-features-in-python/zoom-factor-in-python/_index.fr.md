---
title: Facteur de zoom en Python
type: docs
weight: 80
url: /fr/java/zoom-factor-in-python/
---

## **Aspose.Cells - Facteur de zoom**
Pour définir le facteur de zoom en utilisant **Aspose.Cells Java pour Python**, invoquez simplement le module **ZoomFactor**.

**Code Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Zoom factor set to 75% for sheet 1, please check the output document."

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Facteur de zoom (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
