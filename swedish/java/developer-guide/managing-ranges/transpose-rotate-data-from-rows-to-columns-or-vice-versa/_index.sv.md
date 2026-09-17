---
title: Transponera intervall
linktitle: Transponera intervall
description: Den här artikeln förklarar hur man transponerar eller roterar data från rader till kolumner eller tvärtom i Excel-filer med Aspose.Cells for Java, med tre olika metoder.
keywords: Aspose.Cells, Java-bibliotek, kalkylblad, transponera intervall, rotera data, transponeringsfunktion, dynamisk matrisformel, matrisformel, Excel TRANSPOSE, Rader till Kolumner
type: docs
weight: 80
url: /sv/java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Java stöder transponering (rotering) av data så att rader blir kolumner och kolumner blir rader på tre olika sätt. Den första metoden använder den in-place `Range.transpose()`-metoden och fungerar i alla Excel-versioner, medan den andra använder `Cell.setDynamicArrayFormula()` för att skriva en modern dynamisk matrisformel `=TRANSPOSE(...)` som spiller automatiskt i Excel 365 eller Excel 2021. Den tredje metoden använder `Cell.setArrayFormula()` för att skriva en klassisk Ctrl+Shift+Enter-matrisformel (CSE) som är kompatibel med äldre Excel-versioner. Den här artikeln går igenom varje metod med stegvisa instruktioner och kompletta kodexempel.
{{% /alert %}}

