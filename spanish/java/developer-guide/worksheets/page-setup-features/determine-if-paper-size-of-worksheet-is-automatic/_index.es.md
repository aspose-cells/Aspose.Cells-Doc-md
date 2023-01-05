---
title: Determinar si el tamaño de papel de la hoja de trabajo es automático
type: docs
weight: 20
url: /es/java/determine-if-paper-size-of-worksheet-is-automatic/
---
## **Posibles escenarios de uso**

 La mayoría de las veces, el tamaño del papel de la hoja de trabajo es automático. Cuando es automático, a menudo se establece como*Carta* . A veces, el usuario establece el tamaño del papel de la hoja de trabajo según sus requisitos. En este caso, el tamaño del papel no es automático. Puede encontrar si el tamaño del papel de la hoja de trabajo es automático o no usando el[**Hoja de trabajo.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize)método.

## **Determinar si el tamaño de papel de la hoja de trabajo es automático**

El código de muestra que se proporciona a continuación carga los siguientes dos archivos de Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

y averiguar si el tamaño del papel de su primera hoja de trabajo es automático o no. En Microsoft Excel, puede verificar si el tamaño del papel es automático o no a través de la ventana Configurar página como se muestra en esta captura de pantalla.

![todo:imagen_alternativa_texto](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Salida de consola**

Aquí está la salida de la consola del código de muestra anterior cuando se ejecuta con los archivos de Excel de muestra dados.

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
