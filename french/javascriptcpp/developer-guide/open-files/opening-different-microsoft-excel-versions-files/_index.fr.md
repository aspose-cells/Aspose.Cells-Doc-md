---
title: Ouvrir différents fichiers de différentes versions de Microsoft Excel avec JavaScript via C++
linktitle: Ouvrir des fichiers de différentes versions de Microsoft Excel
type: docs
weight: 20
url: /fr/javascript-cpp/opening-different-microsoft-excel-versions-files/
description: Cet article explique comment ouvrir des fichiers de différentes versions d Excel en utilisant Aspose.Cells for JavaScript via C++.
keywords: JavaScript Ouvrir différents fichiers Microsoft Excel via C++, comment ouvrir des fichiers Excel encryptés en JavaScript via C++
---

{{% alert color="primary" %}}

Aspose.Cells peut ouvrir une gamme de fichiers de différentes versions de Microsoft Excel, tels que Microsoft Excel 95/97 - 2003, SpreadsheetML, ouverture de Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 XLSX ou des fichiers Excel chiffrés.

{{% /alert %}}

## **Comment ouvrir des fichiers de différentes versions de Microsoft Excel**

Une application doit souvent pouvoir ouvrir des fichiers Microsoft Excel créés dans différentes versions, par exemple Microsoft Excel 95, 97, ou Microsoft Excel 2007/2010/2013/2016/2019 et Office 365. Vous devrez peut-être charger un fichier dans l'un des plusieurs formats, y compris XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited ou TSV, CSV, ODS, etc. Utilisez le constructeur, ou spécifiez l'attribut de type [**fileFormat**](https://reference.aspose.com/cells/javascript-cpp/workbook/#fileFormat--) de la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) qui indique le format en utilisant l'énumération [**FileFormatType**](https://reference.aspose.com/cells/javascript-cpp/fileformattype).

L'énumération [**FileFormatType**](https://reference.aspose.com/cells/javascript-cpp/fileformattype) contient plusieurs formats de fichiers prédéfinis, dont certains sont donnés ci-dessous.

|**Types de formats de fichier**|**Description**|
| :- | :- |
|Csv|Représente un fichier CSV|
|Excel97To2003|Représente un fichier Excel 97 - 2003|
|Xlsx|Représente un fichier XLSX Excel 2007/2010/2013/2016/2019 et Office 365|
|Xlsm|Représente un fichier XLSM Excel 2007/2010/2013/2016/2019 et Office 365|
|Xltx|Représente un modèle de fichier XLTX Excel 2007/2010/2013/2016/2019 et Office 365
|Xltm|Représente un fichier activé par macro XLTM Excel 2007/2010/2013/2016/2019 et Office 365|
|Xlsb|Représente un fichier binaire XLSB Excel 2007/2010/2013/2016/2019 et Office 365|
|SpreadsheetML|Représente un fichier SpreadsheetML|
|Tsv|Représente un fichier de valeurs séparées par des tabulations|
|TabDelimited|Représente un fichier de texte à onglets|
|Ods|Représente un fichier ODS|
|Html|Représente un fichier HTML|
|Mhtml|Représente un fichier MHTML|

### **Ouvrir les fichiers Microsoft Excel 95/5.0**

Pour ouvrir un fichier Microsoft Excel 95/5.0, utilisez [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) et définissez l'attribut correspondant pour la classe [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) pour le fichier modèle à charger. Un fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[Fichier Excel95](Excel95.xls)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Excel95_5.0.xls Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Open Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions1 = new LoadOptions(LoadFormat.Auto);

            // Create a Workbook object and opening the file from the stream
            const wbExcel95 = new Workbook(new Uint8Array(arrayBuffer), loadOptions1);
            console.log("Microsoft Excel 95/5.0 workbook opened successfully!");

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 95/5.0 workbook opened successfully!</p>';
        });
    </script>
</html>
```

### **Ouvrir les fichiers Microsoft Excel 97-2003**

Pour ouvrir un fichier Microsoft Excel 97 - 2003, utilisez [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) et définissez l'attribut correspondant pour la classe [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) pour le fichier modèle à charger.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Excel 97-2003 Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel 97-2003 (.xls) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const loadOptions1 = new LoadOptions(LoadFormat.Excel97To2003);
            const wbExcel97 = new Workbook(new Uint8Array(arrayBuffer), loadOptions1);

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 97 - 2003 workbook opened successfully!</p>';

            const outputData = wbExcel97.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

### **Ouvrir les fichiers XLSX de Microsoft Excel 2007/2010/2013/2016/2019 et Office 365**

Pour ouvrir un format Microsoft Excel 2007/2010/2013/2016/2019 et Office 365, c'est-à-dire XLSX ou XLSB, indiquez le chemin du fichier. Vous pouvez également utiliser [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) et définir l'attribut/les options pertinents de la classe [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) pour le fichier modèle à charger.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Open Excel 2007 Xlsx Example</title>
    </head>
    <body>
        <h1>Open Excel 2007 Xlsx Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel .xlsx file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions specified by the LoadFormat.
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);

            // Create a Workbook object and open the file from the uploaded data
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            document.getElementById('result').innerHTML = '<p style="color: green;">Microsoft Excel 2007 - Office365 workbook opened successfully!</p>';

            // Save the workbook back to a downloadable file (unchanged content)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book_Excel2007_output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Opened Workbook';
        });
    </script>
</html>
```

### **Ouvrir des fichiers Excel chiffrés**

Il est possible de créer des fichiers Excel cryptés en utilisant Microsoft Excel. Pour ouvrir un fichier crypté, utilisez [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) et définissez ses attributs et options (par exemple, donnez un mot de passe) pour le fichier modèle à charger.
Un fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant:

[Encrypted Excel](EncryptedExcel.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Encrypted Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Open Encrypted Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an encrypted Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate LoadOptions
            const loadOptions = new LoadOptions();

            // Specify the password (converted from setPassword to property assignment)
            loadOptions.password = "1234";

            // Create a Workbook object opening the file from the uploaded bytes with loadOptions
            const wbEncrypted = new Workbook(new Uint8Array(arrayBuffer), loadOptions);
            console.log("Encrypted excel file opened successfully!");

            // Save the workbook so user can download it (using Excel97To2003 format for .xls)
            const outputData = wbEncrypted.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            // Use original name with a prefix to indicate it's been opened
            const originalName = file.name || 'output.xls';
            downloadLink.download = 'opened_' + originalName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Opened Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Encrypted Excel file opened successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Aspose.Cells prend également en charge l'ouverture de fichiers Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 protégés par mot de passe.
