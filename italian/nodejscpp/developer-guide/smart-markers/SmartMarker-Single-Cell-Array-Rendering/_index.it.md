---
title: Rendering di array in cella singola con SmartMarker | Aspose.Cells for Node.js via C++
description: Scopri come eseguire il rendering dei dati di array in una singola cella utilizzando gli attributi ArrayAsSingle e ExtraDelimiter nei Smart Markers con Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, libreria Node.js, foglio di calcolo, Smart Markers, ArrayAsSingle, ExtraDelimiter, array in cella singola, rendering di array, modello
type: docs
weight: 195
url: /it/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells supporta il rendering dei dati di array in una singola cella tramite gli Smart Markers. Utilizzando l'attributo `ArrayAsSingle` insieme all'attributo `ExtraDelimiter`, gli sviluppatori possono controllare come gli elementi dell'array vengono separati all'interno di una singola cella, offrendo una formattazione flessibile per report e modelli.

{{% /alert %}}

## **Introduzione**

Gli Smart Markers in Aspose.Cells sono una potente funzionalità basata su modelli che consente di popolare dinamicamente i dati del foglio di calcolo utilizzando espressioni marker come `&=DataSource.Field`. Il marker viene posizionato in una cartella di lavoro del designer e, quando il modello viene elaborato dal `WorkbookDesigner`, i marker vengono sostituiti con i valori provenienti dall'origine dati fornita.

Per impostazione predefinita, quando uno Smart Marker fa riferimento a una proprietà di array (ad esempio, `&=DataSource.Numbers`), il motore espande l'array e posiziona ciascun elemento in una cella adiacente separata — orizzontalmente su una riga o verticalmente lungo una colonna. Sebbene questo comportamento sia comodo in molti scenari, ci sono situazioni in cui si preferisce eseguire il rendering dell'intero array in un'unica cella, con gli elementi concatenati e separati da un delimitatore a scelta.

Gli attributi `ArrayAsSingle` e `ExtraDelimiter`, utilizzati insieme all'interno di un tag Smart Marker, soddisfano esattamente questo requisito. Consentono di mantenere i layout dei report compatti e prevedibili, lavorando comunque in modo nativo con origini dati di tipo array.

## **Perché questa funzionalità è necessaria**

### **Comportamento predefinito di espansione dell'array**

Quando uno Smart Marker fa riferimento a una proprietà di array, Aspose.Cells espande l'array su più celle per impostazione predefinita. Ad esempio, un marker come `&=Product.Tags` su un `string[]` contenente quattro valori posizionerà ciascun valore nella propria cella, spingendo il resto del contenuto del modello verso l'esterno e potenzialmente compromettendo layout di report progettati con cura.

### **Limitazioni dei casi d'uso**

Esistono molti scenari pratici in cui il comportamento di espansione predefinito è indesiderato:

- **Report in stile riepilogo** che richiedono un layout compatto con una riga per record.
- **Elenchi di tag, etichette o parole chiave** che devono essere visualizzati come valori separati da virgola o da pipe all'interno di una singola cella.
- **Chip di filtri o indicatori di stato** che raggruppano più valori in un unico punto per migliorare la leggibilità.
- **Pipeline a valle** (esportazione CSV, rendering PDF, stampa unione) che si aspettano un singolo valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità multipiattaforma**, dove alcuni consumatori non tollerano array che si estendono su più celle.

### **Il divario che colma**

Senza un meccanismo integrato, gli sviluppatori sarebbero costretti a pre-elaborare i dati in JavaScript, unendo gli array in stringhe delimitate prima di associarle al designer della cartella di lavoro. Ciò duplica la logica, complica i modelli di dati e aumenta la probabilità di errori. Gli attributi `ArrayAsSingle` e `ExtraDelimiter` eliminano questa soluzione alternativa gestendo la formattazione in modo dichiarativo all'interno dello Smart Marker stesso.

## **Vantaggi della funzionalità**

L'utilizzo degli attributi `ArrayAsSingle` e `ExtraDelimiter` nei propri Smart Markers offre diversi vantaggi:

- **Contenimento in cella singola**: tutti gli elementi dell'array vengono renderizzati in esattamente una cella, mantenendo i layout compatti e prevedibili.
- **Controllo personalizzato del delimitatore**: specificare qualsiasi stringa separatore desiderata — virgola, punto e virgola, trattino, pipe, nuova riga o qualsiasi testo personalizzato.
- **Formattazione guidata dal modello**: non è richiesto codice aggiuntivo per pre-elaborare i dati; le regole di formattazione risiedono all'interno del tag Smart Marker.
- **Report più puliti**: i dati di array non spingono più il contenuto del modello adiacente in righe o colonne diverse.
- **Tipi di dati versatili**: funziona con stringhe, numeri, date e qualsiasi altro tipo di dato che possa essere unito con un delimitatore.
- **Compatibilità con le versioni precedenti**: quando gli attributi vengono omessi, viene preservato il comportamento di espansione originale, quindi i modelli esistenti continuano a funzionare senza modifiche.

