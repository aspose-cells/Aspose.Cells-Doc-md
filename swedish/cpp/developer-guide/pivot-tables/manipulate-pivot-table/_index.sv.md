---
title: Manipulera Pivot tabell
type: docs
weight: 20
url: /sv/cpp/manipulate-pivot-table/
---

## **Möjliga användningsscenario**
Förutom att skapa nya pivottabeller kan du manipulera nya och befintliga pivottabeller. Du kan ändra data i källområdet för pivottabellen och sedan uppdatera och beräkna det och uppnå de nya värdena för pivottabellceller. Använd [PivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) och [PivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) metoder efter att du har ändrat värdena i källområdet för pivottabellen för att uppdatera pivottabellen.
## **Manipulera Pivot-tabell**
Följande exempelkod laddar den [exempel excel-filen](23167013.xlsx) och får åtkomst till den befintliga pivottabellen i dess första arbetsblad. Den ändrar värdet på cell B3 som finns inom källområdet för pivottabell och uppdaterar sedan pivottabellen. Innan den uppdaterar pivottabellen får den tillgång till värdet för pivottabellcell H8 som är 15 och efter att ha uppdaterat pivottabellen ändras dess värde till 6. Se den [utdata excel-fil](23167014.xlsx) som genererats med denna kod och skärmdumpen som visar effekten av exempelkoden på exempel excel-filen. Se även konsollutdata nedan som visar värdet på pivottabellcell H8 före och efter att ha uppdaterat pivottabellen.

![todo:image_alt_text](manipulate-pivot-table_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
## **Konsoloutput**
Nedan finns konsollutdata för ovanstående exempelkod när den körs med den angivna [exempel excel-filen](23167013.xlsx).

{{< highlight java >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
