---
title: Determinar si el Tamaño de Papel de la Hoja de Cálculo es Automático
type: docs
weight: 90
url: /es/net/determine-if-paper-size-of-worksheet-is-automatic/
description: Este artículo explica cómo usar el código de ejemplo de la API de C# o la Biblioteca .NET para determinar si el tamaño de papel de la hoja de cálculo es automático de forma programática.
keywords: determinar si el tamaño de papel de la hoja de cálculo es automático con C#
---

## **Escenarios de uso posibles**

La mayoría de las veces, el tamaño de papel de la hoja de cálculo es automático. Cuando es automático, a menudo se establece en *Carta*. A veces el usuario establece el tamaño de papel de la hoja de cálculo según sus requisitos. En este caso, el tamaño de papel no es automático. Puedes saber si el tamaño de papel de la hoja de cálculo es automático o no utilizando la propiedad [**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize).

## **Determinar si el tamaño de papel de la hoja de cálculo es automático**

El código de muestra proporcionado a continuación carga los dos siguientes archivos de Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

y averigua si el tamaño de papel de su primera hoja de cálculo es automático o no. En Microsoft Excel, puedes verificar si el tamaño de papel es automático o no a través de la ventana de Configuración de página como se muestra en esta captura de pantalla.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

## **Salida de la consola**

Aquí está la salida de la consola del código de muestra anterior cuando se ejecuta con los archivos de Excel de muestra proporcionados.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
