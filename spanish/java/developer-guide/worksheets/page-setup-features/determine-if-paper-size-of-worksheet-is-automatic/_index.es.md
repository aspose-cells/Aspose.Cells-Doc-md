---
title: Determinar si el Tamaño de Papel de la Hoja de Cálculo es Automático
type: docs
weight: 20
url: /es/java/determine-if-paper-size-of-worksheet-is-automatic/
---

## **Escenarios de uso posibles**

La mayoría de las veces, el tamaño de papel de la hoja de cálculo es automático. Cuando es automático, suele estar configurado como *Carta*. A veces, el usuario establece el tamaño de papel de la hoja de cálculo según sus requisitos. En este caso, el tamaño de papel no es automático. Puedes averiguar si el tamaño de papel de la hoja de cálculo es automático o no utilizando el método [**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize).

## **Determinar si el tamaño de papel de la hoja de cálculo es automático**

El código de muestra proporcionado a continuación carga los dos siguientes archivos de Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

y averigua si el tamaño de papel de su primera hoja de cálculo es automático o no. En Microsoft Excel, puedes verificar si el tamaño de papel es automático o no a través de la ventana de Configuración de página como se muestra en esta captura de pantalla.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Salida de la consola**

Aquí está la salida de la consola del código de muestra anterior cuando se ejecuta con los archivos de Excel de muestra proporcionados.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
