---
title: Aspose.Cells for .NET 22.3 Release Notes
type: docs
weight: 10
url: /sv/net/aspose-cells-for-net-22-3-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 22.3](https://www.nuget.org/packages/Aspose.Cells/22.3.0).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-50375|Stöd sortering av PivotField via värden i vald rad/kolumn|
|CELLSNET-50559|Stöd för att få cellens blad rekursivt|
|CELLSNET-50512|Stöd för att räkna om celler som refererar till definierat namn när det definierade namnet ändras och beräkningskedjan är aktiverad|
|CELLSNET-50403|Lägg till SaveFormat.Ots och SaveFormat.Xlt|
|CELLSNET-50422|Stödinställning inuti boders|
|CELLSNET-50342|Pivottabellen sorterar inte vid uppdatering|
|CELLSNET-50451|Om du tar bort kalkylblad tas Slicers bort|
|CELLSNET-50462|Regression: Efter kopiering av cellintervall går formler förlorade|
|CELLSNET-50545| Villkorligt formaterade fält är inte färgade i rätt färg|
|CELLSNET-50565|Formler beräknades inte korrekt|
|CELLSNET-50309|Intervall till PNG: utgången inte som förväntat|
|CELLSNET-50334|Regression: XLS till PDF: rubriken inte renderad korrekt|
|CELLSNET-50367|Att konvertera .XLSX till PDF tar lång tid och ger extra sidor|
|CELLSNET-50401|Numeriska värden eller siffror följt av rader är inte synliga i den resulterande pdf-filen|
|CELLSNET-50478|Workbook.ExportXml returnerar endast första raden med tabelldata|
|CELLSNET-50507|Xml Import visar tidigare dolda kolumner i mallen|
|CELLSNET-50554|Innehållet renderas inte korrekt i Excel till PDF konvertering|
|CELLSNET-50316|Inslagna texter fungerar inte på diagram när PDF genereras|
|CELLSNET-50411|Horisontella axeletiketter i diagrammet återges inte korrekt i utgången PDF|
|CELLSNET-50341|Problem med komprimera och expandera grupper på flera nivåer|
|CELLSNET-50368|ODS till PDF felaktig konvertering|
|CELLSNET-50377|Anpassad "Text"-formatering tillämpas inte i filen XLS|
|CELLSNET-50380| Egenskapen ImportTableOptions.IsHtmlString matar inte ut länkar korrekt|
|CELLSNET-50418|Ladda HTML i arbetsboken fungerar inte|
|CELLSNET-50494|Problem med färg för villkorligt formaterade celler i utdatafilen XLSX|
|CELLSNET-50563|Problem när du ställer in inbäddad licens för att producera singelfil i .NET 6.0-applikationen|
|CELLSNET-50585|Inga snedstreck framåt utan snedstreck bakåt för externa länkar med URL|
|CELLSNET-50390| System.ArgumentException: Radnummer eller kolumnnummer kan inte vara noll vid import av JSON-data som tabell|
|CELLSNET-50555| ArgumentOutOfRangeException när du försöker få formeln för en cell|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Ändrar standardvärdet för HtmlSaveOptions.ExcludeUnusedStyles.**

När vi sparar html-filer, för gamla versioner tar vi ibland bort de oanvända stilarna automatiskt när det finns många stilobjekt i poolen, oavsett vad den här egenskapen har för värde. För de genererade html-filerna kan exkludering av oanvända stilar göra filstorleken mindre utan att påverka de visuella effekterna. Så från den här versionen gör vi standardvärdet för denna egenskap som sant för att det ska överensstämma med sparbeteendet. Om användaren behöver behålla alla stilar i arbetsboken för den genererade HTML-koden (t.ex. scenariot att användaren behöver återställa arbetsboken från den genererade HTML-koden senare), ställ in den här egenskapen som falsk medan du sparar HTML.

### **Lägger till metoden Cell.GetLeafs(bool rekursiv).**

Stöd användaren att få alla blad i en cell rekursivt.

### **Lägger till metoden Range.SetInsideBorders(BorderType, CellBorderType, CellsColor).**

Stöd för att sätta inre gränser för sortimentet.

### **Lägger till SaveFormat.Ots,SaveFormat.Xlt och LoadFormat.Ots enum.**

Förbättring för att ladda och spara ots och xlt-filer.

### **Lägger till klassen FormulaSettings.**

Separera alla formelrelaterade inställningar från WorkbookSettings och gruppera dem som FormulaSettings.

### **Lägger till egenskapen WorkbookSettings.FormulaSettings.**

Hämtar de grupperade inställningarna för formler.

### **Lägger till egenskapen PivotItem.IsHideDetail.**

Hämtar och ställer in om pivotobjektet döljer detaljer.

### **Obsoletes WorkbookSettings.ReCalculateOnOpen-egenskapen.**

Använd WorkbookSettings.FormulaSettings.CalculateOnOpen istället.

### **Obsoletes WorkbookSettings.RecalculateBeforeSave egenskap.**

Använd WorkbookSettings.FormulaSettings.CalculateOnSave istället.

### **Obsoletes WorkbookSettings.ForceFullCalculate-egenskapen.**

Använd WorkbookSettings.FormulaSettings.ForceFullCalculation istället.

### **Obsoletes WorkbookSettings.PrecisionAsVisad egenskap.**

Använd WorkbookSettings.FormulaSettings.PrecisionAsDisplayed istället.

### **Obsoletes WorkbookSettings.CalcMode-egenskapen.**

Använd WorkbookSettings.FormulaSettings.CalculationMode istället.

### **Obsoletes WorkbookSettings.Iteration-egenskap.**

Använd WorkbookSettings.FormulaSettings.EnableIterativeCalculation istället.

### **Obsoletes WorkbookSettings.MaxIteration-egenskap.**

Använd WorkbookSettings.FormulaSettings.MaxIteration istället.

### **Obsoletes WorkbookSettings.MaxChange-egenskap.**

Använd WorkbookSettings.FormulaSettings.MaxChange istället.

### **Obsoletes WorkbookSettings.CalculationId-egenskap.**

Använd WorkbookSettings.FormulaSettings.CalculationId istället.

### **Obsoletes WorkbookSettings.CreateCalcChain-egenskapen.**

Använd WorkbookSettings.FormulaSettings.EnableCalculationChain istället.

### **Obsoletes WorkbookSettings.CalcStackSize-egenskap.**

Använd CalculationOptions med den angivna stapelstorleken istället när du beräknar formler.
