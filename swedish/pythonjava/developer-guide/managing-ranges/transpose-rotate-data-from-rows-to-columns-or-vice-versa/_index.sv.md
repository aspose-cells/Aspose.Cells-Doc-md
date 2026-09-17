---
title: Transponera intervall
linktitle: Transponera intervall
description: Den här artikeln förklarar hur man transponerar eller roterar data från rader till kolumner eller tvärtom i Excel-filer med Aspose.Cells for Python via Java med tre olika metoder.
keywords: Aspose.Cells, Python via Java-bibliotek, kalkylblad, transponera intervall, rotera data, transponeringsfunktion, dynamisk matrisformel, matrisformel, Excel TRANSPOSE, Rader till kolumner
type: docs
weight: 80
url: /sv/python-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via Java stöder transponering (rotering) av data så att rader blir kolumner och kolumner blir rader på tre olika sätt. Den första metoden använder den in-place-metoden `Range.transpose()` och fungerar i alla Excel-versioner, medan den andra använder `Cell.setDynamicArrayFormula()` för att skriva en modern dynamisk matrisformel `=TRANSPOSE(...)` som spills automatiskt i Excel 365 eller Excel 2021. Den tredje metoden använder `Cell.setArrayFormula()` för att skriva en klassisk Ctrl+Skift+Enter-matrisformel (CSE) som är kompatibel med äldre Excel-versioner. Den här artikeln går igenom varje metod med stegvisa instruktioner och fullständiga kodexempel.
{{% /alert %}}

