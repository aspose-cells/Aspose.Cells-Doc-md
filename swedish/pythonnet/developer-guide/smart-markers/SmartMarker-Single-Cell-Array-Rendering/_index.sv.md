---
title: Rendering av array i en enda cell med SmartMarker | Aspose.Cells for Python via .NET
description: Lär dig hur du renderar arraydata till en enda cell med hjälp av Smart Marker-attributen `arrayassingle` och `arraydelimiter` i Aspose.Cells for Python via .NET.
linktitle: SmartMarker – arrayrendering i en enda cell | Aspose.Cells
url: /sv/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Python via .NET-bibliotek, kalkylblad, Smart Markers, arrayassingle, arraydelimiter, array i en enda cell, arrayrendering, mall
type: docs
weight: 195
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells kan rendera en arraydatakälla till en enda cell med hjälp av Smart Markers. Attributet `arrayassingle` stänger av den standardspridning som sker element för element, och attributet `arraydelimiter` väljer den avgränsare som placeras mellan de sammanfogade elementen – komma som standard, eller ett valfritt enskilt tecken eller en citerad flerteckenssträng som du anger.
{{% /alert %}}

## **Introduktion**

Smart Markers i Aspose.Cells är en mallbaserad funktion som dynamiskt fyller kalkylbladsdata med hjälp av marköruttryck som `&=DataSource.Field`. Markören placeras i en designarbok, och när mallen bearbetas av `WorkbookDesigner` ersätts markörerna med värden från den angivna datakällan.
Som standard expanderar motorn arrayen när en Smart Marker refererar till ett arrayfält (t.ex. `&=Product.Tags` som är bundet till en lista med fyra värden) och placerar varje element i en egen cell, spridda lodrätt nedåt i kolumnen under markören. Det här beteendet är bekvämt i många sammanhang, men ibland vill du hellre rendera hela arrayen till en enda cell, där elementen sammanfogas och åtskiljs av en avgränsare som du väljer.
Attributen `arrayassingle` och `arraydelimiter`, som skrivs inom parenteserna för en Smart Marker i formatet `name:value`, tillgodoser exakt detta behov. De gör att du kan hålla rapportlayouterna kompakta och förutsägbara samtidigt som du arbetar direkt med arraydatakällor.

## **Varför den här funktionen behövs**

### **Standardbeteende för spridning av arrayer**

När en Smart Marker refererar till ett arrayfält expanderar Aspose.Cells arrayen över flera celler som standard. En markör som `&=Product.Tags` används mot en lista med fyra värden placerar till exempel varje värde i en egen cell under markören, vilket förskjuter annat mallinnehåll och kan bryta noggrant utformade rapportlayouter.

### **Begränsningar i användningsfallen**

Det finns många praktiska situationer där det standardspridda beteendet är olämpligt:
- **Sammanfattningsrapporter** som behöver en kompakt layout med en rad per post.
- **Listor med taggar, etiketter eller nyckelord** som måste visas som komma- eller pipeåtskilda värden i en enda cell.
- **Filterchips eller statusindikatorer** som grupperar flera värden på ett ställe för att underlätta läsningen.
- **Efterföljande bearbetningskedjor** (CSV-export, PDF-rendering och dokumentkoppling) som förväntar sig ett enda konsoliderat värde per cell i stället för ett expanderat intervall.
- **Plattformsoberoende kompatibilitet**, där vissa mottagare inte kan hantera arrayer som sprider sig över flera celler.

### **Luckan som den fyller**

Utan en inbyggd mekanism skulle utvecklare behöva förbehandla data i Python – sammanfoga listor till avgränsade strängar innan de binds till `WorkbookDesigner`. Detta duplicerar logik, komplicerar datamodeller och ökar risken för fel. Attributen `arrayassingle` och `arraydelimiter` eliminerar denna omväg genom att hantera formateringen deklarativt inuti själva Smart Markern.

## **Funktionens fördelar**

Att använda attributen `arrayassingle` och `arraydelimiter` i Smart Markers ger flera fördelar:
- **Innehåll i en enda cell**: Alla arrayelement renderas till exakt en cell, vilket håller layouterna kompakta och förutsägbara.
- **Kontroll över anpassad avgränsare**: Ange den avgränsare du vill – standardkomma, ett semikolon, en bindestreck, ett vertikalstreck eller en citerad flerteckenssträng som `" | "`.
- **Mallstyrd formatering**: Ingen ytterligare kod krävs för att förbehandla data; formateringsreglerna finns inuti Smart Marker-taggen.
- **Renare rapporter**: Arraydata förskjuter inte längre intilliggande mallinnehåll till andra rader eller kolumner.
- **Mångsidiga datatyper**: Fungerar med stränglistor och numeriska listor som tillhandahålls som JSON-rader.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras det ursprungliga beteendet med spridning, så befintliga mallar fortsätter att fungera utan ändringar.

## **Så använder du funktionen**

### **Syntax för Smart Marker**

Attributen `arrayassingle` och `arraydelimiter` använder Aspose.Cells attributgrammatik i formatet `name:value` inom parenteserna för en vanlig Smart Marker. Den allmänna syntaxen är:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

