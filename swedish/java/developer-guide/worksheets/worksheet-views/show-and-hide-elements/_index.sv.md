---
title: Visa och dölj element
type: docs
weight: 60
url: /sv/java/show-and-hide-elements/
---
{{% alert color="primary" %}}

Aspose.Cells låter användaren visa och dölja delar av en arbetsbok inklusive kalkylblad, rader, kolumner, flikar, rullningslister, rutnät,

{{% /alert %}}

## **Visa och dölj ett arbetsblad**

 En Excel-fil kan ha ett eller flera kalkylblad. När vi skapar en Excel-fil lägger vi till kalkylblad till Excel-filen som vi arbetar i. Varje kalkylblad i en Excel-fil är oberoende av det andra kalkylbladet genom att ha sina egna data och formateringsinställningar etc. Ibland kan utvecklare behöva göra några kalkylblad dolda och andra synliga i Excel-filen för sitt eget intresse. Så,**Aspose.Cells** låter utvecklare kontrollera synligheten för kalkylbladen i sina Excel-filer.

**Styra arbetsbladens synlighet:**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Excel-fil.[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[**Arbetsbladssamling**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)som gör det möjligt att komma åt varje kalkylblad i Excel-filen.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass.[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. Men för att kontrollera synligheten för ett kalkylblad kan utvecklare använda[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metod för[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass.

### **Göra ett arbetsblad synligt**

 Utvecklare kan göra ett kalkylblad synligt genom att passera**Sann** som en parameter till[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metod för[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass.

### **Dölja ett arbetsblad**

 Utvecklare kan dölja ett kalkylblad genom att skicka det**falsk** som en parameter till[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metod för[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass.

**Exempel:**

 Ett komplett exempel ges nedan som visar användningen av[**setVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metod av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass för att dölja det första kalkylbladet i Excel-filen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**Arbetsblad - före ändring:**

 På skärmdumpen nedan kan du se det**Bok1.xls** filen innehåller tre arbetsblad:**Blad 1** , **Blad 2** och**Blad 3** .

![todo:image_alt_text](show-and-hide-elements_1.png)

**Figur:** Arbetsbladsvy före eventuell ändring

**Arbetsblad - Efter exekvering av exempelkoden:**

**Bok1.xls** filen öppnas med hjälp av[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass och sedan det första kalkylbladet i**Bok1.xls** filen görs dold. Den ändrade filen sparas som**output.xls**fil vars bildvy visas nedan:

![todo:image_alt_text](show-and-hide-elements_2.png)

**Figur:** Arbetsbladsvy efter ändring

**Ställa in VisibilityType**

 Du kan också dölja kalkylbladen på ett speciellt sätt. Den här funktionen kan dölja kalkylbladet så att det enda sättet för dig att göra det synligt igen är genom att ge[**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) som parametervärde för[**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) metod i koden (det bör noteras här, användaren kan inte göra objektet synligt i MS Excel direkt genom att använda dess menyalternativ). Användare kan också använda[**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) metod för att kontrollera om ett kalkylblad är markerat som VeryHidden eller inte.

## **Visa eller dölj flikar**

Om du tittar noga på botten av en Microsoft Excel-fil kommer du att se ett antal kontroller. Dessa inkluderar:

- Bladflikar.
- Tabbrullningsknappar.

Bladflikar representerar kalkylbladen i Excel-filen. Klicka på valfri flik för att växla till det kalkylbladet. Ju fler kalkylblad i arbetsboken, desto fler flikar finns det. Om Excel-filen har ett stort antal kalkylblad behöver du knappar för att navigera genom dem. Så, Microsoft Excel tillhandahåller flikrullningsknappar för att rulla igenom arkflikarna.

**Bladflikar & flikrullningsknappar**

![todo:image_alt_text](show-and-hide-elements_3.png)

Med hjälp av Aspose.Cells kan utvecklare styra synligheten för arkflikar och flikars rullningsknappar i Excel-filer.

**Styra synligheten för flikar:**
 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil.

### **Döljer flikar**

 Dölj flikar i en Excel-fil genom att ställa in[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass'[**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **Göra flikar synliga**

 Gör flikarna synliga med[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass'[**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**Komplett kodexempel:**

Nedan är ett komplett exempel som öppnar en Excel-fil (book1.xls), gömmer dess flikar och sparar den ändrade filen som output.xls.

Du kan se att filen Book1.xls innehåller flikar i figuren nedan. Efter att exempelkoden har körts är flikarna dolda, som du kan se från skärmdumpen av filen output.xls nedan.

**book1.xls: Excel-fil före eventuella ändringar**

![todo:image_alt_text](show-and-hide-elements_4.png)

**output.xls: Excel-fil efter modifiering**

![todo:image_alt_text](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **Visa och dölj rader och kolumner**

Alla kalkylblad i en Excel-fil är sammansatta av celler som är ordnade i rader och kolumner. Alla rader och kolumner har unika värden som används för att identifiera dem och för att identifiera enskilda celler. Till exempel är rader numrerade – 1, 2, 3, 4, etc. – och kolumner ordnas i alfabetisk ordning – A, B, C, D, etc. Rad- och kolumnvärdena visas i rubrikerna. Med hjälp av Aspose.Cells kan utvecklare kontrollera synligheten för dessa rad- och kolumnrubriker.

**Styra arbetsbladens synlighet:**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen Workbook innehåller en WorksheetCollection som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)klass. Klassen Worksheet tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att kontrollera synligheten för rad- och kolumnrubriker, använd klassen Worksheet'[**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) metod.

### **Döljer rad-/kolumnrubriker**

 Dölj rad- och kolumnrubriker genom att använda[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) metod.

### **Gör rad-/kolumnrubriker synliga**

 Gör rad- och kolumnrubriker synliga genom att använda[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) metod.

 Ett komplett exempel ges nedan som visar hur man använder[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) metod för att dölja rad- och kolumnrubriker i det första kalkylbladet i en Excel-fil.

Skärmdumpen nedan visar att Book1.xls innehåller tre arbetsblad: Blad1, Blad2 och Blad3. Varje kalkylblad visar rad- och kolumnrubriker.

**Book1.xls: kalkylblad före ändring**

![todo:image_alt_text](show-and-hide-elements_6.png)

 Book1.xls öppnas med hjälp av[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class' och rad- och kolumnrubriken på det första kalkylbladet är dolda. Den ändrade filen sparas som output.xls.

**Arbetsbladsvy efter ändring**

![todo:image_alt_text](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **Visa och dölj rullningslister**

Rullningslister är mycket använda för att navigera i innehållet i alla filer. Normalt finns det två typer av rullningslister:

- Vertikala rullningslister
- Horisontella rullningslister

Microsoft Excel tillhandahåller även horisontella och vertikala rullningslister så att användare kan rulla igenom kalkylbladets innehåll. Med hjälp av Aspose.Cells kan utvecklare kontrollera synligheten för båda typerna av rullningslister i Excel-filer.

**Styra synligheten för rullningslisterna:**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Excel-fil.[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. Men för att kontrollera synligheten för rullningslisterna i Excel-filen kan utvecklare använda[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) & [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) metoder för[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass.

### **Döljer rullningslister**

 Dölj rullningslister genom att ställa in[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass'[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) eller[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) metoder för att**falsk**.

### **Göra rullningslister synliga**

 Gör rullningslister synliga genom att ställa in Workbook-klassen'[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) eller[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) metoder för att**Sann**.

**Komplett kodexempel:**

Nedan finns en komplett kod som öppnar en Excel-fil, book1.xls, döljer båda rullningslisterna och sedan sparar den ändrade filen som output.xls.

Skärmdumpen nedan visar filen Book1.xls som innehåller båda rullningslisterna. Den modifierade filen sparas som output.xls-fil, även visad nedan.

**Book1.xls: Excel-fil före eventuella ändringar**

![todo:image_alt_text](show-and-hide-elements_8.png)

**output.xls: Excel-fil efter modifiering**

![todo:image_alt_text](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **Visa och dölj rutnätslinjer**

Alla Microsoft Excel-kalkylblad har rutnät som standard. De hjälper till att avgränsa celler, så att det är lätt att mata in data i särskilda celler. Gridlines gör det möjligt för oss att se ett kalkylblad som en samling celler, där varje cell är lätt att identifiera.

Aspose.Cells låter dig också kontrollera synligheten för rutnätet.

### **Styra rutnätets synlighet**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[**Arbetsbladssamling**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som ger åtkomst till varje kalkylblad i filen.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att kontrollera synligheten av rutnät, använd[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) metod.

#### **Gör rutnät synliga**

 För att göra rutnät synliga, använd[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) metod.

#### **Dölja rutnät**

 Dölj rutnät med hjälp av the[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) metod.

{{% alert color="primary" %}}

Rutnätslinjer appliceras på hela arket. Använd[kantformatering](/cells/sv/java/create-table-by-using-border-lines-for-a-range/) för att ställa in kanterna till en färg som smälter in i arkets färgschema.

{{% /alert %}}

**Exempel: Dölja rutnätslinjer på ett visst kalkylblad**

 Exemplet nedan visar användningen av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) metod för att dölja rutnät i det första kalkylbladet i en Excel-fil.

Skärmdumpen nedan visar att Book1.xls-filen innehåller tre kalkylblad: Sheet1, Sheet2 och Sheet3. Alla dessa kalkylblad har rutnät.

**Arbetsbladsvy före ändring**

![todo:image_alt_text](show-and-hide-elements_10.png)

 Book1.xls-filen öppnas med hjälp av[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass och sedan döljs rutnätslinjerna för det första kalkylbladet. Den ändrade filen sparas som output.xls-fil.

**Arbetsbladsvy efter ändring**

![todo:image_alt_text](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **relaterade artiklar**

{{% alert color="primary" %}}

- [Sidinställningsfunktioner](/cells/sv/java/page-setup-features/).
- [Lägga till kanter till celler för att skapa en tabell](/cells/sv/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
