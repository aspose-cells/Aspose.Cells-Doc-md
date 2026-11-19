---
title: Rendering di array a singola cella con SmartMarker | Aspose.Cells for Node.js via Java
description: Scopri come rendere i dati di array in una singola cella utilizzando gli attributi Smart Marker arrayassingle e arraydelimiter in Aspose.Cells for Node.js via Java.
linktitle: Rendering di array a singola cella con SmartMarker | Aspose.Cells for Node.js via Java
url: /it/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, libreria Node.js via Java, foglio di calcolo, Smart Marker, arrayassingle, arraydelimiter, array a singola cella, rendering di array, modello
type: docs
weight: 195
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells può rendere un'origine dati di array in un'unica cella tramite gli Smart Marker. L'attributo `arrayassingle` disattiva l'espansione predefinita elemento per elemento, mentre l'attributo `arraydelimiter` sceglie il separatore inserito tra gli elementi uniti — virgola per impostazione predefinita, oppure qualsiasi carattere singolo o stringa di più caratteri tra virgolette specificato.
{{% /alert %}}

## **Introduzione**

Gli Smart Marker di Aspose.Cells sono una funzionalità basata su modelli che popola dinamicamente i dati del foglio di calcolo utilizzando espressioni come `&=DataSource.Field`. Lo Smart Marker viene inserito in una cartella di lavoro di progettazione e, quando il modello viene elaborato da `WorkbookDesigner`, i marker vengono sostituiti dai valori dell'origine dati fornita.
Per impostazione predefinita, quando uno Smart Marker fa riferimento a un campo array (ad esempio, `&=Product.Tags` associato a un array di quattro valori), il motore espande l'array e inserisce ogni elemento in una cella propria, distribuendo i valori verticalmente nella colonna sotto il marker. Sebbene questo comportamento sia comodo in molti scenari, ci sono situazioni in cui è preferibile rendere l'intero array in un'unica cella, con gli elementi concatenati e separati da un delimitatore a scelta.
Gli attributi `arrayassingle` e `arraydelimiter`, scritti all'interno delle parentesi di uno Smart Marker nella forma `name:value`, rispondono esattamente a questa esigenza. Consentono di mantenere strutture di report compatte e prevedibili, continuando a utilizzare in modo nativo le origini dati di array.

## **Perché è necessaria questa funzionalità**

### **Comportamento predefinito di espansione degli array**

Quando uno Smart Marker fa riferimento a un campo array, Aspose.Cells espande l'array su più celle per impostazione predefinita. Ad esempio, un marker come `&=Product.Tags` associato a un array contenente quattro valori inserisce ogni valore in una propria cella sotto il marker, spostando altro contenuto del modello verso il basso e potenzialmente compromettendo strutture di report accuratamente progettate.

### **Limitazioni dei casi d'uso**

Esistono molti scenari pratici in cui il comportamento predefinito di espansione non è desiderabile:
- **Report in stile riepilogo** che richiedono una struttura compatta con una sola riga per ogni dato.
- **Elenchi di tag, etichette o parole chiave** che devono essere visualizzati come valori separati da virgole o da barre all'interno di una singola cella.
- **Schede filtro o indicatori di stato** che raggruppano più valori in un unico punto per favorire la leggibilità.
- **Flussi di elaborazione successiva** (esportazione CSV, rendering PDF, stampa unione) che richiedono un singolo valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità multipiattaforma**, in cui alcune applicazioni di destinazione non riescono a gestire array estesi su più celle.

### **La lacuna che colma**

Senza un meccanismo integrato, gli sviluppatori sarebbero costretti a pre-elaborare i dati in JavaScript, unendo gli array in stringhe delimitate prima di associarli al designer della cartella di lavoro. Ciò duplicherebbe la logica, complicherebbe i modelli di dati e aumenterebbe la probabilità di errori. Gli attributi `arrayassingle` e `arraydelimiter` eliminano questa soluzione alternativa gestendo la formattazione in modo dichiarativo all'interno dello stesso Smart Marker.

## **Vantaggi della funzionalità**

L'uso degli attributi `arrayassingle` e `arraydelimiter` negli Smart Marker offre diversi vantaggi:
- **Contenimento in una singola cella**: tutti gli elementi dell'array vengono renderizzati in esattamente una cella, mantenendo la struttura compatta e prevedibile.
- **Controllo personalizzato del delimitatore**: specificare il separatore desiderato — la virgola predefinita, un punto e virgola, un trattino, una barra verticale o una stringa di più caratteri tra virgolette come `" | "`.
- **Formattazione guidata dal modello**: non è richiesto codice aggiuntivo per pre-elaborare i dati; le regole di formattazione sono contenute nel tag Smart Marker.
- **Report più puliti**: i dati di array non spostano più il contenuto circostante del modello in righe o colonne diverse.
- **Tipi di dati versatili**: funziona con array di stringhe forniti come righe JSON, inclusi valori numerici renderizzati come stringhe.
- **Compatibilità con le versioni precedenti**: quando gli attributi vengono omessi, viene mantenuto il comportamento di espansione originale, così i modelli esistenti continuano a funzionare senza modifiche.

## **Come utilizzare la funzionalità**

### **Sintassi dello Smart Marker**

Gli attributi `arrayassingle` e `arraydelimiter` usano la grammatica degli attributi `name:value` di Aspose.Cells all'interno delle parentesi di uno Smart Marker standard. La sintassi generale è:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

Lo Smart Marker è composto dalle seguenti parti:
- `&=DataSource.ArrayField` — lo Smart Marker standard che fa riferimento al campo array dell'origine dati associata.
- `arrayassingle:true` — indica al motore di rendere l'intero array in una singola cella anziché distribuirne gli elementi.
- `arraydelimiter:;` — facoltativo; definisce il separatore inserito tra gli elementi dell'array. Se viene omesso, viene utilizzata una virgola.

