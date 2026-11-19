---
title: Smart Marker nelle intestazioni e nei piè di pagina | Aspose.Cells for Python via Java
description: Inserire segnaposto Smart Marker nelle intestazioni e nei piè di pagina delle pagine con la sintassi a doppio segno angolare e l'interruttore WorkbookDesigner.setEnableHeaderFooterMarkers usando fonti dati tabulari a riga o JSON, e associare immagini tramite URI dati, in Aspose.Cells for Python via Java.
linktitle: Smart Marker intestazione e piè di pagina | Aspose.Cells
keywords: Aspose.Cells, Aspose.Cells for Python via Java, Smart Marker, intestazioni, piè di pagina, marcatori intestazione piè di pagina, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, ICellsDataTable, tabella dati personalizzata, associazione dati, immagine, URI dati, Python via Java
type: docs
weight: 196
url: /it/python-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scenari di utilizzo possibili**
Le intestazioni e i piè di pagina di una pagina contengono comunemente i metadati di un report, come il titolo del report, il periodo di riferimento, l'autore e il dipartimento. Quando queste informazioni esistono già nella fonte dati usata per popolare il Workbook, ripeterle manualmente crea duplicazioni inutili.  
La sintassi classica di Smart Marker, `&=Source.Field`, viene elaborata nelle celle del corpo del Worksheet. Se si inserisce un marcatore classico in un'intestazione o in un piè di pagina tramite `PageSetup.setHeader` o `PageSetup.setFooter`, rimane testo letterale poiché le stringhe di intestazione e piè di pagina non fanno parte della griglia delle celle del Worksheet scansionata da `WorkbookDesigner.process()`.  
A partire da **Aspose.Cells for Python via Java 26.11**, l'interruttore `WorkbookDesigner.setEnableHeaderFooterMarkers`, che è `False` per impostazione predefinita, fa sì che `process()` risolva i segnaposto scritti come `<<Source.Field>>` nelle stringhe delle sezioni di intestazione e piè di pagina — impostalo su `True` prima di chiamare `process()`. I segnaposto di intestazione e piè di pagina utilizzano la stessa fonte dati dei marcatori nel corpo.  
Ogni intestazione e piè di pagina contiene tre sezioni indirizzabili:
- La sezione `0` è quella sinistra.
- La sezione `1` è quella centrale.
- La sezione `2` è quella destra.  
Usa `PageSetup.setHeader(int section, str value)` e `PageSetup.setFooter(int section, str value)` per scrivere queste sezioni. Dopo l'elaborazione, usa `PageSetup.getHeader(int section)` e `PageSetup.getFooter(int section)` per recuperare il testo completato.

{{% alert color="primary" %}}
Un segnaposto come `<<Source.Field>>` inserisce il valore del campo come testo nella stringa della sezione. Le immagini vengono associate con il suffisso `(picture)` e un valore URI dati.  
{{% /alert %}}

## **Abilitare i segnaposto intestazione/piè di pagina con una tabella dati personalizzata**
Utilizza la seguente sequenza per risolvere i segnaposto di intestazione e piè di pagina con una fonte dati tabulare personalizzata in **Aspose.Cells for Python via Java 26.11**:
1. Crea un `Workbook` e ottieni il suo primo `Worksheet` all'indice `0` mediante `workbook.getWorksheets().get(0)`.
2. Scrivi i segnaposto `<<Source.Field>>` nelle sezioni desiderate di intestazione e piè di pagina con `worksheet.getPageSetup().setHeader(section, value)` e `worksheet.getPageSetup().setFooter(section, value)`.
3. Definisci una piccola classe che implementa `ICellsDataTable` per esporre i dati tabulari della riga — i nomi delle colonne, il conteggio delle righe e un cursore con `beforeFirst()`, `next()` e `get()` — e utilizza un nome di fonte che corrisponda al prefisso usato nei segnaposto. Per esempio, una fonte denominata `node` supporta segnaposto come `<<node.Name>>`. Una semplice classe Python o un elenco di dizionari **non** si collega su questa piattaforma; l'implementazione `ICellsDataTable` è la fonte dati personalizzata.
4. Crea un `WorkbookDesigner` per il workbook.
5. Chiama `designer.setEnableHeaderFooterMarkers(True)` prima dell'elaborazione.
6. Associa la tabella e il nome della fonte con `designer.setDataSource("node", table)`.
7. Chiama `designer.process()`.
8. Dopo l'elaborazione, i segnaposto non sono più presenti nel testo di intestazione o piè di pagina. Usa `worksheet.getPageSetup().getHeader(section)` e `worksheet.getPageSetup().getFooter(section)` per recuperare le stringhe delle sezioni completate.

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

