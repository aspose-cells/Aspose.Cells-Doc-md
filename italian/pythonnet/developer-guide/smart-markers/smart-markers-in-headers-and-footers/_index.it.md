---
title: Smart Marker nelle intestazioni e nei piè di pagina | Aspose.Cells for Python via .NET
description: Posizionare segnaposti Smart Marker nelle intestazioni e nei piè di pagina delle pagine con la sintassi a doppio segno di minore e maggiore e l'interruttore WorkbookDesigner.enable_header_footer_markers utilizzando implementazioni personalizzate di ICellsDataTable o sorgenti dati JSON, e collegare immagini tramite data URI, in Aspose.Cells for Python via .NET.
linktitle: Smart Marker per intestazione e piè di pagina | Aspose.Cells
keywords: Aspose.Cells, Smart Marker, intestazioni, piè di pagina, segnaposti intestazione piè di pagina, enable_header_footer_markers, WorkbookDesigner, PageSetup, set_header, set_footer, set_json_data_source, set_data_source, ICellsDataTable, tabella dati personalizzata, associazione dati, immagine, data URI, Aspose.Cells for Python via .NET
type: docs
weight: 196
url: /it/python-net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
Le intestazioni e i piè di pagina delle pagine contengono frequentemente metadati del report, come il titolo del report, il periodo di riferimento, l'autore e il dipartimento. Quando queste informazioni sono già presenti nella sorgente dati utilizzata per popolare la cartella di lavoro, ripeterle manualmente provoca una duplicazione inutile.  
La sintassi classica dei Smart Marker, `&=Source.Field`, viene elaborata nelle celle del corpo del foglio di lavoro. Se si inserisce un marker classico in un'intestazione o in un piè di pagina tramite `page_setup.set_header` o `page_setup.set_footer`, rimane come testo letterale perché le stringhe di intestazione e piè di pagina non fanno parte della griglia di celle scansionata da `workbook_designer.process()`.  
A partire da **Aspose.Cells for Python via .NET 26.11**, l'interruttore `workbook_designer.enable_header_footer_markers`, che è `False` per impostazione predefinita, consente a `process()` di risolvere i segnaposti scritti come `<<Source.Field>>` nelle stringhe di intestazione e piè di pagina — impostalo su `True` prima di chiamare `process()`. I segnaposti di intestazione e piè di pagina utilizzano la stessa sorgente dati dei marker del corpo.  
Ogni intestazione e piè di pagina contiene tre sezioni indirizzabili:
- La sezione `0` è quella sinistra.
- La sezione `1` è quella centrale.
- La sezione `2` è quella destra.  
Utilizza `page_setup.set_header(section, value)` e `page_setup.set_footer(section, value)` per scrivere queste sezioni. Dopo l'elaborazione, usa `page_setup.get_header(section)` e `page_setup.get_footer(section)` per recuperare il testo completato.

{{% alert color="primary" %}}
Un segnaposto come `<<Source.Field>>` inserisce il valore del campo come testo nella stringa della sezione. Le immagini vengono associate mediante il suffisso `(picture)` e un valore data-URI.
{{% /alert %}}

## **Abilitare i segnaposti intestazione/πè di pagina con una tabella dati personalizzata**
Segui la sequenza seguente per risolvere i segnaposti di intestazione e piè di pagina con una sorgente dati tabellare personalizzata in **Aspose.Cells for Python via .NET 26.11**:
1. Crea un `Workbook` e ottieni il suo primo `Worksheet` all'indice `0`.
2. Scrivi i segnaposti `<<Source.Field>>` nelle sezioni di intestazione e piè di pagina desiderate con `page_setup.set_header` e `page_setup.set_footer`.
3. Definisci una piccola classe che implementa `ICellsDataTable` per esporre i dati tabellari — i nomi delle colonne, il conteggio delle righe e un cursore con `before_first()`, `next()` e l'indicizzatore `__getitem__` — e utilizza un nome sorgente che corrisponda al prefisso usato nei segnaposti. Per esempio, una sorgente chiamata `node` supporta segnaposti come `<<node.Name>>`. Una semplice classe Python o un elenco di dizionari **non** viene collegato su questa piattaforma; l'implementazione di `ICellsDataTable` è la sorgente dati personalizzata.
4. Crea un `WorkbookDesigner` per la cartella di lavoro.
5. Imposta `designer.enable_header_footer_markers` su `True` prima dell'elaborazione.
6. Associa la tabella e il nome della sorgente con `designer.set_data_source("node", table)`.
7. Chiama `designer.process()`.
8. Dopo l'elaborazione, i segnaposti non sono più presenti nel testo dell'intestazione o del piè di pagina. Usa `get_header` e `get_footer` per recuperare le stringhe delle sezioni completate.

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

