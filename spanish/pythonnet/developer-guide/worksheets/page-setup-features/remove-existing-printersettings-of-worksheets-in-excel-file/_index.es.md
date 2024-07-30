---
title: Eliminar Configuraciones de Impresora Existente de Hojas de Cálculo en Archivo Excel
type: docs
weight: 60
url: /es/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: En este artículo, aprenderás cómo eliminar las Configuraciones de Impresora existentes de la Hoja de Trabajo dentro del archivo de Excel a través del objeto Page Setup de forma programática con código de ejemplo usando la Biblioteca de Excel de Python de Aspose.Cells for Python.
keywords: Biblioteca de Excel de Python, eliminar las configuraciones de impresora de la hoja de trabajo en Python, eliminar las configuraciones de impresora de la hoja de trabajo de excel en Python.
---

## **Escenarios de uso posibles**
A veces los desarrolladores quieren evitar que Excel incluya archivos *.bin* de las configuraciones de impresora en los archivos XLSX guardados. Los archivos de configuraciones de impresora se encuentran en *“[file "root"]\xl\printerSettings”.* Este documento explica cómo eliminar las configuraciones de impresora existentes utilizando las APIs de Aspose.Cells for Python via .NET.

## **Eliminar la configuración existente de PrinterSettings de las hojas de cálculo en el archivo de Excel**
Aspose.Cells for Python via .NET te permite eliminar las configuraciones de impresora existentes especificadas para diferentes hojas en el archivo de Excel. El siguiente código de muestra ilustra cómo eliminar las configuraciones de impresora existentes para todas las hojas de trabajo en el libro. Consulta su [archivo de Excel de muestra](45056020.xlsx), [archivo de Excel de salida](45056021.xlsx), la salida de la consola y la captura de pantalla como referencia.

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
