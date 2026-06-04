---
title: Rendering di Array in Cella Singola con SmartMarker | Aspose.Cells for Node.js via Java
description: Scopri come eseguire il rendering dei dati di array in una singola cella utilizzando gli attributi ArrayAsSingle ed ExtraDelimiter negli Smart Markers con Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, libreria Node.js via Java, foglio di calcolo, Smart Markers, ArrayAsSingle, ExtraDelimiter, array in cella singola, rendering di array, modello
type: docs
weight: 195
url: /it/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells supporta il rendering dei dati di array in una singola cella tramite Smart Markers. Utilizzando l'attributo `ArrayAsSingle` insieme all'attributo `ExtraDelimiter`, gli sviluppatori possono controllare come gli elementi dell'array vengono separati all'interno di una singola cella, offrendo una formattazione flessibile per report e modelli.

{{% /alert %}}

## **Introduzione**

Gli Smart Markers in Aspose.Cells sono una potente funzionalità basata su modelli che consente di popolare dinamicamente i dati del foglio di calcolo utilizzando espressioni di marker come `&=DataSource.Field`. Il marker viene posizionato in una cartella di lavoro del designer e, quando il modello viene elaborato dal `WorkbookDesigner`, i marker vengono sostituiti con i valori provenienti dall'origine dati fornita.

Per impostazione predefinita, quando uno Smart Marker fa riferimento a una proprietà di array (ad esempio, `&=DataSource.Numbers`), il motore espande l'array e posiziona ciascun elemento in una cella adiacente separata, orizzontalmente lungo una riga o verticalmente lungo una colonna. Sebbene questo comportamento sia comodo in molti scenari, ci sono situazioni in cui si preferisce eseguire il rendering dell'intero array in un'unica cella, con gli elementi concatenati e separati da un delimitatore a scelta.

Gli attributi `ArrayAsSingle` e `ExtraDelimiter`, utilizzati insieme all'interno di un tag Smart Marker, soddisfano esattamente questo requisito. Consentono di mantenere i layout dei report compatti e prevedibili, lavorando comunque in modo nativo con origini dati di tipo array.

## **Perché Questa Funzionalità È Necessaria**

### **Comportamento Predefinito di Espansione degli Array**

Quando uno Smart Marker fa riferimento a una proprietà di array, Aspose.Cells espande l'array su più celle per impostazione predefinita. Ad esempio, un marker come `&=Product.Tags` applicato a un `string[]` contenente quattro valori posizionerà ciascun valore nella propria cella, spingendo verso l'esterno gli altri contenuti del modello e potenzialmente interrompendo layout di report progettati con cura.

### **Limitazioni dei Casi d'Uso**

Esistono molti scenari pratici in cui il comportamento predefinito di espansione è indesiderabile:

- **Report in stile riepilogo** che richiedono un layout compatto con una riga per record.
- **Elenchi di tag, etichette o parole chiave** che devono essere visualizzati come valori separati da virgola o da pipe all'interno di una singola cella.
- **Chip di filtro o indicatori di stato** che raggruppano più valori in un unico punto per migliorare la leggibilità.
- **Pipeline a valle** (esportazione CSV, rendering PDF, stampa unione) che si aspettano un unico valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità multipiattaforma**, dove alcuni consumatori non tollerano array che si distribuiscono su più celle.

### **Il Gap che Colma**

Senza un meccanismo integrato, gli sviluppatori sarebbero costretti a pre-elaborare i dati in JavaScript, unendo gli array in stringhe delimitate prima di associarle al designer della cartella di lavoro. Ciò duplica la logica, complica i modelli di dati e aumenta la probabilità di errori. Gli attributi `ArrayAsSingle` e `ExtraDelimiter` eliminano questa soluzione alternativa gestendo la formattazione in modo dichiarativo direttamente all'interno dello Smart Marker.

## **Vantaggi della Funzionalità**

L'utilizzo degli attributi `ArrayAsSingle` e `ExtraDelimiter` negli Smart Markers offre numerosi vantaggi:

- **Contenimento in singola cella**: tutti gli elementi dell'array vengono resi esattamente in una sola cella, mantenendo i layout compatti e prevedibili.
- **Controllo del delimitatore personalizzato**: specificare qualsiasi stringa separatore desiderata: virgola, punto e virgola, trattino, pipe, nuova riga o qualsiasi testo personalizzato.
- **Formattazione basata su modello**: non è richiesto alcun codice aggiuntivo per pre-elaborare i dati; le regole di formattazione risiedono all'interno del tag Smart Marker.
- **Report più puliti**: i dati di array non spingono più il contenuto adiacente del modello in righe o colonne diverse.
- **Tipi di dati versatili**: funziona con stringhe, numeri, date e qualsiasi altro tipo di dato che possa essere unito con un delimitatore.
- **Compatibilità con le versioni precedenti**: quando gli attributi vengono omessi, viene mantenuto il comportamento originale di espansione, quindi i modelli esistenti continuano a funzionare senza modifiche.

