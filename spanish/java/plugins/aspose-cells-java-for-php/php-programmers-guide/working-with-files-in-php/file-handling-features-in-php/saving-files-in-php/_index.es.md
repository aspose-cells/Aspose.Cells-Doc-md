---
title: Guardando Archivos en PHP
type: docs
weight: 20
url: /es/java/saving-files-in-php/
---

## **Aspose.Cells - Guardando archivos**
### **Guardar archivo en alguna ubicación**
Si los desarrolladores necesitan guardar sus archivos usando **Aspose.Cells Java para PHP** en alguna ubicación de almacenamiento, simplemente pueden especificar el nombre del archivo (con su ruta de almacenamiento completa) y el formato de archivo deseado (usando la enumeración **FileFormatType**) al llamar al método **guardar** del objeto **WorkBook**

**Código PHP**

{{< highlight php >}}

 $fileFormatType = new FileFormatType();

//Creating an Workbook object with an Excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Save in default (Excel2003) format

$workbook->save($dataDir . "book.default.out.xls");

//Save in Excel2003 format

$workbook->save($dataDir . "book.out.xls",$fileFormatType->EXCEL_97_TO_2003);

//Save in Excel2007 xlsx format

$workbook->save($dataDir . "book.out.xlsx", $fileFormatType->XLSX);

//Save in SpreadsheetML format

$workbook->save($dataDir . "book.out.xml", $fileFormatType->EXCEL_2003_XML);

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Guardando Archivos (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
