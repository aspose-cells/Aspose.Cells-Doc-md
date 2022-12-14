---
title: Vista previa de salto de página en Python
type: docs
weight: 60
url: /es/java/page-break-preview-in-python/
---
## **Aspose.Cells - Hello World**
 Para configurar la hoja de trabajo para la vista previa de salto de página usando**Aspose.Cells Java para Python** , simplemente invocar**La previsualización del salto de página** módulo.

**Código Python**

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
## **Descargar código de ejecución**
 Descargar**Vista previa de salto de página (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
