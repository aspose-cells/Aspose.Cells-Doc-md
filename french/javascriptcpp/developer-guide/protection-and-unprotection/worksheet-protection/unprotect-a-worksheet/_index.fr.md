---
title: Déprotéger une feuille avec JavaScript via C++
linktitle: Déprotéger une feuille de calcul
type: docs
weight: 20
url: /fr/javascript-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Si un développeur doit supprimer la protection d'une feuille de calcul protégée pendant l'exécution pour pouvoir apporter des modifications au fichier? Cela peut être facilement fait avec Aspose.Cells.

{{% /alert %}}

## **Déprotéger une feuille de calcul**

### **Utilisation de Microsoft Excel**

Pour supprimer la protection d'une feuille de calcul:

Dans le menu **Outils**, sélectionnez **Protection** puis **Déprotéger la feuille**. La protection sera levée sauf si la feuille est protégée par un mot de passe. Dans ce cas, une fenêtre de dialogue demande le mot de passe. Saisissez-le et la feuille sera déprotégée.

### **Déprotéger une feuille de calcul simplement protégée en utilisant Aspose.Cells**

Une feuille de calcul peut être déprotégée en appelant la méthode [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--) de la classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Une feuille simplement protégée n'est pas protégée par un mot de passe. Ces feuilles peuvent être déprotégées en appelant la méthode [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--) sans passer de paramètre.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Unprotect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unprotecting the worksheet without a password
            worksheet.unprotect();

            // Saving the Workbook in Excel97To2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Déprotéger une feuille de calcul protégée par mot de passe à l'aide d'Aspose.Cells**

Une feuille protégée par mot de passe est une feuille qui est protégée avec un mot de passe. Ces feuilles peuvent être déprotégées en appelant une version surchargée de la méthode [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--) qui prend le mot de passe en paramètre.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unprotecting the worksheet with a password (empty password in original code)
            worksheet.unprotect("");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