## **Utilizzare una fonte dati JSON**
È possibile usare JSON al posto di un `ICellsDataTable` personalizzato quando i dati del report sono già disponibili in formato JSON. Chiama `designer.setJsonDataSource(name, json)` per associare la fonte.  
Il parametro `name` svolge lo stesso ruolo del nome della fonte usato con i dati tabulari. Per esempio, il nome `node` supporta segnaposto come `<<node.Company>>` e `<<node.Title>>`.  
Passa i dati delle righe direttamente a `setJsonDataSource`:
- È supportato un array di righe, ad esempio un array JSON contenente uno o più oggetti riga.
- È possibile passare direttamente anche un singolo oggetto riga.
- Non avvolgere le righe sotto una chiave di livello superiore denominata, tipo `{"rows":[...]}`. Questo involucro non corrisponde alla forma di input orientata alle righe prevista per questo flusso di lavoro.  
Una singola fonte JSON può popolare entrambi gli stili di segnaposto durante la stessa chiamata a `process()`. Può risolvere un marcatore classico `&=` in una cella del corpo del Worksheet e segnaposto `<<>>` nelle sezioni di intestazione e piè di pagina. È comunque necessario abilitare `setEnableHeaderFooterMarkers` affinché i segnaposto di intestazione e piè di pagina vengano risolti.

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

## **Semantica dell’interruttore e della fonte multi-riga**
L’impostazione dei segnaposto di intestazione e piè di pagina è `False` per impostazione predefinita, e `designer.setEnableHeaderFooterMarkers(True)` controlla solo i segnaposto `<<Source.Field>>` di intestazione e piè di pagina. Quando l’interruttore è disattivato, `process()` risolve comunque i marcatori classici `&=` nel corpo, ma un segnaposto `<<Source.Field>>` in un’intestazione o in un piè di pagina rimane testo letterale.  
Una sezione di intestazione o piè di pagina è una singola stringa, non una banda ripetibile. Se la fonte dati contiene più righe, la prima riga fornisce i valori di intestazione e piè di pagina. Una volta risolti, i valori diventano testo ordinario di intestazione o piè di pagina. Rimangono nel workbook dopo aver chiamato `workbook.save(...)` e sono presenti quando si ricarica nuovamente il workbook salvato.  
L’esempio seguente crea due workbook sulla stessa fonte dati tabulare multi-riga per confrontare il comportamento disattivato e quello attivato. Il `plainDesigner` lascia il segnaposto invariato, mentre il `enabledDesigner` lo risolve usando la prima riga.

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

## **Associa un’immagine a un’intestazione o a un piè di pagina**
Il suffisso `(picture)` associa un’immagine a una sezione di intestazione o piè di pagina. Scrivi `<<node.logo(picture)>>` nel punto in cui l’immagine deve apparire e fornisci il valore del campo come URI dati — il prefisso `data:image/png;base64,` seguito dal testo Base64 dei byte dell’immagine. L’immagine decodificata viene gestita come un array `byte[]`. Una stringa Base64 senza il prefisso `data:` non incorpora un’immagine.  
Dopo `process()`:
1. Il segnaposto viene sostituito da `&G`, il codice standard per immagine di intestazione e piè di pagina. Poiché il marcatore diventa un codice all’interno della stringa della sezione, può trovarsi in testi più lunghi, ad es. `Logo: <<node.logo(picture)>>`.
2. I byte dell’immagine sono incorporati nel workbook come parte multimediale allegata al livello di disegno intestazione/πè di pagina di quel Worksheet, così l’immagine viene stampata con l’intestazione o il piè di pagina.

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

Il `&G` stampato è il codice immagine che Excel interpreta durante il rendering dell’intestazione — i byte di `logo.png` ora vivono all’interno di `HeaderFooterPicture.xlsx`, e l’immagine stampa al posto del codice.  
Per utilizzare i Smart Marker in intestazione e piè di pagina, scrivi segnaposto `<<Source.Field>>` nelle sezioni sinistra, centrale e destra con `setHeader` e `setFooter`. Chiama `designer.setEnableHeaderFooterMarkers(True)` prima di `process()`, e fornisci i valori tramite `designer.setDataSource("node", table)` con un’implementazione `ICellsDataTable` personalizzata o `designer.setJsonDataSource(name, json)`. Leggi le sezioni completate con `getHeader` e `getFooter`. La stessa fonte dati può popolare sia i marcatori del corpo sia i segnaposto di intestazione o piè di pagina in un unico passaggio di elaborazione. Aggiungi il suffisso `(picture)` con un valore URI dati per associare un’immagine a una sezione.

## Articoli correlati
- [Rendering di Array a Cella Singola con SmartMarker](/cells/it/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python" >}}