## **Come Utilizzare Questa Funzionalità**

### **Sintassi dello Smart Marker**

Gli attributi `ArrayAsSingle` e `ExtraDelimiter` vengono passati come coppie chiave-valore all'interno delle parentesi di uno Smart Marker standard. La sintassi generale è:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Il marker è composto dalle seguenti parti:

- `&=DataSource.ArrayProperty` — lo Smart Marker standard che fa riferimento alla proprietà di array sull'origine dati associata.
- `arrayasSingle=true` — indica al motore di eseguire il rendering dell'intero array in una singola cella. Solo il valore `true` attiva il comportamento a cella singola.
- `extraDelimiter=", "` — definisce il separatore posizionato tra gli elementi dell'array. Il valore è una stringa letterale; può essere vuoto, un singolo carattere o una stringa multi-carattere.

{{% alert color="primary" %}}

L'attributo `extraDelimiter` accetta qualsiasi stringa letterale, inclusi delimitatori multi-carattere, testo personalizzato o sequenze di escape come `\n` per output separati da nuova riga. Se l'array è vuoto, la cella risultante viene lasciata vuota.

{{% /alert %}}

### **Flusso di Lavoro Passo per Passo**

Il flusso di lavoro seguente descrive come eseguire il rendering di un array in una singola cella utilizzando gli Smart Markers.

1. **Preparare l'origine dati**: creare una classe (o struttura dati) che esponga una proprietà che restituisce un array. La proprietà può restituire `string[]`, `int[]` o qualsiasi altro tipo di array supportato.
2. **Creare una cartella di lavoro del designer**: creare un nuovo `Workbook`, aggiungere una riga di intestazione e posizionare una cella con uno Smart Marker che faccia riferimento alla proprietà di array con gli attributi `arrayasSingle` e `extraDelimiter`.
3. **Istanziare il WorkbookDesigner**: creare un oggetto `WorkbookDesigner`, associarvi la cartella di lavoro del designer e collegare l'origine dati utilizzando il metodo `setDataSource`.
4. **Elaborare i marker**: chiamare il metodo `workbookDesigner.process()` per espandere gli Smart Markers e popolare la cartella di lavoro con i dati reali.
5. **Salvare il risultato**: salvare la cartella di lavoro risultante su disco in formato XLSX o in qualsiasi altro formato di file supportato.

### **Esempio di Codice 1 — Rendering di Array di Stringhe di Base**

```javascript
class Product {
    constructor() {
        this.Tags = null;
    }
}

const product = new Product();
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

const designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");
```

### **Esempio di Codice 2 — Array Numerico con Delimitatore Personalizzato**

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
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayasSingle=true, extraDelimiter=\" - \")");

const designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Student", student);
designer.process();

workbook.save("output_numericArray.xlsx");
```

### **Esempio di Codice 3 — Confronto tra Comportamento Predefinito e ArrayAsSingle**

```javascript
const AsposeCells = require("aspose.cells");

function main() {
    const order = {
        Items: ["Apple", "Banana", "Cherry", "Date"]
    };

    const workbook = new AsposeCells.Workbook();
    const sheet = workbook.getWorksheets().get(0);
    const cells = sheet.getCells();

    // Sezione 1: Smart Marker predefinito - valori distribuiti orizzontalmente tra le celle
    cells.get("A1").putValue("Default Spreading Behavior:");
    cells.get("A2").putValue("&=Order.Items");

    // Sezione 2: Nuovo rendering a cella singola utilizzando arrayasSingle e extraDelimiter
    cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):");
    cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // Associa l'origine dati ed elabora gli Smart Marker
    const designer = new AsposeCells.WorkbookDesigner(workbook);
    designer.setDataSource("Order", order);
    designer.process();

    // Salva la cartella di lavoro risultante
    workbook.save("output_comparison.xlsx");
}

main();
```

### **Note e Best Practices**

Tenere presente i seguenti punti quando si lavora con gli attributi `ArrayAsSingle` e `ExtraDelimiter`:

- Il valore di `extraDelimiter` viene trattato come una stringa letterale; eseguire l'escape di eventuali caratteri speciali che il processore del modello potrebbe interpretare.
- L'attributo `arrayasSingle` accetta un valore booleano (`true` / `false`). Solo `true` attiva il comportamento a cella singola; qualsiasi altro valore ripristina il comportamento predefinito di espansione.
- Se l'array è vuoto o null, la cella viene lasciata vuota (oppure contiene una stringa vuota a seconda del tipo di dato).
- La funzionalità funziona con origini dati di tipo oggetto, nonché con origini `DataSet` e `DataTable` in cui una colonna può essere suddivisa in array.
- Per output separati da nuova riga, è possibile utilizzare `\n` come valore del delimitatore.
- Posizionare lo Smart Marker in una cella che abbia larghezza sufficiente per visualizzare la stringa concatenata risultante; in caso contrario, il contenuto potrebbe traboccare visivamente nelle celle adiacenti a seconda del formato.



{{< app/cells/assistant language="javascript" >}}