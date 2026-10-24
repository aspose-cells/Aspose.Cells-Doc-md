---
title: Transponera intervall
linktitle: Transponera intervall
description: Den här artikeln förklarar hur du transponerar eller roterar data från rader till kolumner eller vice versa i Excel-filer med Aspose.Cells for Python via .NET, på tre olika sätt.
keywords: Aspose.Cells for Python via .NET, kalkylblad, transponera intervall, rotera data, TRANSPOSE-funktion, dynamisk arrayformel, arrayformel, Excel TRANSPOSE, Rader till kolumner
type: docs
weight: 80
url: /sv/python-net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET stöder transponering (rotering) av data, så att rader blir kolumner och kolumner blir rader, på tre olika sätt. Det första tillvägångssättet använder metoden `range.transpose()` för att transponera på plats och fungerar i alla Excel-versioner. Det andra använder `cell.set_dynamic_array_formula()` för att skriva en modern dynamisk arrayformel `=TRANSPOSE(...)`, vars resultat sprids ut automatiskt i Excel 365 eller Excel 2021. Det tredje tillvägångssättet använder `cell.set_array_formula()` för att skriva en klassisk arrayformel med Ctrl+Shift+Enter (CSE) som är kompatibel med äldre Excel-versioner. Den här artikeln går igenom varje tillvägångssätt med steg-för-steg-instruktioner och fullständiga kodexempel.
{{% /alert %}}

