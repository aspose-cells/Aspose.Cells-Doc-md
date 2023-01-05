---
title: Aspose.Cells for .NET 21.2 Release Notes
type: docs
weight: 29
url: /sv/net/aspose-cells-for-net-21-2-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 21.2](https://www.nuget.org/packages/Aspose.Cells/21.2.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-42427|Stöd i procent av kolumnvisningsformat för pivottabell|Ny funktion|
|CELLSNET-44288|Använda LightCells API med XLSB filer|Ny funktion|
|CELLSNET-47817|Uppdatera datakälla när du ändrar vattenfallsdiagram till kolumndiagram.|Förbättring|
|CELLSNETCORE-99|Stöd för uppdatering av displayikon för inbäddade jpg-, zip-, msg-objekt.|Förbättring|
|CELLSNET-47827|Vänta på CalculateFormula|Prestanda|
|CELLSNET-47832|Cells.DeleteBlankRows slutar aldrig (oändlig loop) på ett visst kalkylblad|Prestanda|
|CELLSNETCORE-98|Laddar xlsb-resultat med OOM-undantag|Prestanda|
|CELLSNET-47805|Fel placering av vissa polylinjer när .html-filer sparas.|Insekt|
|CELLSNET-47810|Pilens position är fel|Insekt|
|CELLSNET-43717|Pivotfältssortering återges inte till PDF|Insekt|
|CELLSNET-43751|Radetikettsortering går förlorad efter att ha refererat pivottabellen|Insekt|
|CELLSNET-47777|Formateringsfel i konverterade HTML|Insekt|
|CELLSNET-47824|Problem med PPMT-formel som ger fel resultat|Insekt|
|CELLSNET-47847| Fel formelreferens efter radering av rader|Insekt|
|CELLSNET-47818|Shape.ToImage återger inte text i docker-miljö|Insekt|
|CELLSNET-47820|Gränser saknas i Aspose EMF/OfficeCompatibleEMF konverterad från XLSX|Insekt|
|CELLSNET-47844| Fel konvertering av dubbel understruken redovisningsformaterad cell när du sparar till PDF|Insekt|
|CELLSNET-47819|Dataetiketter visas inte korrekt när du sparar|Insekt|
|CELLSNET-47821|Dataetiketter är inte korrekta|Insekt|
|CELLSNET-47813| Konstigt beteende (och skillnader) med Treemap-diagram (och andra avancerade diagram)|Insekt|
|CELLSNET-47815|Trådade kommentarer överförs inte med den omslutande formen|Insekt|
|CELLSNET-47816|Filstorlek och MaxColumn för arbetsboken ökas efter att ha ställt in konturgränsen|Insekt|
|CELLSNET-47828|Ytterligare Ctls-ström i XLS-filen efter uppgradering till Aspose.Cells for .NET 21.1|Insekt|
|CELLSNET-47838|Inbyggd diagramfärgpalett bevaras inte|Insekt|
|CELLSNET-47845| Kanter togs oväntat bort efter inklistring med DefaultExceptBorders inklistringstyp|Insekt|
|CELLSNET-47848|Problem med AutoFilter-borttagning av ListObject eller Add Filter Button-flaggan för det|Insekt|
|CELLSNET-47840|Undantag uppstod vid öppning av Excel-fil genererad från en HTML|Undantag|
|CELLSNET-47841|StackOverflowException med xlsx-fil|Undantag|
|CELLSNET-47854|Cells.Find kastar undantag när filen är öppen via stream|Undantag|
|CELLSNET-47825| Aspose.Cells 21.01 Undantag vid öppningshandling|Undantag|
|CELLSNET-47831|Ny arbetsbok misslyckades|Undantag|
|


## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Ändrar beteendet för Cells.DeleteBlankRows()/Cells.DeleteBlankRows(DeleteOptions)**

gamla versioner tar vi bort alla kolumninställningar samtidigt som vi raderar tomma rader om kalkylbladet är tomt (inga celldata). Detta gör det omöjligt för användaren att bara ta bort tomma rader och behålla alla kolumninställningar. Från 21.2 rensar vi inte längre kolumninställningar. Om användaren behöver ta bort kolumninställningar för tomt kalkylblad, bör han kontrollera att det inte finns några data i arket och sedan rensa kolumnsamlingen manuellt.
I gamla versioner tar vi inte bort tomma rader under form. Detta gör det omöjligt för användaren att ta bort alla tomma rader som de förväntar sig. Från 12.2 tar vi bort de tomma raderna under form tillsammans med andra vanliga tomma rader.

### **Föråldrad Range.CellCount-egenskap.**

Använd Range.RowCount och Range.ColumnCount för att få det totala cellantalet istället.

### **Lägger till egenskapen AutoFilter.ShowFilterButton.**

Indikerar om filterknappen för autofiltret visas.

### **Tar bort föråldrad SeriesCollection.SecondCatergoryData-egenskap.**

Använd egenskapen SeriesCollection.SecondCategoryData istället.

### **Tar bort StyleModifyFlag.Spacing enum.**

Den är inte använd.

