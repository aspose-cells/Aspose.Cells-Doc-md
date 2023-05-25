---
title: Aspose.Cells for .NET 23.2 Release Notes
type: docs
weight: 11
url: /sv/net/aspose-cells-for-net-23-2-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 23.2](https://www.nuget.org/packages/Aspose.Cells/23.2.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
| :- | :- | :- |
|CELLSNET-52620|Stöd för att analysera/läsa/spara SCAN och Lambda-funktioner|
|CELLSNET-52666|Stöder flera sideringsformat vid konvertering av Excel till pptx|
|CELLSNET-52627|Extrahera cellformat till ett generiskt objekt (t.ex. JSON)|
|CELLSNET-52683|Cell.Formeln är inte densamma som visas i MS Excel|
|CELLSNET-52691|Formler är felaktigt beräknade|
|CELLSNET-52519|Problem med att läsa diagram från Excel-fil (genererad av Aspose.Cells) till Microsoft Graf API|
|CELLSNET-52544|Diagram till PDF inte samma som till bild|
|CELLSNET-52635| Texten i diagrammet i SVG har fel position|
|CELLSNET-52585|Genererad xps-fil kunde inte laddas av System.Windows.Xps.Packaging.XpsDocument|
|CELLSNET-52622|Kan inte generera SVG med upphöjd och nedsänkt från Excel-fil|
|CELLSNET-52692|Text har förlorats i det konverterade XPS-dokumentet|
|CELLSNET-52438| Dataförlust när du sparar ett pivottabelldiagram|
|CELLSNET-52555|Skillnad i tecken/textposition när det valda kalkylbladet renderas till HTML|
|CELLSNET-52583|Konvertering till Docx ger en extra tom sida|
|CELLSNET-52612|Problem att öppna PowerQuery efter ändring|
|CELLSNET-52613|Konvertering av Numbers till Pptx ger trasigt resultat|
|CELLSNET-52630|HTML till Excel-konvertering - tabeller renderas inte korrekt|
|CELLSNET-52631| Att spara en XLSX-fil som XLSB skadar färger och lägger till filter|
|CELLSNET-52639|Sjökortsaxelns titelrotation återställs efter kopiering med Aspose.Cells|
|CELLSNET-52662| Xml Import förlorar formler i beräknade kolumner|
|CELLSNET-52671|XmlImport korrumperar filen när man försöker uppdatera pivottabeller med beräknad kolumn|
|CELLSNET-52675|Stilen på cellen förlorade efter import av xml.|
|CELLSNET-52684|Kommentarsformatering förlorat vid kopiering av Range|
|CELLSNET-52690|JsonLayoutOptions fungerar inte.|
|CELLSNET-52696|Tabelloperationer genererar skadade Excel-filer|
|CELLSNET-52549|Spara ark till HTML med SmartArt-kast System.NullReferenceException|

##  **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

###  **Lägger till egenskapen ChartTextFrame.IsAutomaticRotation**

Indikerar om texten i diagrammet roteras automatiskt.

###  **Föråldrade egenskaperna JsonLayoutOptions.IgnoreObjectTitle och JsonLayoutOptions.IgnoreArrayTitle**

Använd egenskapen JsonLayoutOptions.IgnoreTitle istället.

###  **Lägger till egenskapen JsonLayoutOptions.IgnoreTitle**

Ingores titlar på Json-attribut vid konvertering av json till Excel.

###  **Lägger till metoden Style.ToJson().**

Konverterar stil av Excel-filer till json-fil

###  **Lägger till metoden Cell.ToJson().**

Konverterar en cell med celler till json-fil.

