---
title: Kontrollera om arbetsboken innehåller dolda externa länkar
type: docs
weight: 950
url: /sv/java/check-if-workbook-contains-hidden-external-links/
---

## **Möjliga användningsscenario**
Ibland innehåller arbetsboken externa länkar som är dolda och inte kan ses i Microsoft Excel. Aspose.Cells hämtar alla externa länkar oavsett om de är synliga eller dolda. Du kan dock använda [ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible) egenskapen för att kontrollera om den externa länken är synlig eller inte
## **Kontrollera om arbetsboken innehåller dolda externa länkar**
Följande exempelkod laddar [käll-excelfilen](5472525.xlsx) som innehåller dolda externa länkar. Dessa länkar kan inte ses i Microsoft Excel men de finns i arbetsboken. Efter att ha skrivit ut [ExternalLink.DataSource](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#DataSource) och [ExternalLink.IsReferred](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsReferred) egenskapen skriver den [ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible) egenskapen. I konsolresultatet nedan ser du att ingen av externa länkarna är synliga.
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckWorkbookContainsHiddenExternalLinks-CheckWorkbookContainsHiddenExternalLinks.java" >}}
## **Konsoloutput**
Här är konsolresultatet av ovanstående exempelkod när den körs med den givna [käll-excelfilen](5472525.xlsx).



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
