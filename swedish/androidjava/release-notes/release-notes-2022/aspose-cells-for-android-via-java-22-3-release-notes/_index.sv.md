---
title: Aspose.Cells for Android via Java 22.3 Release Notes
type: docs
weight: 10
url: /sv/java/aspose-cells-for-android-via-java-22-3-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Android via Java 22.3.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-44162|Stöd för att ta bort extern länk utan att ta bort formlerna|
|CELLSJAVA-44214|Stöd för att autopassa rader för GridWeb|
|CELLSJAVA-44205|Stöd platsberoende enhetstext för koordinataxlar i diagrammet|
|CELLSJAVA-44238|Stöd för att behålla sessionen efter omstart av servern för GridWeb|
|CELLSJAVA-44317|Texten i denna xlsx är förvrängd|
|CELLSJAVA-44126|Cell.getDependents() kastar undantag om cellens formel inte har analyserats|
|CELLSJAVA-44161|Fel i extern formel när du importerar en arbetsbok till en annan arbetsbok|
|CELLSJAVA-44130|Texten på dataetiketterna lindas in i utdatadiagrambilden|
|CELLSJAVA-44204|pagineringsproblem för csv|
|CELLSJAVA-43934|Cirkeldiagrametiketterna matchas inte med Excel efter manipulering eller uppdatering av diagram|
|CELLSJAVA-44122|Vid export av HTML skiljer sig dataetiketterna från Excel|
|CELLSJAVA-41949| Innehållet återges annorlunda när du sparar arbetsbok i XLSX- och HTML-format|
|CELLSJAVA-44207|Vid export till HTML blir radhöjden högre|
|CELLSJAVA-44233|Oändlig loop vid konvertering av XLSX-fil|
|CELLSJAVA-44271|När du konverterar Excel till PDF skiftar utdatapositionen jämfört med fallet med manuell konvertering|
|CELLSJAVA-44197|När du konverterar XLSX till PDF visas inte pivottabellens tidslinjeform (fönster).|
|CELLSJAVA-44267|Arbetsbok som innehåller en pivottabell blir skadad|
|CELLSJAVA-44114|XLSX till PDF: Data i vetenskapligt nummerformat från XLSX-filen matchar inte data i utdata-PDF-filen|
|CELLSJAVA-44293|Återsparad Excel-fil måste återställas när den öppnas i MS Excel|
|CELLSJAVA-43194|Bilderna visas felaktigt|
|CELLSJAVA-44243|GridWeb spring demo spara fil misslyckades i jdk1.8|
|CELLSJAVA-44276|radhuvudets höjd överensstämmer inte med radinnehållet efter redigeringscellen för filen 249.xls|
|CELLSJAVA-44284|öka minnesundantaget för filen bug.xlsx|
|CELLSJAVA-44229|Formel går förlorad när td-innehåll lindas med div-tagg|
|CELLSJAVA-44247|En rad text lindas under konvertering till pdf|
|CELLSJAVA-44175| problem med överlappande Donut Chart-etiketter|
|CELLSJAVA-44192| Kategoriaxelns objektnamn i grafen är avskuret i Excel till PDF-konvertering|
|CELLSJAVA-44233|Oändlig loop vid konvertering av XLSX-fil|
|CELLSJAVA-44263|Att ställa in riktningen för kartetiketttexten till vertikalt träder inte i kraft|
|CELLSJAVA-44268| Undantag "java.lang.NullPointerException" på Chart.toPdf-metoden|
|CELLSJAVA-44302|Textriktningen för koordinataxeln är fel efter att Excel-filen konverterats till HTML|
|CELLSJAVA-44314|Fel axeletiketter för diagramkategori i diagram till bild-rendering|
|CELLSJAVA-44274|Stöds SVG-format för läsning eller rendering till PDF|
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
|CELLSJAVA-44234|Fel på minnet för filen data.xls|
|CELLSJAVA-44246|Undantag "Invalid endrow index" för tom fil|
|CELLSJAVA-44258| Null pekare undantag för fil|
|CELLSJAVA-44311|Undantag "java.lang.OutOfMemoryError: Java heap space" vid rendering till HTML-filformat|
|CELLSJAVA-44285|Undantag "java.lang.ClassCastException: com.aspose.cells.n2f kan inte castas till com.aspose.cells.o90" när Workbook.calculateFormula() anropas|
|CELLSJAVA-44323|Undantag när signaturrad läggs till|
|CELLSJAVA-44361|CellsException höjdes när xlsx konverterades till html|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts för allmänheten API, t.ex. tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Android via Java. Om du har frågor om någon ändring i listan, vänligen ta upp det på supportforumet Aspose.Cells.

### **Ändrar beteende för att ta bort externa länkar från arbetsboken.**

I gamla versioner tar vi inte bort den externa länken vars url innehåller "AddIns". Sådant beteende är utformat för vissa användares speciella krav. Defekten med en sådan lösning är uppenbar: användare kan ange vilket giltigt filnamn eller sökväg som helst för de externa referenserna och i själva verket vill de flesta inte att de externa länkarna ska behandlas annorlunda. Från den här versionen filtrerar vi inte längre dessa externa länkar. Om användare har särskilda krav på vissa externa länkar, kan de kontrollera alla objekt i ExternalLinkCollection en efter en och bara ta bort de som de vill ta bort (med ExternalLinkCollection.RemoveAt(int)-metoden).

