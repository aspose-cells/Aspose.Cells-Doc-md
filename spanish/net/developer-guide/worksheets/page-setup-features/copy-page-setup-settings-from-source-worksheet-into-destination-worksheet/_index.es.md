---
title: Copie la configuración de configuración de página de la hoja de trabajo de origen a la hoja de trabajo de destino
type: docs
weight: 80
url: /es/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Este artículo explica cómo usar el código de muestra de la biblioteca C# API o .NET para copiar la configuración de configuración de página de la hoja de trabajo de origen a la hoja de trabajo de destino mediante programación.
keywords: copy page setup settings c#, copy page setup settings to target worksheet c#
---
##  **Posibles escenarios de uso**

Cuando agrega una nueva hoja a un libro de trabajo, contiene la *configuración de configuración de página* predeterminada. Puede haber ocasiones en las que necesite transferir la configuración ([**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) de una hoja de trabajo a otra hoja de trabajo. Este documento explica cómo copiar la configuración de Configuración de página de una hoja de trabajo a otra utilizando las API Aspose.Cells.

##  **Copie la configuración de configuración de página de la hoja de trabajo de origen a la hoja de trabajo de destino**

El siguiente código de ejemplo ilustra cómo copiar*Configuración de configuración de página*de una hoja de trabajo a otra usando[**PageSetup.Copiar()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy)método. Consulte el siguiente código de ejemplo y su salida de la consola para obtener una referencia.

##  **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

##  **Salida de consola**

{{< highlight "java" >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
