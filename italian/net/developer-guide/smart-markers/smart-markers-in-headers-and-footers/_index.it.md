---
title: Marcatori intelligenti nelle intestazioni e nei piè di pagina | Aspose.Cells .NET
description: Inserisci segnaposto Smart Marker nelle intestazioni e nei piè di pagina usando la sintassi a doppio segno di maggiore e l'interruttore WorkbookDesigner.EnableHeaderFooterMarkers con sorgenti dati DataTable o JSON, e associa immagini tramite data URI, in Aspose.Cells for .NET.
linktitle: Marcatori intelligenti per intestazioni e piè di pagina | Aspose.Cells
keywords: Aspose.Cells, Marcatori intelligenti, intestazioni, piè di pagina, marcatori intestazione/piè di pagina, EnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, SetHeader, SetFooter, SetJsonDataSource, DataTable, collegamento dati, immagine, data URI, C#
type: docs
weight: 196
url: /it/net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Le intestazioni e i piè di pagina contengono comunemente metadati del report, come il titolo del report, il periodo di riferimento, l'autore e il dipartimento. Quando queste informazioni sono già presenti nella sorgente dati usata per popolare la cartella di lavoro, ripeterle manualmente genera duplicazioni inutili.  
La sintassi classica degli Smart Marker, `&=Source.Field`, viene elaborata nelle celle del corpo del foglio di lavoro. Se si inserisce un marcatore classico in un'intestazione o in un piè di pagina tramite `PageSetup.SetHeader` o `PageSetup.SetFooter`, rimane come testo letterale perché le stringhe di intestazione e piè di pagina non fanno parte della griglia di celle scansionata da `WorkbookDesigner.Process()`.  
A partire da **Aspose.Cells for .NET 26.11**, l'interruttore `WorkbookDesigner.EnableHeaderFooterMarkers`, che per impostazione predefinita è `false`, consente a `Process()` di risolvere i segnaposto scritti come `<<Source.Field>>` nelle stringhe delle sezioni di intestazione e piè di pagina — impostalo a `true` prima di chiamare `Process()`. I segnaposto di intestazione e piè di pagina utilizzano la stessa sorgente dati dei marcatori del corpo.
Ogni intestazione e piè di pagina contiene tre sezioni indirizzabili:
- La sezione `0` è la sezione sinistra.
- La sezione `1` è la sezione centrale.
- La sezione `2` è la sezione destra.
Usa `PageSetup.SetHeader(int section, string value)` e `PageSetup.SetFooter(int section, string value)` per scrivere queste sezioni. Dopo l'elaborazione, utilizza `PageSetup.GetHeader(int section)` e `PageSetup.GetFooter(int section)` per recuperare il testo completato.

{{% alert color="primary" %}}
Un segnaposto come `<<Source.Field>>` inserisce il valore del campo come testo nella stringa della sezione. Le immagini vengono associate usando il suffisso `(picture)` e un valore data-URI.
{{% /alert %}}

## **Abilitare i marcatori intestazione/piè di pagina con un DataTable**
Segui la sequenza seguente per risolvere i segnaposto di intestazione e piè di pagina con un `DataTable` in **Aspose.Cells for .NET 26.11**:
1. Crea un `Workbook` e ottieni il suo primo `Worksheet` all'indice `0`.
2. Scrivi i segnaposto `<<Source.Field>>` nelle sezioni desiderate di intestazione e piè di pagina con `PageSetup.SetHeader` e `PageSetup.SetFooter`.
3. Crea un `DataTable` il cui nome della tabella corrisponde al prefisso sorgente usato nei segnaposto. Per esempio, una tabella chiamata `node` supporta segnaposto come `<<node.Name>>`.
4. Crea un `WorkbookDesigner` per la cartella di lavoro.
5. Imposta `designer.EnableHeaderFooterMarkers` su `true` prima dell'elaborazione.
6. Collega la tabella con `designer.SetDataSource(table)`.
7. Chiama `designer.Process()`.
8. Dopo l'elaborazione, i segnaposto non sono più presenti nel testo di intestazione o piè di pagina. Usa `GetHeader` e `GetFooter` per recuperare le stringhe di sezione completate.

```csharp
using System;
using System.Data;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.PageSetup.SetHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.PageSetup.SetFooter(1, "Prepared by <<node.Author>>");
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Columns.Add("Author");
table.Rows.Add("Q4 2026", "Aspose.Cells");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
Console.WriteLine("Footer: " + worksheet.PageSetup.GetFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.Save("HeaderFooterSmartMarkers.xlsx");
```

