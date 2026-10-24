---
title: SmartMarker – rendering av array i en enda cell | Aspose.Cells for Python via .NET
linktitle: SmartMarker – rendering av array i en enda cell | Aspose.Cells for Python via .NET
description: Lär dig hur du renderar arraydata till en enda cell med hjälp av attributen ArrayAsSingle och ExtraDelimiter i Smart Markers med Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Python via .NET-bibliotek, kalkylblad, Smart Markers, ArrayAsSingle, ExtraDelimiter, array i en enda cell, arrayrendering, mall
type: docs
weight: 195
url: /sv/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder rendering av arraydata till en enda cell via Smart Markers. Genom att använda attributet `ArrayAsSingle` tillsammans med attributet `ExtraDelimiter` kan utvecklare styra hur arrayelement skiljs åt i en enda cell, vilket ger flexibel formatering för rapporter och mallar.
{{% /alert %}}

## **Introduction**
Smart Markers i Aspose.Cells är en kraftfull, mallbaserad funktion som låter dig fylla kalkylbladsdata dynamiskt med marköruttryck som `&=DataSource.Field`. Markören placeras i en arbetsbok för design och när mallen bearbetas av `WorkbookDesigner` ersätts markörerna med värden från den angivna datakällan.
Som standard expanderar motorn arrayen och placerar varje element i en separat intilliggande cell när en Smart Marker refererar till en arrayegenskap, till exempel `&=DataSource.Numbers`. Elementen placeras antingen horisontellt längs en rad eller vertikalt nedåt i en kolumn. Det här beteendet är praktiskt i många sammanhang, men i vissa situationer är det bättre att rendera hela arrayen till en enda cell där elementen sammanfogas och skiljs åt med en valfri avgränsare.
Attributen `ArrayAsSingle` och `ExtraDelimiter`, som används tillsammans i en Smart Marker-tagg, möter exakt detta behov. De gör att du kan hålla rapportlayouter kompakta och förutsägbara samtidigt som du arbetar direkt med arraybaserade datakällor.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
När en Smart Marker refererar till en arrayegenskap expanderar Aspose.Cells arrayen över flera celler som standard. En markör som `&=Product.Tags` och som refererar till en `string[]` med fyra värden placerar exempelvis varje värde i sin egen cell, skjuter annat mallinnehåll utåt och kan på så sätt bryta en noggrant utformad rapportlayout.

### **Use Case Limitations**
Det finns många praktiska situationer där standardbeteendet för spridning är olämpligt:
- **Sammanfattande rapporter** som behöver en kompakt layout med en rad per post.
- **Tagg-, etikett- eller nyckelordslistor** som behöver visas som värden med komma eller vertikalstreck som avgränsare i en enda cell.
- **Filterchips eller statusindikatorer** som grupperar flera värden på ett ställe för bättre läsbarhet.
- **Nedströmsflöden** (CSV-export, PDF-rendering och sammanslagning av dokument) som förväntar ett enda samlat värde per cell i stället för ett expanderat intervall.
- **Kompatibilitet mellan plattformar**, där vissa mottagare inte kan hantera arrayer som sprids över flera celler.

### **The Gap It Fills**
Utan en inbyggd mekanism skulle utvecklare behöva förbehandla data i Python – sammanfoga arrayer till strängar med avgränsare innan data binds till `WorkbookDesigner`. Detta duplicerar logik, komplicerar datamodeller och ökar risken för fel. Attributen `ArrayAsSingle` och `ExtraDelimiter` eliminerar denna lösning genom att hantera formateringen deklarativt i själva Smart Marker.

## **Feature Benefits**
Att använda attributen `ArrayAsSingle` och `ExtraDelimiter` i Smart Markers ger flera fördelar:
- **Inneslutning i en enda cell**: Alla arrayelement renderas till exakt en cell, vilket håller layouten kompakt och förutsägbar.
- **Kontroll över avgränsare**: Ange valfri avgränsarsträng – komma, semikolon, bindestreck, vertikalstreck, ny rad eller valfri egen text.
- **Mallstyrd formatering**: Ingen ytterligare kod krävs för att förbehandla data; formateringsreglerna finns i Smart Marker-taggen.
- **Renare rapporter**: Arraydata skjuter inte längre intilliggande mallinnehåll till andra rader eller kolumner.
- **Mångsidiga datatyper**: Fungerar med strängar, tal, datum och alla andra datatyper som kan sammanfogas med en avgränsare.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras det ursprungliga spridningsbeteendet, så befintliga mallar fortsätter att fungera utan ändringar.

## **How to Use This Feature**

