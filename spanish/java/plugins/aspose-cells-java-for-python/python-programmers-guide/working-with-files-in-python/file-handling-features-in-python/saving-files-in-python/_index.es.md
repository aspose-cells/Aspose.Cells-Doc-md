---
title: Guardado de Archivos en Python
type: docs
weight: 20
url: /es/java/saving-files-in-python/
---

## **Aspose.Cells - Guardando archivos**
### **Guardar archivo en alguna ubicación**
Si los desarrolladores necesitan guardar sus archivos usando **Aspose.Cells Java para Python** en alguna ubicación de almacenamiento, simplemente podrán especificar el nombre del archivo (con su ruta de almacenamiento completa) y el formato de archivo deseado (usando la enumeración **FileFormatType**) al llamar al método **save** del objeto **Workbook**.

**Código Python**

{{< highlight python >}}

 fileFormatType = self.FileFormatType


#Creating an Workbook object with an Excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save in default (Excel2003) format

workbook.save(self.dataDir + "book.default.out.xls")

#Save in Excel2003 format

workbook.save(self.dataDir + "book.out.xls", fileFormatType.EXCEL_97_TO_2003)

#Save in Excel2007 xlsx format

workbook.save(self.dataDir + "book.out.xlsx", fileFormatType.XLSX)

#Save in SpreadsheetML format

workbook.save(self.dataDir + "book.out.xml", fileFormatType.EXCEL_2003_XML)

#Print Message

print("<BR>")

print("Worksheets are saved successfully.")

{{< /highlight >}}

Descargar **Guardado de Archivo (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
