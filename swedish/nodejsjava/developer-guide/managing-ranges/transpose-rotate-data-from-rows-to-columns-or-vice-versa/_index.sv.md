---
title: Transponera intervall
linktitle: Transponera intervall
description: Denna artikel förklarar hur man transponerar eller roterar data från rader till kolumner eller vice versa i Excel-filer med Aspose.Cells for Node.js via Java, med tre olika metoder.
keywords: Aspose.Cells, Node.js via Java-bibliotek, kalkylblad, transponera intervall, rotera data, transponeringsfunktion, dynamisk matrisformel, matrisformel, Excel TRANSPOSE, Rader till kolumner
type: docs
weight: 80
url: /sv/nodejs-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java stöder transponering (rotering) av data så att rader blir kolumner och kolumner blir rader på tre olika sätt. Det första tillvägagångssättet använder den inbyggda metoden `Range.transpose()` och fungerar i alla Excel-versioner, medan det andra använder `Cell.setDynamicArrayFormula()` för att skriva en modern dynamisk matrisformel `=TRANSPOSE(...)` som spills automatiskt i Excel 365 eller Excel 2021. Det tredje tillvägagångssättet använder `Cell.setArrayFormula()` för att skriva en klassisk Ctrl+Skift+Enter-matrisformel (CSE) som är kompatibel med äldre Excel-versioner. Denna artikel går igenom varje tillvägagångssätt med stegvisa instruktioner och fullständiga kodexempel.
{{% /alert %}}

