---
title: Convertir archivos de Excel a HTML en PHP
type: docs
weight: 20
url: /es/java/converting-excel-files-to-html-in-php/
---
## **Aspose.Cells - Conversión de archivos de Excel a HTML**
Para convertir Excel a HTML usando Aspose.Cells for Java en PHP, simplemente invoque la hoja de trabajo_a_método html() del módulo Converter.

**Código PHP**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Conversión de archivos de Excel a HTML (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
