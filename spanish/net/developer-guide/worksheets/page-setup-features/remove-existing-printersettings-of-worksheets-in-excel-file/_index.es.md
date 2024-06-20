---
title: Eliminar Configuraciones de Impresora Existente de Hojas de Cálculo en Archivo Excel
type: docs
weight: 60
url: /es/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: En este artículo, aprenderás cómo eliminar la configuración existente de PrinterSettings de la hoja de cálculo dentro del archivo de Excel a través del objeto Page Setup programáticamente con código de ejemplo utilizando la API de C# o la Biblioteca .NET.
keywords: eliminar la configuración de impresora de la hoja de cálculo c#, eliminar la configuración de impresora de la hoja de cálculo de excel c#
---

## **Escenarios de uso posibles**
A veces, los desarrolladores desean evitar que Excel incluya archivos * .bin * de la configuración de impresora en los archivos XLSX guardados. Los archivos de configuración de impresora se encuentran en * "[file \"root\"] \xl \ printerSettings". *  Este documento explica cómo eliminar la configuración de impresora existente utilizando las API de Aspose.Cells.
## **Eliminar la configuración existente de PrinterSettings de las hojas de cálculo en el archivo de Excel**
Aspose.Cells te permite eliminar la configuración de impresora existente especificada para diferentes hojas en el archivo de Excel. El siguiente código de ejemplo ilustra cómo eliminar la configuración de impresora existente para todas las hojas de trabajo en el libro. Consulta su [archivo de Excel de muestra](45056020.xlsx), [archivo de Excel de salida](45056021.xlsx), salida de la consola y captura de pantalla como referencia.
## **Captura de pantalla**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
## **Salida de la consola**
{{< highlight java >}}

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
