---
title: Guardar archivos en Python
type: docs
weight: 20
url: /es/java/saving-files-in-python/
---
## **Aspose.Cells - Guardar archivos**
### **Guardar archivo en alguna ubicación**
 Si los desarrolladores necesitan guardar sus archivos usando**Aspose.Cells Java for Python** a alguna ubicación de almacenamiento, simplemente pueden especificar el nombre del archivo (con su ruta de almacenamiento completa) y el formato de archivo deseado (usando el**Tipo de formato de archivo**enumeración) mientras llama al**ahorrar**método de**Libro de trabajo**objeto.

**Código Python**

{{< highlight "python" >}}

 fileFormatType = self.FileFormatType


# Creating an Workbook object with an Excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save in default (Excel2003) format

workbook.save(self.dataDir + "book.default.out.xls")

# Save in Excel2003 format

workbook.save(self.dataDir + "book.out.xls", fileFormatType.EXCEL_97_TO_2003)

# Save in Excel2007 xlsx format

workbook.save(self.dataDir + "book.out.xlsx", fileFormatType.XLSX)

# Save in SpreadsheetML format

workbook.save(self.dataDir + "book.out.xml", fileFormatType.EXCEL_2003_XML)

# Print Message

print("<BR>")

print("Worksheets are saved successfully.")

{{< /highlight >}}

 Descargar**Guardar archivo (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
