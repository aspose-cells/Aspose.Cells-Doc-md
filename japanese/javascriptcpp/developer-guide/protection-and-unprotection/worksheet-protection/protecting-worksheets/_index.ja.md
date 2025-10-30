---
title: C++を利用したJavaScriptによるワークシートの保護
linktitle: ワークシートの保護
type: docs
weight: 10
url: /ja/javascript-cpp/protecting-worksheets/
description: Excelでのワークシートの保護方法を学びます。C++を利用したAspose.Cells for JavaScriptを使って、行、列、特定のセルの保護も含めて解説します。
---

{{% alert color="primary" %}}

ワークシートが保護された場合、ユーザーが行えない操作が制限されます。例えば、データ入力、行や列の挿入・削除などです。

{{% /alert %}}

## **ワークシートを保護**

### **紹介**

Microsoft Excelの一般的な保護オプション:

- コンテンツ
- オブジェクト
- シナリオ

保護されたワークシートは機密データを非表示または保護しないため、ファイルの暗号化とは異なります。一般的に、ワークシートの保護はプレゼンテーション目的に適しています。ユーザーはワークシート内のデータ、コンテンツ、および書式設定を変更できなくなります。

### **ワークシートを保護する**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスは、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスによって表されます。

[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは、ワークシートに保護を適用するための[**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-)メソッドを提供します。[**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-)メソッドは、次のパラメータを受け取ります：

- 保護の種類、ワークシートに適用する保護の種類。保護の種類はProtectionType列挙型のヘルプを使用して適用されます。
- 新しいパスワード、ワークシートを保護するために使用する新しいパスワード。
- 古いパスワード、ワークシートがすでにパスワードで保護されている場合は、古いパスワードを渡します。ワークシートがすでに保護されていない場合は、nullを渡します。

[**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype)列挙型は、次の事前定義された保護タイプを含みます：

|**保護タイプ**|**説明**|
| :- | :- |
|All|このワークシート上で何も変更できない|
|Contents|このワークシートにデータを入力できない|
|Objects|描画オブジェクトを変更できない|
|Scenarios|保存されたシナリオを変更できない|
|Structure|ユーザーは構造を変更できません|
|Windows|保護はウィンドウに適用されています|
|None|保護は適用されていません|

以下の例は、ワークシートにパスワードを設定して保護する方法を示しています。

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

上記のコードを使用してワークシートを保護した後、ワークシートの保護を開いて確認することができます。ファイルを開いてワークシートにデータを追加しようとすると、次のダイアログが表示されます:

|**ユーザーがワークシートを変更できないと警告するダイアログ**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

ワークシートで作業するには、**ツール**メニューの**保護**から**ワークシートの保護を解除**を選択します。

ワークシートの保護を解除メニュー項目を選択すると、次のようなダイアログが開きます。パスワードを入力するように求められます。

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Microsoft Excelを使用してワークシート内の一部のセルを保護する**

特定のシナリオでは、ワークシート内の一部のセルだけをロックする必要がある場合があります。特定のセルだけをロックしたい場合は、他のすべてのセルのロックを解除する必要があります。ワークシート内のすべてのセルは既にロック状態に初期設定されています。これは、MS Excelで任意のExcelファイルを開き、**書式 | セル**をクリックして**セルの書式設定**ダイアログボックスを表示し、次に**保護**タブをクリックして「ロック済み」のチェックボックスがデフォルトでONになっていることを確認できます。

以下のポイントは、MS Excelを使ってセルのロックを行う方法を示しています。この方法はMicrosoft Office Excel 97、2000、2002、2003やそれ以降のバージョンに適用されます。

1. **全選択**ボタン(行1の行番号の直上および列文字Aの左直上の灰色の四角形)をクリックしてワークシート全体を選択します。
2. **書式**メニューから**セル**をクリックし、**保護**タブを選択して、**ロック**のチェックを外す。
   これにより、ワークシート上のすべてのセルのロックが解除されます。
   **セル**コマンドが利用できない場合、ワークシートの一部は既にロックされている可能性があります。 **ツール**メニューで、**保護**を指して、**ワークシートの保護を解除**をクリックします。
3. ロックしたいセルだけを選択し、ステップ2を繰り返しますが、その際は**ロック**のチェックを入れます。
4. **ツール**メニューから**保護**にマウスを合わせて**シートの保護**をクリックし、その後**OK**をクリックします。
5. **シートの保護**ダイアログボックスで、パスワードを指定したり、ユーザーに変更させたい要素を選択できます。

### **Aspose.Cellsを使ったワークシートの一部セルの保護**

この方法では、Aspose.Cells APIのみを使用してタスクを実行します。

例：以下は、ワークシートの一部セルを保護する方法の例です。最初にすべてのセルのロックを解除し、その後、セル（A1、B1、C1）をロックします。最後に、ワークシートを保護します。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトには、ブール型の[**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)が含まれています。[**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)プロパティをtrueまたはfalseに設定し、*Column/Row.applyStyle()*メソッドを適用して行または列のロック状態を制御できます。

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

### **ワークシート内の行を保護する**

Aspose.Cellsを使えば、任意の行を簡単にロックできます。ここでは、[**Aspose.Cells.Row**](https://reference.aspose.com/cells/javascript-cpp/row)クラスの[**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-)メソッドを使用して、特定の行に[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)を適用します。このメソッドは二つの引数を取ります：[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトと、適用されるフォーマットに関するすべてのメンバーを持つ[**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag)オブジェクト。

以下の例は、ワークシートの行を保護する方法を示しています。最初にすべてのセルのロックを解除し、その後最初の行だけをロックします。最後に、ワークシートを保護します。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトには、ブール型の[**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)があります。[**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)プロパティをtrueまたはfalseに設定して、行または列のロックを制御します。

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

### **ワークシート内の列を保護する**

Aspose.Cellsを使えば、任意の列を簡単にロックできます。ここでは、[**Aspose.Cells.Column**](https://reference.aspose.com/cells/javascript-cpp/column)クラスの[**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/column/#applyStyle-style-styleflag-)メソッドを使用して、特定の列に[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)を適用します。このメソッドは二つの引数を取ります：[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトと、適用されるフォーマットに関するすべてのメンバーを持つ[**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag)オブジェクト。

以下の例は、ワークシートの列を保護する方法を示しています。最初にすべてのセルのロックを解除し、その後最初の列だけをロックします。最後に、ワークシートを保護します。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトには、ブール型の[**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)があります。[**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--)プロパティをtrueまたはfalseに設定して、行または列のロックを制御します。

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

### **ユーザーに範囲の編集を許可する**

次の例は、保護されたワークシートで範囲の編集を許可する方法を示しています。

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
