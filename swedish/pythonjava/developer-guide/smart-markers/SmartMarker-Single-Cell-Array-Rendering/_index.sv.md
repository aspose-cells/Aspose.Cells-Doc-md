---
title: SmartMarker-rendering av array i en enda cell | Aspose.Cells Python via Java
description: Lär dig hur du renderar arraydata till en enda cell med hjälp av Smart Marker-attributen arrayassingle och arraydelimiter i Aspose.Cells for Python via Java.
linktitle: SmartMarker-array i en enda cell | Aspose.Cells
url: /sv/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Python via Java-bibliotek, kalkylblad, Smart Markers, arrayassingle, arraydelimiter, array i en enda cell, arrayrendering, mall
type: docs
weight: 195
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells kan rendera en arraydatakälla till en enda cell via Smart Markers. Attributet `arrayassingle` stänger av den standardsättliga spridningen element för element, och attributet `arraydelimiter` väljer separatorn som placeras mellan de sammanfogade elementen – komma som standard, eller valfritt enskilt tecken eller citerad sträng med flera tecken som du anger.
{{% /alert %}}

## **Introduktion**

Smart Markers i Aspose.Cells är en mallbaserad funktion som dynamiskt fyller kalkylbladsdata med hjälp av markörexpressioner som `&=DataSource.Field`. Markören placeras i en designarbok, och när mallen behandlas av `WorkbookDesigner` ersätts markörerna med värden från den angivna datakällan.
Som standard expanderar motorn arrayen och placerar varje element i en egen cell när en Smart Marker refererar till ett arrayfält (t.ex. `&=Product.Tags` som är bundet till en lista med fyra värden), så att värdena sprids vertikalt nedåt i kolumnen under markören. Även om detta beteende är praktiskt i många scenarier finns situationer där du hellre vill rendera hela arrayen till en enda cell, med elementen sammanfogade och åtskilda av en separator som du väljer.
Attributen `arrayassingle` och `arraydelimiter`, som skrivs inom parenteserna för en Smart Marker i formen `name:value`, tar precis itu med detta behov. De gör att du kan hålla layouten för rapporter kompakt och förutsägbar samtidigt som du arbetar direkt med arraydatakällor.

## **Varför den här funktionen behövs**

### **Standardspridning av arrayer**

När en Smart Marker refererar till ett arrayfält expanderar Aspose.Cells som standard arrayen över flera celler. En markör som `&=Product.Tags` för en lista med fyra värden placerar exempelvis varje värde i en egen cell under markören, vilket flyttar annat mallinnehåll utåt och kan bryta mot omsorgsfullt utformade rapportlayouter.

### **Begränsningar i användningsfall**

Det finns många praktiska scenarier där standardspridningen är olämplig:
- **Sammanfattande rapporter** som behöver en kompakt layout med en rad per post.
- **Tagg-, etikett- eller nyckelordslistor** som behöver visas som kommaseparerade eller rörseparerade värden i en enda cell.
- **Filterchips eller statusindikatorer** som grupperar flera värden på ett ställe för läsbarhet.
- **Nedströmspipeliner** (CSV-export, PDF-rendering, sammanslagning av post) som förväntar sig ett enda samlat värde per cell i stället för ett expanderat intervall.
- **Kompatibilitet mellan plattformar**, där vissa konsumenter inte kan hantera arrayer som sträcker sig över flera celler.

### **Luckan som funktionen fyller**

Utan en inbyggd mekanism skulle utvecklare behöva förbehandla data i Python – sammanfoga listor till strängar med separatorer innan de kopplas till `WorkbookDesigner`. Detta duplicerar logiken, komplicerar datamodellerna och ökar risken för fel. Attributen `arrayassingle` och `arraydelimiter` eliminerar denna omvägning genom att hantera formateringen deklarativt i själva Smart Markern.

## **Fördelar med funktionen**

Användning av attributen `arrayassingle` och `arraydelimiter` i dina Smart Markers ger flera fördelar:
- **Sammanhållning i en cell**: Alla arrayelement renderas till exakt en cell, vilket håller layouter kompakta och förutsägbara.
- **Kontroll över anpassad separator**: Ange den separator du vill använda – standardskomma, semikolon, bindestreck, lodstreck eller en citerad sträng med flera tecken som `" | "`.
- **Mallstyrd formatering**: Ingen ytterligare kod krävs för att förbehandla data; formateringsreglerna ligger i Smart Marker-taggen.
- **Renare rapporter**: Arraydata skjuter inte längre intilliggande mallinnehåll till andra rader eller kolumner.
- **Flexibla datatyper**: Fungerar med strängarrayer som tillhandahålls som JSON-rader, inklusive numeriska värden som återges som strängar.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras det ursprungliga spridningsbeteendet, så befintliga mallar fortsätter att fungera oförändrat.

## **Så använder du funktionen**

### **Syntax för Smart Marker**

Attributen `arrayassingle` och `arraydelimiter` använder Aspose.Cells attributgrammatik med `name:value` inom parenteserna för en vanlig Smart Marker. Den allmänna syntaxen är:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

