---
title: Verificar si el libro de trabajo contiene enlaces externos ocultos
type: docs
weight: 950
url: /es/java/check-if-workbook-contains-hidden-external-links/
---

## **Escenarios de uso posibles**
A veces, la hoja de cálculo contiene enlaces externos que están ocultos y no se pueden ver en Microsoft Excel. Aspose.Cells recupera todos los enlaces externos, ya sean visibles u ocultos. Sin embargo, puedes verificar la propiedad [ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible) para ver si el enlace externo es visible o no
## **Verificar si la Hoja de Cálculo contiene Enlaces Externos Ocultos**
El siguiente código de ejemplo carga el [archivo de Excel fuente](5472525.xlsx) que contiene enlaces externos ocultos. Estos enlaces no se pueden ver en Microsoft Excel, pero están presentes dentro de la hoja de cálculo. Después de imprimir la propiedad [ExternalLink.DataSource](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#DataSource) y [ExternalLink.IsReferred](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsReferred), imprime la propiedad [ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible). En la salida de consola a continuación, puedes ver que ninguno de sus enlaces externos es visible.
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckWorkbookContainsHiddenExternalLinks-CheckWorkbookContainsHiddenExternalLinks.java" >}}
## **Salida de la consola**
Esta es la salida de consola del código de ejemplo anterior cuando se ejecuta con el [archivo de Excel de ejemplo](5472525.xlsx).



{{< highlight java >}}

 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
