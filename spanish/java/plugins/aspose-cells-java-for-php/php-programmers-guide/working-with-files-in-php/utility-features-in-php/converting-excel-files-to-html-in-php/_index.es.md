---
title: Convertir archivos de Excel a HTML en PHP
type: docs
weight: 20
url: /es/java/converting-excel-files-to-html-in-php/
---

## **Aspose.Cells - Convertir archivos de Excel a HTML**
Para convertir Excel a HTML utilizando Aspose.Cells for Java en PHP, simplemente invoque el método worksheet_to_html() del módulo de conversión.

**Código PHP**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Convertir archivos de Excel a HTML (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
