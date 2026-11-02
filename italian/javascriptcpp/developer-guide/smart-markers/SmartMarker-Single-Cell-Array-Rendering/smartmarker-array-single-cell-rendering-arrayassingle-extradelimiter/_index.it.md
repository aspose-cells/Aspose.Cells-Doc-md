---
title: Rendering di un array in una singola cella con SmartMarker | Aspose.Cells for JavaScript via C++
linktitle: Rendering di un array in una singola cella con SmartMarker | Aspose.Cells for JavaScript via C++
description: Scopri come eseguire il rendering di dati di tipo array in una singola cella utilizzando gli attributi ArrayAsSingle ed ExtraDelimiter nei Smart Markers con Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, libreria Aspose.Cells for JavaScript via C++, foglio di calcolo, Smart Markers, ArrayAsSingle, ExtraDelimiter, array in una singola cella, rendering di array, modello
type: docs
weight: 195
url: /it/javascript-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta il rendering di dati di tipo array in una singola cella tramite Smart Marker. Utilizzando l'attributo `ArrayAsSingle` insieme all'attributo `ExtraDelimiter`, gli sviluppatori possono controllare come gli elementi dell'array vengono separati all'interno di una singola cella, offrendo una formattazione flessibile per report e modelli.
{{% /alert %}}

## **Introduzione**
I Smart Marker di Aspose.Cells sono una potente funzionalità basata su modelli che consente di popolare dinamicamente i dati di un foglio di calcolo mediante espressioni di marcatore come `&=DataSource.Field`. Il marcatore viene inserito in una cartella di lavoro di progettazione e, quando il modello viene elaborato da `WorkbookDesigner`, i marcatori vengono sostituiti dai valori della sorgente dati fornita.
Per impostazione predefinita, quando uno Smart Marker fa riferimento a una proprietà di tipo array, ad esempio `&=DataSource.Numbers`, il motore espande l'array e inserisce ogni elemento in una cella adiacente distinta, orizzontalmente lungo una riga o verticalmente in una colonna. Sebbene questo comportamento sia comodo in molti scenari, in alcuni casi è preferibile eseguire il rendering dell'intero array in una singola cella, con gli elementi concatenati e separati da un delimitatore a scelta.
L'uso combinato degli attributi `ArrayAsSingle` ed `ExtraDelimiter` all'interno di un tag di Smart Marker soddisfa esattamente questa esigenza. Consente di mantenere compatti e prevedibili i layout dei report, utilizzando al contempo in modo nativo le sorgenti dati di tipo array.

## **Perché è necessaria questa funzionalità**

### **Comportamento predefinito di espansione degli array**
Quando uno Smart Marker fa riferimento a una proprietà di tipo array, Aspose.Cells espande l'array su più celle per impostazione predefinita. Ad esempio, un marcatore come `&=Product.Tags` applicato a un array contenente quattro stringhe inserisce ogni valore in una cella separata, spostando il restante contenuto del modello e potenzialmente compromettendo layout di report progettati con cura.

### **Limitazioni dei casi d'uso**
Esistono molti scenari pratici in cui il comportamento predefinito di espansione non è desiderabile:
- **Report di riepilogo** che richiedono un layout compatto, con una sola riga per voce.
- **Elenchi di tag, etichette o parole chiave** che devono essere visualizzati come valori separati da virgole o barre verticali all'interno di una singola cella.
- **Chip di filtro o indicatori di stato** che raggruppano più valori in un unico punto per migliorare la leggibilità.
- **Flussi di elaborazione a valle**, come l'esportazione in CSV, il rendering in PDF o la stampa unione, che richiedono un singolo valore consolidato per cella anziché un intervallo espanso.
- **Compatibilità tra piattaforme**, in cui alcuni consumatori non possono gestire array che si estendono su più celle.

### **La lacuna che colma**
Senza un meccanismo integrato, gli sviluppatori sarebbero costretti a pre-elaborare i dati in JavaScript, unendo gli array in stringhe delimitate prima di associarli al `WorkbookDesigner`. Questa soluzione duplicherebbe la logica, complicherebbe i modelli di dati e aumenterebbe la probabilità di errori. Gli attributi `ArrayAsSingle` ed `ExtraDelimiter` eliminano la necessità di ricorrere a soluzioni alternative, gestendo la formattazione in modo dichiarativo direttamente nel tag di Smart Marker.

## **Vantaggi della funzionalità**
L'utilizzo degli attributi `ArrayAsSingle` ed `ExtraDelimiter` nei Smart Marker offre diversi vantaggi:
- **Contenimento in una singola cella**: il rendering di tutti gli elementi dell'array viene effettuato in una sola cella, mantenendo layout compatti e prevedibili.
- **Personalizzazione del delimitatore**: consente di specificare una stringa di separazione qualsiasi, ad esempio una virgola, un punto e virgola, un trattino, una barra verticale, un a capo o un testo personalizzato.
- **Formattazione guidata dal modello**: non è necessario scrivere codice aggiuntivo per pre-elaborare i dati; le regole di formattazione sono definite all'interno del tag di Smart Marker.
- **Report più puliti**: i dati di tipo array non spostano più il contenuto circostante del modello in righe o colonne diverse.
- **Tipi di dati versatili**: supporta stringhe, numeri, date e qualsiasi altro tipo di dati che possa essere unito mediante un delimitatore.
- **Compatibilità con le versioni precedenti**: quando gli attributi vengono omessi, il comportamento originale di espansione viene mantenuto, pertanto i modelli esistenti continuano a funzionare senza modifiche.

## **Come utilizzare la funzionalità**

