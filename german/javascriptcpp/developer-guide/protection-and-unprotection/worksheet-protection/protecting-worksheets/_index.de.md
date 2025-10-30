---
title: Arbeitsblätter mit JavaScript über C++ schützen
linktitle: Arbeitsblätter schützen
type: docs
weight: 10
url: /de/javascript-cpp/protecting-worksheets/
description: Erfahren Sie, wie Sie Arbeitsblätter in Excel mit Aspose.Cells for JavaScript über C++ schützen, einschließlich des Schutzes von Zeilen, Spalten und spezifischen Zellen.
---

{{% alert color="primary" %}}

Wenn ein Arbeitsblatt geschützt ist, sind die Aktionen, die ein Benutzer durchführen kann, eingeschränkt. Zum Beispiel können sie keine Daten eingeben, Zeilen oder Spalten einfügen oder löschen usw.

{{% /alert %}}

## **Arbeitsblätter schützen**

### **Einführung**

Die allgemeinen Schutzeinstellungen in Microsoft Excel sind:

- Inhalt
- Objekte
- Szenarien

Geschützte Arbeitsblätter verbergen oder schützen keine sensiblen Daten, daher unterscheidet es sich von der Datei-Verschlüsselung. Allgemein ist der Arbeitsblattschutz für Präsentationszwecke geeignet. Er verhindert, dass der Endbenutzer Daten, Inhalt und Formatierung im Arbeitsblatt ändert.

### **Ein Arbeitsblatt schützen**

Aspose.Cells stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-Klasse enthält eine [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)-Sammlung, die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) dargestellt.

