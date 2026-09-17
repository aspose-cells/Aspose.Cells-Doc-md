---
title: SmartMarker-rendering av array i en cell | Aspose.Cells for Python via .NET
linktitle: SmartMarker-rendering av array i en cell | Aspose.Cells for Python via .NET
description: Lär dig hur du renderar arraydata till en enskild cell med hjälp av attributen ArrayAsSingle och ExtraDelimiter i Smart Markers med Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET-bibliotek, kalkylblad, Smart Markers, ArrayAsSingle, ExtraDelimiter, array i en cell, array-rendering, mall
type: docs
weight: 195
url: /sv/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder rendering av arraydata till en enskild cell via Smart Markers. Genom att använda attributet `ArrayAsSingle` tillsammans med attributet `ExtraDelimiter` kan utvecklare styra hur arrayelement separeras inom en enskild cell, vilket ger flexibel formatering för rapporter och mallar.

## **Introduction**
Smart Markers i Aspose.Cells är en kraftfull, mallbaserad funktion som låter dig dynamiskt fylla kalkylbladsdata med hjälp av marköruttryck som `&=DataSource.Field`. Markören placeras i en designrarbetsbok, och när mallen bearbetas av `WorkbookDesigner` ersätts markörerna med värden från den tillhandahållna datakällan.
Som standard, när en Smart Marker refererar till en arrayegenskap (till exempel `&=DataSource.Numbers`), expanderar motorn arrayen och placerar varje element i en separat intilliggande cell — antingen horisontellt över en rad eller vertikalt nedför en kolumn. Även om detta beteende är bekvämt i många scenarier finns det situationer där du skulle föredra att rendera hela arrayen i en enda cell, med elementen sammanfogade och åtskilda av en avgränsare efter eget val.
Attributen `ArrayAsSingle` och `ExtraDelimiter`, som används tillsammans inom en Smart Marker-tagg, uppfyller just detta krav. De låter dig hålla rapportlayouter kompakta och förutsägbara samtidigt som du arbetar inbyggt med array-datakällor.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
När en Smart Marker refererar till en arrayegenskap expanderar Aspose.Cells arrayen över flera celler som standard. Till exempel kommer en markör som `&=Product.Tags` mot en `string[]` som innehåller fyra värden att placera varje värde i sin egen cell, vilket skjuter annat mallinnehåll utåt och potentiellt bryter noggrant utformade rapportlayouter.

### **Use Case Limitations**
Det finns många praktiska scenarier där standardspridningsbeteendet är oönskat:
- **Sammanfattningsrapporter** som behöver en kompakt layout med en rad per post.
- **Tagg-, etikett- eller nyckelordslistor** som behöver visas som kommaseparerade eller pipe-separerade värden i en enda cell.
- **Filterchips eller statusindikatorer** som grupperar flera värden på ett ställe för läsbarhet.
- **Nedströms pipelines** (CSV-export, PDF-rendering, sammanfogning av e-post) som förväntar sig ett enda konsoliderat värde per cell snarare än ett expanderat intervall.
- **Plattformsoberoende kompatibilitet**, där vissa konsumenter inte tolererar arrayer som sprids över flera celler.

### **The Gap It Fills**
Utan en inbyggd mekanism skulle utvecklare tvingas förbehandla data i Python — sammanfoga arrayer till avgränsade strängar innan de binds till arbetsboksdesignern. Detta duplicerar logik, komplicerar datamodeller och ökar risken för fel. Attributen `ArrayAsSingle` och `ExtraDelimiter` eliminerar detta kringgående genom att hantera formateringen deklarativt inuti själva Smart Marker.

## **Feature Benefits**
Att använda attributen `ArrayAsSingle` och `ExtraDelimiter` i dina Smart Markers ger flera fördelar:
- **Inneslutning i en cell**: Alla arrayelement renderas till exakt en cell, vilket håller layouter kompakta och förutsägbara.
- **Anpassad avgränsarkontroll**: Ange vilken separatorsträng du vill — komma, semikolon, bindestreck, pipe, nyrad, eller annan anpassad text.
- **Malldriven formatering**: Ingen ytterligare kod krävs för att förbehandla data; formateringsregler finns inuti Smart Marker-taggen.
- **Renare rapporter**: Arraydata skjuter inte längre intilliggande mallinnehåll till olika rader eller kolumner.
- **Mångsidiga datatyper**: Fungerar med strängar, tal, datum och andra datatyper som kan sammanfogas med en avgränsare.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras det ursprungliga spridningsbeteendet, så befintliga mallar fortsätter att fungera oförändrat.

## **How to Use This Feature**

