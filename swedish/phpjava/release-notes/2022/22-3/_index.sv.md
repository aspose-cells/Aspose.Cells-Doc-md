---
title: Aspose.Cells for PHP via Java 22.3 Release Notes
type: docs
weight: 10
url: /sv/php-java/aspose-cells-for-php-via-java-22-3-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for PHP via Java 22.3](https://downloads.aspose.com/cells/php/new-releases/aspose.cells-for-php-via-java-22.3/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44369| formhöjden är inte korrekt|
|CELLSJAVA-44366|Att kopiera arkinnehållet till en ny arksida och spara det som html orsakar att Excel-matteformelns stil är onormal|
|CELLSJAVA-44408|Procentformatet Cell går förlorat när vi utökar de två raderna som vi har ändrat|
|CELLSJAVA-44341|Cell bredd är inte korrekt i utdata DOCX i Excel till DOCX konvertering|
|CELLSJAVA-44383|Villkorlig formatering slutade fungera efter att ha lagt till anpassade egenskaper|
|CELLSJAVA-44370|Excel-filen blir korrupt när den öppnas och sparas med Aspose.Cells|
|CELLSJAVA-44344| Problem med horisontell kopiering av intervall i utgången XLSX|
|CELLSJAVA-44363| radhuvudets höjd matchar inte radinnehållet i filen med freezepan|
|CELLSJAVA-44349|bild/form ska behållas efter omstart av servern för GridWeb|
|CELLSJAVA-44367|Färgen på kolumndiagrammet blir vit vid konvertering till html|
|CELLSJAVA-44328| Vissa dataetiketter för Excel-diagram går förlorade när Excel-fil sparas som HTML|
|CELLSJAVA-44193|Vinkeln för kategoriaxelobjekt i grafen är annorlunda i Excel till PDF-konvertering|
|CELLSJAVA-44314|Fel axeletiketter för diagramkategori i diagram till bild-rendering|
|CELLSJAVA-44332|Cell länk understrykning kan inte ta bort när du konverterar xlsx till html|
|CELLSJAVA-44323|Undantag när signaturrad läggs till|
|CELLSJAVA-44361|CellsException höjdes när xlsx konverterades till html|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

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
