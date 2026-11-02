---
title: Suddivisione dei file Excel in più file
linktitle: Suddivisione dei file Excel in più file
description: Aspose.Cells for JavaScript via C++ è una libreria JavaScript via C++ per lavorare con file di foglio elettronico, che supporta la suddivisione di un singolo file Excel in più file. Questo articolo illustrerà come suddividere i file Excel copiando ogni foglio di lavoro in una cartella di lavoro separata e copiando intervalli di celle specifici in altre cartelle di lavoro.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++ library, foglio di calcolo, dividere file Excel, copiare foglio di lavoro, copiare intervallo, più cartelle di lavoro, salvare come file separati
type: docs
weight: 195
url: /it/javascript-cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ supporta la suddivisione di un singolo file Excel in più file. Esistono due modalità principali per farlo: (1) copiando ogni foglio di lavoro della cartella di lavoro di origine in una nuova cartella di lavoro e salvandola come file separato, e (2) copiando un intervallo di celle specifico da un foglio di lavoro in una nuova cartella di lavoro. Entrambi gli approcci sono utili quando è necessario distribuire sottoinsiemi di dati, creare report più piccoli per destinatari diversi o isolare dati per l'elaborazione individuale.
{{% /alert %}}

## **Introduzione**
Esistono molti scenari reali in cui uno sviluppatore deve dividere un singolo file Excel in diversi file più piccoli. Ad esempio, una cartella di lavoro può contenere un foglio per ogni dipartimento, e ogni responsabile di dipartimento ha bisogno di ricevere solo il proprio foglio. In altri casi, potresti voler estrarre una tabella o un blocco di dati specifico da un foglio e inviarlo come file autonomo via email, senza esporre il resto della cartella di lavoro. Grandi cartelle di lavoro consolidate possono anche dover essere suddivise in pezzi più piccoli per una gestione più semplice, un caricamento più veloce o una successiva elaborazione da parte di altri sistemi.  
Aspose.Cells for JavaScript via C++ fornisce due approcci flessibili per questa attività. Il primo approccio itera attraverso tutti i fogli della cartella di lavoro di origine e copia il loro contenuto in una nuova istanza di `Workbook`, salvando ciascuno come file separato. Il secondo approccio si concentra su un intervallo di celle specifico all'interno di un foglio e copia solo quell'intervallo in una nuova cartella di lavoro. In entrambi i casi, il flusso generale è lo stesso: caricare la cartella di lavoro di origine usando la classe `Workbook`, accedere ai dati pertinenti tramite gli oggetti `Worksheet` e `Cells`, trasferire il contenuto in una `Workbook` di destinazione e quindi salvare la destinazione su disco.

## **Suddivisione di un file Excel copiando ogni foglio di lavoro in una nuova cartella di lavoro**

### **Panoramica dell'approccio**
In questo approccio, la cartella di lavoro di origine viene aperta una sola volta e, per ogni `Worksheet` nella sua raccolta `Worksheets`, viene creata una nuova `Workbook` di destinazione. Il contenuto del foglio di lavoro di origine viene quindi copiato nel primo foglio della cartella di lavoro di destinazione, e la cartella di lavoro di destinazione viene salvata come file il cui nome deriva dal nome del foglio di lavoro di origine. Il risultato è un file di output per ogni foglio, con ciascun file contenente i dati di un singolo foglio di origine.  
Questo metodo è la scelta giusta quando ogni foglio della cartella di lavoro di origine rappresenta un'unità di informazione logicamente indipendente (come un dipartimento, una regione, un mese o una linea di prodotto) e si desidera consegnare o elaborare ogni unità separatamente.

### **Passaggi**
I seguenti passaggi descrivono come suddividere un file Excel copiando ogni foglio di lavoro in una nuova cartella di lavoro:
1. Apri il file Excel di origine istanziando un oggetto `Workbook` e passando il percorso del file al suo costruttore.
2. Itera attraverso la raccolta `Workbook.Worksheets` usando un ciclo `for` o `for...of` in modo che ogni `Worksheet` nel file di origine sia elaborato.
3. All'interno del ciclo, crea una nuova istanza di `Workbook` di destinazione (una cartella di lavoro vuota) per il foglio corrente.
5. Copia il contenuto del foglio di origine nel foglio di destinazione. Questo può essere fatto iterando le celle della raccolta `Cells` del foglio di origine e scrivendo i loro valori nelle celle corrispondenti del foglio di destinazione, oppure usando il metodo `Cells.Copy` per trasferire un intero intervallo in un'unica operazione.
6. Costruisci un percorso di file di output che includa il nome del foglio di origine (ad esempio, `dataDir + worksheet.Name + ".xls"`) in modo che ogni file generato abbia un nome univoco.
7. Chiama il metodo `Workbook.Save` della destinazione per scrivere il file su disco.
8. Ripeti i passaggi 3‑7 per il foglio successivo fino a quando tutti i fogli non sono stati elaborati.

