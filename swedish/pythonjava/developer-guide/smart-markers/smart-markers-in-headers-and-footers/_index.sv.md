---
title: Smart Markörer i sidhuvuden och sidfötter | Aspose.Cells for Python via Java
linktitle: Smartmarkörer i sidhuvud och sidfot | Aspose.Cells
description: Placera Smart Marker-platshållare i sidhuvuden och sidfötter med dubbelvinkel-klammer-syntax och WorkbookDesigner.setEnableHeaderFooterMarkers-växeln genom att använda tabellbaserade rad- eller JSON-datakällor, samt binda bilder via data-URI-er, i Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Aspose.Cells for Python via Java, Smart Markörer, sidhuvuden, sidfötter, sidhuvud- och sidfot-markörer, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, ICellsDataTable, anpassad datatabell, databindning, bild, data URI, Python via Java
type: docs
weight: 196
url: /sv/python-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Sidhuvuden och sidfötter innehåller ofta rapportmetadata såsom rapporttitel, rapportperiod, författare och avdelning. När denna information redan finns i datakällan som används för att fylla arbetsboken, skapar manuell upprepning onödig duplicering.  
Klassisk Smart Marker-syntax, `&=Source.Field`, bearbetas i kalkylbladets cellinnehåll. Om du placerar en klassisk markör i ett sidhuvud eller en sidfot via `PageSetup.setHeader` eller `PageSetup.setFooter`, förblir den bokstavlig text eftersom sidhuvuds- och sidfotssträngar inte är en del av kalkylbladets cellnät som skannas av `WorkbookDesigner.process()`.  
Från och med **Aspose.Cells for Python via Java 26.11**, gör växeln `WorkbookDesigner.setEnableHeaderFooterMarkers`, som är `False` som standard, så att `process()` löser platshållare skrivna som `<<Source.Field>>` i sidhuvuds- och sidfotsektionernas strängar — sätt den till `True` innan du anropar `process()`. Platshållare i sidhuvud och sidfot använder samma datakälla som markörer i kroppen.  
Varje sidhuvud och sidfot innehåller tre adresserbara sektioner:
- Section `0` är den vänstra sektionen.
- Section `1` är den centrala sektionen.
- Section `2` är den högra sektionen.  
Använd `PageSetup.setHeader(int section, str value)` och `PageSetup.setFooter(int section, str value)` för att skriva dessa sektioner. Efter bearbetning, använd `PageSetup.getHeader(int section)` och `PageSetup.getFooter(int section)` för att hämta den färdiga texten.

{{% alert color="primary" %}}
En platshållare som `<<Source.Field>>` infogar fältvärdet som text i sektionens sträng. Bilder bindas med suffixet `(picture)` och ett data-URI-värde.
{{% /alert %}}

