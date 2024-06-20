---
title: Vista Preliminar de Salto de Página en Python
type: docs
weight: 60
url: /es/java/page-break-preview-in-python/
---

## **Aspose.Cells - Hello World**
Para configurar la vista preliminar de salto de página en la hoja de cálculo usando **Aspose.Cells Java para Python**, simplemente invoque el módulo **PageBreakPreview**.

**Código Python**

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
## **Descargar Código en Ejecución**
Descargue **Vista previa de salto de página (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
