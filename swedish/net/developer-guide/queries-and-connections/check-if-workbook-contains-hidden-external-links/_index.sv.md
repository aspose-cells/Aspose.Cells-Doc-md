---
title: Kontrollera om arbetsboken innehåller dolda externa länkar
type: docs
weight: 230
url: /sv/net/check-if-workbook-contains-hidden-external-links/
---
## **Möjliga användningsscenarier**
Ibland innehåller arbetsboken externa länkar som är dolda och inte kan visas i Microsoft Excel. Aspose.Cells hämtar alla externa länkar oavsett om de är synliga eller dolda. Du kan dock kontrollera[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)egendom för att kontrollera om den externa länken är synlig eller inte
## **Kontrollera om arbetsboken innehåller dolda externa länkar**
 Följande exempelkod laddar[källkod excel-fil](5115413.xlsx) som innehåller dolda externa länkar. Dessa länkar kan inte visas i Microsoft Excel men de finns i arbetsboken. Efter utskrift[ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) och[ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) egenskapen, skriver den ut[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)fast egendom. I konsolutgången nedan ser du att alla dess externa länkar inte är synliga.
### **Exempelkod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
### **Konsolutgång**
 Här är konsolutgången för ovanstående exempelkod när den körs med den givna[exempel på excel-fil](5115413.xlsx).



{{< highlight "java" >}}

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