## **Come utilizzare questa funzionalità**

### **Sintassi dello Smart Marker**

Gli attributi `ArrayAsSingle` e `ExtraDelimiter` vengono passati come coppie chiave-valore all'interno delle parentesi di uno Smart Marker standard. La sintassi generale è:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Il marker è composto dalle seguenti parti:

- `&=DataSource.ArrayProperty` — lo Smart Marker standard che fa riferimento alla proprietà di array sull'origine dati associata.
- `arrayasSingle=true` — indica al motore di eseguire il rendering dell'intero array in una singola cella. Solo il valore `true` attiva il comportamento a cella singola.
- `extraDelimiter=", "` — definisce il separatore inserito tra gli elementi dell'array. Il valore è una stringa letterale; può essere vuoto, un singolo carattere o una stringa multi-carattere.

{{% alert color="primary" %}}

L'attributo `extraDelimiter` accetta qualsiasi stringa letterale, inclusi delimitatori multi-carattere, testo personalizzato o sequenze di escape come `\n` per un output separato da nuova riga. Se l'array è vuoto, la cella risultante viene lasciata vuota.

{{% /alert %}}

### **Flusso di lavoro passo-passo**

Il seguente flusso di lavoro descrive come eseguire il rendering di un array in una singola cella utilizzando gli Smart Markers.

1. **Preparare l'origine dati**: creare una classe (o struttura dati) che esponga una proprietà che restituisce un array. La proprietà può restituire `string[]`, `int[]` o qualsiasi altro tipo di array supportato.
2. **Creare una cartella di lavoro del designer**: creare un nuovo `Workbook`, aggiungere una riga di intestazione e posizionare una cella Smart Marker che faccia riferimento alla proprietà di array con gli attributi `arrayasSingle` e `extraDelimiter`.
3. **Istanziare il WorkbookDesigner**: creare un oggetto `WorkbookDesigner`, associare ad esso la cartella di lavoro del designer e associare l'origine dati utilizzando il metodo `setDataSource`.
4. **Elaborare i marker**: chiamare il metodo `workbookDesigner.process()` per espandere gli Smart Markers e popolare la cartella di lavoro con i dati reali.
5. **Salvare il risultato**: salvare la cartella di lavoro risultante su disco in formato XLSX o in qualsiasi altro formato di file supportato.

### **Esempio di codice 1 — Rendering di base di un array di stringhe**

```javascript
let product = {
    Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
};

let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue('&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")');

let designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");
```

### **Esempio di codice 2 — Array numerico con delimitatore personalizzato**

```javascript
class Student {
    constructor() {
        this.Scores = [];
    }
}

const student = new Student();
student.Scores = [95, 88, 76, 100, 67];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Scores");
worksheet.getCells().get("A2").putValue(student.Scores.join(" - "));

workbook.save("output_numericArray.xlsx");
```

### **Esempio di codice 3 — Confronto tra il comportamento predefinito e ArrayAsSingle**

```javascript
var order = {
    Items: ["Apple", "Banana", "Cherry", "Date"]
};

var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Sezione 1: Smart Marker predefinito - valori distribuiti orizzontalmente tra le celle
cells.get("A1").putValue("Default Spreading Behavior:");
cells.get("A2").putValue("&=Order.Items");

// Sezione 2: Nuovo rendering a cella singola utilizzando arrayasSingle e extraDelimiter
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

// Associa l'origine dati ed elabora gli Smart Marker
var designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setDataSource("Order", order);
designer.process();

// Salva la cartella di lavoro risultante
workbook.save("output_comparison.xlsx");
```

### **Note e best practice**

Tenere presente i seguenti punti quando si lavora con gli attributi `ArrayAsSingle` e `ExtraDelimiter`:

- Il valore di `extraDelimiter` viene trattato come una stringa letterale; eseguire l'escape di eventuali caratteri speciali che il processore del modello potrebbe interpretare.
- L'attributo `arrayasSingle` accetta un valore booleano (`true` / `false`). Solo `true` attiva il comportamento a cella singola; qualsiasi altro valore ricade nel comportamento di espansione predefinito.
- Se l'array è vuoto o null, la cella viene lasciata vuota (oppure contiene una stringa vuota a seconda del tipo di dati).
- La funzionalità funziona con origini dati di oggetti, nonché con origini `DataSet` e `DataTable` in cui una colonna può essere suddivisa in array.
- Per un output separato da nuova riga, è possibile utilizzare `\n` o `os.EOL` come valore del delimitatore.
- Posizionare lo Smart Marker in una cella che abbia larghezza sufficiente per visualizzare la stringa concatenata risultante; in caso contrario, il contenuto potrebbe traboccare visivamente nelle celle adiacenti a seconda del formato.

## **Articoli correlati**

- [Unione e separazione delle celle](/cells/it/nodejs-cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="javascript" >}}