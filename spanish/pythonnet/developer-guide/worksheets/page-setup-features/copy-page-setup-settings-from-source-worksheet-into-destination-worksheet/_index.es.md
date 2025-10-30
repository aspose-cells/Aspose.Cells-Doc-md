---
title: Copiar Configuraciones de Configuración de Página de la Hoja de Cálculo de Origen en la Hoja de Cálculo de Destino
type: docs
weight: 80
url: /es/python-net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Este artículo explica cómo usar el código de ejemplo de Aspose.Cells para Python via .NET para copiar la configuración de Configuración de Página de la hoja de origen a la hoja de destino mediante programación.
keywords: Biblioteca de Excel para Python, copiar configuraciones de configuración de página, copiar configuración de página a la hoja de destino en Python.
---

## **Escenarios de uso posibles**

Cuando agregas una nueva hoja a un libro de trabajo, contiene las configuraciones predeterminadas de *Configuración de Página*. A veces necesitas transferir estas configuraciones ([**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)) de una hoja de cálculo a otra. Este documento explica cómo copiar configuraciones de configuración de página de una hoja a otra usando las APIs de Aspose.Cells para Python via .NET.

## **Copiar Configuraciones de Configuración de Página de la Hoja de Cálculo de Origen en la Hoja de Cálculo de Destino**

El siguiente código de ejemplo ilustra cómo copiar las *Configuraciones de Configuración de Página* de una hoja a otra utilizando el método [**PageSetup.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/copy/#aspose.cells.PageSetup-aspose.cells.CopyOptions). Por favor, consulta el siguiente código de ejemplo y su salida en consola para una referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.py" >}}

## **Salida de la consola**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
