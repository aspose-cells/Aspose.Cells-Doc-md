---
title: Convertir a archivos MHTML en PHP
type: docs
weight: 40
url: /es/java/converting-to-mhtml-files-in-php/
---
## **Aspose.Cells - Conversión a archivos MHTML**
Para convertir la hoja de trabajo a un archivo MHTML usando Aspose.Cells for Java en PHP, simplemente invoque la hoja de trabajo_a_Método mhtml() del módulo Converter.

**Código PHP**

{{< highlight "php" >}}

 $sveFormat = new SaveFormat();

//Specify the file path

$filePath = $dataDir . "Book1.xlsx";

//Specify the HTML saving options

$sv = new HtmlSaveOptions($sveFormat->M_HTML);

//Instantiate a workbook and open the template XLSX file

$wb = new Workbook($filePath);

//Save the MHT file

$wb->save($filePath . ".out.mht", $sv);

{{< /highlight >}}
## **Descargar código de ejecución**
Descargar**Conversión a archivos MHTML (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
