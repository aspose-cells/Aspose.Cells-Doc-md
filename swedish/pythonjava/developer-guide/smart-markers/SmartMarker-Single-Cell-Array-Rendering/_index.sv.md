---
title: SmartMarker-rendering av enstaka cellarray | Aspose.Cells Python via Java
linktitle: SmartMarker-rendering av enstaka cellarray | Aspose.Cells Python
description: Lär dig hur du renderar arraydata i en enda cell med attributen ArrayAsSingle och ExtraDelimiter i Smart Markers med Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java-bibliotek, kalkylblad, Smart Markers, ArrayAsSingle, ExtraDelimiter, enstaka cellarray, arrayrendering, mall
type: docs
weight: 195
url: /sv/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder rendering av arraydata i en enda cell via Smart Markers. Genom att använda attributet `ArrayAsSingle` tillsammans med attributet `ExtraDelimiter` kan utvecklare styra hur arrayelement separeras inom en enda cell, vilket ger flexibel formatering för rapporter och mallar.

{{% /alert %}}

## **Introduktion**

Smart Markers i Aspose.Cells är en kraftfull, mallbaserad funktion som låter dig dynamiskt fylla kalkylbladsdata med hjälp av markörexpressioner som `&=DataSource.Field`. Markören placeras i en designarbetsbok, och när mallen bearbetas av `WorkbookDesigner` ersätts markörerna med värden från den angivna datakällan.

Som standard, när en Smart Marker refererar till en array-egenskap (till exempel `&=DataSource.Numbers`), expanderar motorn arrayen och placerar varje element i en separat intilliggande cell — antingen horisontellt över en rad eller vertikalt nedåt i en kolumn. Även om detta beteende är bekvämt i många scenarier finns det situationer där du skulle föredra att rendera hela arrayen i en enda cell, med elementen sammanfogade och åtskilda av en avgränsare som du väljer.

Attributen `ArrayAsSingle` och `ExtraDelimiter`, som används tillsammans inuti en Smart Marker-tagg, tar itu med just detta krav. De låter dig hålla rapportlayouter kompakta och förutsägbara samtidigt som du arbetar naturligt med arraydatakällor.

## **Varför denna funktion behövs**

### **Standardbeteende för arrayspridning**

När en Smart Marker refererar till en array-egenskap expanderar Aspose.Cells arrayen över flera celler som standard. Till exempel kommer en markör som `&=Product.Tags` mot en `string[]` som innehåller fyra värden att placera varje värde i sin egen cell, vilket skjuter ut annat mallinnehåll och potentiellt förstör noggrant utformade rapportlayouter.

### **Begränsningar i användningsfall**

Det finns många praktiska scenarier där standardspridningsbeteendet är oönskat:

- **Sammanfattningsrapporter** som behöver en kompakt layout med en rad per post.
- **Tagg-, etikett- eller nyckelordslistor** som behöver visas som kommaseparerade eller pipe-separerade värden i en enda cell.
- **Filterchips eller statusindikatorer** som grupperar flera värden på ett ställe för läsbarhet.
- **Nedströms pipelines** (CSV-export, PDF-rendering, dokumentkoppling) som förväntar sig ett enda konsoliderat värde per cell snarare än ett expanderat intervall.
- **Plattformskompatibilitet**, där vissa konsumenter inte tolererar arrayer som sprider sig över flera celler.

### **Vilket gap det fyller**

Utan en inbyggd mekanism skulle utvecklare tvingas förbehandla data i Python — sammanfoga arrayer till avgränsade strängar innan de binds till arbetsboksdesignern. Detta duplicerar logik, komplicerar datamodeller och ökar risken för fel. Attributen `ArrayAsSingle` och `ExtraDelimiter` eliminerar denna lösning genom att hantera formateringen deklarativt inuti Smart Marker-taggen själv.

## **Funktionsfördelar**

Att använda attributen `ArrayAsSingle` och `ExtraDelimiter` i dina Smart Markers ger flera fördelar:

- **Inneslutning i en cell**: Alla arrayelement renderas i exakt en cell, vilket håller layouter kompakta och förutsägbara.
- **Anpassad avgränsarkontroll**: Ange valfri separatorsträng — komma, semikolon, bindestreck, pipe, nyrad eller annan anpassad text.
- **Malldriven formatering**: Ingen ytterligare kod krävs för att förbehandla datan; formateringsregler finns inuti Smart Marker-taggen.
- **Renare rapporter**: Arraydata skjuter inte längre ut närliggande mallinnehåll till olika rader eller kolumner.
- **Mångsidiga datatyper**: Fungerar med strängar, tal, datum och alla andra datatyper som kan sammanfogas med en avgränsare.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras det ursprungliga spridningsbeteendet, så befintliga mallar fortsätter att fungera oförändrat.

## **Hur man använder denna funktion**

### **Syntax för Smart Marker**

