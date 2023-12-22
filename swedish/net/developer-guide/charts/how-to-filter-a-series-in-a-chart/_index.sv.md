---
title: Tre metoder för att filtrera diagramdata
description: Lär dig hur du filtrerar diagram i Excel med Aspose.Cells for .NET. Vår omfattande guide visar hur du använder filter på diagram, anpassar diagramelement och använder dataanalysverktyg för bättre insikter och välgrundat beslutsfattande.
keywords: Aspose.Cells for .NET, Filtering Charts in Excel, Data Analysis, Decision Making, Visualization.
type: docs
weight: 2210
url: /sv/net/filtering-charts-in-excel/
---
{{% alert color="primary" %}}

##  **1. Filtrera ut serier för att rendera ett diagram**

###  **Steg för att filtrera serier från ett diagram i Excel**
 I Excel kan vi filtrera bort specifika serier från ett diagram, vilket gör att de filtrerade serierna inte visas i diagrammet. Det ursprungliga diagrammet visas i**Figur 1**. Men när vi filtrerar bort **Testseries2** och *Testseries4**, kommer diagrammet att visas som visas i *Figur 2**.

 I Aspose.Cells kan vi utföra en liknande operation. För en[prov](seriesFiltered.xlsx) fil så här, om vi vill filtrera bort**Testserie 2** och *Testseries4**, kan vi köra följande kod. Dessutom kommer vi att upprätthålla två listor: en ([NSerien](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)) lista för att lagra alla valda serier och en annan ([FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)) för att lagra den filtrerade serien.

Snälla du**notera** det i koden, när vi ställer in**chart.NSeries[0].IsFiltered = true;**, den första serien i [NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) kommer att tas bort och placeras i lämplig position inom [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/). Därefter, den tidigare **NSerien[1]** kommer att bli det nya första objektet i listan, och alla följande serier kommer att flyttas framåt med en position. Detta betyder att om vi sedan kör *chart.NSeries[1].IsFiltered = true;**, tar vi bort den ursprungliga tredje serien. Detta kan ibland leda till förvirring, så vi rekommenderar att du följer operationen i koden, som tar bort serier från slutet till början.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

###  **Exempelkod**
 Följande exempelkod laddar[exempel på Excel-fil](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

##  **2. Filtrera data och låt diagrammet ändras**

Att filtrera din data är ett utmärkt sätt att hantera diagramfilter med mycket data. När du filtrerar data ändras diagrammet. En fråga vi måste ta itu med är att se till att diagrammet stannar på skärmen. När du filtrerar får du dolda rader, och ibland kommer diagrammet att finnas i de dolda raderna.

![todo:image_alt_text](Figure3.png)

###  **Steg för att använda datafilter för att ändra diagrammet i Excel**

1. Klicka inom ditt dataintervall.
 2. Klicka på**Data** och aktivera Filter genom att klicka på Filter. Din rubrikrad kommer att ha nedrullningsbara pilar.
 3. Skapa ett diagram genom att gå till**Föra in** fliken och välja ett kolumndiagram.
4. Filtrera nu dina data med hjälp av rullgardinspilarna i datan. Använd inte diagramfiltren.

###  **Exempelkod**
Följande exempelkod visar samma funktion med Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

##  **3. Filtrera data med hjälp av en tabell och låt diagrammet ändras**

Att använda en tabell liknar metod 2, att använda ett intervall, men du har fördelar med tabeller över intervall. När du ändrar ditt intervall till en tabell och lägger till data uppdateras diagrammet automatiskt. Med ett intervall måste du ändra datakällan.

###  **Formatera som tabell i Excel**

 Klicka inuti din data och använd**CTRL + T** eller använd fliken Hem,**Formatera som tabell**

![todo:image_alt_text](Figure4.png)

###  **Exempelkod**
 Följande exempelkod laddar[exempel på Excel-fil](TableFilters.xlsx) visar samma funktion med Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}