## **Aktivera sidhuvud/sidfot-markörer med en anpassad datatabell**
1. Skapa ett `Workbook` och hämta dess första `Worksheet` på index `0` med `workbook.getWorksheets().get(0)`.  
2. Skriv `<<Source.Field>>`-platshållare i önskade sidhuvuds- och sidfotsektioner med `worksheet.getPageSetup().setHeader(section, value)` och `worksheet.getPageSetup().setFooter(section, value)`.  
3. Definiera en liten klass som implementerar `ICellsDataTable` för att exponera den tabellbaserade raddatan — kolumnnamnen, antalet rader och en markör med `beforeFirst()`, `next()` och `get()` — och använd ett källnamn som matchar källprefixet som används av platshållarna. Till exempel, en källa med namn `node` stödjer platshållare som `<<node.Name>>`. En vanlig Python-klass eller en lista med ordböcker bindas INTE på denna plattform; `ICellsDataTable`-implementeringen är den anpassade objekt-datakällan.  
4. Skapa en `WorkbookDesigner` för arbetsboken.  
5. Anropa `designer.setEnableHeaderFooterMarkers(True)` innan bearbetning.  
6. Fäst tabellen och källnamnet med `designer.setDataSource("node", table)`.  
7. Anropa `designer.process()`.  
8. Efter bearbetning finns inte platshållarna längre i sidhuvuds- eller sidfotstexten. Använd `worksheet.getPageSetup().getHeader(section)` och `worksheet.getPageSetup().getFooter(section)` för att hämta de färdiga sektionernas strängar.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name", "Author"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>")
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
print("Footer: " + worksheet.getPageSetup().getFooter(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
jpype.shutdownJVM()
```

## **Använd en JSON-datakälla**
Du kan använda JSON istället för en anpassad `ICellsDataTable` när rapportdata redan finns i JSON-format. Anropa `designer.setJsonDataSource(name, json)` för att fästa källan.  
`name`-argumentet har samma funktion som källnamnet som används med tabellbaserade data. Till exempel, namnet `node` stödjer platshållare som `<<node.Company>>` och `<<node.Title>>`.  
Skicka raddata direkt till `setJsonDataSource`:
- En radarray, såsom en JSON-array som innehåller en eller flera radobjekt, stöds.  
- Ett enstaka radobjekt kan också skickas direkt.  
- Packa inte in raderna under en namngiven toppnivå-nyckel som `{"rows":[...]}`. Detta omslag är inte den förväntade radorienterade inmatningsformen för detta arbetsflöde.  

En JSON-källa kan fylla båda markörstilarna under samma `process()`-anrop. Den kan lösa en klassisk `&=`-markör i en kalkylbladscell och dubbelvinkel-klammer-platshållare `<<>>` i sidhuvuds- och sidfotsektioner. Du måste fortfarande aktivera `setEnableHeaderFooterMarkers` för att platshållarna i sidhuvud och sidfot ska lösas.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>")
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>")
worksheet.getCells().get("A1").putValue("&=node.Company")
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setJsonDataSource(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.getPageSetup().getHeader(0))
print("Right: " + worksheet.getPageSetup().getHeader(2))
print("Body: " + worksheet.getCells().get("A1").getStringValue())
workbook.save("HeaderFooterJsonMarkers.xlsx")
jpype.shutdownJVM()
```

## **Växel- och flerradsskälla-semantik**
Inställningen för sidhuvuds- och sidfot-markörer är `False` som standard, och `designer.setEnableHeaderFooterMarkers(True)` styr endast `<<Source.Field>>`-platshållarna i sidhuvud och sidfot. När växeln är avstängd löser `process()` fortfarande klassiska `&=`-kroppsmarkörer, men en `<<Source.Field>>`-platshållare i ett sidhuvud eller en sidfot förblir bokstavlig text.  
En sidhuvuds- eller sidfot-sektion är en enda sträng, inte ett upprepande band. Om datakällan innehåller flera rader, ger den första raden värden för sidhuvud och sidfot. När de har lösts blir värdena vanlig sidhuvuds- eller sidfotstext. De kvarstår i arbetsboken efter att du anropar `workbook.save(...)` och är närvarande när du laddar den sparade arbetsboken igen.  

Följande exempel skapar två arbetsböcker med samma flerradiga tabellbaserade datakälla för att jämföra det inaktiverade och det aktiverade beteendet. `plainDesigner` lämnar platshållaren oförändrad, medan `enabledDesigner` löser den med den första raden.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
table = NodeTable([
    ("First Row",),
    ("Second Row",),
])
# Without the switch the placeholder stays literal text
plain_workbook = Workbook()
plain_sheet = plain_workbook.getWorksheets().get(0)
plain_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
plain_designer = WorkbookDesigner(plain_workbook)
plain_designer.setDataSource("node", table)
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = Workbook()
enabled_sheet = enabled_workbook.getWorksheets().get(0)
enabled_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
enabled_designer = WorkbookDesigner(enabled_workbook)
enabled_designer.setEnableHeaderFooterMarkers(True)
enabled_designer.setDataSource("node", table)
enabled_designer.process()
print("Without switch: " + plain_sheet.getPageSetup().getHeader(1))
print("With switch: " + enabled_sheet.getPageSetup().getHeader(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
jpype.shutdownJVM()
```

## **Binda en bild i ett sidhuvud eller en sidfot**
`(picture)`-suffixet binder en bild i en sidhuvuds- eller sidfotssektion. Skriv `<<node.logo(picture)>>` där bilden ska visas, och ange fältvärdet som en data-URI — prefixet `data:image/png;base64,` följt av Base64-texten för bildbytes. Den avkodade bilden hanteras som en `byte[]`-array. En ren Base64-sträng utan `data:`-prefixet bäddar inte in en bild.  

Efter `process()`:
1. Platshållaren ersätts med `&G`, den standardiserade sidhuvuds- och sidfot-bildkoden. Eftersom markören blir kod i sektionens sträng kan den ligga i längre text såsom `Logo: <<node.logo(picture)>>`.  
2. Bildbytet bäddas in i arbetsboken som en mediedel kopplad till sidhuvud/sidfot-ritningslagret i det kalkylbladet, så bilden skrivs ut med sidhuvudet eller sidfoten.

```python
import base64
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["logo"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    image_bytes = image_file.read()
logo_data = "data:image/png;base64," + base64.b64encode(image_bytes).decode("ascii")
table = NodeTable([(logo_data,)])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
jpype.shutdownJVM()
```

Den utskrivna `&G` är bildkoden som Excel tolkar när sidhuvudet renderas — `logo.png`-bytesen finns nu i `HeaderFooterPicture.xlsx`, och bilden skrivs ut i stället för koden.  
För att använda Smart Markörer i sidhuvud och sidfot, skriv `<<Source.Field>>`-platshållare i den vänstra, centrala och högra sidhuvuds- eller sidfotsektionen med `setHeader` och `setFooter`. Anropa `designer.setEnableHeaderFooterMarkers(True)` innan du anropar `process()`, och leverera värden antingen via `designer.setDataSource("node", table)` med en anpassad `ICellsDataTable`-implementation eller `designer.setJsonDataSource(name, json)`. Läs de färdiga sektionerna med `getHeader` och `getFooter`. Samma datakälla kan fylla både kroppsmärkare och sidhuvud- eller sidfot-platshållare i ett bearbetningspass. Lägg till `(picture)`-suffixet med ett data-URI-värde för att binda en bild i en sektion.

## Relaterade artiklar
- [SmartMarker enkel cellarray-rendering](/cells/sv/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python" >}}