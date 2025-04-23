---
title: Copiar Configuraciones de Configuración de Página de la Hoja de Cálculo de Origen en la Hoja de Cálculo de Destino
type: docs
weight: 80
url: /es/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Este artículo explica cómo usar el código de ejemplo de la API de C# o la Biblioteca .NET para copiar las configuraciones de la Configuración de Página de la hoja de cálculo de origen en la hoja de cálculo de destino de forma programática.
keywords: copiar configuraciones de configuración de página con C#, copiar configuraciones de configuración de página en hoja de trabajo de destino con C#
---

## **Escenarios de uso posibles**

Cuando agregas una nueva hoja a un libro de trabajo, contiene las configuraciones de la *Configuración de Página* predeterminadas. Puede haber momentos en los que necesites transferir las configuraciones ([**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) de una hoja de cálculo a otra. Este documento explica cómo copiar las configuraciones de la Configuración de Página de una hoja a otra utilizando las APIs de Aspose.Cells.

## **Copiar Configuraciones de Configuración de Página de la Hoja de Cálculo de Origen en la Hoja de Cálculo de Destino**

El siguiente código de ejemplo ilustra cómo copiar las *Configuraciones de Configuración de Página* de una hoja a otra utilizando el método [**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy). Por favor, consulta el siguiente código de ejemplo y su salida en consola para una referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

## **Salida de la consola**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
