---
title: Convirtiendo archivos de Excel a PDF en Python
type: docs
weight: 20
url: /es/java/converting-excel-to-pdf-files-in-python/
---

## **Aspose.Cells - Convertir Excel a Pdf**
Para convertir Excel a archivo Pdf usando Aspose.Cells for Java en Python, simplemente invoque el método excel_to_pdf() del módulo Converter.

**Código Python**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Convertir Excel a Pdf (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