## **Introduction**
Att transponera ett intervall innebär att rotera det så att det som var en rad blir en kolumn och det som var en kolumn blir en rad, vilket effektivt speglar data över dess huvuddiagonal. I Microsoft Excel utför kalkylbladsfunktionen `TRANSPOSE` denna operation, och den konceptuella referensen dokumenteras på [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Detta koncept kan tillämpas programmatiskt på ett cellintervall, vilket är användbart i många affärs- och rapporteringsscenarier.
- Omorientera kvartals- eller årsrapporter där kvartal normalt löper över sidan och regioner nedåt på sidan, eller vice versa.
- Byta axelorientering i instrumentpaneler eller diagram så att en tidsserie löper nedåt på sidan istället för tvärs över.
- Omforma data som importerats från externa system så att det matchar layouten som förväntas av nedströmsanalys- eller rapporteringsmallar.
För att göra resten av artikeln konkret använder varje exempel följande lilla tabell över försäljning per region per kvartal. I exempelarbetsboken upptar denna tabell intervallet **A1:D5**, där **A1** lämnas tomt som det övre vänstra hörnet, **B1:D1** innehåller regionrubrikerna och **A2:A5** innehåller kvartalsrubrikerna.
| Region            | Europa     | Asien      | Nordamerika  |
|-------------------|------------|------------|--------------|
| Q1                | 21704714   | 8774099    | 12094215     |
| Q2                | 17987034   | 12214447   | 10873099     |
| Q3                | 19485029   | 14356879   | 15689543     |
| Q4                | 22567894   | 15763492   | 17456723     |
Artikeln presenterar sedan tre olika sätt att transponera dessa data med Aspose.Cells for Node.js via Java, var och ett lämpat för en annan Excel-version och användningsfall.

## **Approach 1 — Transpose Range in Place (Range.transpose)**
Använd detta tillvägagångssätt när du vill transponera data utan att använda kalkylbladsfunktionen `TRANSPOSE`. Det fungerar i **alla versioner av Excel** och har inget beroende av dynamiska matriser, vilket gör det till det säkraste alternativet för kompatibilitet mellan versioner. Det är idealiskt när du bara behöver det slutliga transponerade resultatet och inte behöver behålla den ursprungliga `TRANSPOSE`-formeln i arbetsboken.

### **API used**
`Range.transpose()` är en instansmetod på klassen `com.aspose.cells.Range`. Att anropa den vänder intervallet på plats genom att byta dess rader och kolumner, så det som var en rad blir en kolumn och det som var en kolumn blir en rad. Metoden modifierar de underliggande cellerna direkt utan att skriva en formel.

### **Steps**
1. Öppna källarbetsboken med `LoadOptions` inställt på `.xlsx`-formatet genom att anropa `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Hämta det första kalkylbladet från arbetsboken med `workbook.getWorksheets().get(0)`.
3. Få åtkomst till kalkylbladets cellsamling via `worksheet.getCells()`.
4. Skapa källintervallet som täcker **A1:D5** genom att anropa `cells.createRange("A1:D5")`.
5. Anropa `source.transpose()` för att rotera intervallet på plats och byta rader och kolumner.
6. Spara arbetsboken med `workbook.save(outputFile)`.
Efter transponeringen innehåller det ursprungliga ankarintervallet den roterade datan. Den första raden läser (tomt, **Europa**, **Asien**, **Nordamerika**) och den första kolumnen läser (tomt, **Q1**, **Q2**, **Q3**, **Q4**). Varje ursprunglig kolumn med försäljning blir en rad i det transponerade intervallet.

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outputFile = "transposed.xlsx";
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, loadOptions);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
const source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
Använd detta tillvägagångssätt när du vill bevara formeln `=TRANSPOSE(A1:D5)` som en levande formel i utdataarbetsboken så att resultatet uppdateras automatiskt om källdatan ändras, och Excel-målfilen kommer att öppnas i **Excel 365 / Excel 2021 eller senare** där dynamiska matriser och spilloperatorn stöds.

### **API used**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` är en metod på `com.aspose.cells.Cell` som ställer in cellens formel som en **dynamisk matrisformel**. Excel utvärderar formeln en gång och spiller automatiskt resultatet till de omgivande cellerna. Den tredje parametern, när den är satt till `true`, instruerar Aspose.Cells att även beräkna resultatvärdena vid skrivtillfället.

### **Steps**
1. Ladda källarbetsboken med `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Hämta det första kalkylbladet och få åtkomst till dess `Cells`-samling.
3. Placera den dynamiska matrisformeln i cell **A6**, precis under källintervallet, genom att anropa `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. Argumentet `null` skickar standard-`FormulaParseOptions`, och det tredje argumentet `true` talar om för Aspose.Cells att behandla formeln som en dynamisk matris och att utvärdera den så att de spillda värdena skrivs till arbetsboken.
5. Spara arbetsboken med `workbook.save(outputFile)`.
Cell **A6** innehåller formeln `=TRANSPOSE(A1:D5)` och Excel spiller automatiskt resultatet till området **A6:D10**, ett block på 5 rader gånger 4 kolumner lika med den transponerade datan.

{{% alert color="primary" %}}
Detta tillvägagångssätt fungerar **endast på Excel 365 / 2021 eller senare**. Äldre Excel-versioner kommer inte att spilla dynamiska matrisformler korrekt.
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
Använd detta tillvägagångssätt när du vill bevara en `TRANSPOSE`-formel i arbetsboken men Excel-målfilen kan öppnas i **äldre Excel-versioner (före 2021, inklusive 2019, 2016, 2013 och så vidare)** där dynamisk matris-spillning inte stöds. Den klassiska CSE-matrisformeln (Ctrl+Skift+Enter) är det bakåtkompatibla alternativet som alla Excel-versioner kan utvärdera.

### **API used**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` är en metod på `com.aspose.cells.Cell` som tilldelar en **klassisk matrisformel (CSE)** till ankarcellen och anger dimensionerna för den resulterande matrisen. Aspose.Cells skriver markören för flercellsmatrisformel så att Excel utvärderar formeln som ett enda matrisuttryck som fyller det deklarerade intervallet.

### **Steps**
1. Ladda källarbetsboken enligt beskrivningen i de tidigare metoderna.
2. Hämta det första kalkylbladet och få åtkomst till dess `Cells`-samling.
3. Anropa `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Det andra argumentet `4` är antalet rader i destinationsmatrisen och det tredje argumentet `5` är antalet kolumner.
4. Spara arbetsboken med `workbook.save(outputFile)`.
Cell **A6** är ankaret för matrisformeln och den utvärderade matrisen spänner över 4 rader gånger 5 kolumner med start från A6, vilket matchar de transponerade dimensionerna för källintervallet A1:D5. Excel skriver en enda markör för matrisformel över det resulterande intervallet så att äldre Excel-versioner utvärderar det korrekt.

{{% alert color="primary" %}}
CSE-matrisformler är det klassiska Excel-sättet att utvärdera ett `TRANSPOSE`-uttryck och detta tillvägagångssätt är universellt kompatibelt över Excel-versioner.
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
// Load the source workbook with xlsx LoadOptions
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// Access the first worksheet and its Cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Set the classic CSE array formula on cell A6.
// The formula =TRANSPOSE(A1:D5) rotates the 5-row x 4-column source range
// into a 4-row x 5-column array. The second argument (4) is the number of rows
// and the third argument (5) is the number of columns of the resulting array.
// Aspose.Cells writes the CSE array-formula marker so Excel evaluates it as
// a single multi-cell array formula, compatible with older Excel versions
// (2019, 2016, 2013, etc.) that do not support dynamic array spilling.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Save the workbook so the array-formula marker is persisted
workbook.save("output.xlsx");
```

## **Comparison — When to Use Each Approach**
| Metod | API / Metod | Excel-version | Källformel bevarad? | Utdataintervall |
|----------|--------------|---------------|--------------------------|--------------|
| Metod 1 — Transponering på plats | `Range.transpose()` | Alla Excel-versioner | Nej (endast värden) | Ursprungligt ankarintervall, 5×4 |
| Metod 2 — Dynamisk matrisformel | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Ja (spillar dynamiskt) | Spillad från ankarpunkt |
| Metod 3 — Klassisk matrisformel (CSE) | `Cell.setArrayFormula` | Alla Excel-versioner | Ja (flercellsmatrisformel) | Explicit storlek, 4×5 |
Använd **Metod 1** när du behöver en snabb, versionsöverskridande transformation och bara behöver de transponerade värdena skrivna till filen. Använd **Metod 2** när modern Excel är garanterat och du vill att formeln ska förbli levande och uppdateras om källan ändras. Använd **Metod 3** när du behöver den bredaste kompatibiliteten med en bevarad formel över alla Excel-versioner, inklusive de äldre versionerna som inte stöder dynamiska matriser.

## **Related Articles**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Node.js via Java](/cells/sv/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Infoga en bild i en cell](/cells/sv/nodejs-java/inserting-an-image-into-a-cell/)
- [Dela upp Excel-filer i flera filer](/cells/sv/nodejs-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-java" >}}