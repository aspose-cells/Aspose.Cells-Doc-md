---
title: Manipulera pivottabell
type: docs
weight: 20
url: /sv/cpp/manipulate-pivot-table/
---
##  **Möjliga användningsscenarier**
Förutom att skapa nya pivottabeller kan du manipulera de nya och befintliga pivottabellerna. Du kan ändra data i källintervallet för pivottabellen och sedan uppdatera och beräkna det och uppnå de nya värdena för pivottabellceller. Snälla använd[PivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) och[PivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/)metoder efter att du har ändrat värdena i källområdet för pivottabellen för att uppdatera pivottabellen.
##  **Manipulera pivottabell**
 Följande exempelkod laddar[exempel på excel-fil](23167013.xlsx) och kommer åt den befintliga pivottabellen i sitt första kalkylblad. Det ändrar värdet på cell B3 som ligger inom källområdet för pivottabellen och uppdaterar sedan pivottabellen. Innan den uppdaterar pivottabellen kommer den åt värdet för pivottabellcell H8 som är 15 och efter att ha uppdaterat pivottabellen ändras dess värde till 6. Se[output excel-fil](23167014.xlsx)genereras med den här koden och skärmdumpen som visar effekten av exempelkoden på exemplets Excel-fil. Se även konsolutgången nedan som visar värdet på pivottabellscellen H8 före och efter uppdatering av pivottabellen.

![todo:image_alt_text](manipulate-pivot-table_1.png)
##  **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
##  **Konsolutgång**
 Nedan är konsolutgången för ovanstående exempelkod när den körs med den medföljande[exempel på excel-fil](23167013.xlsx).

{{< highlight "java" >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