## **Utilizzare una sorgente dati JSON**
È possibile impiegare JSON al posto di un `ICellsDataTable` personalizzato quando i dati del report sono già disponibili in formato JSON. Chiama `workbook_designer.set_json_data_source(name, json)` per collegare la sorgente.  
L'argomento `name` ha lo stesso ruolo del nome sorgente usato con i dati tabellari. Per esempio, il nome `node` supporta segnaposti come `<<node.Company>>` e `<<node.Title>>`.  
Passa i dati di riga direttamente a `set_json_data_source`:
- È supportato un array di righe, cioè un array JSON contenente uno o più oggetti riga.
- È possibile passare direttamente un singolo oggetto riga.
- Non avvolgere le righe sotto una chiave di livello superiore denominata, ad esempio `{"rows":[...]}`. Questo involucro non corrisponde alla struttura di input orientata alle righe prevista per questo flusso di lavoro.  
Una singola sorgente JSON può alimentare entrambi gli stili di marker durante la stessa chiamata a `process()`. Può risolvere un marker classico `&=` in una cella del corpo del foglio e segnaposti a doppio segno di minore e maggiore `<<>>` nelle sezioni di intestazione e piè di pagina. È comunque necessario abilitare `enable_header_footer_markers` affinché i segnaposti di intestazione e piè di pagina vengano risolti.

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

## **Semantica dell'interruttore e della sorgente multi-riga**
`enable_header_footer_markers` è `False` per impostazione predefinita e l'interruttore controlla solo i segnaposti `<<Source.Field>>` di intestazione e piè di pagina. Quando l'interruttore è disattivato, `process()` risolve comunque i marker classici `&=` nel corpo, ma un segnaposto `<<Source.Field>>` in un'intestazione o in un piè di pagina rimane testo letterale.  
Una sezione di intestazione o piè di pagina è una singola stringa, non una banda ripetuta. Se la sorgente dati contiene più righe, la prima riga fornisce i valori di intestazione e piè di pagina. Una volta risolti, i valori diventano testo ordinario di intestazione o piè di pagina. Rimangono nella cartella di lavoro dopo la chiamata a `save` e sono presenti quando si carica nuovamente la cartella di lavoro salvata.  
L'esempio seguente crea due cartelle di lavoro sulla stessa sorgente dati tabellare multi-riga per confrontare il comportamento con l'interruttore disattivato e attivato. Il `plain_designer` lascia il segnaposto invariato, mentre il `enabled_designer` lo risolve usando la prima riga.

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

## **Associa un'immagine a un'intestazione o a un piè di pagina**
Il suffisso `(picture)` associa un'immagine a una sezione di intestazione o di piè di pagina. Scrivi `<<node.logo(picture)>>` dove desideri che appaia l'immagine e fornisci il valore del campo come data URI — il prefisso `data:image/png;base64,` seguito dal testo Base64 dei byte dell'immagine. Una stringa Base64 senza il prefisso `data:` non incorpora l'immagine.  
Dopo `process()`:
1. Il segnaposto viene sostituito da `&G`, il codice standard per immagini di intestazione e piè di pagina. Poiché il marker diventa un codice all'interno della stringa della sezione, può convivere con testo più lungo, ad esempio `Logo: <<node.logo(picture)>>`.
2. I byte dell'immagine vengono incorporati nella cartella di lavoro come parte multimediale allegata al livello di disegno intestazione/piè di pagina di quel foglio, quindi l'immagine viene stampata insieme all'intestazione o al piè di pagina.

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

Il codice `&G` stampato è il codice immagine che Excel interpreta durante il rendering dell'intestazione — i byte di `logo.png` ora vivono all'interno di `HeaderFooterPicture.xlsx`, e l'immagine viene stampata al posto del codice.  
Per utilizzare i Smart Marker nelle intestazioni e nei piè di pagina, scrivi segnaposti `<<Source.Field>>` nelle sezioni sinistra, centrale e destra con `set_header` e `set_footer`. Imposta `enable_header_footer_markers` su `True` sul `WorkbookDesigner` prima di chiamare `process()`, e fornisci i valori tramite `set_data_source("node", table)` con un'implementazione personalizzata di `ICellsDataTable` o `set_json_data_source(name, json)`. Leggi le sezioni completate con `get_header` e `get_footer`. La stessa sorgente dati può alimentare sia i marker del corpo sia i segnaposti di intestazione o piè di pagina in un unico passaggio di elaborazione. Aggiungi il suffisso `(picture)` con un valore data-URI per associare un'immagine a una sezione.

## Articoli correlati
- [Rendering di Array a Singola Cella SmartMarker](/cells/it/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python-net" >}}