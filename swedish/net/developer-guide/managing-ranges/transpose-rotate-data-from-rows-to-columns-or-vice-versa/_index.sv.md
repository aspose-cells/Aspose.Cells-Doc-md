---
title: Transponera intervall
linktitle: Transponera intervall
description: Den här artikeln förklarar hur man transponerar eller roterar data från rader till kolumner eller tvärtom i Excel-filer med Aspose.Cells for .NET och tre olika metoder.
keywords: Aspose.Cells, .NET-bibliotek, kalkylblad, transponera intervall, rotera data, transponeringsfunktion, dynamisk matrisformel, matrisformel, Excel TRANSPOSE, rader till kolumner
type: docs
weight: 80
url: /sv/net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for .NET stöder transponering (rotering) av data så att rader blir kolumner och kolumner blir rader på tre olika sätt. Den första metoden använder den inbyggda `Range.Transpose()`-metoden och fungerar i alla Excel-versioner, medan den andra använder `Cell.SetDynamicArrayFormula()` för att skriva en modern dynamisk matrisformel `=TRANSPOSE(...)` som spills automatiskt i Excel 365 eller Excel 2021. Den tredje metoden använder `Cell.SetArrayFormula()` för att skriva en klassisk Ctrl+Shift+Enter (CSE) matrisformel som är kompatibel med äldre Excel-versioner. Den här artikeln guidar dig genom varje metod med stegvisa instruktioner och kompletta kodexempel.
{{% /alert %}}

## **Introduktion**
Att transponera ett intervall innebär att man roterar det så att det som var en rad blir en kolumn och det som var en kolumn blir en rad, vilket i praktiken speglar datan över dess huvuddiagonal. I Microsoft Excel utför kalkylbladsfunktionen `TRANSPOSE` denna operation, och den konceptuella referensen dokumenteras på [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Detta koncept kan tillämpas programmatiskt på ett intervall av celler, vilket är användbart i många affärs- och rapporteringsscenarier.
- Omorientering av kvartals- eller årsförsäljningsrapporter där kvartal normalt löper över sidan och regioner nedåt på sidan, eller tvärtom.
- Byta axelorientering i instrumentpaneler eller diagram så att en tidsserie löper nedåt på sidan istället för över.
- Omforma data som importerats från externa system så att den matchar den layout som förväntas av nedströms analys- eller rapporteringsmallar.
För att göra resten av artikeln konkret använder varje exempel följande lilla tabell över försäljning per region per kvartal. I exempelarbetsboken upptar denna tabell intervallet **A1:D5**, med **A1** lämnat tomt som det övre vänstra hörnet, **B1:D1** som innehåller regionrubrikerna och **A2:A5** som innehåller kvartalsrubrikerna.
| Region            | Europa     | Asien      | Nordamerika |
|-------------------|------------|------------|-------------|
| Kvartal 1         | 21704714   | 8774099    | 12094215    |
| Kvartal 2         | 17987034   | 12214447   | 10873099    |
| Kvartal 3         | 19485029   | 14356879   | 15689543    |
| Kvartal 4         | 22567894   | 15763492   | 17456723    |
Artikeln presenterar sedan tre olika sätt att transponera dessa data med Aspose.Cells for .NET, var och ett lämpat för en annan Excel-version och användningsfall.

## **Metod 1 — Transponera intervall på plats (Range.Transpose)**
Använd denna metod när du vill transponera data utan att använda kalkylbladsfunktionen `TRANSPOSE`. Den fungerar i **alla versioner av Excel** och har inget beroende av dynamiska matriser, vilket gör den till det säkraste alternativet för kompatibilitet över alla versioner. Den är idealisk när du bara behöver det slutliga transponerade resultatet och inte behöver behålla den ursprungliga `TRANSPOSE`-formeln i arbetsboken.

### **API som används**
`Range.Transpose()` är en instansmetod på klassen `Aspose.Cells.Range`. Genom att anropa den vänds intervallet på plats genom att byta dess rader och kolumner, så det som var en rad blir en kolumn och det som var en kolumn blir en rad. Metoden modifierar de underliggande cellerna direkt utan att skriva en formel.

### **Steg**
1. Öppna källarbetsboken med `LoadOptions` inställt på `.xlsx`-formatet genom att anropa `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Hämta det första kalkylbladet från arbetsboken med `workbook.Worksheets[0]`.
3. Kom åt kalkylbladets cellsamling via `worksheet.Cells`.
4. Skapa källintervallet som täcker **A1:D5** genom att anropa `cells.CreateRange("A1:D5")`.
5. Anropa `source.Transpose()` för att rotera intervallet på plats och byta rader och kolumner.
6. Spara arbetsboken med `workbook.Save(outputFile)`.
Efter transponeringen innehåller detta ankarpunktintervall den roterade datan. Den första raden läser (tom, **Europa**, **Asien**, **Nordamerika**) och den första kolumnen läser (tom, **Kvartal 1**, **Kvartal 2**, **Kvartal 3**, **Kvartal 4**). Varje ursprunglig kolumn av försäljning blir en rad i det transponerade intervallet.

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
var source = cells.CreateRange("A1:D5");
source.Transpose();
workbook.Save(outputFile);
```

## **Metod 2 — Transponera med en dynamisk matrisformel (Excel 365 / 2021)**
Använd denna metod när du vill bevara `=TRANSPOSE(A1:D5)`-formeln som en levande formel i utdataarbetsboken så att resultatet uppdateras automatiskt om källdatan ändras, och målets Excelfil kommer att öppnas i **Excel 365 / Excel 2021 eller senare** där dynamiska matriser och spilloperatorn stöds.

### **API som används**
`Cell.SetDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` är en metod på `Aspose.Cells.Cell` som ställer in cellens formel som en **dynamisk matrisformel**. Excel utvärderar formeln en gång och spiller automatiskt resultatet till de omgivande cellerna. Den tredje parametern, när den sätts till `true`, instruerar Aspose.Cells att även beräkna de resulterande värdena vid skrivningstillfället.

### **Steg**
1. Ladda källarbetsboken med `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Hämta det första kalkylbladet och få åtkomst till dess `Cells`-samling.
3. Placera den dynamiska matrisformeln på cell **A6**, precis under källintervallet, genom att anropa `cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)`.
4. Argumentet `new FormulaParseOptions()` använder standardinställningarna för `FormulaParseOptions`, och det tredje argumentet `true` anger att Aspose.Cells ska behandla formeln som en dynamisk matris och utvärdera den så att de spillda värdena skrivs till arbetsboken.
5. Spara arbetsboken med `workbook.Save(outputFile)`.
Cell **A6** innehåller formeln `=TRANSPOSE(A1:D5)` och Excel spiller automatiskt resultatet till området **A6:E9**, ett block med 4 rader och 5 kolumner som motsvarar den transponerade datan.

{{% alert color="primary" %}}
Denna metod fungerar **endast i Excel 365 / 2021 eller senare**. Äldre Excel-versioner kommer inte att spilla dynamiska matrisformler korrekt.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.Save(outFile, SaveFormat.Xlsx);
```

