---
title: Tre metoder för att filtrera Diagramdata
description: Lär dig hur man filtrerar diagram i Excel med hjälp av Aspose.Cells for .NET. Vår omfattande guide kommer att visa hur man tillämpar filter på diagram, anpassa diagramelement och använda dataanalystjänster för bättre insikter och informerade beslut.
keywords: Aspose.Cells for .NET, Filtrera diagram i Excel, Dataanalys, Beslutsfattande, Visualisering
type: docs
weight: 2210
url: /sv/net/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. Filtrera bort serier för att rendera ett diagram**

### **Steg för att filtrera serier från ett diagram i Excel**
I Excel kan vi filtrera specifika serier från ett diagram, vilket gör att de filtrerade serierna inte visas i diagrammet. Det ursprungliga diagrammet visas i **Figur 1**. Men när vi filtrerar ut **Testserie2** och **Testserie4**, kommer diagrammet att visas som i **Figur 2**.

I Aspose.Cells kan vi utföra en liknande operation. För en [provpunkt](seriesFiltered.xlsx) fil som denna, om vi vill filtrera ut **Testserie2** och **Testserie4**, kan vi köra följande kod. Dessutom kommer vi att behålla två listor: en ([NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)) lista för att lagra alla valda serier och en annan ([FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)) för att lagra de filtrerade serierna.

Observera att i koden, när vi ställer in **chart.NSeries[0].IsFiltered = true;**, kommer den första serien i [NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) att tas bort och placeras på rätt plats inom [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/). Därefter kommer föregående **NSeries[1]** att bli det nya första objektet i listan, och alla följande serier kommer att skifta framåt med en position. Det betyder att om vi kör **chart.NSeries[1].IsFiltered = true;**, tar vi effektivt bort den ursprungliga tredje serien. Detta kan ibland leda till förvirring, så vi rekommenderar att följa operationen i koden, som tar bort serier från slutet till början.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Exempelkod**
Följande kodexempel laddar den [exempelfil i Excel](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

## **2. Filtrera datan och låt diagrammet ändras**

Att filtrera din data är ett bra sätt att hantera diagramfilter med mycket data. När du filtrerar datan kommer diagrammet att ändras. En fråga vi kommer att behöva ta itu med är att se till att diagrammet stannar kvar på skärmen. När du filtrerar får du dolda rader, och ibland kan diagrammet finnas i dessa dolda rader.

![todo:image_alt_text](Figure3.png)

### **Steg för att använda Datafilter för att ändra diagrammet i Excel**

1. Klicka inom ditt datarange.
2. Klicka på fliken **Data**, och slå på filter genom att klicka på Filter. Din rubrikrad kommer att ha nedrullningspilar.
3. Skapa ett diagram genom att gå till fliken **Infoga** och välja en kolumnsdiagram.
4. Filtrera nu din data med hjälp av nedrullningspilarna i datan. Använd inte Diagramfilter.

### **Exempelkod**
Följande kodexempel visar samma funktion med hjälp av Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

## **3. Filtrera datan med ett tabell och låt diagrammet ändras**

Att använda en tabell är liknande som metod 2, som använder ett intervall, men du har fördelar med tabeller över intervall. När du ändrar ditt intervall till en tabell och lägger till data, uppdateras diagrammet automatiskt. Med ett intervall måste du ändra datakällan.

### **Formatera som tabell i Excel**

Klicka inuti din data och använd **CTRL + T** eller använd fliken Hem, **Formatera som tabell**

![todo:image_alt_text](Figure4.png)

### **Exempelkod**
Följande exempelkod laddar [prov Excel-fil](TableFilters.xlsx) som visar samma funktion med Aspose.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}
