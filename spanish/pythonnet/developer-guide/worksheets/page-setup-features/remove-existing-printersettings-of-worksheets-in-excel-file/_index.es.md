---
title: Eliminar Configuraciones de Impresora Existente de Hojas de Cálculo en Archivo Excel
type: docs
weight: 60
url: /es/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: En este artículo, aprenderás cómo eliminar la configuración del impresor existente de la hoja de cálculo dentro del archivo de Excel mediante el objeto Configuración de página con código de ejemplo usando Aspose.Cells para Python.
keywords: Biblioteca de Excel en Python, eliminar configuración de impresora de la hoja en Python, eliminar configuración de impresora en una hoja de Excel en Python.
---

## **Escenarios de uso posibles**
A veces, los desarrolladores desean evitar que Excel incluya archivos *.bin* de configuraciones de impresora en los archivos XLSX guardados. Los archivos de configuración de impresora se encuentran en *“[archivo "raíz"]\xl\printerSettings”.* Este documento explica cómo eliminar la configuración de impresora existente usando Aspose.Cells para las APIs de Python via .NET.

## **Eliminar la configuración existente de PrinterSettings de las hojas de cálculo en el archivo de Excel**
Aspose.Cells para Python via .NET permite eliminar configuraciones de impresora existentes especificadas para diferentes hojas en el archivo Excel. El siguiente código de ejemplo ilustra cómo eliminar la configuración de impresora existente para todas las hojas del libro. Consulta su [archivo de ejemplo de Excel](45056020.xlsx), [archivo de Excel de salida](45056021.xlsx), la salida en consola y la captura de pantalla para referencia.

## **Captura de pantalla**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Código de muestra**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
