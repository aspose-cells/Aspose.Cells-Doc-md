---
title: Proteggi o Rimuovi la Protezione del Workbook condiviso con JavaScript via C++
linktitle: Proteggere o sbloccare la cartella di lavoro condivisa
type: docs
weight: 10
url: /it/javascript-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **Possibili Scenari di Utilizzo**

 Puoi proteggere o rimuovere la protezione dal workbook condiviso con Microsoft Excel come mostrato nella schermata successiva. Aspose.Cells for JavaScript via C++ supporta anche questa funzione con i metodi [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#protectSharedWorkbook-string-) e [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#unprotectSharedWorkbook-string-).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Proteggi o rimuovi la protezione con password dalla cartella di lavoro condivisa**

Il seguente codice di esempio crea una cartella di lavoro e la protegge abilitando la condivisione, quindi la salva come [file Excel di output](55541777.xlsx). La schermata mostra che quando si tenta di sbloccarla, Microsoft Excel richiede di inserire la password per sbloccarla.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Shared Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Creating an empty Workbook
            const workbook = new Workbook();

            // Protect the Shared Workbook with Password
            workbook.protectSharedWorkbook("1234");

            // Uncomment this line to Unprotect the Shared Workbook
            // workbook.unprotectSharedWorkbook("1234");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputProtectSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