Attributen `ArrayAsSingle` och `ExtraDelimiter` skickas som nyckel-värde-par inom parenteserna i en standard Smart Marker. Den allmänna syntaxen är:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Markören består av följande delar:

- `&=DataSource.ArrayProperty` — den standardiserade Smart Marker som refererar till array-egenskapen på den bundna datakällan.
- `arrayasSingle=true` — instruerar motorn att rendera hela arrayen i en enda cell. Endast värdet `true` utlöser enstaka cell-beteendet.
- `extraDelimiter=", "` — definierar separatorn som placeras mellan arrayelement. Värdet är en strängliteral; det kan vara tomt, ett enskilt tecken eller en flerteckensträng.

{{% alert color="primary" %}}

Attributet `extraDelimiter` accepterar valfri strängliteral, inklusive flerteckenavgränsare, anpassad text eller escape-sekvenser som `\n` för nyradsseparerad utdata. Om arrayen är tom lämnas den resulterande cellen tom.

{{% /alert %}}

### **Steg-för-steg-arbetsflöde**

Följande arbetsflöde beskriver hur man renderar en array i en enda cell med hjälp av Smart Markers.

1. **Förbered datakällan**: Skapa en klass (eller datastruktur) som exponerar en egenskap som returnerar en array. Egenskapen kan returnera `string[]`, `int[]` eller någon annan stödd arraytyp.
2. **Skapa en designarbetsbok**: Skapa en ny `Workbook`, lägg till en rubrikrad och placera en Smart Marker-cell som refererar till array-egenskapen med attributen `arrayasSingle` och `extraDelimiter`.
3. **Instansiera WorkbookDesigner**: Skapa ett `WorkbookDesigner`-objekt, bifoga designarbetsboken till det och bind din datakälla med metoden `set_data_source`.
4. **Bearbeta markörerna**: Anropa metoden `WorkbookDesigner.process()` för att expandera Smart Markers och fylla arbetsboken med riktig data.
5. **Spara resultatet**: Spara den resulterande arbetsboken till disk i XLSX eller något annat stödd filformat.

### **Kodexempel 1 — Grundläggande rendering av strängarray**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

class Product:
    def __init__(self, tags):
        self._tags = tags
    
    def getTags(self):
        return self._tags

product = Product(["C#", "Aspose", "SmartMarker", "Excel"])

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Tags")
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = WorkbookDesigner()
designer.setWorkbook(workbook)
designer.setDataSource("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")

jpype.shutdownJVM()
```

### **Kodexempel 2 — Numerisk array med anpassad avgränsare**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook

# Definiera Student-klass
class Student:
    def __init__(self):
        self.Scores = []

student = Student()
student.Scores = [95, 88, 76, 100, 67]

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Scores")
worksheet.getCells().get("A2").putValue(" - ".join(str(s) for s in student.Scores))

workbook.save("output_numericArray.xlsx")

jpype.shutdownJVM()
```

### **Kodexempel 3 — Jämförelse av standard- kontra ArrayAsSingle-beteende**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

# Definiera datakällan som en ordbok (motsvarande Order-klassen)
order = {"Items": ["Apple", "Banana", "Cherry", "Date"]}

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Sektion 1: Standard Smart Marker - värden sprids horisontellt över celler
cells.get("A1").putValue("Default Spreading Behavior:")
cells.get("A2").putValue("&=Order.Items")

# Sektion 2: Ny enskild cellrendering med arrayasSingle och extraDelimiter
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):")
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")")

# Bind datakällan och bearbeta Smart Markers
designer = WorkbookDesigner(workbook)
designer.setDataSource("Order", order)
designer.process()

# Spara den resulterande arbetsboken
workbook.save("output_comparison.xlsx")

jpype.shutdownJVM()
```

### **Anteckningar och bästa praxis**

Tänk på följande punkter när du arbetar med attributen `ArrayAsSingle` och `ExtraDelimiter`:

- Värdet på `extraDelimiter` behandlas som en strängliteral; escapa alla specialtecken som din mallprocessor kan tolka.
- Attributet `arrayasSingle` accepterar ett boolean-värde (`true` / `false`). Endast `true` utlöser enstaka cell-beteendet; alla andra värden faller tillbaka till standardspridningsbeteendet.
- Om arrayen är tom eller null lämnas cellen tom (eller innehåller en tom sträng beroende på datatypen).
- Funktionen fungerar med objektdatakällor såväl som `DataSet`- och `DataTable`-källor där en kolumn kan delas upp i arrayer.
- För nyradsseparerad utdata kan du använda `\n` eller plattformens nyradskonstant som avgränsat värde.
- Placera Smart Marker i en cell som har tillräcklig bredd för att visa den resulterande sammanfogade strängen; annars kan innehållet visuellt spilla över i intilliggande celler beroende på formatet.

## **Relaterade artiklar**

- [Smart Markers](/cells/sv/python-java/smart-markers/)

{{< app/cells/assistant language="python" >}}