### **Smart Marker Syntax**
Attributen `ArrayAsSingle` och `ExtraDelimiter` skickas som nyckel-värde-par inom parenteserna i en vanlig Smart Marker. Den allmänna syntaxen är:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Markören består av följande delar:
- `&=DataSource.ArrayProperty` – den vanliga Smart Marker som refererar till arrayegenskapen i den bundna datakällan.
- `arrayasSingle=true` – instruerar motorn att rendera hela arrayen till en enda cell. Endast värdet `true` utlöser beteendet för en enda cell.
- `extraDelimiter=", "` – anger avgränsaren mellan arrayelementen. Värdet är en strängliteral; det kan vara tomt, ett tecken långt eller en sträng med flera tecken.

{{% alert color="primary" %}}
Attributet `extraDelimiter` accepterar alla strängliteraler, inklusive avgränsare med flera tecken, egen text eller escape-sekvenser som `\n` för utdata med ny rad som avgränsare. Om arrayen är tom lämnas den resulterande cellen tom.
{{% /alert %}}

### **Step-by-Step Workflow**
Följande arbetsflöde beskriver hur du renderar en array till en enda cell med Smart Markers.
1. **Förbered datakällan**: Skapa en klass eller datastruktur som exponerar en egenskap som returnerar en array. Egenskapen kan returnera `list[str]`, `list[int]` eller någon annan arraytyp som stöds.
2. **Skapa en arbetsbok för design**: Skapa ett nytt `Workbook`, lägg till en rubrikrad och placera en cell med en Smart Marker som refererar till arrayegenskapen med attributen `arrayasSingle` och `extraDelimiter`.
3. **Instantiera `WorkbookDesigner`**: Skapa ett `WorkbookDesigner`-objekt, koppla arbetsboken för design till det och bind datakällan med metoden `set_data_source`.
4. **Bearbeta markörerna**: Anropa metoden `WorkbookDesigner.process()` för att expandera markörerna och fylla arbetsboken med verkliga data.
5. **Spara resultatet**: Spara den resulterande arbetsboken på disk i XLSX eller något annat filformat som stöds.

### **Code Example 1 — Basic String Array Rendering**

```python
import aspose.cells as ac
class Product:
    def __init__(self):
        self.Tags = []
product = Product()
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Tags")
worksheet.cells.get("A2").put_value("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")
designer = ac.WorkbookDesigner()
designer.workbook = workbook
designer.set_data_source("Product", product)
designer.process()
workbook.save("output_arraySingle.xlsx")
```

### **Code Example 2 — Numeric Array with Custom Delimiter**

```python
import aspose.cells as ac
class Student:
    def __init__(self):
        self.scores = []
student = Student()
student.scores = [95, 88, 76, 100, 67]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Scores")
worksheet.cells.get("A2").put_value(" - ".join(str(s) for s in student.scores))
workbook.save("output_numericArray.xlsx")
```

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

```python
import aspose.cells as ac
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
cells.get("A1").put_value("Default Spreading Behavior:")
cells.get("A2").put_value("&=Order.Items")
# Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
cells.get("A4").put_value("Single Cell Rendering (arrayasSingle=true):")
cells.get("A5").put_value('&=Order.Items(arrayasSingle=true, extraDelimiter="; ")')
# Bind the data source and process Smart Markers
designer = ac.WorkbookDesigner(workbook)
designer.set_data_source("Order", order)
designer.process()
# Save the resulting workbook
workbook.save("output_comparison.xlsx")
```

### **Notes & Best Practices**
Ha följande punkter i åtanke när du arbetar med attributen `ArrayAsSingle` och `ExtraDelimiter`:
- Värdet för `extraDelimiter` behandlas som en strängliteral; escapa alla specialtecken som mallprocessorn kan tolka.
- Attributet `arrayasSingle` accepterar ett booleskt värde (`True` / `False`). Endast `True` utlöser beteendet för en enda cell; alla andra värden återgår till standardbeteendet för spridning.
- Om arrayen är tom eller har värdet `null` lämnas cellen tom eller innehåller en tom sträng, beroende på datatypen.
- Funktionen fungerar med objektdatakällor och med källor av typen `DataSet` och `DataTable`, där en kolumn kan delas upp i arrayer.
- För utdata med ny rad som avgränsare kan du använda `\n` eller `os.linesep`.
- Placera Smart Marker i en cell som är tillräckligt bred för att visa den resulterande sammanfogade strängen; annars kan innehållet visuellt spilla över i angränsande celler, beroende på formateringen.

## Related Articles
- [Lägg till filterfält till en pivottabell i Aspose.Cells for Python via .NET](/cells/sv/python-net/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller i Aspose.Cells for Python via .NET](/cells/sv/python-net/apply-style-to-pivot-table/)
- [Ändra layouten för sidfält i pivottabell](/cells/sv/python-net/change-page-field-layout/)
- [Konvertera sparkline till bild och HTML i Aspose.Cells for Python via .NET](/cells/sv/python-net/convert-sparkline-to-image-and-html/)
- [Konvertera Excel till OFD-format](/cells/sv/python-net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python-net" >}}