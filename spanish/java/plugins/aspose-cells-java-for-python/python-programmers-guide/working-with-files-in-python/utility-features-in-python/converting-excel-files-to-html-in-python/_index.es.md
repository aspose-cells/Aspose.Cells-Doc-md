---
title: Convirtiendo archivos de Excel a HTML en Python
type: docs
weight: 10
url: /es/java/converting-excel-files-to-html-in-python/
---

## **Aspose.Cells - Convertir archivo de Excel a HTML**
Para convertir Excel a HTML usando Aspose.Cells for Java en Python, simplemente invoque el método worksheet_to_html() del módulo Converter.

**Código Python**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Convertir archivo de Excel a HTML (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
