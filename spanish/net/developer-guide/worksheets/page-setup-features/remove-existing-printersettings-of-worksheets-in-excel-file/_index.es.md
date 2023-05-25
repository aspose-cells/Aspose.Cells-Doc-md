---
title: Eliminar la configuración de impresora existente de las hojas de trabajo en el archivo de Excel
type: docs
weight: 60
url: /es/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: En este artículo, aprenderá cómo eliminar las configuraciones de impresora existentes de la hoja de trabajo dentro del archivo de Excel a través del objeto Configuración de página mediante programación con código de muestra usando la biblioteca C# API o .NET.
keywords: remove printer settings of worksheet c#, remove printer settings of excel worksheet c#
---
##  **Posibles escenarios de uso**
A veces, los desarrolladores quieren evitar que Excel incluya*.papelera* archivos de configuración de la impresora en los archivos XLSX guardados. Los archivos de configuración de la impresora se encuentran en*“[archivo "raíz"]\xl\printerSettings”.* Este documento explica cómo eliminar la configuración de la impresora existente mediante las API Aspose.Cells.
##  **Eliminar la configuración de impresora existente de las hojas de trabajo en el archivo de Excel**
Aspose.Cells le permite eliminar la configuración de impresora existente especificada para diferentes hojas en el archivo de Excel. El siguiente código de ejemplo ilustra cómo quitar la configuración de impresora existente para todas las hojas de cálculo del libro. Por favor vea su[ejemplo de archivo de Excel](45056020.xlsx), [archivo de salida de Excel](45056021.xlsx)salida de la consola, así como la captura de pantalla como referencia.
##  **Captura de pantalla**
![todo:imagen_alt_texto](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
##  **Código de muestra**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
##  **Salida de consola**
{{< highlight "java" >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