Die [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-Klasse bietet die [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-)-Methode, die zum Anwenden des Schutzes auf das Arbeitsblatt verwendet wird. Die [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-)-Methode akzeptiert die folgenden Parameter:

- Schutzttyp, der Typ des Schutzes, der auf das Arbeitsblatt angewendet werden soll. Der Schutzttyp wird mithilfe der Enumeration [**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype) angewendet.
- Neues Passwort, das neue Passwort, das zum Schutz des Arbeitsblatts verwendet wird.
- Altes Kennwort, das alte Kennwort, wenn das Arbeitsblatt bereits passwortgeschützt ist. Wenn das Arbeitsblatt noch nicht geschützt ist, dann einfach null übergeben.

Das [**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype)-Enum enthält die folgenden vordefinierten Schutzarten:

|**Schutztypen**|**Beschreibung**|
| :- | :- |
|All|Der Benutzer kann nichts auf diesem Arbeitsblatt ändern|
|Contents|Der Benutzer kann keine Daten in dieses Arbeitsblatt eingeben|
|Objects|Der Benutzer kann Zeichenobjekte nicht ändern|
|Scenarios|Der Benutzer kann gespeicherte Szenarien nicht ändern|
|Structure|Der Benutzer kann die Struktur nicht ändern|
|Windows|Der Schutz wird auf Fenster angewendet|
|None|Es ist kein Schutz angewendet|

Das folgende Beispiel zeigt, wie ein Arbeitsblatt mit einem Passwort geschützt wird.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Protect Worksheet Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Ensure Aspose.Cells is initialized before proceeding
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Protecting the worksheet with a password
            worksheet.protect(ProtectionType.All, "aspose", null);

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Nachdem der obige Code zum Schutz des Arbeitsblatts verwendet wurde, können Sie den Schutz auf dem Arbeitsblatt überprüfen, indem Sie es öffnen. Sobald Sie die Datei öffnen und versuchen, einige Daten in das Arbeitsblatt einzufügen, sehen Sie den folgenden Dialog:

|**Ein Dialog, der darauf hinweist, dass ein Benutzer das Arbeitsblatt nicht ändern kann**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Um am Arbeitsblatt zu arbeiten, heben Sie den Schutz des Arbeitsblatts auf, indem Sie im **Werkzeuge**-Menüpunkt **Schutz** und dann **Arbeitsblatt entsperren** auswählen.

Nachdem Sie den Menüpunkt Arbeitsblatt entsperren ausgewählt haben, öffnet sich ein Dialog, der Sie auffordert, das Passwort einzugeben, damit Sie am Arbeitsblatt arbeiten können, wie unten gezeigt:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Einige Zellen im Arbeitsblatt mit Microsoft Excel schützen**

Es kann bestimmte Szenarien geben, bei denen Sie nur einige Zellen im Arbeitsblatt sperren müssen. Wenn Sie bestimmte Zellen im Arbeitsblatt sperren möchten, müssen Sie alle anderen Zellen im Arbeitsblatt entsperren. Alle Zellen in einem Arbeitsblatt sind bereits für das Sperren initialisiert; Sie können dies überprüfen, indem Sie eine beliebige Excel-Datei in MS Excel öffnen und auf **Format | Zellen...** klicken, um das **Zellen formatieren**-Dialogfeld zu öffnen, dann die Registerkarte **Schutz** anklicken und sehen, dass das Kontrollkästchen "Gesperrt" standardmäßig aktiviert ist.

Die folgenden Punkte beschreiben, wie man einige Zellen mit MS Excel sperrt. Diese Methode gilt für Microsoft Office Excel 97, 2000, 2002, 2003 und spätere Versionen.

1. Wählen Sie das gesamte Arbeitsblatt aus, indem Sie auf die Schaltfläche **Alles auswählen** klicken (das graue Rechteck direkt über der Zeilennummer von Zeile 1 und links von Spaltenbuchstabe A).
2. Klicken Sie im **Format**-Menü auf **Zellen**, klicken Sie auf die Registerkarte **Schutz** und deaktivieren Sie das Kontrollkästchen **Gesperrt**.
   Dies entsperrt alle Zellen im Arbeitsblatt.
   Wenn der Befehl **Zellen** nicht verfügbar ist, können Teile des Arbeitsblatts bereits gesperrt sein. Klicken Sie im **Menü Extras** auf **Schutz**, und klicken Sie dann auf **Arbeitsblatt schützen**.
3. Wählen Sie nur die Zellen aus, die Sie sperren möchten, und wiederholen Sie Schritt 2, aber dieses Mal aktivieren Sie das Kontrollkästchen **Gesperrt**.
4. Beim **Tools**-Menü auf **Schutz** zeigen, klicken Sie auf **Blatt schützen** und dann auf **OK**.
5. Im Dialogfeld **Blatt schützen** haben Sie die Möglichkeit, ein Passwort festzulegen und die Elemente auszuwählen, die Benutzer ändern dürfen.

### **Einige Zellen im Arbeitsblatt mit Aspose.Cells schützen**

In dieser Methode verwenden wir nur die Aspose.Cells API, um die Aufgabe auszuführen.

Beispiel: Das folgende Beispiel zeigt, wie man wenige Zellen im Arbeitsblatt schützt. Es entsperrt zuerst alle Zellen im Arbeitsblatt und sperrt dann 3 Zellen (A1, B1, C1). Schließlich schützt es das Arbeitsblatt. Das Objekt [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) enthält eine boolesche Eigenschaft, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Sie können die Eigenschaft [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) auf true oder false setzen und die Methode *Column/Row.applyStyle()* anwenden, um die Zeile/Spalte mit den gewünschten Attributen zu sperren oder zu entsperren.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unlock Columns and Protect Specific Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            await readyPromise;

            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object
            const styleflag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                styleflag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, styleflag);
            }

            // Lock the three cells...i.e. A1, B1, C1.
            style = sheet.cells.get("A1").style;
            style.isLocked = true;
            sheet.cells.get("A1").style = style;

            style = sheet.cells.get("B1").style;
            style.isLocked = true;
            sheet.cells.get("B1").style = style;

            style = sheet.cells.get("C1").style;
            style.isLocked = true;
            sheet.cells.get("C1").style = style;

            // Finally, Protect the sheet now.
            sheet.protect(ProtectionType.All);

            // Save the excel file and provide download link
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Schützen Sie eine Zeile im Arbeitsblatt**

