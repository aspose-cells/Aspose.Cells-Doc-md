---
title: Inserimento di un'immagine in una cella
linktitle: Inserimento di un'immagine in una cella
description: Aspose.Cells for JavaScript via C++ è una libreria per lavorare con i file di fogli di calcolo. Questo articolo spiega come adattare esattamente un'immagine a una singola cella, sia posizionando un'immagine flottante sopra la cella sia incorporandola direttamente nella cella.
keywords: Aspose.Cells, libreria JavaScript via C++, foglio di calcolo, inserire immagine, incorporare immagine, immagine nella cella, adattare immagine alla cella, Pictures, EmbeddedImage
type: docs
weight: 80
url: /it/javascript-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre due modi distinti per associare un'immagine a una singola cella. Un'immagine flottante è una forma sul livello di disegno del foglio di lavoro che si sovrappone visivamente a un intervallo di celle, mentre un'immagine incorporata viene memorizzata nella cella stessa e ridimensionata automaticamente per adattarsi all'area di visualizzazione della cella. Scegliere l'approccio che meglio soddisfa i requisiti di disposizione.
{{% /alert %}}

## **Introduzione**
L'adattamento esatto di un'immagine a una singola cella è un requisito comune quando si progettano fogli di calcolo che fungono da report visivi, cataloghi di prodotti, elenchi dipendenti, dashboard o elenchi di inventario. Invece di estendere un'immagine su molte celle o di collocarla in modo approssimativo su un foglio di lavoro, potrebbe essere necessaria un'immagine pulita e associata a una cella, che rimanga allineata alla cella proprietaria.
Aspose.Cells supporta questo scenario in due modi complementari:
- **Approccio 1 — Posizionare un'immagine flottante sopra una cella.** Aggiungere un `Picture` al foglio di lavoro, impostarne il posizionamento con `picture.setPlacement(PlacementType.MoveAndSize)` e regolare le celle di ancoraggio mediante `picture.setUpperLeftRow()`, `picture.setUpperLeftColumn()`, `picture.setLowerRightRow()` e `picture.setLowerRightColumn()`, in modo che l'immagine copra esattamente una cella.
- **Approccio 2 — Incorporare un'immagine direttamente in una cella.** Assegnare alla cella un `Buffer` contenente i dati dell'immagine con `cell.setEmbeddedImage(imageBuffer)`. L'immagine viene ridimensionata automaticamente per adattarsi all'area di visualizzazione della cella e la accompany nella cella.
Il resto di questo articolo descrive entrambi gli approcci, spiega le API pertinenti e mostra come usarle nel codice.

## **Approccio 1: Posizionare un'immagine sopra una cella**
Un'immagine flottante è un oggetto `Picture` che si trova nel livello di disegno del foglio di lavoro. Sebbene non faccia parte di alcuna singola cella, è ancorato a un intervallo di celle. Le celle di ancoraggio dell'immagine — gli angoli superiore sinistro e inferiore destro — ne determinano l'estensione visiva nel foglio di lavoro. Per impostazione predefinita, un'immagine appena aggiunta si estende su più celle.
 affinché un'immagine flottante copra **esattamente una cella**, è necessario:
1. Aggiungere l'immagine con `worksheet.getPictures().add(row, column, imageBuffer)`, dove `imageBuffer` è un `Buffer` contenente i dati dell'immagine. La nuova immagine viene ancorata alla cella specificata.
2. Impostare i quattro valori di ancoraggio in modo che il rettangolo delimitante dell'immagine coincida con la cella di destinazione.
3. Chiamare `picture.setPlacement(PlacementType.MoveAndSize)` in modo che l'immagine si sposti e venga ridimensionata con la cella sottostante quando l'utente modifica la larghezza della colonna o l'altezza della riga.

### **Ancoraggio dell'immagine a una singola cella**
L'ancoraggio dell'immagine è definito da quattro accessor con indice a base zero:
- `picture.getUpperLeftRow()` e `picture.setUpperLeftRow(value)` — l'indice di riga del bordo superiore dell'immagine.
- `picture.getUpperLeftColumn()` e `picture.setUpperLeftColumn(value)` — l'indice di colonna del bordo sinistro dell'immagine.
- `picture.getLowerRightRow()` e `picture.setLowerRightRow(value)` — l'indice di riga del bordo inferiore dell'immagine. Per posizionare il bordo inferiore dell'immagine nella parte inferiore della riga `r`, impostare questo valore su `r + 1`.
- `picture.getLowerRightColumn()` e `picture.setLowerRightColumn(value)` — l'indice di colonna del bordo destro dell'immagine. Per posizionare il bordo destro dell'immagine nella parte destra della colonna `c`, impostare questo valore su `c + 1`.

{{% alert color="primary" %}}
Gli indici di riga e colonna in Aspose.Cells sono **a base zero**. La cella C6 ha indice di riga 5 e indice di colonna 2. Gli errori di una unità sull'ancoraggio inferiore destro sono la causa più comune di immagini che sembrano sovrapporsi a una cella adiacente.
{{% /alert %}}

### **Controllo del comportamento di posizionamento**
`picture.getPlacement()` e `picture.setPlacement(value)` usano il tipo enumerato `PlacementType` per controllare il comportamento dell'immagine quando l'utente ridimensiona la riga o la colonna sottostante. Il valore consigliato per un'immagine in una singola cella è `PlacementType.MoveAndSize`, che fa sì che l'immagine si sposti e venga ridimensionata insieme alla cella sottostante, preservandone l'adattamento esatto.