## **Utilizzare una sorgente dati JSON**
È possibile usare JSON al posto di un `DataTable` quando i dati del report sono già disponibili in formato JSON. Chiama `WorkbookDesigner.SetJsonDataSource(string name, string json)` per collegare la sorgente.  
L'argomento `name` ha lo stesso ruolo del nome del `DataTable`. Per esempio, il nome `node` supporta segnaposto come `<<node.Company>>` e `<<node.Title>>`.  
Passa i dati di riga direttamente a `SetJsonDataSource`:
- È supportato un array di righe, ad esempio un array JSON contenente uno o più oggetti riga.
- È possibile passare direttamente un singolo oggetto riga.
- Non avvolgere le righe sotto una chiave di livello superiore denominata, ad esempio `{"rows":[...]}`. Questo involucro non corrisponde alla forma di input orientata alle righe prevista per questo flusso di lavoro.  
Una singola sorgente JSON può popolare entrambi gli stili di marcatore durante la stessa chiamata a `Process()`. Può risolvere un marcatore classico `&=` in una cella del corpo del foglio di lavoro e segnaposto a doppio segno di maggiore `<<>>` in intestazioni e piè di pagina. È comunque necessario abilitare `EnableHeaderFooterMarkers` perché i segnaposto di intestazione e piè di pagina vengano risolti.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.PageSetup.SetHeader(0, "<<node.Company>>");
worksheet.PageSetup.SetHeader(2, "Page <<node.Title>>");
worksheet.Cells["A1"].PutValue("&=node.Company");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
designer.Process();
Console.WriteLine("Left: " + worksheet.PageSetup.GetHeader(0));
Console.WriteLine("Right: " + worksheet.PageSetup.GetHeader(2));
Console.WriteLine("Body: " + worksheet.Cells["A1"].StringValue);
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.Save("HeaderFooterJsonMarkers.xlsx");
```

## **Semantica dell'interruttore e della sorgente multi-riga**
`EnableHeaderFooterMarkers` è `false` per impostazione predefinita, e l'interruttore controlla solo i segnaposto `<<Source.Field>>` di intestazione e piè di pagina. Quando l'interruttore è disattivato, `Process()` continua a risolvere i marcatori classici `&=` nel corpo, ma un segnaposto `<<Source.Field>>` in un'intestazione o in un piè di pagina rimane testo letterale.  
Una sezione di intestazione o piè di pagina è una singola stringa, non una banda ripetitiva. Se la sorgente dati contiene più righe, la prima riga fornisce i valori di intestazione e piè di pagina. Una volta risolti, i valori diventano testo ordinario di intestazione o piè di pagina. Restano nella cartella di lavoro dopo aver chiamato `Save` e sono presenti quando ricarichi la cartella di lavoro salvata.  
L'esempio seguente crea due cartelle di lavoro basate sulla stessa `DataTable` multi-riga per confrontare il comportamento con l'interruttore disattivato e attivato. Il `plainDesigner` lascia il segnaposto invariato, mentre il `enabledDesigner` lo risolve usando la prima riga.

```csharp
using System;
using System.Data;
using Aspose.Cells;
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Rows.Add("First Row");
table.Rows.Add("Second Row");
// Without the switch the placeholder stays literal text
Workbook plainWorkbook = new Workbook();
Worksheet plainSheet = plainWorkbook.Worksheets[0];
plainSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
plainDesigner.SetDataSource(table);
plainDesigner.Process();
// With the switch on, the FIRST row of a multi-row source wins
Workbook enabledWorkbook = new Workbook();
Worksheet enabledSheet = enabledWorkbook.Worksheets[0];
enabledSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
enabledDesigner.EnableHeaderFooterMarkers = true;
enabledDesigner.SetDataSource(table);
enabledDesigner.Process();
Console.WriteLine("Without switch: " + plainSheet.PageSetup.GetHeader(1));
Console.WriteLine("With switch: " + enabledSheet.PageSetup.GetHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.Save("HeaderFooterMarkersEnabled.xlsx");
```

## **Associa un'immagine a un'intestazione o a un piè di pagina**
Il suffisso `(picture)` associa un'immagine a una sezione di intestazione o di piè di pagina. Scrivi `<<node.logo(picture)>>` dove desideri che l'immagine appaia e fornisci il valore del campo come data-URI — il prefisso `data:image/png;base64,` seguito dal testo Base64 dei byte dell'immagine. Una stringa Base64 senza il prefisso `data:` non incorpora un'immagine.  
Dopo `Process()`:
1. Il segnaposto viene sostituito da `&G`, il codice standard di immagine per intestazione e piè di pagina. Poiché il marcatore diventa un codice all'interno della stringa di sezione, può coesistere con testo più lungo, ad esempio `Logo: <<node.logo(picture)>>`.
2. I byte dell'immagine vengono incorporati nella cartella di lavoro come parte multimediale allegata al livello di disegno intestazione/piè di pagina di quel foglio di lavoro, quindi l'immagine viene stampata con l'intestazione o il piè di pagina.

```csharp
using System;
using System.Data;
using System.IO;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.PageSetup.SetHeader(1, "Logo: <<node.logo(picture)>>");
DataTable table = new DataTable("node");
table.Columns.Add("logo");
table.Rows.Add("data:image/png;base64," + Convert.ToBase64String(File.ReadAllBytes("logo.png")));
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
// This prints:
// Header: Logo: &G
workbook.Save("HeaderFooterPicture.xlsx");
```

Il `&G` stampato è il codice immagine che Excel interpreta durante il rendering dell'intestazione — i byte di `logo.png` ora vivono dentro `HeaderFooterPicture.xlsx`, e l'immagine viene stampata al posto del codice.  
Per usare i Marcatori intelligenti nelle intestazioni e nei piè di pagina, scrivi segnaposto `<<Source.Field>>` nelle sezioni sinistra, centrale e destra con `SetHeader` e `SetFooter`. Imposta `EnableHeaderFooterMarkers` su `true` sul `WorkbookDesigner` prima di chiamare `Process()`, e fornisci i valori tramite `SetDataSource(DataTable)` o `SetJsonDataSource`. Leggi le sezioni completate con `GetHeader` e `GetFooter`. La stessa sorgente dati può popolare marcatori del corpo e segnaposto di intestazione o piè di pagina in un unico passaggio di elaborazione. Aggiungi il suffisso `(picture)` con un valore data-URI per associare un'immagine a una sezione.

## Articoli correlati
- [Rendering di un array a cella singola con SmartMarker](/cells/it/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="csharp" >}}