Aspose.Cells ermöglicht es Ihnen, jede Zeile im Arbeitsblatt bequem zu sperren. Hier können wir die [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-)-Methode der [**Aspose.Cells.Row**](https://reference.aspose.com/cells/javascript-cpp/row)-Klasse verwenden, um [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) auf eine bestimmte Zeile im Arbeitsblatt anzuwenden. Diese Methode nimmt zwei Argumente: ein [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt und ein [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag)-Objekt, das alle Mitglieder im Zusammenhang mit angewendeter Formatierung enthält.

Das folgende Beispiel zeigt, wie man eine Zeile im Arbeitsblatt schützt. Es entsperrt zuerst alle Zellen im Arbeitsblatt und sperrt dann die erste Zeile. Schließlich schützt es das Arbeitsblatt. Das [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt enthält eine boolesche Eigenschaft, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Sie können die Eigenschaft [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) auf true oder false setzen, um die Zeile/Spalte mit dem [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag)-Objekt zu sperren oder zu entsperren.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType, Utils } = AsposeCells;

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
            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first row style.
            style = sheet.cells.rows.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Set the lock setting.
            flag.locked = true;

            // Apply the style to the first row.
            sheet.cells.applyRowStyle(0, style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and protected. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Schützen Sie eine Spalte im Arbeitsblatt**

Aspose.Cells ermöglicht es Ihnen, jede Spalte im Arbeitsblatt bequem zu sperren. Hier können wir die [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/column/#applyStyle-style-styleflag-)-Methode der [**Aspose.Cells.Column**](https://reference.aspose.com/cells/javascript-cpp/column)-Klasse verwenden, um [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) auf eine bestimmte Spalte im Arbeitsblatt anzuwenden. Diese Methode nimmt zwei Argumente: ein [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt und ein [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag)-Objekt, das alle Mitglieder im Zusammenhang mit angewendeter Formatierung enthält.

Das folgende Beispiel zeigt, wie man eine Spalte im Arbeitsblatt schützt. Es entsperrt zuerst alle Zellen im Arbeitsblatt und sperrt dann die erste Spalte. Schließlich schützt es das Arbeitsblatt. Das [**Style**](https://reference.aspose.com/cells/javascript-cpp/style)-Objekt enthält eine boolesche Eigenschaft, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Sie können die Eigenschaft [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) auf true oder false setzen, um die Zeile/Spalte mit dem [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag)-Objekt zu sperren oder zu entsperren.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Unlock Columns and Protect Sheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
                // If no file provided, a new workbook will be created
                document.getElementById('result').innerHTML = '<p style="color: orange;">No file selected. A new workbook will be created and processed.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Processing selected file...</p>';
            }

            await readyPromise;

            // Load workbook from file if provided, otherwise create new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a worksheet object and obtain the first sheet.
            const sheet = workbook.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first column style.
            style = sheet.cells.columns.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Apply the style to the first column.
            sheet.cells.columns.get(0).applyStyle(style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Benutzern das Bearbeiten von Bereichen ermöglichen**

Das folgende Beispiel zeigt, wie man Benutzern das Bearbeiten eines Bereichs in einem geschützten Arbeitsblatt erlaubt.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Protect Range</title>
    </head>
    <body>
        <h1>Protect Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Instantiate a new or loaded Workbook
            let book;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                book = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                book = new Workbook();
            }

            // Get the first (default) worksheet
            const sheet = book.worksheets.get(0);

            // Get the Allow Edit Ranges
            const allowRanges = sheet.allowEditRanges;

            // Define ProtectedRange
            let protected_range;

            // Create the range
            const idx = allowRanges.add("r2", 1, 1, 3, 3);
            protected_range = allowRanges.get(idx);

            // Specify the password
            protected_range.password = "123";

            // Protect the sheet
            sheet.protect(ProtectionType.All);

            // Save the Excel file
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'protectedrange.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Range Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Protected range added and sheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