### **Ändrar beteende för Cell. Typ för ogiltigt datum och tid.**

I gamla versioner, om en cell begärs att formateras som datum och tid, returnerar Cell.Type CellValueType.IsDateTime oavsett om det numeriska värdet för denna cell är giltigt för datum och tid eller inte. Detta kan orsaka undantag om användare är beroende av Cell.Skriv endast och försöker ringa Cell.DateTimeValue. Från den här versionen returnerar vi CellValueType.IsNumeric för sådana typer av celler så att användaren kan vägledas att få cellvärdet med korrekt API.

### **Ändrar beteende för Cells.MaxDisplayRange.**

I gamla versioner täcker intervallvärdet för den här egenskapen alla celler som har instansierats i cellsamlingen. Från denna version gör vi att de osynliga raderna/kolumnerna exkluderas från kanterna på visningsområdet om det bara finns instansierade celler i dessa rader/kolumner.

### **Ändrar DataSorter.Sort()-metoder för att returnera de ursprungliga indexen för sorterade rader/kolumner.**

gamla versioner? DataSorter.Sort() metoder returnerar ingenting. Från denna version returnerar vi de ursprungliga indexen för rader/kolumner som motsvarar intervallet som har sorterats. Detta ger användaren möjlighet att utföra avancerad kontroll och operationer för sorteringen.

### **Lägger till egenskapen TxtLoadOptions.ExtendToNextSheet.**

Stöder import av CSV/TSV-data till flera kalkylblad om radantalet eller kolumnantal data överskrider ms excels gräns.

### **Lägger till metoden ExternalLinkCollection.Clear().**

Tar bort alla externa länkar från arbetsboken.

### **Lägger till metoden ExternalLinkCollection.Clear(bool updateReferencesAsLocal).**

När du tar bort alla externa länkar från arbetsboken kan användaren bestämma hur man ska göra med formlerna som har referenser till dessa externa länkar. Om "updateReferencesAsLocal" är sant, kommer alla anpassade definierade funktioner i de externa länkarna att flyttas till den aktuella arbetsboken. Till exempel är en cells formel "='externalsource.xlam'!customfunction()", efter att den externa länken "externalsource.xlam" har tagits bort, kommer denna cells formel att bli "=customfunction()".

### **Lägger till ExternalLinkCollection.RemoveAt(int)-metoden.**

Tar bort en angiven extern länk från arbetsboken.

### **Lägger till metoden ExternalLinkCollection.RemoveAt(int, bool updateReferencesAsLocal).**

I likhet med metoden ExternalLinkCollection.Clear(bool updateReferencesAsLocal) kan användaren bestämma hur formler som refererar till den angivna externa länken ska göras samtidigt som den tas bort från arbetsboken.

### **Lägger till metoden ExternalLinkCollection.GetEnumerator().**

Tillhandahåller en enumerator för att iterera genom alla externa länkar i arbetsboken.

### **Föråldrade Workbook.RemoveExternalLinks()-metoden.**

Använd metoden ExternalLinkCollection.Clear() istället.

### **Obsoletes Workbook.HasExernalLinks()-metoden.**

Använd ExternalLinkCollection.Count för att kontrollera om det finns externa länkar i arbetsboken.

### **Tar bort föråldrad klass StyleCollection.**

Använd Workbook.CreateStyle() och Workbook.GetNamedStyle(sträng) för att manipulera stilar.

### **Lägger till konstruktorn PptxSaveOptions(bool saveAsImage).**

Representerar alternativ för att spara .pptx-fil. Om det är sant kommer arbetsboken att konverteras till några bilder av .pptx-filen. Om False, kommer arbetsboken att konverteras till vissa tabeller av .pptx-fil.

### **Lägger till klassen ChartGlobalizationSettings.**

 Representerar globaliseringsinställningarna för diagram.

### **Lägger till egenskapen DataLabels.IsNeverOverlap.**

Indikerar om dataetiketterna aldrig överlappar varandra. (För cirkeldiagram)

### **Lägger till TickLabelItem-klassen.**

Inkludera information om ett Ticklabel-objekt.

### **Lägger till egenskapen TickLabelItem.Height.**

Får höjden på Ticklabel-objektet i förhållande till diagramhöjden.

### **Lägger till egenskapen TickLabelItem.Width.**

Får bredden på Ticklabel-objektet i förhållande till diagrambredden.

### **Lägger till egenskapen TickLabelItem.X.**

Får X av Ticklabel-objekt i förhållande till diagrambredd.

### **Lägger till egenskapen TickLabelItem.Y.**

Får Y av Ticklabel-objekt i förhållande till diagramhöjd.

### **Lägger till egenskapen TickLabels.TickLabelItems.**

Får föremålen från TickLabel.

### **Föråldrad Cells.AddAddInFunction()-metoden.**

Använd metoderna WorksheetCollection.RegisterAddInFunction() istället.

### **Lägger till metoden NameCollection.Filter() och NameScopeType enum.**

Hämtar de definierade namnen efter omfattning.

### **Lägger till MsoDrawingType.Timeline enum.**

Representerar typ av tidslinjeritningsobjekt.

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