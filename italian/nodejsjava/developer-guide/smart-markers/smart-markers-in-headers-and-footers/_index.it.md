---
title: Smart Marker nelle intestazioni e nei piè di pagina | Aspose.Cells for Node.js via Java
description: Inserisci segnaposto Smart Marker nelle intestazioni e nei piè di pagina delle pagine con sintassi a doppia parentesi angolare e l'interruttore WorkbookDesigner.setEnableHeaderFooterMarkers usando fonti dati JSON, e associa immagini tramite URI dati, in Aspose.Cells for Node.js via Java.
linktitle: Smart Marker per intestazioni e piè di pagina | Aspose.Cells for Node.js via Java
keywords: Aspose.Cells for Node.js via Java, Smart Marker, intestazioni, piè di pagina, segnaposto intestazione piè di pagina, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, righe JSON, associazione dei dati, immagine, URI dati, JavaScript
type: docs
weight: 196
url: /it/nodejs-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
Le intestazioni e i piè di pagina delle pagine contengono comunemente metadati del report, come il titolo del report, il periodo di riferimento, l'autore e il dipartimento. Quando queste informazioni sono già presenti nella fonte dati utilizzata per popolare la cartella di lavoro, ripeterle manualmente crea duplicazioni non necessarie.  
La sintassi classica di Smart Marker, `&=Source.Field`, viene elaborata nelle celle del corpo del foglio di lavoro. Se si inserisce un marcatore classico in un'intestazione o in un piè di pagina tramite `PageSetup.setHeader` o `PageSetup.setFooter`, rimane testo letterale perché le stringhe di intestazione e piè di pagina non fanno parte della griglia di celle del foglio di lavoro scansionata da `WorkbookDesigner.process()`.  
A partire da **Aspose.Cells for Node.js via Java 26.11**, l'impostazione `WorkbookDesigner.setEnableHeaderFooterMarkers`, che è `false` per impostazione predefinita, fa sì che `process()` risolva i segnaposto scritti come `<<Source.Field>>` nelle stringhe delle sezioni di intestazione e piè di pagina. Chiamare `designer.setEnableHeaderFooterMarkers(true)` prima di chiamare `process()`. I segnaposto di intestazione e piè di pagina utilizzano la stessa fonte dati dei marcatori del corpo.  
Ogni intestazione e piè di pagina contiene tre sezioni indirizzabili:
- La sezione `0` è la sezione sinistra.  
- La sezione `1` è la sezione centrale.  
- La sezione `2` è la sezione destra.  
Usa `PageSetup.setHeader(int section, String value)` e `PageSetup.setFooter(int section, String value)` per scrivere queste sezioni. Dopo l'elaborazione, utilizza `PageSetup.getHeader(int section)` e `PageSetup.getFooter(int section)` per recuperare il testo completato.

{{% alert color="primary" %}}
Un segnaposto come `<<Source.Field>>` inserisce il valore del campo come testo nella stringa della sezione. Le immagini vengono associate con il suffisso `(picture)` e un valore URI dati.
{{% /alert %}}

