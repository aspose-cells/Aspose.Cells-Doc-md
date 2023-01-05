---
title: Eliminar la configuración de impresora existente de las hojas de trabajo en el archivo de Excel
type: docs
weight: 40
url: /es/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---
## **Posibles escenarios de uso**
A veces, los desarrolladores quieren evitar que Excel incluya*.compartimiento* archivos de configuración de la impresora en los archivos XLSX guardados. Los archivos de configuración de la impresora se encuentran en*“[archivo "raíz"]\xl\printerSettings”*. Este documento explica cómo eliminar la configuración de la impresora existente mediante las API Aspose.Cells.
## **Eliminar la configuración de impresora existente de las hojas de trabajo en el archivo de Excel**
Aspose.Cells le permite eliminar la configuración de impresora existente especificada para diferentes hojas en el archivo de Excel. El siguiente código de ejemplo ilustra cómo quitar la configuración de impresora existente para todas las hojas de cálculo del libro. Por favor vea su[ejemplo de archivo de Excel](45056023.xlsx), [archivo de salida de Excel](45056024.xlsx), salida de la consola, así como una captura de pantalla como referencia.
## **Captura de pantalla**
![todo:imagen_alternativa_texto](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **Salida de consola**
{{< highlight "java" >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: 5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: 34

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: 70

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: 8

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
