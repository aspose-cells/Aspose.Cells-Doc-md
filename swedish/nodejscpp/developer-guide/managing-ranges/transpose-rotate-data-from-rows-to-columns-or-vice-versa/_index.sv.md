---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Node.js via C++ with three different approaches.
linktitle: Transponera intervall
url: /sv/nodejs-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, Node.js via C++-bibliotek, kalkylblad, transponera intervall, rotera data, transponeringsfunktion, dynamisk matrisformel, matrisformel, Excel TRANSPOSE, Rader till kolumner
type: docs
weight: 80
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ stöder transponering (rotering) av data så att rader blir kolumner och kolumner blir rader på tre olika sätt. Den första metoden använder in-place-metoden `range.transpose()` och fungerar i alla Excel-versioner, medan den andra använder `cell.setDynamicArrayFormula()` för att skriva en modern dynamisk matrisformel `=TRANSPOSE(...)` som spills automatiskt i Excel 365 eller Excel 2021. Den tredje metoden använder `cell.setArrayFormula()` för att skriva en klassisk Ctrl+Shift+Enter (CSE)-matrisformel som är kompatibel med äldre Excel-versioner. Den här artikeln går igenom varje metod med stegvisa instruktioner och kompletta kodexempel.
{{% /alert %}}

## **Introduktion**
Att transponera ett intervall innebär att rotera det så att det som var en rad blir en kolumn och det som var en kolumn blir en rad, vilket effektivt speglar datan över dess huvuddiagonal. I Microsoft Excel utför kalkylbladsfunktionen `TRANSPOSE` denna operation, och den konceptuella referensen dokumenteras på [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Samma idé kan tillämpas programmatiskt på ett intervall av celler, vilket är användbart i många affärs- och rapporteringsscenarier.
Vanliga scenarier där transponering är användbart inkluderar följande.
- Att omorientera kvartals- eller årsvisa försäljningsrapporter där kvartal normalt löper över sidan och regioner nedför sidan, eller tvärtom.
- Att byta axelorientering i instrumentpaneler eller diagram så att en tidsserie löper nedåt på sidan istället för tvärs över.
- Att omforma data som importerats från externa system så att det matchar layouten som förväntas av nedströmsanalys eller rapporteringsmallar.
För att göra resten av artikeln konkret använder varje exempel följande lilla tabell över försäljning per region och kvartal. I exempelarbetsboken upptar denna tabell intervallet **A1:D5**, där **A1** lämnas tom som det övre vänstra hörnet, **B1:D1** innehåller regionrubrikerna och **A2:A5** innehåller kvartalsrubrikerna.
| Region            | Europa      | Asien       | Nordamerika   |
|-------------------|-------------|-------------|---------------|
| Kvartal 1         | 21704714    | 8774099     | 12094215      |
| Kvartal 2         | 17987034    | 12214447    | 10873099      |
| Kvartal 3         | 19485029    | 14356879    | 15689543      |
| Kvartal 4         | 22567894    | 15763492    | 17456723      |
Artikeln presenterar sedan tre olika sätt att transponera denna data med Aspose.Cells for Node.js via C++, var och ett lämpat för en annan Excel-version och användningsfall.

## **Metod 1 — Transponera intervall på plats (range.transpose)**
Använd denna metod när du vill transponera data utan att använda kalkylbladsfunktionen `TRANSPOSE`. Den fungerar i **alla versioner av Excel** och har inget beroende av dynamiska matriser, vilket gör den till det säkraste korsversionskompatibla alternativet. Den är idealisk när du bara behöver det slutliga transponerade resultatet och inte behöver behålla den ursprungliga `TRANSPOSE`-formeln i arbetsboken.

### **Använd API**
`range.transpose()` är en instansmetod på klassen `Aspose.Cells.Range`. Att anropa den vänder intervallet på plats genom att byta dess rader och kolumner, så det som var en rad blir en kolumn och det som var en kolumn blir en rad. Metoden modifierar de underliggande cellerna direkt utan att skriva en formel.

### **Steg**
1. Öppna källarbetsboken med `LoadOptions` inställt på `.xlsx`-formatet genom att anropa `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Hämta det första kalkylbladet från arbetsboken med hjälp av `workbook.getWorksheets().get(0)`.
3. Få åtkomst till kalkylbladets cellsamling via `worksheet.getCells()`.
4. Skapa källintervallet som täcker **A1:D5** genom att anropa `cells.createRange("A1:D5")`.
5. Anropa `source.transpose()` för att rotera intervallet på plats, så att rader och kolumner byter plats.
6. Spara arbetsboken med `workbook.save(outputFile)`.
Efter transponeringen innehåller samma ankarpunkt den roterade datan. Den första raden läser (tom, **Europa**, **Asien**, **Nordamerika**) och den första kolumnen läser (tom, **Kvartal 1**, **Kvartal 2**, **Kvartal 3**, **Kvartal 4**). Varje ursprunglig kolumn av försäljning blir en rad i det transponerade intervallet.

```python
var srcFile = "source.xlsx";
var outputFile = "transposed.xlsx";
var workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
var worksheet = workbook.getWorksheets().get(0);
var cells = worksheet.getCells();
var source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Metod 2 — Transponera med en dynamisk matrisformel (Excel 365 / 2021)**
Använd denna metod när du vill bevara formeln `=TRANSPOSE(A1:D5)` som en levande formel i utdataarbetsboken så att resultatet uppdateras automatiskt om källdatan ändras, och målets Excelfil öppnas i **Excel 365 / Excel 2021 eller senare** där dynamiska matriser och spill-operatorn stöds.

### **Använd API**
`cell.setDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` är en metod på `Aspose.Cells.Cell` som anger cellens formel som en **dynamisk matrisformel**. Excel utvärderar formeln en gång och spills automatiskt resultatet till de omgivande cellerna. Den tredje parametern, när den är satt till `true`, instruerar Aspose.Cells att också beräkna de resulterande värdena vid skrivtillfället.

### **Steg**
1. Ladda källarbetsboken med `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Hämta det första kalkylbladet och få åtkomst till dess `Cells`-samling.
3. Placera den dynamiska matrisformeln på cell **A6**, precis under källintervallet, genom att anropa `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. Argumentet `null` skickar standard `FormulaParseOptions`, och det tredje argumentet `true` talar om för Aspose.Cells att behandla formeln som en dynamisk matris och att utvärdera den så att de spillade värdena skrivs till arbetsboken.
5. Spara arbetsboken med `workbook.save(outputFile)`.
Cell **A6** innehåller formeln `=TRANSPOSE(A1:D5)` och Excel spills resultatet automatiskt till regionen **A6:D10**, ett block på 5 rader gånger 4 kolumner som är lika med den transponerade datan.

{{% alert color="primary" %}}
Denna metod fungerar **endast på Excel 365 / 2021 eller senare**. Äldre Excel-versioner kommer inte att spilla dynamiska matrisformler korrekt.
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, opts);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Metod 3 — Transponera med en klassisk matrisformel (CSE)**
Använd denna metod när du vill ha en `TRANSPOSE`-formel bevarad i arbetsboken men målets Excelfil kan öppnas i **äldre Excel-versioner (före 2021, inklusive 2019, 2016, 2013 och så vidare)** där dynamisk matris-spilling inte stöds. Den klassiska CSE (Ctrl+Shift+Enter)-matrisformeln är det äldre kompatibla alternativet som alla Excel-versioner kan utvärdera.

