---
title: Aspose.Cells for .NET 21.1 Release Notes
type: docs
weight: 30
url: /sv/net/aspose-cells-for-net-21-1-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 21.1](https://www.nuget.org/packages/Aspose.Cells/21.1.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-47376|Release Aspose.Cells for .NET 5.0|Ny funktion|
|CELLSNET-40624| Hur man byter rad/kolumndataserie med aspose|Ny funktion|
|CELLSNET-42195|Konvertera kontroll från xlsm till xls|Ny funktion|
|CELLSNET-47806|Hämtar datakällans intervall för diagrammet.|Ny funktion|
|CELLSNET-47756|SmartArt-former renderas inte bra i Excel till PDF-konvertering|Insekt|
|CELLSNET-47391|Former är inte korrekt placerade i excel till pdf-konverteringar|Insekt|
|CELLSNET-47766|Pildiagrammet är ofullständigt|Insekt|
|CELLSNET-47653|Diagram block flyttas vid konvertering till HTML|Insekt|
|CELLSNET-47720|Ogiltig CSS- och HTML-uppmärkning vid konvertering av XLSX till HTML|Insekt|
|CELLSNET-47746|Okodade citattecken i värden för HTML-attribut|Insekt|
|CELLSNET-47792|Bilder överlappar texten när du importerar html till Excel|Insekt|
|CELLSNET-47797|Dålig länk när XLSM-fil renderas i HTML|Insekt|
|CELLSNET-47807|Ogiltig HTML-uppmärkning med kapslade A-element|Insekt|
|CELLSNET-47778|IRR-beräkning utvärderas till #NUM|Insekt|
|CELLSNET-47814|GridDesktop rullningslister är inte dolda|Insekt|
|CELLSNET-47744|Radiella plotter kläms när de exporteras till pdf|Insekt|
|CELLSNET-47786|XErrorBar visas inte i diagrammet|Insekt|
|CELLSNET-47787|XErrorBars försvinner när du kopierar diagram från en arbetsbok till en annan|Insekt|
|CELLSNET-43907|WordArt renderas inte när XLS konverteras till PDF|Insekt|
|CELLSNET-47780|Problem med att ställa in två intervall som datakälla för diagrammet|Insekt|
|CELLSNET-47781|Wrap Text fungerar inte för ODS-filer|Insekt|
|CELLSNETCORE-94| Pivottabellgrupp efter dag ökar när den uppdateras|Insekt|
|CELLSNETCORE-77|Fel vid konvertering av XLSX till PDF på Azure|Insekt|
|CELLSNETCORE-90|Problem med att infoga bilagor i excel-kalkylblad|Insekt|
|CELLSNETCORE-93|H1-tagg renderas inte utan ytterligare taggar som understruken, kursiv eller fetstil|Insekt|
|CELLSNETCORE-97|Att anropa RemoveExternalLinks() ger upphov till undantag|Insekt|
|CELLSNET-47719|Det gick inte att spara xlsb till xlsx|Undantag|
|CELLSNET-47784|Undantag vid import av HTML-dokument med IStreamProvider|Undantag|
|CELLSNET-47801|CalculateData på pivottabellen ger undantag|Undantag|
|CELLSNET-47809|Cell.ContainsExternalLink kastar "Kan inte casta|Undantag|
|CELLSNET-47791| Diagram som orsakar att Workbook.Save misslyckas|Undantag|
|CELLSNET-47808|Undantag uppstod vid beräkning av ett tomt diagram|Undantag|
|


## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Tar bort föråldrad ReplaceOptions.IsCaseSensitive-egenskap (ENDAST .NET).**

Använd ReplaceOptions.CaseSensitive istället.

### **Föråldrad PdfSaveOptions(SaveFormat) konstruktor.**

Använd PdfSaveOptions()-konstruktorn istället.

### **Föråldrad XlsbSaveOptions(SaveFormat) konstruktor.**

Använd XlsbSaveOptions()-konstruktorn istället.

### **Föråldrad XlsSaveOptions(SaveFormat) konstruktor.**

Använd XlsSaveOptions()-konstruktorn istället.

### **Föråldrad SpreadsheetML2003SaveOptions(SaveFormat) konstruktor.**

Använd SpreadsheetML2003SaveOptions()-konstruktorn istället.

### **Lägger till metoden Chart.GetChartDataRange().**

Hämtar dataintervallskällan för diagrammet.

### **Lägger till metoden Chart.SwitchRowColumn().**

Byter rad/kolumn för diagrammets dataintervallskälla.

### **Lägger till metoden OleObject.SetEmbeddedObject().**

Ställer in inbäddat objekt.

### **Lägger till metoden VbaProject.ValidatePassword().**

 
Validerar lösenordet för VBA-projektet.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerBackgroundColor och Series.MarkerBackgroundColor, lägger till egenskapen Marker.BackgroundColor.**

Använder Marker.BackgroundColor istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerForegroundColor och Series.MarkerForegroundColor , lägger till egenskapen Marker.ForegroundColor.**

Använder Marker.ForegroundColor istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerBackgroundColorSetType och Series.MarkerBackgroundColorSetType , lägger till egenskapen Marker.BackgroundColorSetType.**

Använder Marker.BackgroundColorSetType istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerForegroundColorSetType och Series.MarkerForegroundColorSetType , lägger till egenskapen Marker.ForegroundColorSetType.**

Använder Marker.ForegroundColorSetType istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerSize och Series.MarkerSize.**

Använder Marker.MarkerSize istället.

### **Tar bort föråldrade egenskaper för ChartPoint.MarkerStyle och Series.MarkerStyle.**

Använder Marker.MarkerStyle istället.

