---
title: Hitta celler med specifik stil
type: docs
weight: 80
url: /sv/java/find-cells-with-specific-style/
description: Den här artikeln visar hur du hittar celler med specifik stil med MS Excel och Aspose.Cells for Java API.
keywords: find cells with specific style, find cells with specific style excel, find cells with specific style excel java, search cells with specific style, search cells with specific style excel, search cells with specific style excel java, how to find cells with specific style, how to find cells with specific style excel, how to find cells with specific style excel java
---
{{% alert color="primary" %}}

Ibland måste du hitta cellerna med någon speciell stil. Den här artikeln visar hur du uppnår detta genom att använda Microsoft Excel samt Aspose.Cells for Java API.

{{% /alert %}}

## Använder Microsoft Excel

Det här är stegen som krävs för att söka i celler med specifika stilar i MS Excel.

1.  Välj**Hitta och välj** i**Fliken Hem**.
1.  Välj**Hitta**.
1.  Klick**alternativ**om avancerade alternativ inte är synliga.
1.  Välj**Välj format från Cell...** från**Formatera** falla ner.
1. Markera cellen med stilen som du vill söka efter.
1.  Klick**Hitta alla** för att hitta alla celler med stil som liknar din valda cell.

## Använder Aspose.Cells for Java

 Aspose.Cells for Java tillhandahåller funktionen för att hitta celler i kalkylblad med någon specifik stil. För detta tillhandahåller API[**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style) fast egendom.

### Exempelkod

 Följande kodavsnitt hittar alla celler som har samma stil som cellen**A1** och ändrar texten i dessa celler. Se skärmdumpen av käll- och utdatafilerna för att analysera utdata från exempelkoden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

Efter exekvering av kod kommer alla celler som har samma stil som cell A1 att ha texten "Found".

### Skärmdumpar

![todo:image_alt_text](find-cells-with-specific-style_1.png)

**Figur:** Källfil med celler som har stilar

 Här är utdatafilen som genereras av följande kod. Du kan se alla celler som har samma stil som cellen**A1** har texten "Found"

![todo:image_alt_text](find-cells-with-specific-style_2.png)

**Figur:**Utdatafil med hittade celler efter sökning efter**A1** stil
