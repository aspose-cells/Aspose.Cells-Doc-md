---
title: Convertir archivos de Excel a PDF en PHP
type: docs
weight: 30
url: /es/java/converting-excel-to-pdf-files-in-php/
---
## **Aspose.Cells - Conversión de archivos de Excel a PDF**
Para convertir archivos de Excel a Pdf usando Aspose.Cells for Java en PHP, simplemente invoque Excel_a_Método pdf() del módulo Converter.

**Código PHP**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Conversión de archivos de Excel a PDF (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
