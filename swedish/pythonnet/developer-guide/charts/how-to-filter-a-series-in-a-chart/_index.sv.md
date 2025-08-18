---
title: Tre metoder för att filtrera Diagramdata
description: Lär dig hur man filterar diagram i Excel med Aspose.Cells för Python via .NET. Vår omfattande guide visar hur man applicerar filter på diagram, anpassar diagramelement och använder datanalysverktyg för bättre insikter och informerade beslut.
keywords: Aspose.Cells för Python via .NET, Filtrering av diagram i Excel, Datanalys, Beslutsfattande, Visualisering.
type: docs
weight: 2210
url: /sv/python-net/filtering-charts-in-excel/
---


## **1. Filtrera bort serier för att rendera ett diagram**

### **Steg för att filtrera serier från ett diagram i Excel**
I Excel kan vi filtrera specifika serier från ett diagram, vilket gör att de filtrerade serierna inte visas i diagrammet. Det ursprungliga diagrammet visas i **Figur 1**. Men när vi filtrerar ut **Testserie2** och **Testserie4**, kommer diagrammet att visas som i **Figur 2**.

I Aspose.Cells för Python via .NET kan vi utföra en liknande operation. För en [exempel](seriesFiltered.xlsx)-fil som denna, om vi vill filtrera bort **Testseries2** och **Testseries4**, kan vi köra följande kod. Dessutom behåller vi två listor: en ([n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/)) för att lagra alla valda serier och en ([filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/)) för att lagra de filtrerade serierna.

Observera att i koden, när vi sätter **chart.nSeries[0].is_filtered = TRUE;**, tas den första serien i [n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/) bort och placeras i den passande positionen inom [filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/). Därefter blir den föregående **nSeries[1]** den nya första posten i listan, och alla följande serier skiftar framåt med en position. Det innebär att om vi sedan kör **chart.nSeries[1].is_filtered = TRUE;**, tar vi i praktiken bort den ursprungliga tredje serien. Detta kan ibland orsaka förvirring, så vi rekommenderar att följa operationen i koden som tar bort serierna från slutet till början.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Exempelkod**
Följande kodexempel laddar den [exempelfil i Excel](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-seriesFiltered.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DataFilters.py" >}}

## **3. Filtrera datan med ett tabell och låt diagrammet ändras**

Att använda en tabell är liknande som metod 2, som använder ett intervall, men du har fördelar med tabeller över intervall. När du ändrar ditt intervall till en tabell och lägger till data, uppdateras diagrammet automatiskt. Med ett intervall måste du ändra datakällan.

### **Formatera som tabell i Excel**

Klicka inuti din data och använd **CTRL + T** eller använd fliken Hem, **Formatera som tabell**

![todo:image_alt_text](Figure4.png)

### **Exempelkod**
Följande exempelkod laddar [prov Excel-fil](TableFilters.xlsx) som visar samma funktion med Aspose.Cells.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TableFilters.py" >}}
