---
title: Smart Markers i sidhuvuden och sidfötter | Aspose.Cells for Python via .NET
linktitle: Smartmarkörer i sidhuvud och sidfot | Aspose.Cells
description: Placera Smart Marker-platshållare i sidhuvuden och sidfötter med dubbelvinkel-bracket-syntax och WorkbookDesigner.enable_header_footer_markers-växeln med hjälp av anpassade ICellsDataTable-implementationer eller JSON-datakällor, samt binda bilder via data-URI, i Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, Smart Markörer, sidhuvuden, sidfötter, sidhuvud-sidfot-markörer, enable_header_footer_markers, WorkbookDesigner, PageSetup, set_header, set_footer, set_json_data_source, set_data_source, ICellsDataTable, anpassad datatabell, databindning, bild, data URI, Aspose.Cells for Python via .NET
type: docs
weight: 196
url: /sv/python-net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
Sidhuvuden och sidfötter innehåller ofta rapportmetadata som rapporttitel, rapportperiod, författare och avdelning. När denna information redan finns i datakällan som används för att fylla arbetsboken, skapar manuell upprepning onödig duplicering.  
Klassisk Smart Marker-syntax, `&=Source.Field`, bearbetas i kalkylbladets celler i kroppen. Om du placerar en klassisk markör i ett sidhuvud eller en sidfot via `page_setup.set_header` eller `page_setup.set_footer`, förblir den bokstavlig text eftersom sidhuvuds- och sidfotsträngar inte är en del av kalkylblads-cellerna som skannas av `workbook_designer.process()`.  
Från och med **Aspose.Cells for Python via .NET 26.11** finns växeln `workbook_designer.enable_header_footer_markers`, som är `False` som standard, och som får `process()` att lösa platshållare skrivna som `<<Source.Field>>` i sidhuvuds- och sidfotsektioners strängar — sätt den till `True` innan du anropar `process()`. Platshållare i sidhuvud och sidfot använder samma datakälla som markörer i kroppen.  
Varje sidhuvud och varje sidfot innehåller tre adresserbara sektioner:
- Sektion `0` är den vänstra sektionen.
- Sektion `1` är den centrala sektionen.
- Sektion `2` är den högra sektionen.
Använd `page_setup.set_header(section, value)` och `page_setup.set_footer(section, value)` för att skriva dessa sektioner. Efter bearbetning, använd `page_setup.get_header(section)` och `page_setup.get_footer(section)` för att hämta den färdiga texten.

{{% alert color="primary" %}}
En platshållare som `<<Source.Field>>` infogar fältvärdet som text i sektionens sträng. Bilder bindas med suffixet `(picture)` och ett data-URI-värde.
{{% /alert %}}

