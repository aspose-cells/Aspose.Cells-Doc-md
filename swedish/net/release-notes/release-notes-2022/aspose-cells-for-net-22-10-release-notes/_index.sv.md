---
title: Aspose.Cells för .NET 22.10 Release Notes
type: docs
weight: 3
url: /sv/net/aspose-cells-for-net-22-10-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 22.10](https://www.nuget.org/packages/Aspose.Cells/22.10.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-42037|Pivottabelltidslinjefiltret försvinner efter att Excel-dokumentet har laddats och uppdaterats|
|CELLSNET-51963|Stöd för CRTX-filer|
|CELLSNET-51952|MAXIFS-formler tar lång tid att beräkna|
|CELLSNET-52064|Det är inte tillåtet att trycka bort icke-tomma celler från slutet av kalkylbladsfelet när du använder metoden Cells.InsertRows|
|CELLSNET-52029|Översätt etiketter för förklaringsposter i enlighet med lokala/regionala inställningar|
|CELLSNET-51419|External Link of Pivot-tabell togs bort när XLS-filen konverterades till XLSM|
|CELLSNET-51984|XLSX-fil med PivotTable-fil är skadad efter att ha sparats på nytt|
|CELLSNET-51987|Problem med några smarta markörer (insatta) i pivottabellen och pivotdiagrammet|
|CELLSNET-52065|Fel externa dataanslutningar vid konvertering av externa anslutningar|
|CELLSNET-52088| Extra rad läggs till när du skapar klassisk pivottabell|
|CELLSNET-52018| GetValidationValue felaktigt med NotBetween-operatorn|
|CELLSNET-52069|Decimalvärden i resultatet av Cell. Formeln kan skilja sig från vad ms excel visar|
|CELLSNET-52078|Style.SetPatternColor(BackgroundType,Color,Color) träder inte i kraft|
|CELLSNET-52105|LightCellsDataHandler.StartSheet(Worksheet) kan inte hoppa över arket när det returneras false för xlsb-mallfilen|
|CELLSNET-46764|Saknade diagramtitel vid konvertering till pdf|
|CELLSNET-52049|XLSX till PDF: Texten är inte korrekt formaterad|
|CELLSNET-52073|Problem gällande Arial Tur-font i Excel till PDF-rendering|
|CELLSNET-52083|Vissa celler med kontonummerformatet återges som #####.|
|CELLSNET-52091|När du ställer in kalkylbladets innehåll till svartvitt skrivs det fortfarande ut i färg och ramar visas i onödan|
|CELLSNET-51972|Kalkylblad som innehåller knappobjekt känns inte igen ordentligt när arket kopieras|
|CELLSNET-51973| Html-tabell till Excel-ark har inte konverterats korrekt|
|CELLSNET-52001|Återsparar en XLSX-fil genererad korrupt fil|
|CELLSNET-52015|Det gick inte att ladda energifrågaformeln från Excel-filen|
|CELLSNET-52054| Stilkorruption efter att ha sparat och öppnat en Aspose.Cells-genererad arbetsbok|
|CELLSNET-52056| Hyperlänkdupliceringsproblem|
|CELLSNET-52071| Excel till XML-konvertering - Elementnamn är inte escaped|
|CELLSNET-52074|HTML till XLSX: Cellinnehåll saknas|
|CELLSNET-52084|Positionen för texten "Northwind Traders" är felaktig (det vänstra indragsvärdet tolkas inte korrekt).|
|CELLSNET-52063|PivotTable.CalculateData orsakade NullReferenceException|
|CELLSNET-51986|Att beräkna arbetsbok två gånger med aktiverad beräkningskedja orsakade undantag|
|CELLSNET-52081|Att öppna XLSX-fil vars stilar har tagits bort ger undantag|
|CELLSNET-52044|Undantag togs upp vid import av kundens fil i GridWeb|
|CELLSNET-52002|Undantag görs när man försöker öppna ett oskyddat dokument med ett lösenord|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Ändrade gränsen för att flytta celler ut från arket för att infoga rader**

I gamla versioner, om det finns celler som har formateringsinställningar men som inte har något värde? och som kommer att flyttas ut från arket, är infogning inte tillåten. Från 22.10 är infogning tillåten för en sådan typ av situation och sådant beteende är samma sak med ms excel nu.

### **Lägger till klassen DataModelConnection**

Anger en datamodellanslutning.

### **Lägger till metoder för Chart.ChangeTemplate(byte[]).**

Ändra diagramtyp med förinställd mallfil.

### **Lägger till ChartCollection.Add(byte[] data, sträng dataRange, bool isVertical, int topRow, int leftColumn,int rightRow, int bottomColumn).**

Lägger till diagram med förinställd mallfil.
