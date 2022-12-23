---
title: Aspose.Cells for .NET 20.6 Release Notes
type: docs
weight: 20
url: /sv/net/aspose-cells-for-net-20-6-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 20.6](https://www.nuget.org/packages/Aspose.Cells/20.6.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47353|Stöd för lagring av temporär fil för sessionsinformation i GridWeb|Förbättring|
|CELLSNET-47388|GridWeb SessionMode.File ska lagra cachefil för olika sidor/flikar|Förbättring|
|CELLSNET-46062|Legend of Chart renderas inte korrekt på grund av asiatiska och latinska tecken|Förbättring|
|CELLSNET-47373|Att spara arbetsboken i PDF MemoryStream varar i mer än 2 minuter|Förbättring|
|CELLSNET-43418|Kopiera och klistra in (endast data) ett icke sammanhängande intervall|Förbättring|
|CELLSNET-47315|Filen kunde inte öppnas när den sparades i zip64|Förbättring|
|CELLSNET-47384|Förbättra laddningsprestanda för bild/form|Prestanda|
|CELLSNET-47382|HTML till Excel-konvertering förlorar formatering|Insekt|
|CELLSNET-47390|Färgen på vissa ord är fel i renderingen HTML till ODS|Insekt|
|CELLSNET-47385|Cells.InsertCutCells-avbrott i arbetsböcker med en intervallskärning|Insekt|
|CELLSNET-47389|HLOOKUP-beräkningen är inte korrekt|Insekt|
|CELLSNET-47352|Efter att ha klickat på texten försvinner texten|Insekt|
|CELLSNET-47380|Kolumnen är inte justerad|Insekt|
|CELLSNET-47366|Poäng renderade inte till filen PDF|Insekt|
|CELLSNET-47364|Axeletiketter renderas felaktigt om kalkylbladet renderas som en bild|Insekt|
|CELLSNET-47370|Kartpunkten saknas och formen kläms när Excel-fil laddas och sparas|Insekt|
|CELLSNET-47367|Fel axelpilriktning vid konvertering av diagrammet till en bild|Insekt|
|CELLSNET-47362|SourceFullName och ImageType är felaktiga|Insekt|
|CELLSNET-47375|XLSX konverterad till skadad XLS fil.|Insekt|
|CELLSNET-47398|Arbetsblad.Cells.ImportData hoppar över rader när data delas upp i flera ark|Insekt|
|CELLSNET-47371|Undantag för att uppdatera pivottabell(er) i arket|Undantag|
|CELLSNET-47377|Worksheet.RefreshPivotTables() väcker undantag|Undantag|
|CELLSNET-47393|Aspose.Cells.CellsException: Cirkulära referenser|Undantag|
|CELLSNET-47365|Undantag vid laddning av en XLSX-fil|Undantag|
|CELLSNET-47381|Picture.Data-egenskapen skapar ett ArgumentOutOfRange-undantag|Undantag|
|CELLSNET-47374|Breaking Change i RemoveACell vid uppgradering från 19.10 till 20.5|Regression|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till metoden ReferredArea.GetValues(bool calculateFormulas)/GetValue(int rowOffset, int colOffset, bool calculateFormulas).**
Ger användaren möjlighet att styra om formler ska beräknas rekursivt i implementeringen av AbstractCalculationEngine.
#### **Lägger till WarningType.InvalidFontName och WarningType.InvalidTextOfDefinedName enum.**
Representerar varningstypen.
#### **Lägger till egenskaperna WarningInfo.CorrectedObject och WarningInfo.ErrorObject.**
Representerar fel data och uppdaterad data när en varning skickas.
#### **Lägger till WorkbookDesigner.RepeatFormulasWithSubtotal-egenskaper.**
Anger om repeterande formler med delsumma rader.
#### **Lägger till egenskapen PlotArea.IsAutomaticSize.**
Den indikerar om storleken på tomtytan är automatisk.
#### **Tar bort föråldrad Style.Rotation-egenskap.**
Använd Style.RotationAngle-egenskapen istället.
#### **Lägger till metoden Gridweb.SetFontFolder(string fontFolder, bool rekursiv)/SetFontFolders(string[] fontFolders, bool rekursiv).**
Ställer in typsnittsmapp/mappar