## **Introduktion**
Att transponera ett intervall innebär att man roterar det så att det som var en rad blir en kolumn och det som var en kolumn blir en rad, vilket effektivt speglar datan över dess huvuddiagonal. I Microsoft Excel utför kalkylbladsfunktionen `TRANSPOSE` denna operation, och den konceptuella referensen dokumenteras på [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Detta koncept kan tillämpas programmatiskt på ett intervall av celler, vilket är användbart i många affärs- och rapporteringsscenarier.
- Omorientering av kvartals- eller årsrapporter där kvartal normalt löper över sidan och regioner nedåt, eller tvärtom.
- Byta axelorientering i instrumentpaneler eller diagram så att en tidsserie löper nedåt istället för över sidan.
- Omforma data som importerats från externa system så att de matchar layouten som förväntas av nedströms analys- eller rapporteringsmallar.
För att göra resten av artikeln konkret använder varje exempel följande lilla tabell över försäljning per region och kvartal. I exempelarbetsboken upptar denna tabell intervallet **A1:D5**, där **A1** lämnas tom som det övre vänstra hörnet, **B1:D1** innehåller regionrubrikerna, och **A2:A5** innehåller kvartalsrubrikerna.
| Region            | Europa     | Asien      | Nordamerika  |
|-------------------|------------|------------|--------------|
| Q1                | 21704714   | 8774099    | 12094215     |
| Q2                | 17987034   | 12214447   | 10873099     |
| Q3                | 19485029   | 14356879   | 15689543     |
| Q4                | 22567894   | 15763492   | 17456723     |
Artikeln presenterar sedan tre olika sätt att transponera dessa data med Aspose.Cells for Java, var och ett lämpat för en annan Excel-version och användningsfall.

## **Metod 1 — Transponera intervall på plats (Range.transpose)**
Använd denna metod när du vill transponera data utan att använda kalkylbladsfunktionen `TRANSPOSE`. Den fungerar i **alla versioner av Excel** och har inget beroende av dynamiska matriser, vilket gör den till det säkraste alternativet för kompatibilitet över versioner. Den är idealisk när du bara behöver det slutliga transponerade resultatet och inte behöver behålla den ursprungliga `TRANSPOSE`-formeln i arbetsboken.

### **API som används**
`Range.transpose()` är en instansmetod på klassen `com.aspose.cells.Range`. När den anropas vänder den intervallet på plats genom att byta dess rader och kolumner, så det som var en rad blir en kolumn och det som var en kolumn blir en rad. Metoden modifierar de underliggande cellerna direkt utan att skriva en formel.

### **Steg**
1. Öppna källarbetsboken med `LoadOptions` inställt på `.xlsx`-formatet genom att anropa `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Hämta det första kalkylbladet från arbetsboken med `workbook.getWorksheets().get(0)`.
3. Kom åt kalkylbladets cellsamling via `worksheet.getCells()`.
4. Skapa källintervallet som täcker **A1:D5** genom att anropa `cells.createRange("A1:D5")`.
5. Anropa `source.transpose()` för att rotera intervallet på plats, så att rader och kolumner byts.
6. Spara arbetsboken med `workbook.save(outputFile)`.
Efter transponeringen innehåller det ursprungliga ankarpunktsintervallet den roterade datan. Den första raden läser (tom, **Europa**, **Asien**, **Nordamerika**) och den första kolumnen läser (tom, **Q1**, **Q2**, **Q3**, **Q4**). Varje ursprunglig kolumn av försäljning blir en rad i det transponerade intervallet.

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
source.transpose();
workbook.save(outputFile);
```

## **Metod 2 — Transponera med en dynamisk matrisformel (Excel 365 / 2021)**
Använd denna metod när du vill bevara formeln `=TRANSPOSE(A1:D5)` som en levande formel i utdataarbetsboken så att resultatet uppdateras automatiskt om källdatan ändras, och målets Excelfil kommer att öppnas i **Excel 365 / Excel 2021 eller senare** där dynamiska matriser och spilloperatorn stöds.

### **API som används**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` är en metod på `com.aspose.cells.Cell` som ställer in cellens formel som en **dynamisk matrisformel**. Excel utvärderar formeln en gång och spiller automatiskt resultatet till de omgivande cellerna. Den tredje parametern, när den sätts till `true`, instruerar Aspose.Cells att också beräkna de resulterande värdena vid skrivtillfället.

### **Steg**
1. Ladda källarbetsboken med `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Hämta det första kalkylbladet och kom åt dess `Cells`-samling.
3. Placera den dynamiska matrisformeln i cell **A6**, precis under källintervallet, genom att anropa `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. Argumentet `null` skickar standard-`FormulaParseOptions`, och det tredje argumentet `true` anger att Aspose.Cells ska behandla formeln som en dynamisk matris och utvärdera den så att de spillda värdena skrivs till arbetsboken.
5. Spara arbetsboken med `workbook.save(outputFile)`.
Cell **A6** innehåller formeln `=TRANSPOSE(A1:D5)` och Excel spiller automatiskt resultatet till området **A6:D10**, ett block på 5 rader gånger 4 kolumner lika med den transponerade datan.

{{% alert color="primary" %}}
Denna metod fungerar **endast i Excel 365 / 2021 eller senare**. Äldre Excel-versioner kommer inte att spilla dynamiska matrisformler korrekt.
{{% /alert %}}

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.save(outFile, SaveFormat.XLSX);
```

## **Metod 3 — Transponera med en klassisk matrisformel (CSE)**
Använd denna metod när du vill ha en `TRANSPOSE`-formel bevarad i arbetsboken men målets Excelfil kan öppnas i **äldre Excel-versioner (före 2021, inklusive 2019, 2016, 2013 och så vidare)** där dynamisk matrisformler inte stöds. Den klassiska CSE-matrisformeln (Ctrl+Shift+Enter) är det bakåtkompatibla alternativet som alla Excel-versioner kan utvärdera.

### **API som används**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` är en metod på `com.aspose.cells.Cell` som tilldelar en **klassisk matrisformel (CSE)** till ankarcellen och deklarerar dimensionerna för den resulterande matrisen. Aspose.Cells skriver markören för flercells matrisformel så att Excel utvärderar formeln som ett enda matrisuttryck som fyller det deklarerade intervallet.

### **Steg**
1. Ladda källarbetsboken enligt beskrivningen i de tidigare metoderna.
2. Hämta det första kalkylbladet och kom åt dess `Cells`-samling.
3. Anropa `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Det andra argumentet `4` är antalet rader i destinationsmatrisen och det tredje argumentet `5` är antalet kolumner.
4. Spara arbetsboken med `workbook.save(outputFile)`.
Cell **A6** är ankaret för matrisformeln och den utvärderade matrisen spänner över 4 rader gånger 5 kolumner med start vid A6, vilket matchar de transponerade dimensionerna för A1:D5-källan. Excel skriver en enda matrisformelmarkör över det resulterande intervallet så att äldre Excel-versioner utvärderar det korrekt.

{{% alert color="primary" %}}
CSE-matrisformler är det klassiska Excel-sättet att utvärdera ett `TRANSPOSE`-uttryck och denna metod är universellt kompatibel över Excel-versioner.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Ladda källarbetsboken med xlsx LoadOptions
String srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
// Öppna det första kalkylbladet och dess Cells-samling
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
// Ställ in den klassiska CSE-matrisformeln på cell A6.
// Formeln =TRANSPOSE(A1:D5) roterar källintervallet med 5 rader x 4 kolumner
// till en matris med 4 rader x 5 kolumner. Det andra argumentet (4) är antalet rader
// och det tredje argumentet (5) är antalet kolumner i den resulterande matrisen.
// Aspose.Cells skriver CSE-matrisformelmarkören så att Excel utvärderar den som
// en enda flercelligs matrisformel, kompatibel med äldre Excel-versioner
// (2019, 2016, 2013 osv.) som inte stöder dynamisk matrisavsakning.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Spara arbetsboken så att matrisformelmarkören bevaras
workbook.save("output.xlsx");
```

## **Jämförelse — När ska varje metod användas**
| Metod | API / Metod | Excel-version | Källformel bevarad? | Utdataintervall |
|-------|-------------|---------------|---------------------|-----------------|
| Metod 1 — Transponera på plats | `Range.transpose()` | Alla Excel-versioner | Nej (endast värden) | Ursprungligt ankarpunktsintervall, 5×4 |
| Metod 2 — Dynamisk matrisformel | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Ja (spill dynamiskt) | Spillt från ankarpunkten |
| Metod 3 — Klassisk matrisformel (CSE) | `Cell.setArrayFormula` | Alla Excel-versioner | Ja (flercells matrisformel) | Explicit storlek, 4×5 |
Använd **Metod 1** när du behöver en snabb, versionsövergripande transformation och bara behöver de transponerade värdena skrivna till filen. Använd **Metod 2** när modern Excel är garanterad och du vill att formeln ska förbli levande och uppdateras om källan ändras. Använd **Metod 3** när du behöver den bredaste kompatibiliteten med en bevarad formel över alla Excel-versioner, inklusive de äldre versionerna som inte stöder dynamiska matriser.

## **Relaterade artiklar**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells Java](/cells/sv/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Infoga en bild i en cell](/cells/sv/java/inserting-an-image-into-a-cell/)
- [Dela upp Excel-filer i flera filer](/cells/sv/java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="java" >}}