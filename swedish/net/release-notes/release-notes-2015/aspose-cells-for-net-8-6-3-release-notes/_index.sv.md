---
title: Aspose.Cells for .NET 8.6.3 Release Notes
type: docs
weight: 10
url: /sv/net/aspose-cells-for-net-8-6-3-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 8.6.3](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.6.3/)

{{% /alert %}}

Följande är en lista över förbättringar och ändringar i denna version av Aspose.Cells

## 1) Aspose.Cells

### **Andra förbättringar och förändringar**

### **Nya egenskaper**

(CELLSNET-44084) - Analysera HTML-taggar samtidigt som du importerar data i bulk

(CELLSNET-40889) - Ladda alternativ: Öppna endast synliga ark

### **Förbättringar**

(CELLSNET-44133) - Stöd för Print Page Size Thermal 3x11

(CELLSNET-44095) - Stöd för läsning/skrivning Externt länkad tabell.

(CELLSNET-44093) - Obfuskerat undantag vid inläsning av ogiltig arbetsbok

(CELLSNET-43425) - Cells.ImportGridView importerar inte Header Row

(CELLSNET-41718) - Stöd för insamling av kapslade objekt i Smart Markers

(CELLSNET-41482) - Stöd för DateTime vid sammanslagning med Smart Markers

### **Prestanda**

(CELLSNET-44096) - Arbetsbok.CalculateFormula fastnar på obestämd tid

(CELLSNET-44102) - Prestandafördröjning vid konvertering av kalkylblad till EMF

### **Buggar**

(CELLSNET-44092) - Problem med att läsa Hyperlink.Address med kyrilliska tecken

(CELLSNET-44090) - XLSB-fil med pivottabell blir skadad i v8.6.2

(CELLSNET-44073) - Konvertering till HTML med HtmlHiddenColDisplayType.Remove skapar ett tomt diagram

(CELLSNET-43917) - Text beskärs medan kalkylarket konverterades till HTML

(CELLSNET-43914) - Text svämmar över rutan medan kalkylarket renderas till PDF

(CELLSNET-44111) - Hyperlänkadressen som innehåller kinesiska tecken konverteras inte korrekt

(CELLSNET-44080) - Cells texten ändrades något åt höger under konverteringen till PDF

(CELLSNET-44125) - Spara till PDF misslyckas för ett Excel-dokument

(CELLSNET-44117) - Felaktig konvertering för diagrammets titel och förklaring

(CELLSNET-44086) - Horisontell axel för diagrammet inuti pdf-filen är fel skalad och omvänd

(CELLSNET-44079) - Vissa poster i diagramförklaringen saknas när du sparar till PDF

(CELLSNET-44046) - Chart.ToImage ändrar etikettjustering

(CELLSNET-44134) - #VÄRDE! returneras för SUMPRODUCT baserat på ListObject

(CELLSNET-44132) - Formel ger "#REF!" värde när du infogar nya rader i utdatafilen

(CELLSNET-44131) - Vissa felaktiga formler visas runt beroende på antalet infogade rader

(CELLSNET-44128) - Spara till XLSB bryter formler som =SUM(Tabell[Kol])

(CELLSNET-44082) - Aspose.Cells visar dolda stilar när du sparar

(CELLSNET-44081) - När två arbetsböcker kombineras skapas en skadad fil

(CELLSNET-44076) - ListObject.ListColumns[i].Namnet är felaktigt när arbetsboken öppnar XLS-fil

(CELLSNET-44028) - Pivottabellen uppdateras inte när du klickar på knappen Data>Uppdatera alla

(CELLSNET-43084) - Utdatafilen är skadad när ett ark kopieras

(CELLSNET-43083) - Referensen till den namngivna cellen är ogiltig "#Name?" när du kopierar ett ark

(CELLSNET-42114) - Problem med att konvertera från xml till XLSX

(CELLSNET-41886) - Diagrammet uppdateras inte med storleken på ListObject

(CELLSNET-41492) - Enorma mängder valideringar

### **Undantag**

(CELLSNET-44097) - Inmatningssträngen var inte i rätt format, på Workbook.Save

(CELLSNET-44099) - CalculateFormula ger undantag

(CELLSNET-44127) - Att spara till PDF-fil/minnesström orsakar undantag

(CELLSNET-44085) - System.Undantag vid laddning av ODS

(CELLSNET-43720) - Fel i okänt område vid kombination av arbetsböcker med pivottabeller

## 2) Aspose.Cells Grid Suite

### **Andra förbättringar och förändringar**

### **Buggar**

(CELLSNET-44123) - Det går inte att serialisera sessionstillståndet System.Collections.Specialized.BitVector32

(CELLSNET-44108) - Worksheet.RemoveColumn/RemoveRow fungerar inte i GridDesktop

(CELLSNET-44105) - Att klicka på knappen Spara utan att ändra fokus på GridWeb uppdaterar inte cellinnehållet i exporterad DataTable

(CELLSNET-44104) - Att använda OnCellClickOnAjax-händelsen gör navigering med knappknapp omöjlig från redigerbar cell

(CELLSNET-44100) - Att zooma ut på GridDesktop-arbetsbladet gör att innehållet krymper i det övre vänstra hörnet

### **Undantag**

(CELLSNET-44107) - Undantag inträffade vid infogning av kolumn i GridDesktop

### **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

Lägger till egenskapen ImportTableOptions.IsHtmlString.

Anger om strängvärdet i datatabellen innehåller html-taggar.

Lägger till metoden Workbook.CreateBuiltinStyle(BuiltinStyleType).

Skapar inbyggd stil efter given typ.

Föråldrad Cells.Slutegendom.

Använd egenskapen Cells.LastCell istället.

Lägger till metoden Cells.ImportGridView(GridView gridView, int firstRow, int firstColumn,ImportTableOptions).

Importerar en rutnätsvy till denna cell med alternativ

Lägger till egenskapen ImportTableOptions.ConvertGridStyle.

Anger om formatet för rutnätsvyn tillämpas på celler.

 Föråldrad Cells.ImportGridView(GridView gridView,int firstRow,int firstColumn, bool insertRows, bool convertStringToNumber, bool convertStyle).

Använd Cells.ImportGridView(GridView gridView, int firstRow, int firstColumn,ImportTableOptions alternativ).

Lägger till egenskapen LoadDataOption.OnlyVisibleWorksheet.

Laddar endast data från det synliga kalkylbladet.

Obsoletes Worksheet.CopyConditionalFormatting-metod.

Använd metoden Cells.CopyRows() eller Range.Copy() istället.