## **Introduktion**
Att transponera ett intervall innebär att rotera det så att det som var en rad blir en kolumn och det som var en kolumn blir en rad, vilket i praktiken spegelvänder data längs huvuddiagonalen. I Microsoft Excel utför kalkylbladsfunktionen `TRANSPOSE` den här åtgärden. Referensen till konceptet finns i [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Konceptet kan också tillämpas programmatiskt på ett cellintervall, vilket är användbart i många affärs- och rapporteringsscenarier.
- Orientera om kvartals- eller årsrapporter för försäljning där kvartalen normalt går tvärs över sidan och regionerna lodrätt på sidan, eller vice versa.
- Byta axelorientering i instrumentpaneler eller diagram så att en tidsserie går lodrätt på sidan i stället för tvärs över.
- Forma om data som importerats från externa system så att de passarar den layout som efterföljande analys- eller rapporteringsmallar förutsätter.
För att konkretisera resten av artikeln använder varje exempel följande lilla tabell med försäljning per region och kvartal. I exempelarbetsboken täcker denna tabell intervallet **A1:D5**, där cellen **A1** lämnas tom som det övre vänstra hörnet, **B1:D1** innehåller regionrubriker och **A2:A5** innehåller kvartalsrubriker.
| Region            | Europa    | Asien     | Nordamerika |
|-------------------|-----------|-----------|-------------|
| Kv. 1            | 21704714  | 8774099   | 12094215    |
| Kv. 2            | 17987034  | 12214447  | 10873099    |
| Kv. 3            | 19485029  | 14356879  | 15689543    |
| Kv. 4            | 22567894  | 15763492  | 17456723    |
Artikeln presenterar sedan tre olika sätt att transponera dessa data med Aspose.Cells for Python via .NET, där varje tillvägångssätt passar en viss Excel-version och ett visst användningsfall.

## **Tillvägångssätt 1 — Transponera intervall på plats (range.transpose)**
Använd det här tillvägångssättet när du vill transponera data utan att använda kalkylbladsfunktionen `TRANSPOSE`. Det fungerar i **alla Excel-versioner** och är inte beroende av dynamiska arrayer, vilket gör det till det säkraste valet för bred kompatibilitet. Det är lämpligt när du endast behöver det slutliga transponerade resultatet och inte behöver behålla den ursprungliga `TRANSPOSE`-formeln i arbetsboken.

### **API som används**
`range.transpose()` är en instansmetod i klassen `Aspose.Cells.Range`. När metoden anropas vänds intervallet på plats genom att rader och kolumner byts ut, så att det som var en rad blir en kolumn och det som var en kolumn blir en rad. Metoden ändrar underliggande celler direkt utan att skriva någon formel.

### **Steg**
1. Öppna källarbetsboken med `LoadOptions` inställd på filformatet `.xlsx` genom att anropa `Workbook(srcFile, LoadOptions(LoadFormat.XLSX))`.
2. Hämta det första kalkylbladet från arbetsboken med `workbook.worksheets[0]`.
3. Få åtkomst till kalkylbladets cellssamling via `worksheet.cells`.
4. Skapa källintervallet som täcker **A1:D5** genom att anropa `cells.create_range("A1:D5")`.
5. Anropa `source.transpose()` för att rotera intervallet på plats så att rader och kolumner byts ut.
6. Spara arbetsboken med `workbook.save(outputFile)`.
Efter transponeringen innehåller det ursprungliga ankareintervallet de roterade data. Den första raden innehåller (tom, **Europa**, **Asien**, **Nordamerika**) och den första kolumnen innehåller (tom, **Kv. 1**, **Kv. 2**, **Kv. 3**, **Kv. 4**). Varje ursprunglig försäljningskolumn blir en rad i det transponerade intervallet.

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

## **Tillvägångssätt 2 — Transponera med en dynamisk arrayformel (Excel 365 / 2021)**
Använd det här tillvägångssättet när du vill bevara formeln `=TRANSPOSE(A1:D5)` som en aktiv formel i utdataarbetsboken, så att resultatet uppdateras automatiskt när källdatan ändras. Det förutsätter att målfilen öppnas i **Excel 365 / Excel 2021 eller senare**, där dynamiska arrayer och spilloperatorn stöds.

### **API som används**
`cell.set_dynamic_array_formula(formula, options, calculate_value)` är en metod i klassen `Aspose.Cells.Cell` som anger cellens formel som en **dynamisk arrayformel**. Excel beräknar formeln en gång och sprider automatiskt ut resultatet i de omgivande cellerna. Om den tredje parametern sätts till `True`, instruerar Aspose.Cells att även beräkna de resulterande värdena när filen skrivs.

### **Steg**
1. Ladda källarbetsboken med `Workbook(srcFile, LoadOptions(LoadFormat.XLSX))`.
2. Hämta det första kalkylbladet och få åtkomst till dess `cells`-samling.
3. Placera den dynamiska arrayformeln i cell **A6**, precis under källintervallet, genom att anropa `cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", None, True)`.
4. Argumentet `None` anger att standardalternativen för `FormulaParseOptions` ska användas, och det tredje argumentet `True` anger att Aspose.Cells ska behandla formeln som en dynamisk array och beräkna den, så att de värden som sprids ut skrivs till arbetsboken.
5. Spara arbetsboken med `workbook.save(outputFile)`.
Cell **A6** innehåller formeln `=TRANSPOSE(A1:D5)`, och Excel sprider automatiskt ut resultatet i intervallet **A6:D10**, ett block med 5 rader och 4 kolumner som motsvarar de transponerade data.

{{% alert color="primary" %}}
Det här tillvägångssättet fungerar **endast i Excel 365 / 2021 eller senare**. Äldre Excel-versioner sprider inte dynamiska arrayformler korrekt.
{{% /alert %}}

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.XLSX))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
cells.get("A6").set_dynamic_array_formula("=TRANSPOSE(A1:D5)", ac.FormulaParseOptions(), True)
workbook.save(outFile, ac.SaveFormat.XLSX)
```

## **Tillvägångssätt 3 — Transponera med en klassisk arrayformel (CSE)**
Använd det här tillvägångssättet när du vill bevara en `TRANSPOSE`-formel i arbetsboken, men målfilen kan komma att öppnas i **äldre Excel-versioner (före 2021, inklusive 2019, 2016, 2013 och så vidare)**, där spridning av dynamiska arrayer inte stöds. Den klassiska CSE-arrayformeln (Ctrl+Shift+Enter) är det alternativ som är kompatibelt med äldre versioner och som alla Excel-versioner kan utvärdera.

### **API som används**
`cell.set_array_formula(array_formula, n_rows, n_columns)` är en metod i klassen `Aspose.Cells.Cell` som tilldelar ankarcellen en **klassisk arrayformel (CSE)** och anger dimensionerna för den resulterande arrayen. Aspose.Cells skriver en markör för arrayformel över flera celler, så att Excel utvärderar formeln som ett enda arrayuttryck som fyller det angivna intervallet.

### **Steg**
1. Ladda källarbetsboken som beskrivs i de föregående tillvägångssätten.
2. Hämta det första kalkylbladet och få åtkomst till dess `cells`-samling.
3. Anropa `cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)`. Det andra argumentet `4` anger antalet rader i destinationsarrayen, och det tredje argumentet `5` anger antalet kolumner.
4. Spara arbetsboken med `workbook.save(outputFile)`.
Cell **A6** är ankarcell för arrayformeln, och den beräknade arrayen sträcker sig över 4 rader och 5 kolumner med början vid A6, vilket motsvarar de transponerade dimensionerna av källintervallet A1:D5. Excel skriver en enda markör för arrayformel över det resulterande intervallet, så att äldre Excel-versioner utvärderar formeln korrekt.

{{% alert color="primary" %}}
Arrayformler med CSE är det klassiska Excel-sättet att utvärdera ett `TRANSPOSE`-uttryck, och det här tillvägångssättet är kompatibelt med alla Excel-versioner.
{{% /alert %}}

```python
import aspose.cells as ac
# Ladda källarboken med xlsx LoadOptions
srcFile = "source.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.XLSX))
# Få åtkomst till det första kalkylarket och dess Cells-samling
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Ange den klassiska CSE-arrayformeln i cell A6.
# Formeln =TRANSPOSE(A1:D5) roterar källområdet med 5 rader och 4 kolumner
# till en array med 4 rader och 5 kolumner. Det andra argumentet (4) är antalet rader
# och det tredje argumentet (5) är antalet kolumner i den resulterande arrayen.
# Aspose.Cells skriver CSE-markören för arrayformler så att Excel utvärderar den
# som en enda arrayformel för flera celler, kompatibel med äldre Excel-versioner
# (2019, 2016, 2013 etc.) som inte stöder dynamisk array spilling.
cells.get("A6").set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)
# Spara arbetsboken så att markören för arrayformeln sparas
workbook.save("output.xlsx")
```

## **Jämförelse — När du ska använda varje tillvägångssätt**
| Tillvägångssätt | API / metod | Excel-version | Bevaras formeln? | Utdataintervall |
|----------------|-------------|---------------|------------------|----------------|
| Tillvägångssätt 1 — Transponering på plats | `range.transpose()` | Alla Excel-versioner | Nej (endast värden) | Ursprungligt ankareintervall, 5×4 |
| Tillvägångssätt 2 — Dynamisk arrayformel | `cell.set_dynamic_array_formula` | Excel 365 / 2021+ | Ja (sprids ut dynamiskt) | Sprids ut från ankarcellen |
| Tillvägångssätt 3 — Klassisk arrayformel (CSE) | `cell.set_array_formula` | Alla Excel-versioner | Ja (arrayformel för flera celler) | Explicit storlek, 4×5 |
Använd **Tillvägångssätt 1** när du behöver en snabb versionsöverskridande omvandling och endast behöver att de transponerade värdena skrivs till filen. Använd **Tillvägångssätt 2** när du vet att en modern version av Excel används och vill att formeln ska förbli aktiv och uppdateras om källdatan ändras. Använd **Tillvägångssätt 3** när du behöver maximal kompatibilitet och vill bevara formeln i alla Excel-versioner, inklusive äldre versioner som inte stöder dynamiska arrayer.

## **Relaterade artiklar**
- [SmartMarker – rendering av en array med en enda cell | Aspose.Cells for Python via .NET](/cells/sv/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Infoga en bild i en cell](/cells/sv/python-net/inserting-an-image-into-a-cell/)
- [Dela Excel-filer i flera filer](/cells/sv/python-net/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python-net" >}}