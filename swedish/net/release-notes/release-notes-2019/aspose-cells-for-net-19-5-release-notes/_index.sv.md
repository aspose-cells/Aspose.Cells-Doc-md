---
title: Aspose.Cells for .NET 19.5 Release Notes
type: docs
weight: 80
url: /sv/net/aspose-cells-for-net-19-5-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 19.5](https://www.nuget.org/packages/Aspose.Cells/19.5.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46703|Den nya japanska kalendern visas inte korrekt|Ny funktion|
|CELLSNET-46693|Supportbakgrund för ODS|Ny funktion|
|CELLSNET-46695|Ställ in bakgrund av ODS-fil|Ny funktion|
|CELLSNET-46706|Ogiltig nummerordning vid konvertering av arabiskt teckensnitt till PDF.|Förbättring|
|CELLSNET-46692|Styr all extern data med IStreamProvider-gränssnittet|Förbättring|
|CELLSNET-46711|ImportCustomObjects till sammanslagna områdesbrytningar sammanfogas|Förbättring|
|CELLSNET-46713|Metoden "String.StartsWith("\0")" returnerar alltid true på macOS|Förbättring|
|CELLSNET-46719|Undantag vid inställning av HTML sträng med RGBA-färgmodellen|Förbättring|
|CELLSNET-46701|Bearbetningen av bubbeldiagram hänger med version 19.4|Insekt|
|CELLSNET-46682|Alternativet "Dölj objekt utan data" för Slicer-inställningar är avmarkerat|Insekt|
|CELLSNET-46707|PivotTable.GetChildren() returnerar fel antal beroenden|Insekt|
|CELLSNET-46689|Att spara en arbetsbok som PDF är annorlunda än excels ursprungliga utdata|Insekt|
|CELLSNET-46704|Resultatet av att konvertera Excel till PDF med Aspose.Cells är annorlunda än Excel|Insekt|
|CELLSNET-46720|Sidstrukturen är skadad på sista sidan i Excel till PDF konvertering|Insekt|
|CELLSNET-46727|Fel sidnumrering när arbetsboken sparades som PDF|Insekt|
|CELLSNET-46700|Etiketter för cirkeldiagramsdata överlappar varandra|Insekt|
|CELLSNET-46696|Att konvertera XLS med Microsoft grafdiagram till XLSX och XLSM orsakar ett oläsbart innehållsfel|Insekt|
|CELLSNET-46697|Att konvertera XLSM med OLE-objekt till XLS orsakar ett fel|Insekt|
|CELLSNET-46712|Att konvertera XLS med Microsoft grafdiagram till XLSX och XLSM orsakar ett oläsbart innehållsfel|Insekt|
|CELLSNET-46715|Cells.InsertCutCells() Issue|Insekt|
|CELLSNET-46725|"_x000a_" sträng läggs till i flerradsdiagram alt textbeskrivning|Insekt|
|CELLSNET-46683|Undantag vid rendering av en Excel-fil till PDF|Undantag|
|CELLSNET-46690|Ett undantag uppstår när Excel-arbetsbok laddas från Shape.ForeignData (Diagram)|Undantag|
|CELLSNET-46728|Undantag när strömmen sparas som arbetsbok|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Lägger till StreamProviderOptions konstruktor**
Nya StreamProviderOptions.
#### **Lägger till FileFormatType.GraphChart enum**
Representerar den inbäddade diagramfilen.
#### **Lägger till egenskaper för ImportTableOptions.CheckMergedCells**
Anger om sammanslagna celler kontrolleras vid import av data.
#### **Lägger till ODSCellFieldCollection, ODSCellField-klasser och ODSCellFieldType enum.**
Representerar cellfältet ODS.
#### **Lägger till Cells.ODSCellFields-egenskaper.**
Hämtar listan över cellfält för ODS.
#### **Lägger till ODSPageBackground-klass och PageSetup.ODSPageBackground-egenskap**
Representerar bakgrunden till ODS.
