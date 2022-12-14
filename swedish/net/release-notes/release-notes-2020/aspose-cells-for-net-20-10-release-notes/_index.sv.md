---
title: Aspose.Cells för .NET 20.10 Release Notes
type: docs
weight: 7
url: /sv/net/aspose-cells-for-net-20-10-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 20.10](https://www.nuget.org/packages/Aspose.Cells/20.10.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47625|Verifierar lösenord för krypterade filer|Ny funktion|
|CELLSNET-47601|Återge extra rad och kolumn i HTML utan störande formler/referenser för att likna utdata med MS Excel|Ny funktion|
|CELLSNET-47619|Aspose Diagram SetChartDataRange Problem|Förbättring|
|CELLSNET-47632|Struktur och ordningsskillnad i OLE för indata och utdata efter att filen har sparats|Förbättring|
|CELLSNET-47644|Olika externa anslutningar hämtade jämfört med MS Excel|Förbättring|
|CELLSNET-47652|Teckensnittsavstånd problem vid inställt teckenformat|Förbättring|
|CELLSNET-47623|Långsam sparoperation med massor av formler i filen|Prestanda|
|CELLSNET-47606|Applikationen hänger sig när Excel konverteras till PDF|Prestanda|
|CELLSNET-47611|Fråga om beräkning av IRR-formel|Insekt|
|CELLSNET-47616|Ta bort Range som beter sig annorlunda mellan v20.8 och v20.9|Insekt|
|CELLSNETCORE-83|Excel-filen visades inte korrekt i GridWeb|Insekt|
|CELLSNETCORE-86|Formvisningsproblem i GridWeb|Insekt|
|CELLSNET-47597|Fyllningsområdena är mycket olika jämfört med källfilen|Insekt|
|CELLSNET-47614|Vissa symboler saknas i PDF-utdata i Excel till PDF-rendering|Insekt|
|CELLSNET-47636|Excel till PDF-konvertering - Resultatet går över sidan i liggande riktning|Insekt|
|CELLSNET-47637|Konvertera Excel till PDF-problem med Calibri Light|Insekt|
|CELLSNET-42982|Diagramstorlek och layout ändrades efter Workbook.Combine|Insekt|
|CELLSNET-47594|Möjlighet att få PlotBy och OnAction-information som liknar MS Excel|Insekt|
|CELLSNET-47595|Diagrammet behölls inte korrekt i Excel-filen när det laddades och sparades tillbaka|Insekt|
|CELLSNET-47599|AddControlRefrernce lägger inte till en referens till MS Forms 2.0|Insekt|
|CELLSNET-47600|Formkontrollnamn och få andra egenskaper är annorlunda jämfört med MS Excel|Insekt|
|CELLSNET-47613|LTR och RTL bevaras inte efter laddning och sparas med XLSB-fil|Insekt|
|CELLSNET-47615|Power Point-fil inbäddad i Excel-fil kan inte öppnas efter spara|Insekt|
|CELLSNET-47645|Reparationsmeddelande från MS Excel efter att ha laddat och sparat Excel-filer med Aspose.Cells|Insekt|
|CELLSNET-47647|Reparationsmeddelande från Excel vid konvertering av XLSB->XLSX->XLSB|Insekt|
|CELLSNET-47648|XLSB-filen är skadad efter konvertering (XLSB->XLSX-XLSB)|Insekt|
|CELLSNET-47658|Teckenstorleken är avrundad när vi har angett decimalsymbol med regioninställning|Insekt|
|CELLSNETCORE-81|Alternativet "Wrap text" bevaras inte i XLSB-filen efter Ladda och spara|Insekt|
|CELLSNETCORE-82|Specifikt ark inuti XLSB-filen går sönder efter laddning och spara|Insekt|
|CELLSNETCORE-84|Stilinformation returnerades tillsammans med rubriktexten|Insekt|
|CELLSNETCORE-85|Cells.InsertCutCells korrumperar anteckningar|Insekt|
|CELLSNET-47544|Bilder saknas och textens position var fel vid rendering av Excel i Linux|Insekt|
|CELLSNET-47571|HTML-konvertering från XLS går in i en kontinuerlig konverteringsslinga|Insekt|
|CELLSNET-47583|PivotTable.TableRange2 ger fel värde för pivottabellen|Insekt|
|CELLSNET-47584|Aspose.Cells HTML till Excel-konvertering visade inga bilder|Insekt|
|CELLSNET-47609|Diagram visas inte i html när arket inte har något annat innehåll|Insekt|
|CELLSNET-47633|Pivottabellen med datum uppdateras inte korrekt|Insekt|
|CELLSNET-47635|Slicer på olika bord genererar skadad fil|Insekt|
|CELLSNET-47620|Forma till bild Fel när du sparade till PDF|Undantag|
|CELLSNET-47608|NullReferenceException vid laddning av XLSX|Undantag|
|CELLSNET-47624|System.ArgumentException vid laddning av krypterad fil till XLAM|Undantag|
|CELLSNET-47630|Det angivna argumentet låg utanför intervallet för giltiga värden undantag vid borttagning av kolumn|Undantag|
|CELLSNET-47649|Undantag höjs vid läsning av DBConnection.PowerQueryFormula från XLSX-fil|Undantag|
|CELLSNET-47655|CellsException under konvertering av Excel till PDF|Undantag|
|CELLSNETCORE-80|Det gick inte att casta objektundantaget när XLSB konverterades till XLSM|Undantag|
|CELLSNET-47593|Undantag när man försöker öppna en viss HTM|Undantag|
|CELLSNET-47656|Form till bild Fel vid konvertering av XLSB till PDF|Undantag|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Lägger till ExceptionType.Permission enum**

Representerar ExceptionType.Permission.

### **Lägger till egenskapen ExternalConnection.PowerQueryFormula.**

Hämtar definitionen av kraftfrågeformel.

### **Lägger till metoden FileFormatUtil.VerifyPassword.**

Verifierar om lösenordet är giltigt för filen.

### **Lägger till metoden VbaProject.Copy().**

Kopierar VBA-projekt.

### **Lägger till egenskapen XlsSaveOptions.MatchColor.**

Indikerar om matchande färg om färgen inte finns i paletten när .xls-filen sparas.

### **Tar bort föråldrad Series.Line-egenskap.**

Använd egenskapen Series.Border istället.
