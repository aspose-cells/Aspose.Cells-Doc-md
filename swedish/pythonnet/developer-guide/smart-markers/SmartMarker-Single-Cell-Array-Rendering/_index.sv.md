---
title: SmartMarker-rendering av encellsmatris | Aspose.Cells for Python via .NET
linktitle: SmartMarker-rendering av encellsmatris | Aspose.Cells
description: Lär dig hur du renderar matrisdata till en enda cell med hjälp av attributen ArrayAsSingle och ExtraDelimiter i Smart Markers med Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET-bibliotek, kalkylblad, Smart Markers, ArrayAsSingle, ExtraDelimiter, encellsmatris, matrisrendering, mall
type: docs
weight: 195
url: /sv/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder rendering av matrisdata till en enda cell via Smart Markers. Genom att använda attributet `ArrayAsSingle` tillsammans med attributet `ExtraDelimiter` kan utvecklare styra hur matriselement separeras inom en enda cell, vilket ger flexibel formatering för rapporter och mallar.

{{% /alert %}}

## **Introduktion**

Smart Markers i Aspose.Cells är en kraftfull, mallbaserad funktion som låter dig dynamiskt fylla i kalkylbladsdata med hjälp av marköruttryck som `&=DataSource.Field`. Markören placeras i en designarbetsbok, och när mallen bearbetas av `WorkbookDesigner` ersätts markörerna med värden från den angivna datakällan.

Som standard expanderar motorn matrisen och placerar varje element i en separat intilliggande cell — antingen horisontellt över en rad eller vertikalt nedför en kolumn — när en Smart Marker refererar till en matrisegenskap (till exempel `&=DataSource.Numbers`). Även om detta beteende är bekvämt i många scenarier finns det situationer där du skulle föredra att rendera hela matrisen i en enda cell, med elementen sammanfogade och åtskilda av en valfri avgränsare.

Attributen `ArrayAsSingle` och `ExtraDelimiter`, som används tillsammans inom en Smart Marker-tagg, uppfyller exakt detta krav. De låter dig hålla rapportlayouter kompakta och förutsägbara samtidigt som du arbetar direkt med matrisdatakällor.

## **Varför denna funktion behövs**

### **Standardspridningsbeteende för matriser**

När en Smart Marker refererar till en matrisegenskap expanderar Aspose.Cells matrisen över flera celler som standard. En markör som `&=Product.Tags` mot en `string[]` som innehåller fyra värden placerar till exempel varje värde i sin egen cell, vilket trycker ut annat mallinnehåll och potentiellt förstör noggrant utformade rapportlayouter.

### **Begränsningar i användningsfall**

Det finns många praktiska scenarier där standardspridningsbeteendet är oönskat:

- **Sammanfattningsrapporter** som behöver en kompakt layout med en rad per post.
- **Tagg-, etikett- eller nyckelordslistor** som behöver visas som kommaseparerade eller rörseparerade värden i en enda cell.
- **Filterchips eller statusindikatorer** som grupperar flera värden på ett ställe för bättre läsbarhet.
- **Nedströms pipelines** (CSV-export, PDF-rendering, koppling av e-post) som förväntar sig ett enda konsoliderat värde per cell snarare än ett expanderat intervall.
- **Plattformskompatibilitet**, där vissa konsumenter inte tolererar matriser som sprider sig över flera celler.

### **Vilket gap det fyller**

Utan en inbyggd mekanism skulle utvecklare tvingas förbehandla data i Python — sammanfoga matriser till avgränsade strängar innan de binds till arbetsboksdesignern. Detta duplicerar logik, komplicerar datamodeller och ökar risken för fel. Attributen `ArrayAsSingle` och `ExtraDelimiter` eliminerar denna lösning genom att hantera formateringen deklarativt inom själva Smart Marker.

## **Funktionens fördelar**

Att använda attributen `ArrayAsSingle` och `ExtraDelimiter` i dina Smart Markers ger flera fördelar:

- **Inneslutning i en enda cell**: Alla matriselement renderas i exakt en cell, vilket håller layouter kompakta och förutsägbara.
- **Anpassad avgränsarkontroll**: Ange valfri separatorsträng — komma, semikolon, bindestreck, rör, nyrad eller annan anpassad text.
- **Maldriven formatering**: Ingen ytterligare kod krävs för att förbehandla data; formateringsregler finns inuti Smart Marker-taggen.
- **Renare rapporter**: Matrisdata trycker inte längre ut intilliggande mallinnehåll till olika rader eller kolumner.
- **Mångsidiga datatyper**: Fungerar med strängar, tal, datum och alla andra datatyper som kan sammanfogas med en avgränsare.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras det ursprungliga spridningsbeteendet, så befintliga mallar fortsätter att fungera oförändrat.