### **Smart Marker Syntax**
Attributen `ArrayAsSingle` och `ExtraDelimiter` skickas som nyckel-värde-par inom parenteserna i en standard Smart Marker. Den allmänna syntaxen är:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Markören består av följande delar:
- `&=DataSource.ArrayProperty` — standard Smart Marker som refererar till arrayegenskapen på den bundna datakällan.
- `arrayasSingle=true` — instruerar motorn att rendera hela arrayen till en enda cell. Endast värdet `true` utlöser encellsbeteendet.
- `extraDelimiter=", "` — definierar avgränsaren som placeras mellan arrayelement. Värdet är en strängliteral; det kan vara tomt, ett enskilt tecken, eller en flerteckensträng.

{{% alert color="primary" %}}
Attributet `extraDelimiter` accepterar vilken strängliteral som helst, inklusive flerteckenavgränsare, anpassad text, eller escapesekvenser som `\n` för nyradsseparerad utdata. Om arrayen är tom lämnas den resulterande cellen tom.

### **Step-by-Step Workflow**
Följande arbetsflöde beskriver hur man renderar en array till en enda cell med hjälp av Smart Markers.
1. **Förbered datakällan**: Skapa en klass (eller datastruktur) som exponerar en egenskap som returnerar en array. Egenskapen kan returnera `list[str]`, `list[int]` eller någon annan stödd arraytyp.
2. **Skapa en designrarbetsbok**: Skapa en ny `Workbook`, lägg till en rubrikrad och placera en Smart Marker-cell som refererar till arrayegenskapen med attributen `arrayasSingle` och `extraDelimiter`.
3. **Instansiera WorkbookDesigner**: Skapa ett `WorkbookDesigner`-objekt, koppla designrarbetsboken till det och bind din datakälla med metoden `set_data_source`.
4. **Bearbeta markörerna**: Anropa metoden `WorkbookDesigner.process()` för att expandera Smart Markers och fylla arbetsboken med riktig data.
5. **Spara resultatet**: Spara den resulterande arbetsboken till disk i XLSX eller något annat filformat som stöds.

### **Code Example 1 — Basic String Array Rendering**

```python
class Product:
    def __init__(self):
        self.Tags = []
product = Product()
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells["A1"].put_value("Tags")
worksheet.cells["A2"].put_value("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")
designer = ac.WorkbookDesigner()
designer.workbook = workbook
designer.set_data_source("Product", product)
designer.process()
workbook.save("output_arraySingle.xlsx")
```

### **Code Example 2 — Numeric Array with Custom Delimiter**

```python
class Student:
    def __init__(self):
        self.scores = []
student = Student()
student.scores = [95, 88, 76, 100, 67]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells["A1"].put_value("Scores")
worksheet.cells["A2"].put_value(" - ".join(str(s) for s in student.scores))
workbook.save("output_numericArray.xlsx")
```

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

```python
class Order:
    def __init__(self, items):
        self._items = items
    @property
    def Items(self):
        return self._items
    @Items.setter
    def Items(self, value):
        self._items = value
order = Order(["Apple", "Banana", "Cherry", "Date"])
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Section 1: Default Smart Marker - values spread horizontally across cells
cells["A1"].put_value("Default Spreading Behavior:")
cells["A2"].put_value("&=Order.Items")
# Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
cells["A4"].put_value("Single Cell Rendering (arrayasSingle=true):")
cells["A5"].put_value('&=Order.Items(arrayasSingle=true, extraDelimiter="; ")')
# Bind the data source and process Smart Markers
designer = ac.WorkbookDesigner(workbook)
designer.set_data_source("Order", order)
designer.process()
# Save the resulting workbook
workbook.save("output_comparison.xlsx")
```

### **Notes & Best Practices**
Tänk på följande punkter när du arbetar med attributen `ArrayAsSingle` och `ExtraDelimiter`:
- Värdet `extraDelimiter` behandlas som en strängliteral; escapa alla specialtecken som din mallprocessor kan tolka.
- Attributet `arrayasSingle` accepterar ett boolskt värde (`True` / `False`). Endast `True` utlöser encellsbeteendet; alla andra värden återgår till standardspridningsbeteendet.
- Om arrayen är tom eller null lämnas cellen tom (eller innehåller en tom sträng beroende på datatypen).
- Funktionen fungerar med objektdatakällor såväl som `DataSet`- och `DataTable`-källor där en kolumn kan delas upp i arrayer.
- För nyradsseparerad utdata kan du använda `\n` eller `os.linesep` som avgränsarvärde.
- Placera Smart Marker i en cell som har tillräcklig bredd för att visa den resulterande sammanfogade strängen; annars kan innehållet visuellt spilla över i intilliggande celler beroende på formatet.
{{% /alert %}}

{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via .NET](/cells/sv/python-net/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via .NET](/cells/sv/python-net/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/sv/python-net/change-page-field-layout/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for Python via .NET](/cells/sv/python-net/convert-sparkline-to-image-and-html/)
- [Converting Excel to OFD Format](/cells/sv/python-net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python" >}}