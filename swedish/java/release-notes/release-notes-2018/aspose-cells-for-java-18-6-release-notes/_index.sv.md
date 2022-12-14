---
title: Aspose.Cells för Java 18.6 Release Notes
type: docs
weight: 70
url: /sv/java/aspose-cells-for-java-18-6-release-notes/
---
{{% alert color="primary" %}}

Den här sidan innehåller utgåvor för Aspose.Cells för Java 18.6.

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42339|Implementera anpassad datasortering i pivottabellrapporten via Aspose.Cells API:er|Ny funktion|
|CELLSJAVA-42625|Implementeringen av MS Excel-funktionen "Watch Window"|Ny funktion|
|CELLSJAVA-42612|Det går inte att extrahera texten från kugghjulstypen SmartArt|Ny funktion|
|CELLSJAVA-42646|Undantag: "FormulaBuild](/p Okänd formel token0" på Name.getRefersTo()|Förbättring|
|CELLSJAVA-42645|Undantag: "FormulaBuild More than one token in stack...." på Cell.getFormula()|Förbättring|
|CELLSJAVA-42516|Aspose.Cells accepterar och korrigerar en ogiltig formel|Förbättring|
|CELLSJAVA-42636|Vissa ritningsformer förskjuts eller återges felaktigt i Excel till HTML-rendering|Insekt|
|CELLSJAVA-42627|CELLSJAVA-42619 - Det går inte att extrahera Smart Art-bilder korrekt|Insekt|
|CELLSJAVA-42618|Formen förskjuts för att täcka data i Excel till HTML-rendering|Insekt|
|CELLSJAVA-42628|Beräkning av formler är fel, t.ex. genererar #DIV/0! fel|Insekt|
|CELLSJAVA-42615|Cell A3-formatet är inte korrekt i utdata-HTML|Insekt|
|CELLSJAVA-42621|Dålig prestanda vid generering av PDF-fil från en MS Excel-fil|Insekt|
|CELLSJAVA-42620|XLSX till TIFF - undantag NoClassDefFoundError|Insekt|
|CELLSJAVA-42599|Bilder går förlorade när Excel-filen konverteras till PDF|Insekt|
|CELLSJAVA-42630|Chart.calculate-metoden orsakar OutOfMemoryError|Insekt|
|CELLSJAVA-42623|Minnet ökar vid rendering av Excel-fil till PDF-filformat|Insekt|
|CELLSJAVA-42592|Teckenstorleken har ändrats på diagramtiteln på grund av metoden characters().|Insekt|
|CELLSJAVA-41860|Skuggeffekten ändras medan XLS sparas på nytt|Insekt|
|CELLSJAVA-42654|Excel till PDF-konvertering - konverteringen slutförs aldrig|Insekt|
|CELLSJAVA-42647|Det gick inte att hämta eller ställa in alternativ text för kommentarform|Insekt|
|CELLSJAVA-42644|Aspose.Cells hänger sig vid konvertering av en kalkylarks ml-fil (xml) till PDF med självstängande Styles-tagg|Insekt|
|CELLSJAVA-42632|Det gick inte att ställa in alternativ text för SmartArt-formen|Insekt|
|CELLSJAVA-42631|getFirstVisibleRow() och getFirstVisibleColumn() returnerar ogiltiga index|Insekt|
|CELLSJAVA-42624|Hyperlänkar med kodade symboler (som "%5c") avkodas efter att de har sparats på nytt|Insekt|
|CELLSJAVA-42638|Cell.getDisplayStringValue() kastar java.lang.NullPointerException|Undantag|
|CELLSJAVA-42652|java.lang.ArrayIndexOutOfBoundsException inträffade när en XLS-fil laddades|Undantag|
|CELLSJAVA-42650|Undantag: "Ogiltig kodning: null" när en XLS-fil laddas|Undantag|
|CELLSJAVA-42649|Undantag: "Antalet HPageBreaks kan inte vara större än 1024" när en XLS-fil laddas|Undantag|
|CELLSJAVA-42648|Undantag: "Det gick inte att läsa bilddata" på Picture.getData()|Undantag|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Lägger till klasserna Slicer, SlicerCollection, SlicerCache, SlicerCacheItem och SlicerCacheItemCollection**