### **Esempio di codice**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls" />
        <button id="runExample">Run Example</button>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                const result = document.getElementById('result');
                try {
                    const fileInput = document.getElementById('fileInput');
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an .xls file.</p>';
                        return;
                    }
                    result.innerHTML = '<p>Processing...</p>';
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    const downloadLinks = document.createElement('div');
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const sourceSheet = workbook.worksheets.get(i);
                        const sheetName = sourceSheet.name;
                        const destWorkbook = new Workbook();
                        const destIndex = destWorkbook.worksheets.add();
                        const destSheet = destWorkbook.worksheets.get(destIndex);
                        destSheet.name = sheetName;
                        destSheet.copy(sourceSheet);
                        const outputData = destWorkbook.save(AsposeCells.SaveFormat.Excel97To2003);
                        const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
                        const downloadLink = document.createElement('a');
                        downloadLink.href = URL.createObjectURL(blob);
                        downloadLink.download = `${sheetName}.xls`;
                        downloadLink.textContent = `Download ${sheetName}.xls`;
                        downloadLink.style.display = 'block';
                        downloadLink.style.marginTop = '8px';
                        downloadLinks.appendChild(downloadLink);
                    }
                    result.innerHTML = '<p style="color: green;">Done! Click a download link to get the result file.</p>';
                    result.appendChild(downloadLinks);
                } catch (error) {
                    console.error(error);
                    const errorMessage = document.createElement('p');
                    errorMessage.style.color = 'red';
                    errorMessage.textContent = `Error: ${error instanceof Error ? error.message : error}`;
                    result.replaceChildren(errorMessage);
                }
            });
        </script>
    </body>
</html>
```

L'output previsto è un insieme di nuovi file nella directory dei dati, un file per ogni foglio della cartella di lavoro di origine. Ogni file è denominato in base al foglio corrispondente e contiene i dati (e facoltativamente la formattazione) di quel singolo foglio.

## **Suddivisione di un file Excel copiando un intervallo in una nuova cartella di lavoro**

### **Panoramica dell'approccio**
A volte i dati che devi suddividere non corrispondono a un intero foglio di lavoro, ma a una specifica regione rettangolare di un foglio, come `A1:D10` o un intervallo denominato che rappresenta una tabella particolare. In questi casi, copiare interi fogli è uno spreco, ed è necessario un approccio più preciso: identificare l'intervallo di origine, copiare solo quell'intervallo in una nuova cartella di lavoro e salvare il nuovo file.  
Questo approccio è ideale quando vuoi estrarre una singola tabella, blocco di report o area di dati da un foglio più grande, scartando tutto il contenuto non correlato. È anche utile per esportare regioni selezionate dall'utente di un foglio come file autonomi.

### **Passaggi**
I seguenti passaggi descrivono come suddividere un file Excel copiando un intervallo specifico in una nuova cartella di lavoro:
1. Apri il file Excel di origine istanziando un oggetto `Workbook` con il percorso del file.
2. Recupera il `Worksheet` di destinazione che contiene l'intervallo da copiare, sia per indice (ad esempio, il primo foglio) sia per nome dalla raccolta `Worksheets`.
3. Identifica l'intervallo da copiare. Può trattarsi di un intervallo di celle hard‑coded come `A1:C10`, di un intervallo denominato ottenuto tramite la raccolta `Worksheet.Cells`, oppure di un intervallo creato con `Worksheet.Cells.CreateRange`.
4. Crea una nuova istanza di `Workbook` di destinazione.
5. Accedi al primo `Worksheet` della cartella di lavoro di destinazione (il foglio predefinito).
6. Copia l'intervallo di origine nel foglio di destinazione, tipicamente a partire dalla cella `A1`. Il metodo `Cells.Copy` sulla raccolta `Cells` di destinazione può essere usato per copiare un intero intervallo, oppure puoi iterare le celle dell'intervallo di origine e scrivere i loro valori nelle celle di destinazione con `PutValue`. È possibile fornire `CopyOptions` opzionali per controllare cosa viene trasferito (solo valori, valori e stili, formule, ecc.).
7. Salva la cartella di lavoro di destinazione in un nuovo percorso di file su disco usando il metodo `Workbook.Save`.

### **Esempio di codice**
L'output previsto è un singolo nuovo file nella directory dei dati che contiene solo i valori (e facoltativamente la formattazione) dell'intervallo specificato estratto dalla cartella di lavoro di origine. Il file di destinazione non ha alcuna relazione con altri dati nel file di origine; contiene solo l'intervallo estratto, a partire dalla cella `A1` del suo primo foglio.

## Articoli correlati
- [Aggiungere campi filtro a una Pivot Table in Aspose.Cells for JavaScript via C+](/cells/it/javascript-cpp/add-page-field-in-pivot-table/)
- [Applicare stili alle Pivot Tables in Aspose.Cells for JavaScript via C+](/cells/it/javascript-cpp/apply-style-to-pivot-table/)
- [Modificare layout del campo pagina nella Pivot Table](/cells/it/javascript-cpp/change-page-field-layout/)
- [Convertire Sparkline in immagine e HTML in Aspose.Cells for JavaScript via C+](/cells/it/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Conversione di Excel nel formato OFD](/cells/it/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}