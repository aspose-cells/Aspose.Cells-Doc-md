---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Python via .NET, with three different approaches.
linktitle: Transponera intervall
url: /sv/python-net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells for Python via .NET, kalkylblad, transponera intervall, rotera data, transponeringsfunktion, dynamisk matrisformel, matrisformel, Excel TRANSPOSE, rader till kolumner
type: docs
weight: 80
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET stöder transponering (rotering) av data så att rader blir kolumner och kolumner blir rader på tre olika sätt. Den första metoden använder in-place-metoden `range.transpose()` och fungerar på alla Excel-versioner, medan den andra använder `cell.set_dynamic_array_formula()` för att skriva en modern dynamisk matrisformel `=TRANSPOSE(...)` som spills automatiskt i Excel 365 eller Excel 2021. Den tredje metoden använder `cell.set_array_formula()` för att skriva en klassisk Ctrl+Shift+Enter (CSE)-matrisformel som är kompatibel med äldre Excel-versioner. Den här artikeln går igenom varje metod med steg-för-steg-instruktioner och fullständiga kodexempel.
{{% /alert %}}

## **Introduktion**
Att transponera ett intervall innebär att rotera det så att det som var en rad blir en kolumn och det som var en kolumn blir en rad, vilket effektivt reflekterar data över dess huvuddiagonal. I Microsoft Excel utför kalkylbladsfunktionen `TRANSPOSE` denna operation, och den konceptuella referensen dokumenteras på [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Samma idé kan tillämpas programmatiskt på ett cellintervall, vilket är användbart i många affärs- och rapporteringsscenarier.
Vanliga scenarier där transponering är användbart inkluderar följande.
- Omorientering av kvartals- eller årssäljrapporter där kvartal normalt löper tvärs över sidan och regioner nedför sidan, eller tvärtom.
- Byta axelorientering i instrumentpaneler eller diagram så att en tidsserie löper nedåt på sidan istället för tvärs över.
- Omforma data som importerats från externa system så att det matchar layouten som förväntas av nedströms analys- eller rapporteringsmallar.
För att göra resten av artikeln konkret använder varje exempel följande lilla sälj-per-region-per-kvartal-tabell. I exempelarbetsboken upptar denna tabell intervallet **A1:D5**, med **A1** lämnat tomt som det övre vänstra hörnet, **B1:D1** som innehåller regionrubrikerna, och **A2:A5** som innehåller kvartalsrubrikerna.
| Region            | Europa    | Asien     | Nordamerika   |
|-------------------|-----------|-----------|---------------|
| Kvartal 1         | 21704714  | 8774099   | 12094215      |
| Kvartal 2         | 17987034  | 12214447  | 10873099      |
| Kvartal 3         | 19485029  | 14356879  | 15689543      |
| Kvartal 4         | 22567894  | 15763492  | 17456723      |
Artikeln presenterar sedan tre olika sätt att transponera denna data med Aspose.Cells for Python via .NET, var och ett lämpligt för en annan Excel-version och användningsfall.

## **Metod 1 — Transponera intervall på plats (range.transpose)**
Använd denna metod när du vill transponera data utan att använda kalkylbladsfunktionen `TRANSPOSE`. Den fungerar på **alla versioner av Excel** och har inget beroende av dynamiska matriser, vilket gör den till det säkraste versionsöverskridande kompatibla alternativet. Det är idealiskt när du bara behöver den slutliga transponerade utdata och inte behöver behålla den ursprungliga `TRANSPOSE`-formeln i arbetsboken.

### **API som används**
`range.transpose()` är en instansmetod på klassen `Aspose.Cells.Range`. Att anropa den vänder intervallet på plats genom att byta dess rader och kolumner, så att det som var en rad blir en kolumn och det som var en kolumn blir en rad. Metoden modifierar de underliggande cellerna direkt utan att skriva en formel.

### **Steg**
1. Öppna källarbetsboken med `LoadOptions` inställt på `.xlsx`-formatet genom att anropa `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Hämta det första kalkylbladet från arbetsboken med `workbook.worksheets[0]`.
3. Få åtkomst till kalkylbladets cellsamling via `worksheet.cells`.
4. Skapa källintervallet som täcker **A1:D5** genom att anropa `cells.create_range("A1:D5")`.
5. Anropa `source.transpose()` för att rotera intervallet på plats, vilket byter rader och kolumner.
6. Spara arbetsboken med `workbook.save(outputFile)`.
Efter transponeringen innehåller samma utgångsintervall de roterade data. Den första raden läser (tom, **Europa**, **Asien**, **Nordamerika**) och den första kolumnen läser (tom, **Kvartal 1**, **Kvartal 2**, **Kvartal 3**, **Kvartal 4**). Varje ursprunglig kolumn av försäljning blir en rad i det transponerade intervallet.

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.XLSX))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
source = cells.create_range("A1:D5")
source.transpose()
workbook.save(outputFile)
```

## **Metod 2 — Transponera med en dynamisk matrisformel (Excel 365 / 2021)**
Använd denna metod när du vill bevara formeln `=TRANSPOSE(A1:D5)` som en liveformel i utdataarbetsboken så att resultatet uppdateras automatiskt om källdata ändras, och målets Excel-fil kommer att öppnas i **Excel 365 / Excel 2021 eller senare** där dynamiska matriser och spilloperatorn stöds.

### **API som används**
`cell.set_dynamic_array_formula(formula, options, calculate_value)` är en metod på `Aspose.Cells.Cell` som anger cellens formel som en **dynamisk matrisformel**. Excel utvärderar formeln en gång och spiller automatiskt ut resultatet i de omgivande cellerna. Den tredje parametern, när den är satt till `True`, instruerar Aspose.Cells att också beräkna de resulterande värdena vid skrivtillfället.

### **Steg**
1. Ladda källarbetsboken med `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Hämta det första kalkylbladet och få åtkomst till dess `cells`-samling.
3. Placera den dynamiska matrisformeln i cell **A6**, precis under källintervallet, genom att anropa `cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", None, True)`.
4. `None`-argumentet skickar standard `FormulaParseOptions`, och det tredje argumentet `True` talar om för Aspose.Cells att behandla formeln som en dynamisk matris och att utvärdera den så att de spillda värdena skrivs till arbetsboken.
5. Spara arbetsboken med `workbook.save(outputFile)`.
Cell **A6** innehåller formeln `=TRANSPOSE(A1:D5)` och Excel spiller automatiskt ut resultatet i regionen **A6:D10**, ett block med 5 rader och 4 kolumner som motsvarar den transponerade datan.

{{% alert color="primary" %}}
Denna metod fungerar **endast på Excel 365 / 2021 eller senare**. Äldre Excel-versioner kommer inte att spilla dynamiska matrisformler korrekt.
{{% /alert %}}

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", ac.FormulaParseOptions(), True)
workbook.save(outFile, ac.SaveFormat.Xlsx)
```

## **Metod 3 — Transponera med en klassisk matrisformel (CSE)**
Använd denna metod när du vill ha en `TRANSPOSE`-formel bevarad i arbetsboken men målets Excel-fil kan komma att öppnas i **äldre Excel-versioner (före 2021, inklusive 2019, 2016, 2013 och så vidare)** där dynamisk matris-spilling inte stöds. Den klassiska CSE (Ctrl+Shift+Enter)-matrisformeln är det äldre kompatibla alternativet som alla Excel-versioner kan utvärdera.

### **API som används**
`cell.set_array_formula(array_formula, n_rows, n_columns)` är en metod på `Aspose.Cells.Cell` som tilldelar en **klassisk matrisformel (CSE)** till ankarcellen och deklarerar dimensionerna för den resulterande matrisen. Aspose.Cells skriver multi-cell-matrisformelmarkören så att Excel utvärderar formeln som ett enda matrisuttryck som fyller det deklarerade intervallet.

### **Steg**
1. Ladda källarbetsboken på samma sätt som i de tidigare metoderna.
2. Hämta det första kalkylbladet och få åtkomst till dess `cells`-samling.
3. Anropa `cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)`. Det andra argumentet `4` är antalet rader i destinationsmatrisen och det tredje argumentet `5` är antalet kolumner.
4. Spara arbetsboken med `workbook.save(outputFile)`.
Cell **A6** är ankaret för matrisformeln och den utvärderade matrisen spänner över 4 rader och 5 kolumner med start vid A6, vilket matchar de transponerade dimensionerna för A1:D5-källan. Excel skriver en enda matrisformelmarkör över det resulterande intervallet så att äldre Excel-versioner utvärderar det korrekt.

{{% alert color="primary" %}}
CSE-matrisformler är det klassiska Excel-sättet att utvärdera ett `TRANSPOSE`-uttryck och denna metod är universellt kompatibel mellan Excel-versioner.
{{% /alert %}}

```python
import aspose.cells as ac
# Ladda källarbetsboken med xlsx LoadOptions
srcFile = "source.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
# Få åtkomst till det första kalkylbladet och dess Cells-samling
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Ställ in den klassiska CSE-matrisformeln på cell A6.
# Formeln =TRANSPOSE(A1:D5) roterar källintervallet på 5 rader x 4 kolumner
# till en matris med 4 rader x 5 kolumner. Det andra argumentet (4) är antalet rader
# och det tredje argumentet (5) är antalet kolumner i den resulterande matrisen.
# Aspose.Cells skriver CSE-matrisformelmarkören så att Excel utvärderar den som
# en enda flercellig matrisformel, kompatibel med äldre Excel-versioner
# (2019, 2016, 2013, etc.) som inte stöder dynamisk matrisutspillning.
cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)
# Spara arbetsboken så att matrisformelmarkören sparas
workbook.save("output.xlsx")
```

## **Jämförelse — När du ska använda varje metod**
| Metod | API / Metod | Excel-version | Bevarad källformel? | Utdataintervall |
|----------|--------------|---------------|--------------------------|--------------|
| Metod 1 — In-place-transponering | `range.transpose()` | Alla Excel-versioner | Nej (endast värden) | Samma utgångsintervall, 5×4 |
| Metod 2 — Dynamisk matrisformel | `cell.set_dynamic_array_formula` | Excel 365 / 2021+ | Ja (spillas dynamiskt) | Spillat från ankaret |
| Metod 3 — Klassisk matrisformel (CSE) | `cell.set_array_formula` | Alla Excel-versioner | Ja (multi-cell-matrisformel) | Explicit storlek, 4×5 |
Använd **Metod 1** när du behöver en snabb versionsöverskridande omvandling och bara behöver de transponerade värdena skrivna till filen. Använd **Metod 2** när modern Excel är garanterat och du vill att formeln ska förbli live och uppdateras om källan ändras. Använd **Metod 3** när du behöver bredast möjliga kompatibilitet med en bevarad formel över alla Excel-versioner, inklusive de äldre versionerna som inte stöder dynamiska matriser.

## **Relaterade artiklar**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Python via .NET](/cells/sv/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserting an Image into a Cell](/cells/sv/python-net/inserting-an-image-into-a-cell/)
- [Splitting Excel Files into Multiple Files](/cells/sv/python-net/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python-net" >}}