### **Istruzioni dettagliate**
1. Creare un nuovo `Workbook` (o aprirne uno esistente).
2. Accedere al `Worksheet` di destinazione tramite `workbook.getWorksheets().getAt(0)`.
3. Leggere il file immagine dal disco in un `Buffer`, ad esempio usando Node.js `fs.readFileSync`.
4. Chiamare `worksheet.getPictures().add(5, 2, imageBuffer)` per aggiungere un'immagine ancorata alla cella C6. Il metodo restituisce l'indice della nuova immagine nella raccolta `Pictures`; utilizzarlo per recuperare il corrispondente oggetto `Picture`.
5. Impostare le quattro coordinate di ancoraggio in modo che l'immagine copra solo la cella C6: `picture.setUpperLeftRow(5)`, `picture.setUpperLeftColumn(2)`, `picture.setLowerRightRow(6)` e `picture.setLowerRightColumn(3)`.
6. Chiamare `picture.setPlacement(PlacementType.MoveAndSize)` per mantenere l'immagine allineata a C6 quando la colonna o la riga viene ridimensionata.
7. Facoltativamente, aggiungere testo di esempio alle celle circostanti per dimostrare che solo la cella C6 contiene l'immagine.
8. Salvare la cartella di lavoro su disco come file `.xlsx`.
Il codice seguente dimostra l'approccio completo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,image/png" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const file = fileInput.files[0];
            if (!file) {
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Please select a PNG image.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const imageData = new Uint8Array(await file.arrayBuffer());
            const picIndex = worksheet.pictures.add(5, 2, imageData);
            const picture = worksheet.pictures.get(picIndex);
            picture.upperLeftRow = 5;
            picture.upperLeftColumn = 2;
            picture.lowerRightRow = 6;
            picture.lowerRightColumn = 3;
            picture.placement = AsposeCells.Drawing.PlacementType.MoveAndSize;
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Approccio 2: Incorporare un'immagine direttamente in una cella**
Aspose.Cells espone inoltre un meccanismo più semplice per le immagini associate alle celle: il metodo `cell.setEmbeddedImage(imageBuffer)`. L'assegnazione dei dati dell'immagine mediante questo metodo associa l'immagine alla cella stessa, come se fosse un contenuto in linea.

### **Funzionamento delle immagini incorporate**
- L'immagine viene memorizzata come parte del contenuto della cella anziché come forma sul livello di disegno.
- L'immagine viene ridimensionata automaticamente per adattarsi ai limiti di rendering della cella. Non sono necessarie coordinate di ancoraggio né impostazioni di posizionamento.
- La cella rimane una cella a tutti gli effetti, con un indirizzo che può essere referenziato dalle formule, usato nell'ordinamento come parte di una riga o impiegato in altre operazioni a livello di cella.
Questo rende `cell.setEmbeddedImage(imageBuffer)` l'opzione più concisa quando l'obiettivo è semplicemente «un'immagine che risiede all'interno di questa cella».

### **Istruzioni dettagliate**
1. Creare un nuovo `Workbook` (o aprirne uno esistente).
2. Accedere al `Worksheet` di destinazione tramite `workbook.getWorksheets().getAt(0)`.
3. Leggere il file immagine dal disco in un `Buffer`, ad esempio usando Node.js `fs.readFileSync`.
4. Ottenere un riferimento alla cella di destinazione — tramite `worksheet.getCells().get("C6")` oppure `worksheet.getCells().get(5, 2)`.
5. Passare il `Buffer` alla cella con `cell.setEmbeddedImage(imageBuffer)`.
6. Facoltativamente, regolare l'altezza della riga e la larghezza della colonna di destinazione per dare all'immagine incorporata un aspetto più prominente.
7. Salvare la cartella di lavoro su disco come file `.xlsx`.
Il codice seguente dimostra l'approccio completo.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,.jpg,.jpeg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const asposeReady = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files || fileInput.files.length === 0) {
                result.innerHTML = '<p style="color: red;">Please select an image file.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // Ottenere la cella di destinazione C6
            const cell = worksheet.cells.get("C6");
            // Leggere il file immagine in un array di byte
            const imageData = new Uint8Array(await fileInput.files[0].arrayBuffer());
            // Incorporare l'immagine direttamente nella cella
            cell.embeddedImage = imageData;
            // Se desiderato, regolare l'altezza della riga e la larghezza della colonna per rendere l'immagine incorporata più visibile
            worksheet.cells.setColumnWidth(2, 30); // Colonna C (indice 2)
            worksheet.cells.setRowHeight(5, 100); // Riga 6 (indice 5)
            // Salvare la cartella di lavoro risultante come file .xlsx
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Scelta dell'approccio appropriato**
Entrambi gli approcci producono un'immagine adattata a una singola cella, ma differiscono nel modo in cui l'immagine viene memorizzata e nel suo comportamento:
- **Utilizzare un'immagine flottante (Approccio 1) quando:**
  - È necessario un controllo più preciso del posizionamento, della stratificazione o dell'allineamento con altri oggetti di disegno.
  - Si desidera che l'immagine si comporti come una forma che può essere selezionata, riordinata o raggruppata con altre forme.
  - È richiesta la compatibilità con il codice esistente che già opera con la raccolta `Pictures` accessed tramite `worksheet.getPictures()`.
  - È necessario calcolare dinamicamente le coordinate di ancoraggio in base alla disposizione del foglio di lavoro.
- **Utilizzare un'immagine incorporata (Approccio 2) quando:**
  - Si desidera l'inserimento più semplice possibile di un'immagine in una cella.
  - L'immagine deve spostarsi con la cella come qualsiasi altro contenuto della cella.

## Articoli correlati
- [Telecamera Excel in Aspose.Cells for JavaScript via C++](/cells/it/javascript-cpp/excel-camera/)

{{< app/cells/assistant language="javascript-cpp" >}}