Dessa API:er används för att skapa och ändra Slicer i filen.

### **Lägger till SlicerCacheItemSortType och SlicerStyleType enums**

Dessa API:er används för att skapa och ändra Slicer i filen.

### **Lägger till CellWatchCollection och CellWatch klasser, lägger till Worksheet.CellWatches egendom**

Lägger till Cell Watch Item i "bevakningsfönstret".

### **Lägger till klassen CustomXmlShape och MsoDrawingType.CustomXml enum**

Stöder att behålla anpassad xml-form.

### **Lägger till MsoDrawingType.SmartArt enum**

Representerar den smarta konstformen.

### **Lägger till Font.SchemeType-egenskapen och FontSchemeType-numren**

Hämtar och ställer in schematypen för teckensnittet.

### **Lägger till egendomen CustomXmlPart.ID**

Hämtar och ställer in ID för anpassad xml-del.

### **Lägger till metoden CustomXmlPartCollection.SelectByID().**

Får anpassad xml-del efter id.

### **Lägger till Range.Address, Range.CellCount, EntireColumn, Range.EntireRow och Range.GetOffset(System.Int32,System.Int32)**

Förbättring för bearbetningsområde.

### **Lägger till ColorDepth enum och egenskapen ImageOrPrintOptions.TiffColorDepth**

Hämtar eller ställer in bitdjup för att endast tillämpas när sidor sparas i Tiff-formatet.

### **Överbelastar metoden WorkbookRender.ToImage().**

Återger arbetsboken till bild genom sidindex.

### **Lägger till metoden Legend.LegendEntriesLabels().**

Hämtar etiketterna för förklaringsposterna efter att ha anropat metoden Chart.Calculate().

### **Lägger till metoden CustomFilter.SetCriteria(FilterOperatorType filterOperator, objektkriterier)**

Ställer in filterkriterierna.

### **Tillhandahåller nya API:er för stöd för att hämta/ställa in formler i språkberoende format (FormulaLocal-funktionen i Microsoft Interop)**

Cell.GetFormula(bool ärR1C1, bool ärLokal)
Cell.SetFormula(strängformel, bool ärR1C1, bool ärLokal, objektvärde)
Name.GetRefersTo(bool ärR1C1, bool ärLokal)
Name.SetRefersTo(string refersTo, bool isR1C1, bool isLocal)
FormatCondition.GetFormula1(bool ärR1C1, bool ärLokal)
FormatCondition.SetFormula1(strängformel, bool ärR1C1, bool ärLokal)
FormatCondition.GetFormula2(bool ärR1C1, bool ärLokal)
FormatCondition.SetFormula2(strängformel, bool ärR1C1, bool ärLokal)
FormatCondition.GetFormula1(bool ärR1C1, bool ärLokal, int rad, int kolumn)
FormatCondition.GetFormula2(bool ärR1C1, bool ärLokal, int rad, int kolumn)
GlobalizationSettings.GetTableRowTypeOfHeaders()
GlobalizationSettings.GetTableRowTypeOfData()
GlobalizationSettings.GetTableRowTypeOfAll()
GlobalizationSettings.GetTableRowTypeOfTotals()
GlobalizationSettings.GetTableRowTypeOfCurrent()
GlobalizationSettings.GetErrorValueString(strängfel)
GlobalizationSettings.GetBooleanValueString(bool bv)
GlobalizationSettings.GetLocalFunctionName(sträng standardnamn)
GlobalizationSettings.GetStandardFunctionName(sträng lokalnamn)
GlobalizationSettings.GetLocalBuiltInName(sträng standardnamn)
GlobalizationSettings.GetStandardBuiltInName(sträng lokalnamn)
GlobalizationSettings.ListSeparator
GlobalizationSettings.RowSeparatorOfFormulaArray
GlobalizationSettings.ColumnSeparatorOfFormulaArray