### **Sintassi dello Smart Marker**
Gli attributi `ArrayAsSingle` ed `ExtraDelimiter` vengono passati come coppie chiave-valore tra le parentesi di uno Smart Marker standard. La sintassi generale è:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, WorkbookDesigner } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const product = {
                Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
            };
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Tags";
            cells.get("A2").value = '&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")';
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Product", product);
            designer.process();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_arraySingle.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

Il marcatore è composto dalle seguenti parti:
- `&=DataSource.ArrayProperty` — lo Smart Marker standard che fa riferimento alla proprietà di tipo array della sorgente dati associata.
- `arrayasSingle=true` — istruisce il motore a eseguire il rendering dell'intero array in una singola cella. Solo il valore `true` attiva il comportamento su singola cella.
- `extraDelimiter=", "` — definisce il separatore inserito tra gli elementi dell'array. Il valore è una stringa letterale; la stringa può essere vuota, contenere un solo carattere o più caratteri.

{{% alert color="primary" %}}
L'attributo `extraDelimiter` accetta una stringa letterale arbitraria, ad esempio un delimitatore di più caratteri, testo personalizzato o una sequenza di escape come `\n` per un output con elementi separati da un a capo. Se l'array è vuoto, la cella risultante viene lasciata vuota.
{{% /alert %}}

### **Flusso di lavoro passo per passo**
Il seguente flusso di lavoro descrive come eseguire il rendering di un array in una singola cella utilizzando gli Smart Marker.
1. **Preparare la sorgente dati**: creare un oggetto o una struttura dati che esponga una proprietà che restituisca un array. La proprietà può restituire un array di stringhe, numeri o valori di qualsiasi altro tipo supportato.
2. **Creare una cartella di lavoro di progettazione**: creare un nuovo `Workbook`, aggiungere una riga di intestazione e inserire in una cella uno Smart Marker che faccia riferimento alla proprietà di tipo array, utilizzando gli attributi `arrayasSingle` ed `extraDelimiter`.
3. **Istanziare il `WorkbookDesigner`**: creare un oggetto `WorkbookDesigner`, assegnargli la cartella di lavoro di progettazione e associare la sorgente dati tramite il metodo `setDataSource`.
4. **Elaborare i marcatori**: chiamare il metodo `workbookDesigner.process()` per elaborare gli Smart Marker e popolare la cartella di lavoro con i dati effettivi.
5. **Salvare il risultato**: salvare la cartella di lavoro risultante su disco in XLSX o in qualsiasi altro formato di file supportato.

### **Esempio di codice 1 — Rendering di base di un array di stringhe**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        class Student {
            constructor(scores) {
                this.Scores = scores;
            }
        }
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            document.getElementById("runExample").disabled = false;
            console.log("Aspose.Cells initialized");
        });
        document.getElementById("runExample").addEventListener("click", async () => {
            const student = new Student([95, 88, 76, 100, 67]);
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Scores";
            cells.get("A2").value = student.Scores.join(" - ");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById("downloadLink");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_numericArray.xlsx";
            downloadLink.style.display = "block";
            document.getElementById("result").innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Esempio di codice 2 — Array numerico con delimitatore personalizzato**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, WorkbookDesigner, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const order = {
                Items: ["Apple", "Banana", "Cherry", "Date"]
            };
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Sezione 1: Smart Marker predefinito - valori distribuiti orizzontalmente tra le celle
            cells.get("A1").value = "Default Spreading Behavior:";
            cells.get("A2").value = "&=Order.Items";
            // Sezione 2: Nuovo rendering in una singola cella utilizzando arrayasSingle e extraDelimiter
            cells.get("A4").value = "Single Cell Rendering (arrayasSingle=true):";
            cells.get("A5").value = '&=Order.Items(arrayasSingle=true, extraDelimiter="; ")';
            // Associa l'origine dati ed elabora gli Smart Marker
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Order", order);
            designer.process();
            // Salva il workbook risultante
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_comparison.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Esempio di codice 3 — Confronto tra il comportamento predefinito e quello di ArrayAsSingle**

### **Note e buone pratiche**
Quando si lavora con gli attributi `ArrayAsSingle` ed `ExtraDelimiter`, tenere presenti i seguenti aspetti:
- Il valore `extraDelimiter` viene trattato come una stringa letterale; effettuare l'escape di eventuali caratteri speciali che il processore del modello potrebbe interpretare.
- L'attributo `arrayasSingle` accetta un valore booleano (`true` / `false`). Solo `true` attiva il comportamento su singola cella; qualsiasi altro valore determina l'applicazione del comportamento predefinito di espansione.
- Se l'array è vuoto o nullo, la cella viene lasciata vuota oppure contiene una stringa vuota, a seconda del tipo di dati.
- La funzionalità è compatibile con sorgenti dati di tipo oggetto e tabulari, in cui una colonna può essere suddivisa in array.
- Per un output con elementi separati da un a capo, usare `\n` come valore del delimitatore.

## Articoli correlati
- [Aggiungere campi filtro a una tabella pivot in Aspose.Cells for JavaScript via C++](/cells/it/javascript-cpp/add-page-field-in-pivot-table/)
- [Applicare stili alle tabelle pivot in Aspose.Cells for JavaScript via C++](/cells/it/javascript-cpp/apply-style-to-pivot-table/)
- [Modificare il layout del campo pagina in una tabella pivot](/cells/it/javascript-cpp/change-page-field-layout/)
- [Convertire una sparkline in immagine e HTML in Aspose.Cells for JavaScript via C++](/cells/it/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Conversione di Excel nel formato OFD](/cells/it/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}