{{% alert color="warning" %}}
Scrivere gli attributi nella forma `name:value` (due punti, non segno uguale) e separare più attributi con una virgola **senza spazi**. Uno spazio dopo la virgola sposta di un carattere il valore analizzato — `(arrayassingle:true, arraydelimiter:;)` unirebbe con il separatore errato `:;` invece che `;`.
{{% /alert %}}

### **Forme del delimitatore**

- Un carattere singolo segue direttamente i due punti: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Un separatore di più caratteri è racchiuso tra virgolette doppie: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Flusso di lavoro passo per passo**

Il flusso di lavoro seguente descrive come rendere un array in una singola cella utilizzando gli Smart Marker.
1. **Preparare l'origine dati**: organizzare ciascun dato come un oggetto JSON il cui campo contiene un array, ad esempio `{"Tags": ["C#", "Aspose"]}`. Gli oggetti e gli array JavaScript semplici passati a `setDataSource` non vengono associati su questa piattaforma — le righe JSON sono la forma tabulare supportata.
2. **Creare una cartella di lavoro di progettazione**: creare un nuovo `Workbook`, aggiungere una riga di intestazione e inserire in una cella uno Smart Marker che faccia riferimento al campo array con l'attributo `arrayassingle` (e `arraydelimiter` quando è necessario un separatore personalizzato).
3. **Istanziare `WorkbookDesigner`**: creare un `WorkbookDesigner` associato alla cartella di lavoro e collegare le righe JSON con `setJsonDataSource`.
4. **Elaborare i marker**: chiamare il metodo `workbookDesigner.process()` per espandere gli Smart Marker e popolare la cartella di lavoro con i dati effettivi.
5. **Salvare il risultato**: salvare la cartella di lavoro risultante su disco in XLSX o in qualsiasi altro formato file supportato.

### **Esempio di codice 1 — Rendering di base di un array di stringhe**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Tags");
// No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-single.xlsx");
```

L'esempio stampa il valore concatenato dell'intero array. Le quattro etichette finiscono in una singola cella, separate dalla virgola predefinita:

```
C#,Aspose,SmartMarker,Excel
```

### **Esempio di codice 2 — Valori numerici con un delimitatore personalizzato**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Scores");
// arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-numeric.xlsx");
```

Quando i punteggi sono forniti come stringhe JSON, l'output concatenato conserva i valori numerici come testo semplice:

```
95-88-76-100-67
```

{{% alert color="note" %}}
I numeri JSON passati tramite il motore Java arrivano come valori `double`, quindi `[95, 88]` verrebbe unito come `95.0-88.0`. Mettere tra virgolette i numeri nelle righe JSON quando si desidera ottenere il testo esatto dell'intero nella cella unita.
{{% /alert %}}

### **Esempio di codice 3 — Confronto tra il rendering predefinito e quello a singola cella**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();
// Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default");
cells.get("B2").putValue("&=Order.Items");
// Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell");
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]');
designer.process();
for (let row = 1; row <= 5; row++) {
    const b = cells.get(row, 1).getStringValue() || "";
    const c = cells.get(row, 2).getStringValue() || "";
    if (b || c) console.log(`B${row + 1}=[${b}]  C${row + 1}=[${c}]`);
}
workbook.save("output-array-comparison.xlsx");
```

Il marker predefinito riempie una cella per elemento scendendo nella colonna B, mentre il marker `arrayassingle` compatta lo stesso array in una singola cella nella colonna C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Note e buone pratiche**

Tenere presenti i seguenti punti quando si lavora con gli attributi `arrayassingle` e `arraydelimiter`:
- I valori degli attributi usano la forma `name:value`. La forma con il segno uguale, come `arrayassingle=true`, non viene riconosciuta e ricade silenziosamente nel comportamento predefinito di espansione.
- Separare gli attributi con una virgola e senza spazi; uno spazio dopo la virgola sposta di un carattere il valore del delimitatore (vedere l'avviso precedente).
- Il valore `arraydelimiter` può essere un carattere singolo scritto direttamente dopo i due punti oppure una stringa di più caratteri racchiusa tra virgolette doppie.
- Quando `arraydelimiter` viene omesso, gli elementi vengono uniti con una virgola.
- Fornire i campi array tramite gli oggetti riga di `setJsonDataSource`; gli oggetti e gli array JavaScript semplici passati a `setDataSource` non vengono associati su questa piattaforma.
- I numeri JSON arrivano come `double` tramite il motore Java (`95` viene unito come `95.0`); mettere tra virgolette i valori numerici nelle righe JSON quando è importante il testo esatto dell'intero.
- Collocare lo Smart Marker in una cella con una larghezza sufficiente per visualizzare la stringa concatenata risultante; in caso contrario, il contenuto può traboccare visivamente nelle celle adiacenti, a seconda della formattazione.

## **Articoli correlati**
- [Aggiungere campi filtro a una tabella pivot in Aspose.Cells for Node.js via Java](/cells/it/nodejs-java/add-page-field-in-pivot-table/)
- [Applica stili alle tabelle pivot in Aspose.Cells for Node.js via Java](/cells/it/nodejs-java/apply-style-to-pivot-table/)
- [Modificare il layout del campo pagina in una tabella pivot](/cells/it/nodejs-java/change-page-field-layout/)
- [Convertire Sparkline in Immagine e HTML in Aspose.Cells for Node.js via Java](/cells/it/nodejs-java/convert-sparkline-to-image-and-html/)
- [Conversione di Excel in formato OFD](/cells/it/nodejs-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="nodejs-java" >}}