Markören består av följande delar:
- `&=DataSource.ArrayField` – den vanliga Smart Markern som refererar till arrayfältet i den bundna datakällan.
- `arrayassingle:true` – instruerar motorn att rendera hela arrayen till en enda cell i stället för att sprida elementen.
- `arraydelimiter:;` – valfritt; definierar avgränsaren mellan arrayelementen. Om det utelämnas används ett komma.

{{% alert color="warning" %}}
Skriv attribut i formatet `name:value` (ett kolon, inte ett likhetstecken) och separera flera attribut med ett komma **utan mellanslag**. Ett mellanslag efter kommat gör att det tolkade värdet förskjuts ett tecken – `(arrayassingle:true, arraydelimiter:;)` skulle sammanfoga med den felaktiga avgränsaren `:;` i stället för `;`.
{{% /alert %}}

### **Format för avgränsare**

- Ett enskilt tecken anges direkt efter kolonet: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- En avgränsare med flera tecken skrivs med dubbla citattecken: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Steg-för-steg-arbetsflöde**

Följande arbetsflöde beskriver hur du renderar en array till en enda cell med Smart Markers.
1. **Förbered datakällan**: Ordna varje post som ett JSON-objekt där ett fält innehåller en array, till exempel `{"Tags": ["C#", "Aspose"]}`. Enkla Python-klassinstanser, ordböcker och listor som skickas till `set_data_source` binder inte arrayfält på den här plattformen – JSON-rader är den tabellära form som stöds.
2. **Skapa en designarbok**: Skapa en ny `Workbook`, lägg till en rubrikrad och placera en cell med en Smart Marker som refererar till arrayfältet med attributet `arrayassingle` (och `arraydelimiter` när en anpassad avgränsare behövs).
3. **Instantiera `WorkbookDesigner`**: Skapa en `WorkbookDesigner` för arbetsboken och koppla dina JSON-rader till den med `set_json_data_source`.
4. **Bearbeta markörerna**: Anropa metoden `WorkbookDesigner.process()` för att expandera Smart Markers och fylla arbetsboken med riktiga data.
5. **Spara resultatet**: Spara den resulterande arbetsboken till disk i XLSX eller i något annat filformat som stöds.

### **Kodexempel 1 – grundläggande rendering av en strängarray**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.cells.get("A2").put_value("&=Product.Tags(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-single.xlsx")
```

Exemplet skriver ut det sammanfogade värdet av hela arrayen. De fyra taggarna placeras i en cell, åtskilda av standardkomman:

```
C#,Aspose,SmartMarker,Excel
```

### **Kodexempel 2 – numerisk array med en anpassad avgränsare**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Scores")
# arraydelimiter:- joins the numbers with a hyphen
worksheet.cells.get("A2").put_value("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Student",
    '[{"Scores": [95, 88, 76, 100, 67]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-numeric.xlsx")
```

JSON-nummer sammanfogas precis som strängar – varje element behåller sin oförändrade numeriska text:

```
95-88-76-100-67
```

### **Kodexempel 3 – jämförelse av standardspridning och rendering i en enda cell**

```python
import aspose.cells as ac

workbook = ac.Workbook()
cells = workbook.worksheets[0].cells
# Column B: default marker — values spread vertically down the column
cells.get("B1").put_value("Default")
cells.get("B2").put_value("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").put_value("Single cell")
cells.get("C2").put_value("&=Order.Items(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).string_value or ""
    c = cells.get(row, 2).string_value or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

Standardmarkören fyller en cell per element nedåt i kolumn B, medan `arrayassingle`-markören sammanför samma array till en enda cell i kolumn C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Anteckningar och bästa praxis**

Följande punkter bör beaktas när du arbetar med attributen `arrayassingle` och `arraydelimiter`:
- Attributvärden använder formatet `name:value`. En form med likhetstecken, såsom `arrayassingle=true`, känns inte igen och återgår tyst till standardbeteendet där elementen sprids.
- Separera attribut med ett komma och inga mellanslag; ett mellanslag efter kommat förskjuter avgränsarvärdet ett tecken (se varningen ovan).
- `arraydelimiter`-värdet kan vara ett enskilt tecken som anges direkt efter kolonet eller en flerteckenssträng i dubbla citattecken.
- När `arraydelimiter` utelämnas sammanfogas elementen med ett komma.
- Ange arrayfält via radobjekt för `set_json_data_source`. Enkla Python-objekt och ordböcker som skickas till `set_data_source` binds inte på den här plattformen, och en anpassad `ICellsDataTable` vars kolumn returnerar en Python-lista renderar listans containertext i stället för att sammanfoga elementen.
- JSON-nummer behåller sin vanliga heltalsform i det sammanfogade resultatet.

## **Relaterade artiklar**
- [Lägga till filterfält i en pivottabell i Aspose.Cells för .NET](/cells/sv/python-net/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller i Aspose.Cells for Python via .NET](/cells/sv/python-net/apply-style-to-pivot-table/)
- [Ändra layouten för sidfältet i en pivottabell](/cells/sv/python-net/change-page-field-layout/)
- [Konvertera sparkline till bild och HTML i Aspose.Cells for Python via .NET](/cells/sv/python-net/convert-sparkline-to-image-and-html/)
- [Konvertera Excel till OFD-format](/cells/sv/python-net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python-net" >}}