## **Abilitare i segnaposto intestazione/piè di pagina con dati JSON a livello di riga**
1. Crea un `Workbook` e ottieni il suo primo `Worksheet` con `workbook.getWorksheets().get(0)`.  
2. Scrivi i segnaposto `<<Source.Field>>` nelle sezioni di intestazione e piè di pagina desiderate con `PageSetup.setHeader` e `PageSetup.setFooter`.  
3. Prepara i dati delle righe come un array JSON di oggetti riga e scegli un nome della fonte che corrisponda al prefisso della fonte usato dai segnaposto. Ad esempio, una fonte denominata `node` supporta segnaposto come `<<node.Name>>`. Oggetti JavaScript semplici e array passati a `setDataSource` non si associano su questa piattaforma — il JSON è la forma tabellare supportata.  
4. Crea un `WorkbookDesigner` per la cartella di lavoro.  
5. Chiama `designer.setEnableHeaderFooterMarkers(true)` prima dell'elaborazione.  
6. Allega il JSON con `designer.setJsonDataSource("node", '[{\"Name\":\"...\",\"Author\":\"...\"}]')`.  
7. Chiama `designer.process()`.  
8. Dopo l'elaborazione, i segnaposto non sono più presenti nel testo dell'intestazione o del piè di pagina. Usa `getHeader` e `getFooter` per recuperare le stringhe di sezione completate.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource(
  "node",
  '[{"Name":"Q4 2026","Author":"Aspose.Cells"}]'
);
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
console.log("Footer: " + worksheet.getPageSetup().getFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx");
```

## **Utilizzare una fonte dati JSON**
Quando i dati del report sono già disponibili come JSON, una chiamata a `setJsonDataSource` può alimentare ogni stile di marcatore. Chiama `WorkbookDesigner.setJsonDataSource(String name, String json)` per allegare la fonte.  
L'argomento `name` è il nome della fonte usato dai segnaposto. Ad esempio, il nome `node` supporta segnaposto come `<<node.Company>>` e `<<node.Title>>`.  
Passa i dati delle righe direttamente a `setJsonDataSource`:
- Un array di righe, ad esempio un array JSON contenente uno o più oggetti riga, è supportato.  
- Un singolo oggetto riga può anche essere passato direttamente.  
- Non avvolgere le righe sotto una chiave di livello superiore denominata, ad esempio `{"rows":[...]}`. Questo wrapper non è la forma di input orientata alle righe prevista per questo flusso di lavoro.  
Una fonte JSON può popolare entrambi gli stili di marcatore durante la stessa chiamata a `process()`. Può risolvere un marcatore classico `&=` in una cella del corpo del foglio di lavoro e i segnaposto a doppia parentesi angolare `<<>>` nelle sezioni di intestazione e piè di pagina. È comunque necessario chiamare `designer.setEnableHeaderFooterMarkers(true)` affinché i segnaposto di intestazione e piè di pagina vengano risolti.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
worksheet.getCells().get("A1").putValue("&=node.Company");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]');
designer.process();
console.log("Left: " + worksheet.getPageSetup().getHeader(0));
console.log("Right: " + worksheet.getPageSetup().getHeader(2));
console.log("Body: " + worksheet.getCells().get("A1").getStringValue());
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx");
```

## **Semantica dell'interruttore e della fonte a più righe**
`setEnableHeaderFooterMarkers` è `false` per impostazione predefinita, e l'impostazione controlla solo i segnaposto `<<Source.Field>>` di intestazione e piè di pagina. Quando l'interruttore è spento, `process()` risolve comunque i marcatori classici `&=` del corpo, ma un segnaposto `<<Source.Field>>` in un'intestazione o in un piè di pagina rimane testo letterale.  
Una sezione di intestazione o di piè di pagina è una singola stringa, non una banda ripetitiva. Se la fonte dati contiene diverse righe, la prima riga fornisce i valori di intestazione e piè di pagina. Una volta risolti, i valori diventano testo ordinario di intestazione o piè di pagina. Rimangono nella cartella di lavoro dopo aver chiamato `save` e sono presenti quando si ricarica la cartella di lavoro salvata.  
L'esempio seguente crea due cartelle di lavoro sulla stessa fonte JSON a più righe per confrontare il comportamento con l'interruttore disabilitato e abilitato. Il `plainDesigner` lascia il segnaposto invariato, mentre il `enabledDesigner` lo risolve usando la prima riga.

```javascript
const AsposeCells = require("aspose.cells");
const table = '[{"Name":"First Row"},{"Name":"Second Row"}]';
// Without the switch the placeholder stays literal text
const plainWorkbook = new AsposeCells.Workbook();
const plainSheet = plainWorkbook.getWorksheets().get(0);
plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const plainDesigner = new AsposeCells.WorkbookDesigner(plainWorkbook);
plainDesigner.setJsonDataSource("node", table);
plainDesigner.process();
// With the switch on, the FIRST row of a multi-row source wins
const enabledWorkbook = new AsposeCells.Workbook();
const enabledSheet = enabledWorkbook.getWorksheets().get(0);
enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const enabledDesigner = new AsposeCells.WorkbookDesigner(enabledWorkbook);
enabledDesigner.setEnableHeaderFooterMarkers(true);
enabledDesigner.setJsonDataSource("node", table);
enabledDesigner.process();
console.log("Without switch: " + plainSheet.getPageSetup().getHeader(1));
console.log("With switch: " + enabledSheet.getPageSetup().getHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
```

## **Associare un'immagine a un'intestazione o a un piè di pagina**
Il suffisso `(picture)` associa un'immagine a una sezione di intestazione o di piè di pagina. Scrivi `<<node.logo(picture)>>` dove deve apparire l'immagine e fornisci il valore del campo come URI dati — il prefisso `data:image/png;base64,` seguito dal testo Base64 dei byte dell'immagine. Una stringa Base64 pura senza il prefisso `data:` non incorpora un'immagine.  
Dopo `process()`:
1. Il segnaposto viene sostituito da `&G`, il codice standard per immagini di intestazione e piè di pagina. Poiché il marcatore diventa un codice all'interno della stringa della sezione, può trovarsi in un testo più lungo, ad esempio `Logo: <<node.logo(picture)>>`.  
2. I byte dell'immagine vengono incorporati nella cartella di lavoro come parte media allegata al livello di disegno intestazione/piè di pagina di quel foglio, così l'immagine viene stampata con l'intestazione o il piè di pagina.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
const table = [
    {
        logo: "data:image/png;base64," + fs.readFileSync("logo.png").toString("base64")
    }
];
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", JSON.stringify(table));
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
// This prints:
// Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx");
```

Il codice `&G` stampato è il codice immagine che Excel interpreta durante il rendering dell'intestazione — i byte di `logo.png` ora vivono dentro `HeaderFooterPicture.xlsx`, e l'immagine viene stampata al posto del codice.  
Per utilizzare i Smart Marker in intestazioni e piè di pagina, scrivi i segnaposto `<<Source.Field>>` nelle sezioni sinistra, centrale e destra con `setHeader` e `setFooter`. Chiama `designer.setEnableHeaderFooterMarkers(true)` prima di chiamare `process()`, e fornisci i valori tramite `designer.setJsonDataSource(name, json)`. Leggi le sezioni completate con `getHeader` e `getFooter`. La stessa fonte dati può popolare marcatori del corpo e segnaposto di intestazione o piè di pagina in un unico passaggio di elaborazione. Aggiungi il suffisso `(picture)` con un valore URI dati per associare un'immagine a una sezione.

## Articoli correlati
- [Rendering di array a singola cella SmartMarker](/cells/it/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="nodejs-java" >}}