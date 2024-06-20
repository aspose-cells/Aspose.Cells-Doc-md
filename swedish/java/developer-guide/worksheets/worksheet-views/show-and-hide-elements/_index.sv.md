---
title: Visa och dölj element
type: docs
weight: 60
url: /sv/java/show-and-hide-elements/
---

{{% alert color="primary" %}}

Aspose.Cells låter användaren visa och dölja element i en arbetsbok inklusive arbetsblad, rader, kolumner, flikar, rullfält, rutnät

{{% /alert %}}

## **Visa och dölj ett arbetsblad**

En Excel-fil kan ha ett eller flera arbetsblad. När vi skapar en Excel-fil lägger vi till arbetsblad i Excel-filen där vi arbetar. Varje arbetsblad i en Excel-fil är oberoende från det andra arbetsbladet genom att ha sina egna data och formateringsinställningar osv. Ibland kan utvecklare behöva dölja några arbetsblad och göra andra synliga i Excel-filen för deras eget intresse. Så, **Aspose.Cells** låter utvecklare kontrollera synligheten av arbetsbladen i deras Excel-filer.

**Kontrollera synligheten av arbetsbladen:**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som tillåter att komma åt varje arbetsblad i Excel-filen.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett arbetsblad. Men, för att kontrollera synligheten av ett arbetsblad, kan utvecklare använda [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metoden i [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassen.

### **Göra ett arbetsblad synligt**

Utvecklare kan göra ett arbetsblad synligt genom att skicka **true** som parameter till [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metoden i [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassen.

### **Dölja ett arbetsblad**

Utvecklare kan dölja ett arbetsblad genom att skicka **false** som parameter till [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metoden i [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassen.

**Exempel:**

Ett komplett exempel ges nedan som visar användningen av [**setVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metoden i [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassen för att dölja det första arbetsbladet i Excel-filen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**Arbetsblad - Före modifiering:**

På skärmdumpen nedan kan du se att **Book1.xls** filen innehåller tre arbetsblad: **Blad1** , **Blad2** och **Blad3** .

![todo:image_alt_text](show-and-hide-elements_1.png)

**Figur:** Visning av arbetsblad före någon modifiering

**Arbetsblad - Efter att exempelkoden har utförts:**

**Book1.xls** filen öppnas med hjälp av [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klassen och sedan görs det första arbetsbladet i **Book1.xls** filen dolt. Den modifierade filen sparas som **output.xls** filen vars bildvisning visas nedan:

![todo:image_alt_text](show-and-hide-elements_2.png)

**Figur:** Visning av arbetsblad efter modifiering

**Inställning av VisibilityType**

Du kan också gömma arbetsbladen på ett speciellt sätt. Denna funktion kan gömma arbetsbladet så att det enda sättet för dig att göra det synligt igen är genom att ge [**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) som parametervärde för [**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) metoden i koden (det ska noteras här att användarna inte kan göra objektet synligt i MS Excel direkt genom att använda dess menyalternativ). Användare kan också använda [**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) metoden för att kontrollera om ett arbetsblad är markerat som VeryHidden eller inte.

## **Visa eller göm flikar**

Om du tittar noga längst ner i en Microsoft Excel-fil, kommer du att se ett antal kontroller. Dessa inkluderar:

- Arkflikar.
- Flikbläddringsknappar.

Arkflikar representerar arbetsbladen i Excel-filen. Klicka på vilken flik som helst för att växla till det arbetsbladet. Ju fler arbetsblad i arbetsboken, desto fler arkflikar finns det. Om Excel-filen har ett bra antal arbetsblad behöver du knappar för att navigera genom dem. Så tillhandahåller Microsoft Excel flikbläddringsknappar för att bläddra igenom arkflikarna.

**Arkflikar & flikbläddringsknappar**

![todo:image_alt_text](show-and-hide-elements_3.png)

Genom att använda Aspose.Cells kan utvecklare kontrollera synligheten av arkflikar och flikbläddringsknappar i Excel-filer.

**Kontrollera synligheten av flikar:**
Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil.

### **Gömma flikar**

Göm flikar i en Excel-fil genom att ställa in [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassens [**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs)-metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **Göra flikar synliga**

Gör flikar synliga med [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassens [**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs)-metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**Fullständigt kodexempel:**

Här nedan följer ett komplett exempel som öppnar en Excel-fil (book1.xls), gömmer dess flikar och sparar den modifierade filen som output.xls.

Du kan se att filen Book1.xls innehåller flikar i figuren nedan. Efter att exempelkoden har utförts göms flikarna, som du kan se på skärmbilden av filen output.xls nedan.

**book1.xls: Excel-fil innan någon modifiering**

![todo:image_alt_text](show-and-hide-elements_4.png)

**output.xls: Excel-fil efter modifiering**

![todo:image_alt_text](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **Visa och göm rader och kolumner**

Alla arbetsblad i en Excel-fil består av celler som är placerade i rader och kolumner. Alla rader och kolumner har unika värden som används för att identifiera dem, och för att identifiera enskilda celler. Till exempel är rader numrerade - 1, 2, 3, 4 osv. - och kolumner är ordnade alfabetiskt - A, B, C, D osv. Rad- och kolumnvärden visas i rubrikerna. Genom att använda Aspose.Cells kan utvecklare styra synligheten av dessa rad- och kolumnrubriker.

**Kontrollera synligheten av arbetsbladen:**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. Workbook-klassen innehåller en WorksheetCollection som tillåter åtkomst till varje arbetsblad i en Excel-fil.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassen. Worksheet-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att styra synligheten av rad- och kolumnrubriker, använd Worksheet-klassens [**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)-metod.

### **Gömma rad-/kolumnrubriker**

Göm rad- och kolumnrubriker genom att använda [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassens [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)-metod.

### **Göra rad-/kolumnrubriker synliga**

Gör rad- och kolumnrubriker synliga genom att använda [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassens [**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)-metod.

Ett komplett exempel ges nedan som visar hur man använder [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassens [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)-metod för att gömma rad- och kolumnrubrikerna i det första arbetsbladet i en Excel-fil.

Skärmdumpen nedan visar att Book1.xls innehåller tre arbetsblad: Sheet1, Sheet2 och Sheet3. Varje arbetsblad visar rad- och kolumnrubriker.

**Book1.xls: arbetsblad före modifiering**

![todo:image_alt_text](show-and-hide-elements_6.png)

Book1.xls är öppnad med [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen och rad- och kolumnrubrikerna på första arbetsbladet är dolda. Den modifierade filen sparas som output.xls.

**Arbetsbladsvy efter ändring**

![todo:image_alt_text](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **Visa och dölj bildrullningsfält**

Bildrullningsfält används för att navigera genom innehållet i vilken fil som helst. Normalt sett finns det två typer av bildrullningsfält:

- Vertikala bildrullningsfält
- Horisontella bildrullningsfält

Microsoft Excel tillhandahåller också horisontella och vertikala bildrullningsfält så att användare kan bläddra genom arbetsbladets innehåll. Med Aspose.Cells kan utvecklare kontrollera synligheten av båda typer av bildrullningsfält i Excelfiler.

**Kontrollera synligheten av bildrullningsfälten:**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Excelfil. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excelfil. Men för att kontrollera synligheten av bildrullningsfälten i Excelfilen kan utvecklare använda [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) & [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) metoder i [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen.

### **Dölja bildrullningsfält**

Dölj bildrullningsfält genom att sätta [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassens [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) eller [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible)-metoder till falskt.

### **Gör bildrullningsfält synliga**

Gör rullningsfält synliga genom att ställa in Workbookklassens [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) eller [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) metoder till **true**.

**Fullständigt kodexempel:**

Nedan finns en komplett kod som öppnar en Excel-fil, book1.xls, gömmer båda rullningsfälten och sparar sedan den modifierade filen som output.xls.

Skärmdumpen nedan visar filen Book1.xls som innehåller båda rullningsfälten. Den modifierade filen sparas som output.xls-fil, också visas nedan.

**Book1.xls: Excel-fil innan någon ändring**

![todo:image_alt_text](show-and-hide-elements_8.png)

**output.xls: Excel-fil efter modifiering**

![todo:image_alt_text](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **Visa och dölj rutnät**

Alla Microsoft Excel-arbetsblad har som standard rutnät. De hjälper till att avgränsa celler, så att det är lätt att mata in data i specifika celler. Rutnät gör det möjligt för oss att visa ett arbetsblad som en samling celler, där varje cell är lätt identifierbar.

Aspose.Cells låter dig också kontrollera synligheten av rutnätet.

### **Kontrollera synligheten av rutnätet**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som tillåter åtkomst till varje arbetsblad i filen.

Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att kontrollera synligheten av rutnätet, använd [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassens [**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) metod.

#### **Gör rutnätslinjer synliga**

För att göra rutnätslinjer synliga, använd [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassens [**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) metod.

#### **Gömmer rutnätslinjer**

Göm rutnätslinjer genom att använda [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassens [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) metod.

{{% alert color="primary" %}}

Rutnät appliceras på hela arket. För att 'gömma' rutnätslinjer på en del av ett arbetsblad, använd [bordersformatering](/cells/sv/java/create-table-by-using-border-lines-for-a-range/) för att ställa in gränserna till en färg som smälter samman med arket färgschema.

{{% /alert %}}

**Exempel: Gömma rutnätslinjer på ett visst arbetsblad**

Exemplet nedan demonstrerar användningen av [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassens [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) metod för att gömma rutnätslinjer på det första arbetsbladet i en Excel-fil.

Skärmdumpen nedan visar att filen Book1.xls innehåller tre arbetsblad: Sheet1, Sheet2 och Sheet3. Alla dessa arbetsblad har rutnätslinjer.

**Arbetsbladsvy innan ändring**

![todo:image_alt_text](show-and-hide-elements_10.png)

Filen Book1.xls öppnas med hjälp av [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen och sedan göms rutnätslinjerna på det första arbetsbladet. Den modifierade filen sparas som output.xls-fil.

**Arbetsbladsvy efter ändring**

![todo:image_alt_text](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **Relaterade artiklar**

{{% alert color="primary" %}}

- [Sidinställningsfunktioner](/cells/sv/java/page-setup-features/).
- [Lägga till gränser till celler för att skapa en tabell](/cells/sv/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