## **Aktivera sidhuvud-/sidfot-markörer med en anpassad datatabell**
Använd följande sekvens för att lösa platshållare i sidhuvud och sidfot med en anpassad tabellbaserad datakälla i **Aspose.Cells for Python via .NET 26.11**:
1. Skapa en `Workbook` och hämta dess första `Worksheet` på index `0`.
2. Skriv `<<Source.Field>>`-platshållare i önskade sidhuvuds- och sidfot-sektioner med `page_setup.set_header` och `page_setup.set_footer`.
3. Definiera en liten klass som implementerar `ICellsDataTable` för att exponera raddata i tabellformat — kolumnnamnen, antalet rader och en markör med `before_first()`, `next()` och indexeraren `__getitem__` — och använd ett källnamn som matchar prefikset som används i platshållarna. Till exempel, en källa med namn `node` understöder platshållare som `<<node.Name>>`. En vanlig Python-klass eller en lista med ordböcker bindas INTE på denna plattform; `ICellsDataTable`-implementationen är den anpassade objekt-datakällan.
4. Skapa en `WorkbookDesigner` för arbetsboken.
5. Ställ in `designer.enable_header_footer_markers` till `True` innan bearbetning.
6. Koppla tabellen och källnamnet med `designer.set_data_source("node", table)`.
7. Anropa `designer.process()`.
8. Efter bearbetning finns platshållarna inte längre i sidhuvuds- eller sidfot-texten. Använd `get_header` och `get_footer` för att hämta de färdiga sektionsträngarna.

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name", "Author"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.page_setup.set_header(1, "Quarterly Report - <<node.Name>>")
worksheet.page_setup.set_footer(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
print("Footer: " + worksheet.page_setup.get_footer(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
```

## **Använd en JSON-datakälla**
Du kan använda JSON istället för en anpassad `ICellsDataTable` när rapportdata redan finns i JSON-format. Anropa `workbook_designer.set_json_data_source(name, json)` för att fästa källan.  
`name`-argumentet har samma funktion som källnamnet som används med tabell-data. Till exempel, namnet `node` understöder platshållare som `<<node.Company>>` och `<<node.Title>>`.  
Passa raddata direkt till `set_json_data_source`:
- En radarray, såsom en JSON-array som innehåller ett eller flera radobjekt, stöds.
- Ett enskilt radobjekt kan också passeras direkt.
- Wrapa inte raderna under en namngiven top-nivå-nyckel såsom `{"rows":[...]}`. Denna omslag är inte det förväntade rad-orienterade inmatningsformatet för detta arbetsflöde.  
En JSON-källa kan fylla båda markörstilarna under samma `process()`-anrop. Den kan lösa en klassisk `&=`-markör i en kalkylblads-cell i kroppen och dubbelvinkel-bracket-platshållare `<<>>` i sidhuvuds- och sidfot-sektioner. Du måste fortfarande aktivera `enable_header_footer_markers` för att platshållarna i sidhuvud och sidfot ska lösas.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.page_setup.set_header(0, "<<node.Company>>")
worksheet.page_setup.set_header(2, "Page <<node.Title>>")
worksheet.cells.get("A1").put_value("&=node.Company")
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_json_data_source(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.page_setup.get_header(0))
print("Right: " + worksheet.page_setup.get_header(2))
print("Body: " + worksheet.cells.get("A1").string_value)
# This prints:
# Left: Aspose Pty Ltd
# Right: Page Half-Year Report
# Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx")
```

## **Växel- och flerradskäll-semantik**
`enable_header_footer_markers` är `False` som standard, och växeln styr endast platshållarna `<<Source.Field>>` i sidhuvud och sidfot. När växeln är avstängd löser `process()` fortfarande klassiska `&=`-markörer i kroppen, men en `<<Source.Field>>`-platshållare i ett sidhuvud eller en sidfot förblir bokstavlig text.  
En sidhuvuds- eller sidfot-sektion är en enda sträng, inte ett repeterande band. Om datakällan innehåller flera rader, levererar den första raden värdena för sidhuvud och sidfot. När de har lösts blir värdena vanlig text i sidhuvud eller sidfot. De finns kvar i arbetsboken efter att du anropar `save` och är närvarande när du laddar den sparade arbetsboken igen.  
Följande exempel skapar två arbetsböcker med samma flerradiga tabell-datakälla för att kontrastera det inaktiverade och det aktiverade beteendet. `plain_designer` lämnar platshållaren oförändrad, medan `enabled_designer` löser den med den första raden.

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
rows = [("First Row",), ("Second Row",)]
# Without the switch the placeholder stays literal text
plain_workbook = ac.Workbook()
plain_sheet = plain_workbook.worksheets[0]
plain_sheet.page_setup.set_header(1, "<<node.Name>>")
plain_designer = ac.WorkbookDesigner(plain_workbook)
plain_designer.set_data_source("node", NodeTable(rows))
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = ac.Workbook()
enabled_sheet = enabled_workbook.worksheets[0]
enabled_sheet.page_setup.set_header(1, "<<node.Name>>")
enabled_designer = ac.WorkbookDesigner(enabled_workbook)
enabled_designer.enable_header_footer_markers = True
enabled_designer.set_data_source("node", NodeTable(rows))
enabled_designer.process()
print("Without switch: " + plain_sheet.page_setup.get_header(1))
print("With switch: " + enabled_sheet.page_setup.get_header(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
```

## **Binda en bild i ett sidhuvud eller en sidfot**
Suffixet `(picture)` binder en bild i en sidhuvuds- eller sidfot-sektion. Skriv `<<node.logo(picture)>>` där bilden ska visas, och leverera fältvärdet som en data-URI — prefixet `data:image/png;base64,` följt av Base64-texten för bildens byte. En ren Base64-sträng utan `data:`-prefixet bäddar inte in en bild.  
Efter `process()`:
1. Platshållaren ersätts med `&G`, den standardiserade bildkoden för sidhuvud och sidfot. Eftersom markören blir en kod i sektionens sträng kan den placeras i längre text som `Logo: <<node.logo(picture)>>`.
2. Bildbytena bäddas in i arbetsboken som en mediadel som är bifogad till ritlagret för sidhuvud/sidfot i det kalkylbladet, så bilden skrivs ut tillsammans med sidhuvudet eller sidfoten.

```python
import aspose.cells as ac
import base64
class LogoTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["logo"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.page_setup.set_header(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    logo_data_uri = "data:image/png;base64," + base64.b64encode(image_file.read()).decode("ascii")
table = LogoTable([(logo_data_uri,)])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
```

Den utskrivna `&G` är bildkoden som Excel tolkar när den renderar sidhuvudet — `logo.png`-bytterna finns nu i `HeaderFooterPicture.xlsx`, och bilden skrivs ut i stället för koden.  
För att använda Smart Markers i sidhuvud och sidfot, skriv `<<Source.Field>>`-platshållare i vänstra, centrala och högra sektionerna för sidhuvud eller sidfot med `set_header` och `set_footer`. Sätt `enable_header_footer_markers` till `True` på `WorkbookDesigner` innan du anropar `process()`, och leverera värden via `set_data_source("node", table)` med en anpassad `ICellsDataTable`-implementation eller `set_json_data_source(name, json)`. Läs de färdiga sektionerna med `get_header` och `get_footer`. Samma datakälla kan fylla både kroppens markörer och platshållare i sidhuvud eller sidfot i ett och samma bearbetningssteg. Lägg till suffixet `(picture)` med ett data-URI-värde för att binda en bild i en sektion.

## Relaterade artiklar
- [SmartMarker Rendering av enskild cellarray](/cells/sv/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python-net" >}}