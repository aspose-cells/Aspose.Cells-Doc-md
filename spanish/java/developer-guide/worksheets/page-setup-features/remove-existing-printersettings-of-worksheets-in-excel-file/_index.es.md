---
title: Eliminar Configuraciones de Impresora Existente de Hojas de Cálculo en Archivo Excel
type: docs
weight: 40
url: /es/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---

## **Escenarios de uso posibles**
A veces, los desarrolladores desean evitar que Excel incluya archivos *.bin* de la configuración de impresora en los archivos XLSX guardados. Los archivos de configuración de impresora se encuentran en *“[archivo "raíz"]\xl\printerSettings”*. Este documento explica cómo eliminar las configuraciones de impresora existentes utilizando las API de Aspose.Cells.
## **Eliminar la configuración existente de PrinterSettings de las hojas de cálculo en el archivo de Excel**
Aspose.Cells le permite eliminar la configuración de impresión existente especificada para diferentes hojas en el archivo de Excel. El siguiente código de ejemplo ilustra cómo eliminar la configuración de impresión existente para todas las hojas de cálculo en el libro. Consulte su [archivo de Excel de ejemplo](45056023.xlsx), [archivo de Excel de salida](45056024.xlsx), salida de la consola y una captura de pantalla como referencia.
## **Captura de pantalla**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **Salida de la consola**
{{< highlight java >}}

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
{{< app/cells/assistant language="java" >}}
