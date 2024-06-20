---
title: Convertir Excel a archivos PDF en PHP
type: docs
weight: 30
url: /es/java/converting-excel-to-pdf-files-in-php/
---

## **Aspose.Cells - Convertir Excel a archivos PDF**
Para convertir Excel a archivo Pdf utilizando Aspose.Cells for Java en PHP, simplemente invoque el método excel_to_pdf() del módulo de conversión.

**Código PHP**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Convertir Excel a archivos PDF (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