Markören består av följande delar:
- `&=DataSource.ArrayField` – den vanliga Smart Marker som refererar till arrayfältet i den bundna datakällan.
- `arrayassingle:true` – instruerar motorn att rendera hela arrayen till en enda cell i stället för att sprida elementen.
- `arraydelimiter:;` – valfritt; definierar separatorn mellan arrayelementen. När den utelämnas används ett komma.

{{% alert color="warning" %}}
Skriv attributen i `name:value`-form (ett kolon, inte ett likhetstecken) och separera flera attribut med ett komma **utan mellanrum**. Ett mellanrum efter kommat förskjuter det tolkade värdet med ett tecken – `(arrayassingle:true, arraydelimiter:;)` skulle sammanfoga med den felaktiga separatorn `:;` i stället för `;`.
{{% /alert %}}

### **Former för separatorer**

- Ett enskilt tecken anges direkt efter kolonet: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- En separator med flera tecken skrivs med dubbla citattecken: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Steg-för-steg-arbetsflöde**

Det följande arbetsflödet beskriver hur du renderar en array till en enda cell med Smart Markers.
1. **Förbered datakällan**: Strukturera varje post som ett JSON-objekt där ett fält innehåller en array, till exempel `{"Tags": ["C#", "Aspose"]}`. Vanliga instanser av Python-klasser och ordböcker som skickas till `setDataSource` binds inte på denna plattform – JSON-rader är den tabellform som stöds.
2. **Skapa en designarbok**: Skapa en ny `Workbook`, lägg till en rubrikrad och placera en cell med en Smart Marker som refererar till arrayfältet med attributet `arrayassingle` (och `arraydelimiter` om en anpassad separator behövs).
3. **Instantiera `WorkbookDesigner`**: Skapa en `WorkbookDesigner` runt arbetsboken och koppla dina JSON-rader med `setJsonDataSource`.
4. **Bearbeta markörerna**: Anropa metoden `WorkbookDesigner.process()` för att expandera Smart Markers och fylla arbetsboken med faktiska data.
5. **Spara resultatet**: Spara den resulterande arbetsboken på disk i XLSX eller i något annat filformat som stöds.

### **Kodexempel 1 – Grundläggande rendering av strängarray**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-single.xlsx")
```

Exemplet skriver ut det sammanfogade värdet av hela arrayen. De fyra taggarna hamnar i en cell, åtskilda av standardskomman:

```
C#,Aspose,SmartMarker,Excel
```

### **Kodexempel 2 – Numeriska värden med en anpassad separator**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Scores")
# arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-numeric.xlsx")
```

När poängen tillhandahålls som JSON-strängar behåller det sammanfogade utdatavärdet talen i sin enkla form:

```
95-88-76-100-67
```

{{% alert color="note" %}}
JSON-tal som passerar via Java-motorn kommer fram som flyttal, så `[95, 88]` skulle sammanfogas som `95.0-88.0`. Sätt citattecken runt talen i JSON-raderna när du vill att den sammanfogade cellen ska innehålla exakt heltalstext.
{{% /alert %}}

### **Kodexempel 3 – Jämförelse av standardspridning och rendering i en enda cell**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner

workbook = Workbook()
cells = workbook.getWorksheets().get(0).getCells()
# Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default")
cells.get("B2").putValue("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell")
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).getStringValue() or ""
    c = cells.get(row, 2).getStringValue() or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

Den vanliga markören fyller en cell per element nedåt i kolumn B, medan `arrayassingle`-markören komprimerar samma array till en enda cell i kolumn C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Anteckningar och bästa praxis**

Tänk på följande punkter när du arbetar med attributen `arrayassingle` och `arraydelimiter`:
- Attributvärden använder formen `name:value`. En form med likhetstecken, som `arrayassingle=true`, känns inte igen och faller tyst tillbaka till standardspridningen.
- Separera attribut med ett komma och inga mellanrum; ett mellanrum efter kommat förskjuter separatorvärdet med ett tecken (se varningen ovan).
- Värdet för `arraydelimiter` kan vara ett enskilt tecken som skrivs direkt efter kolonet, eller en sträng med flera tecken omgiven av dubbla citattecken.
- När `arraydelimiter` utelämnas sammanfogas elementen med ett komma.
- Ange arrayfält via radobjekt till `setJsonDataSource`; vanliga Python-objekt och ordböcker som skickas till `setDataSource` binds inte på denna plattform.
- JSON-tal kommer fram som flyttal via Java-motorn (`95` sammanfogas som `95.0`); sätt citattecken runt numeriska värden i JSON-raderna när exakt heltalstext är viktig.
- Placera Smart Markern i en cell som är tillräckligt bred för att visa den resulterande sammanfogade strängen; annars kan innehållet visuellt överspilla till angränsande celler, beroende på formatet.

## **Relaterade artiklar**
- [Lägga till filterfält i en pivottabell i Aspose.Cells for Python via Java](/cells/sv/python-java/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller i Aspose.Cells for Python via Java](/cells/sv/python-java/apply-style-to-pivot-table/)
- [Ändra layouten för sidfältet i en pivottabell](/cells/sv/python-java/change-page-field-layout/)
- [Konvertera sparklinje till bild och HTML i Aspose.Cells for Python via Java](/cells/sv/python-java/convert-sparkline-to-image-and-html/)
- [Konvertera Excel till OFD-format](/cells/sv/python-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python" >}}