## **Hur du använder denna funktion**

### **Syntax för Smart Marker**

Attributen `ArrayAsSingle` och `ExtraDelimiter` skickas som nyckel-värde-par inom parenteserna i en vanlig Smart Marker. Den allmänna syntaxen är:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Markören består av följande delar:

- `&=DataSource.ArrayProperty` — den vanliga Smart Marker som refererar till matrisegenskapen på den bundna datakällan.
- `arrayasSingle=true` — instruerar motorn att rendera hela matrisen i en enda cell. Endast värdet `true` utlöser encellsbeteendet.
- `extraDelimiter=", "` — definierar separatorn som placeras mellan matriselement. Värdet är en strängliteral; det kan vara tomt, ett enskilt tecken eller en sträng med flera tecken.

{{% alert color="primary" %}}

Attributet `extraDelimiter` accepterar valfri strängliteral, inklusive avgränsare med flera tecken, anpassad text eller escape-sekvenser som `\n` för nyradsseparerad utdata. Om matrisen är tom lämnas den resulterande cellen tom.

{{% /alert %}}

### **Steg-för-steg-arbetsflöde**

Följande arbetsflöde beskriver hur du renderar en matris till en enda cell med Smart Markers.

1. **Förbered datakällan**: Skapa en klass (eller datastruktur) som exponerar en egenskap som returnerar en matris. Egenskapen kan returnera `list[str]`, `list[int]` eller någon annan matristyp som stöds.
2. **Skapa en designarbetsbok**: Skapa en ny `Workbook`, lägg till en rubrikrad och placera en Smart Marker-cell som refererar till matrisegenskapen med attributen `arrayasSingle` och `extraDelimiter`.
3. **Instansiera WorkbookDesigner**: Skapa ett `WorkbookDesigner`-objekt, koppla designarbetsboken till den och bind din datakälla med metoden `set_data_source`.
4. **Bearbeta markörerna**: Anropa metoden `WorkbookDesigner.process()` för att expandera Smart Markers och fylla arbetsboken med verklig data.
5. **Spara resultatet**: Spara den resulterande arbetsboken till disk i XLSX eller något annat filformat som stöds.

### **Kodexempel 1 — Grundläggande rendering av strängmatris**

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

### **Kodexempel 2 — Numerisk matris med anpassad avgränsare**

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

### **Kodexempel 3 — Jämförelse av standardbeteende jämfört med ArrayAsSingle-beteende**

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

# Avsnitt 1: Standard Smart Marker - värden sprids horisontellt över celler
cells["A1"].put_value("Default Spreading Behavior:")
cells["A2"].put_value("&=Order.Items")

# Avsnitt 2: Ny encellrendering med arrayasSingle och extraDelimiter
cells["A4"].put_value("Single Cell Rendering (arrayasSingle=true):")
cells["A5"].put_value('&=Order.Items(arrayasSingle=true, extraDelimiter="; ")')

# Bind datakällan och bearbeta Smart Markers
designer = ac.WorkbookDesigner(workbook)
designer.set_data_source("Order", order)
designer.process()

# Spara den resulterande arbetsboken
workbook.save("output_comparison.xlsx")
```

### **Anteckningar och bästa praxis**

Tänk på följande punkter när du arbetar med attributen `ArrayAsSingle` och `ExtraDelimiter`:

- Värdet på `extraDelimiter` behandlas som en strängliteral; escape:a alla specialtecken som din mallprocessor kan tolka.
- Attributet `arrayasSingle` accepterar ett booleskt värde (`True` / `False`). Endast `True` utlöser encellsbeteendet; alla andra värden faller tillbaka till standardspridningsbeteendet.
- Om matrisen är tom eller null lämnas cellen tom (eller innehåller en tom sträng beroende på datatypen).
- Funktionen fungerar med objektdatakällor samt `DataSet`- och `DataTable`-källor där en kolumn kan delas upp i matriser.
- För nyradsseparerad utdata kan du använda `\n` eller `os.linesep` som avgränsarvärde.
- Placera Smart Marker i en cell som har tillräcklig bredd för att visa den resulterande sammanfogade strängen; annars kan innehållet visuellt spilla över till intilliggande celler beroende på formatet.

## **Relaterade artiklar**

- [Smart Markers](/cells/sv/python-net/smart-markers/)
- [Sammanfoga och dela celler](/cells/sv/python-net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="python" >}}