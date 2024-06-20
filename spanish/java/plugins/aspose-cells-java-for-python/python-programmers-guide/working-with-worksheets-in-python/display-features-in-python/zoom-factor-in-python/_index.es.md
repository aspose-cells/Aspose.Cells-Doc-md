---
title: Factor de zoom en Python
type: docs
weight: 80
url: /es/java/zoom-factor-in-python/
---

## **Aspose.Cells - Factor de Zoom**
Para establecer el factor de zoom usando **Aspose.Cells Java para Python**, simplemente invoque el módulo **ZoomFactor**.

**Código Python**

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
## **Descargar Código en Ejecución**
Descargue **Factor de zoom (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