### **Använd API**
`cell.setArrayFormula(string arrayFormula, int nRows, int nColumns)` är en metod på `Aspose.Cells.Cell` som tilldelar en **klassisk matrisformel (CSE)** till ankarcellen och anger dimensionerna på den resulterande matrisen. Aspose.Cells skriver multi-cell matrisformel-markören så att Excel utvärderar formeln som ett enda matrisuttryck som fyller det angivna intervallet.

### **Steg**
1. Ladda källarbetsboken på samma sätt som i de tidigare metoderna.
2. Hämta det första kalkylbladet och få åtkomst till dess `Cells`-samling.
3. Anropa `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Det andra argumentet `4` är antalet rader i destinationsmatrisen och det tredje argumentet `5` är antalet kolumner.
4. Spara arbetsboken med `workbook.save(outputFile)`.
Cell **A6** är ankaret för matrisformeln och den utvärderade matrisen spänner över 4 rader gånger 5 kolumner med början från A6, vilket matchar de transponerade dimensionerna av A1:D5-källan. Excel skriver en enda matrisformel-markör över det resulterande intervallet så att äldre Excel-versioner utvärderar det korrekt.

{{% alert color="primary" %}}
CSE-matrisformler är det klassiska Excel-sättet att utvärdera ett `TRANSPOSE`-uttryck och denna metod är universellt kompatibel över Excel-versioner.
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
// Ladda källarbetsboken med xlsx LoadOptions
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// Hämta det första kalkylbladet och dess Cells-samling
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Ställ in den klassiska CSE-matrisformeln på cell A6.
// Formeln =TRANSPOSE(A1:D5) roterar källintervallet med 5 rader x 4 kolumner
// till en matris med 4 rader x 5 kolumner. Det andra argumentet (4) är antalet rader
// och det tredje argumentet (5) är antalet kolumner i den resulterande matrisen.
// Aspose.Cells skriver CSE-matrisformelmarkören så att Excel utvärderar den som
// en enda flercells-matrisformel, kompatibel med äldre Excel-versioner
// (2019, 2016, 2013, etc.) som inte stöder dynamisk matris-splilling.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Spara arbetsboken så att matrisformelmarkören sparas
workbook.save("output.xlsx");
```

## **Jämförelse — När du ska använda varje metod**
| Metod | API / Metod | Excel-version | Källformel bevarad? | Utdataintervall |
|----------|--------------|---------------|--------------------------|--------------|
| Metod 1 — Transponera på plats | `range.transpose()` | Alla Excel-versioner | Nej (endast värden) | Samma ankarpunkt, 5×4 |
| Metod 2 — Dynamisk matrisformel | `cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Ja (spills dynamiskt) | Spillad från ankaret |
| Metod 3 — Klassisk matrisformel (CSE) | `cell.setArrayFormula` | Alla Excel-versioner | Ja (multi-cell matrisformel) | Explicit storlek, 4×5 |
Använd **Metod 1** när du behöver en snabb, korsversions-kompatibel transformation och bara behöver de transponerade värdena skrivna till filen. Använd **Metod 2** när moderna Excel-versioner är garanterade och du vill att formeln ska förbli levande och uppdateras om källan ändras. Använd **Metod 3** när du behöver den bredaste kompatibiliteten med en bevarad formel över alla Excel-versioner, inklusive de äldre versionerna som inte stödjer dynamiska matriser.
(I'll remove the Related Articles section)

{{< app/cells/assistant language="nodejs-cpp" >}}