## **Metod 3 — Transponera med en klassisk matrisformel (CSE)**
Använd denna metod när du vill att en `TRANSPOSE`-formel ska bevaras i arbetsboken men målets Excelfil kan komma att öppnas i **äldre Excel-versioner (före 2021, inklusive 2019, 2016, 2013 och så vidare)** där dynamiska matrisformler och deras spillning inte stöds. Den klassiska CSE (Ctrl+Shift+Enter) matrisformeln är det bakåtkompatibla alternativet som alla Excel-versioner kan utvärdera.

### **API som används**
`Cell.SetArrayFormula(string arrayFormula, int nRows, int nColumns)` är en metod på `Aspose.Cells.Cell` som tilldelar en **klassisk matrisformel (CSE)** till ankarcellen och deklarerar dimensionerna för den resulterande matrisen. Aspose.Cells skriver markören för flercells-matrisformeln så att Excel utvärderar formeln som ett enda matrisuttryck som fyller det deklarerade intervallet.

### **Steg**
1. Ladda källarbetsboken enligt beskrivningen i de tidigare metoderna.
2. Hämta det första kalkylbladet och få åtkomst till dess `Cells`-samling.
3. Anropa `cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Det andra argumentet `4` är antalet rader i destinationsmatrisen och det tredje argumentet `5` är antalet kolumner.
4. Spara arbetsboken med `workbook.Save(outputFile)`.
Cell **A6** är ankarpunkten för matrisformeln och den utvärderade matrisen spänner över 4 rader och 5 kolumner med början vid A6, vilket motsvarar de transponerade dimensionerna för A1:D5-källintervallet. Excel skriver en enda matrisformelsmarkör över det resulterande intervallet så att äldre Excel-versioner utvärderar det korrekt.

{{% alert color="primary" %}}
CSE-matrisformler är det klassiska Excel-sättet att utvärdera ett `TRANSPOSE`-uttryck och denna metod är universellt kompatibel över alla Excel-versioner.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
// Ladda källarbetsboken med xlsx LoadOptions
string srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
// Kom åt det första kalkylbladet och dess Cells-samling
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
// Ställ in den klassiska CSE-matrisformeln på cell A6.
// Formeln =TRANSPOSE(A1:D5) roterar källintervallet med 5 rader x 4 kolumner
// till en matris med 4 rader x 5 kolumner. Det andra argumentet (4) är antalet rader
// och det tredje argumentet (5) är antalet kolumner i den resulterande matrisen.
// Aspose.Cells skriver CSE-matrisformelmarkeringen så att Excel utvärderar den som
// en enstaka flercells-matrisformel, kompatibel med äldre Excel-versioner
// (2019, 2016, 2013 etc.) som inte stöder dynamisk matrisöversvämning.
cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Spara arbetsboken så att matrisformelmarkeringen bevaras
workbook.Save("output.xlsx");
```

## **Jämförelse — När ska varje metod användas**
| Metod | API / Metod | Excel-version | Bevaras källformeln? | Utdataintervall |
|----------|--------------|---------------|--------------------------|--------------|
| Metod 1 — Transponering på plats | `Range.Transpose()` | Alla Excel-versioner | Nej (endast värden) | Initialt ankarpunktintervall, 5×4 |
| Metod 2 — Dynamisk matrisformel | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | Ja (spills dynamiskt) | Spillat från ankarpunkten |
| Metod 3 — Klassisk matrisformel (CSE) | `Cell.SetArrayFormula` | Alla Excel-versioner | Ja (flercellsmatrisformel) | Explicit storlek, 4×5 |
Använd **Metod 1** när du behöver en snabb, versionsöverskridande transformering och bara behöver de transponerade värdena skrivna till filen. Använd **Metod 2** när modern Excel är garanterad och du vill att formeln ska förbli levande och uppdateras om källan ändras. Använd **Metod 3** när du behöver den bredaste kompatibiliteten med en bevarad formel över alla Excel-versioner, inklusive de äldre versionerna som inte stöder dynamiska matriser.

{{< app/cells/assistant language="csharp" >}}