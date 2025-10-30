---
title: JavaScriptを通じて埋め込みOLEオブジェクトのクラス識別子を取得または設定する C++
linktitle: 埋め込みOLEオブジェクトのクラス識別子を取得または設定する
type: docs
weight: 200
url: /ja/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Aspose.Cellsを使用したJavaScriptで埋め込みOLEオブジェクトのクラス識別子の取得や設定方法を学びます。
---

## **可能な使用シナリオ**  
 Aspose.Cellsは、埋め込みOLEオブジェクトのクラス識別子を取得または設定できる[OleObject.classIdentifier](https://reference.aspose.com/cells/javascript-cpp/oleobject/#classIdentifier--) プロパティを提供します。OLEオブジェクトのクラス識別子は実際にはGUID（グローバルユニーク識別子）です。GUIDは常に16バイトの長さであり、クラス識別子も同じく16バイトです。これらはWindowsレジストリ内によく保存されており、ホストアプリケーションに埋め込みリソースを含むOLEオブジェクトの開き方について情報を提供します。

## **埋め込まれたOLEオブジェクトのクラス識別子を取得または設定する**  
次のスクリーンショットは、PowerPointの埋め込みOLEオブジェクトを含む[サンプルExcelファイル](5115190.xls)から読み取ったOLEオブジェクトのクラス識別子（GUID）を示しています。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **サンプルコード**  
次のサンプルコードとそのコンソール出力を参照してください。これはOLEオブジェクトのクラス識別子（GUID）を表示します。出力されたGUIDは、スクリーンショットに表示されているものと完全に一致します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract OLE Object Class Identifier (GUID)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access its first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first ole object inside the worksheet
            const oleObject = worksheet.oleObjects.get(0);

            // Convert 16-bytes array into GUID
            const bytes = new Uint8Array(oleObject.classIdentifier);
            const guid = bytes.reduce((acc, byte) => acc + String.fromCharCode(byte), '');

            // Print the GUID
            console.log(guid.toUpperCase());
            resultDiv.innerHTML = `<p style="color: green;">GUID: ${guid.toUpperCase()}</p>`;
        });
    </script>
</html>
```  
### **コンソール出力**  
上記のサンプルコードのコンソール出力は、[サンプルExcelファイル](5115190.xls)で実行したときのものです。

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}
