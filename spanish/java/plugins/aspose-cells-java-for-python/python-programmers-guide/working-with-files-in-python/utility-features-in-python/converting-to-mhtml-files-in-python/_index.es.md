---
title: Conversión a archivos MHTML en Python
type: docs
weight: 30
url: /es/java/converting-to-mhtml-files-in-python/
---
## **Aspose.Cells - Conversión a MHTML**
Para convertir la hoja de trabajo al archivo MHTML usando Aspose.Cells for Java en Python, simplemente invoque la hoja de trabajo_a_Método mhtml() del módulo Converter.

**Código Python**

{{< highlight "java" >}}

 saveFormat = self.SaveFormat

# Specify the file path

filePath = self.dataDir + "Book1.xlsx"

# Specify the HTML saving options

sv = self.HtmlSaveOptions(saveFormat.M_HTML)

# Instantiate a workbook and open the template XLSX file

wb = self.Workbook(filePath)

# Save the MHT file

wb.save(filePath + ".out.mht", sv)

\# Print message

print "Excel to MHTML conversion performed successfully."

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Convirtiendo a MHTML (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