## **Introduktion**
Att transponera ett intervall innebär att man roterar det så att det som var en rad blir en kolumn och det som var en kolumn blir en rad, vilket i praktiken speglar datan över dess huvuddiagonal. I Microsoft Excel utför kalkylbladsfunktionen `TRANSPOSE` denna operation, och den konceptuella referensen dokumenteras på [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Samma idé kan användas programmatiskt på ett cellintervall, vilket är användbart i många affärs- och rapporteringsscenarier.
Vanliga scenarier där transponering är användbart inkluderar följande.
- Omorientering av kvartals- eller årsförsäljningsrapporter där kvartal normalt löper över sidan och regioner nedför sidan, eller tvärtom.
- Byta axelorientering i dashboards eller diagram så att en tidsserie löper nedåt sidan istället för tvärs över.
- Omforma data som importerats från externa system så att det matchar den layout som förväntas av nedströmsanalys eller rapportmallar.
För att göra resten av artikeln konkret använder varje exempel följande lilla tabell över försäljning per region per kvartal. I exempelarbetsboken upptar denna tabell intervallet **A1:D5**, med **A1** lämnat tomt som det övre vänstra hörnet, **B1:D1** innehåller regionrubrikerna och **A2:A5** innehåller kvartalsrubrikerna.
| Region            | Europa    | Asien    | Nordamerika |
|-------------------|-----------|-----------|--------------|
| Q1                | 21704714  | 8774099   | 12094215      |
| Q2                | 17987034  | 12214447  | 10873099      |
| Q3                | 19485029  | 14356879  | 15689543      |
| Q4                | 22567894  | 15763492  | 17456723      |
Artikeln presenterar sedan tre olika sätt att transponera denna data med Aspose.Cells for Python via Java, var och ett anpassat för en annan Excel-version och användningsfall.

## **Metod 1 — Transponera intervall på plats (Range.transpose)**
Använd denna metod när du vill transponera data utan att använda kalkylbladsfunktionen `TRANSPOSE`. Den fungerar i **alla versioner av Excel** och har inget beroende av dynamiska matriser, vilket gör den till det säkraste korsversionskompatibla alternativet. Den är idealisk när du bara behöver det slutliga transponerade resultatet och inte behöver behålla den ursprungliga `TRANSPOSE`-formeln i arbetsboken.

### **API som används**
`Range.transpose()` är en instansmetod på klassen `com.aspose.cells.Range`. När den anropas vänder den intervallet på plats genom att byta dess rader och kolumner, så det som var en rad blir en kolumn och det som var en kolumn blir en rad. Metoden modifierar de underliggande cellerna direkt utan att skriva en formel.

### **Steg**
1. Öppna källarbetsboken med `LoadOptions` inställt på `.xlsx`-formatet genom att anropa `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Hämta det första kalkylbladet från arbetsboken med `workbook.getWorksheets().get(0)`.
3. Kom åt kalkylbladets cellsamling via `worksheet.getCells()`.
4. Skapa källintervallet som täcker **A1:D5** genom att anropa `cells.createRange("A1:D5")`.
5. Anropa `source.transpose()` för att rotera intervallet på plats, så att rader och kolumner byter plats.
6. Spara arbetsboken med `workbook.save(outputFile)`.
Efter transponeringen håller samma anchor-intervall den roterade datan. Första raden läser (tom, **Europa**, **Asien**, **Nordamerika**) och första kolumnen läser (tom, **Q1**, **Q2**, **Q3**, **Q4**). Varje ursprunglig kolumn av försäljning blir en rad i det transponerade intervallet.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, LoadOptions, LoadFormat
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
loadOptions = LoadOptions(LoadFormat.Xlsx)
workbook = Workbook(srcFile, loadOptions)
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
source = cells.createRange("A1:D5")
source.transpose()
workbook.save(outputFile)
jpype.shutdownJVM()
```

## **Metod 2 — Transponera med en dynamisk matrisformel (Excel 365 / 2021)**
Använd denna metod när du vill bevara formeln `=TRANSPOSE(A1:D5)` som en live-formel i utdataarbetsboken så att resultatet uppdateras automatiskt om källdatan ändras, och målets Excel-fil kommer att öppnas i **Excel 365 / Excel 2021 eller senare** där dynamiska matriser och spilloperatorn stöds.

### **API som används**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` är en metod på `com.aspose.cells.Cell` som ställer in cellens formel som en **dynamisk matrisformel**. Excel utvärderar formeln en gång och spiller automatiskt resultatet till de omgivande cellerna. Den tredje parametern, när den är satt till `True`, instruerar Aspose.Cells att även beräkna resultatvärdena vid skrivningstillfället.

### **Steg**
1. Ladda källarbetsboken med `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Hämta det första kalkylbladet och kom åt dess `Cells`-samling.
3. Placera den dynamiska matrisformeln på cell **A6**, precis under källintervallet, genom att anropa `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", None, True)`.
4. Argumentet `None` skickar standardinställningarna för `FormulaParseOptions`, och det tredje argumentet `True` talar om för Aspose.Cells att behandla formeln som en dynamisk matris och att utvärdera den så att de spillda värdena skrivs till arbetsboken.
5. Spara arbetsboken med `workbook.save(outputFile)`.
Cell **A6** innehåller formeln `=TRANSPOSE(A1:D5)` och Excel spiller automatiskt resultatet till regionen **A6:D10**, ett block med 5 rader och 4 kolumner som motsvarar den transponerade datan.

{{% alert color="primary" %}}
Denna metod fungerar **bara på Excel 365 / 2021 eller senare**. Äldre Excel-versioner kommer inte att spilla dynamiska matrisformler korrekt.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, LoadOptions, LoadFormat, FormulaParseOptions, SaveFormat
# porterad kod här
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", FormulaParseOptions(), True)
workbook.save(outFile, SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **Metod 3 — Transponera med en klassisk matrisformel (CSE)**
Använd denna metod när du vill att en `TRANSPOSE`-formel ska bevaras i arbetsboken men målets Excel-fil kan komma att öppnas i **äldre Excel-versioner (före 2021, inklusive 2019, 2016, 2013 och så vidare)** där dynamisk matris-spillning inte stöds. Den klassiska CSE-matrisformeln (Ctrl+Skift+Enter) är det äldre kompatibla alternativet som alla Excel-versioner kan utvärdera.

### **API som används**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` är en metod på `com.aspose.cells.Cell` som tilldelar en **klassisk matrisformel (CSE)** till anchor-cellen och deklarerar dimensionerna för den resulterande matrisen. Aspose.Cells skriver markören för flercells-matrisformeln så att Excel utvärderar formeln som ett enda matrisuttryck som fyller det deklarerade intervallet.

### **Steg**
1. Ladda källarbetsboken på samma sätt som i de tidigare metoderna.
2. Hämta det första kalkylbladet och kom åt dess `Cells`-samling.
3. Anropa `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Det andra argumentet `4` är antalet rader i destinationsmatrisen och det tredje argumentet `5` är antalet kolumner.
4. Spara arbetsboken med `workbook.save(outputFile)`.
Cell **A6** är ankaret för matrisformeln och den utvärderade matrisen spänner över 4 rader och 5 kolumner med start vid A6, vilket matchar de transponerade dimensionerna för A1:D5-källan. Excel skriver en enda matrisformelsmarkör över det resulterande intervallet så att äldre Excel-versioner utvärderar det korrekt.

{{% alert color="primary" %}}
CSE-matrisformler är det klassiska Excel-sättet att utvärdera ett `TRANSPOSE`-uttryck och denna metod är universellt kompatibel över Excel-versioner.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, LoadOptions, LoadFormat, Worksheet, Cells
# Ladda källarbetsboken med xlsx LoadOptions
srcFile = "source.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
# Hämta det första kalkylbladet och dess Cells-samling
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Ställ in den klassiska CSE-matrisformeln på cell A6.
# Formeln =TRANSPOSE(A1:D5) roterar 5-rad x 4-kolumn källintervallet
# till en 4-rad x 5-kolumn matris. Det andra argumentet (4) är antalet rader
# och det tredje argumentet (5) är antalet kolumner i den resulterande matrisen.
# Aspose.Cells skriver CSE-matrisformelmarkeringen så att Excel utvärderar den som
# en enda flercells-matrisformel, kompatibel med äldre Excel-versioner
# (2019, 2016, 2013, etc.) som inte stödjer dynamisk matris-sprillning.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)
# Spara arbetsboken så att matrisformelmarkeringen bevaras
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Jämförelse — När du ska använda varje metod**
| Metod | API / Metod | Excel-version | Källformel bevarad? | Utdata-intervall |
|----------|--------------|---------------|--------------------------|--------------|
| Metod 1 — Transponera på plats | `Range.transpose()` | Alla Excel-versioner | Nej (endast värden) | Samma anchor-intervall, 5×4 |
| Metod 2 — Dynamisk matrisformel | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Ja (spiller dynamiskt) | Spillat från anchor |
| Metod 3 — Klassisk matrisformel (CSE) | `Cell.setArrayFormula` | Alla Excel-versioner | Ja (flercells-matrisformel) | Explicit storlek, 4×5 |
Använd **Metod 1** när du behöver en snabb, korsversionskompatibel transformation och bara behöver de transponerade värdena skrivna till filen. Använd **Metod 2** när modern Excel är garanterat och du vill att formeln ska förbli aktiv och uppdateras om källan ändras. Använd **Metod 3** när du behöver den bredaste kompatibiliteten med en bevarad formel över alla Excel-versioner, inklusive de äldre versionerna som inte stöder dynamiska matriser.

## **Relaterade artiklar**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Python via Java](/cells/sv/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Infoga en bild i en cell](/cells/sv/python-java/inserting-an-image-into-a-cell/)
- [Dela Excel-filer i flera filer](/cells/sv/python-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python" >}}