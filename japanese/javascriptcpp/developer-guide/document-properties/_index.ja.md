---
title: JavaScriptを使ったドキュメントプロパティの管理をC++で行う
linktitle: ドキュメントプロパティ
type: docs
weight: 80
url: /ja/javascript-cpp/managing-document-properties/
description: C++を使用したAspose.Cells for JavaScriptのAPIを通じてドキュメントプロパティの管理方法を学ぶ。
keywords: C++を使用したJavaScriptでのドキュメントプロパティ管理、プロパティの取得または設定、追加または削除（via JavaScript）、JavaScriptを通じたドキュメントプロパティの挿入または削除、C++のAspose.Cells for JavaScript APIを使用したドキュメントプロパティへのアクセス方法。
---

## **紹介**

Microsoft Excelはスプレッドシートファイルにプロパティを追加できる機能を提供します。これらのドキュメントプロパティは有用な情報を提供し、以下のように2つのカテゴリに分かれています。

- システム定義（組み込み）プロパティ: 組み込みプロパティには文書のタイトル、作成者名、文書の統計などの一般的な情報が含まれています。
- ユーザー定義（カスタム）プロパティ: ユーザーが名前-値のペアの形式で定義したカスタムプロパティ。

{{% alert color="primary" %}}

組み込みプロパティとカスタムプロパティについて知っておくべき最も重要な点は、組み込みプロパティはアクセスおよび変更が可能ですが、作成または削除はできないということです。一方、カスタムプロパティは作成および管理が可能です。

{{% /alert %}}

## **Microsoft Excelを使用してドキュメントプロパティを管理する方法**

Microsoft Excelでは、ExcelファイルのドキュメントプロパティをWYSIWYG方式で管理できます。Excel 2016で**プロパティ**ダイアログを開く手順については、下記をお尋ねください。

1. **ファイル**メニューから**情報**を選択します。

|**情報メニューを選択**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. **プロパティ**の見出しをクリックし、「詳細プロパティ」を選択します。

|**詳細プロパティの選択をクリック**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. ファイルのドキュメントプロパティを管理します。

|**プロパティダイアログ**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
プロパティダイアログでは、一般、概要、統計、内容、カスタムのような異なるタブがあります。各タブはファイルに関連する異なる種類の情報を設定するのに役立ちます。カスタムタブはカスタムプロパティを管理するために使用されます。

## **Aspose.Cellsを使用してドキュメントプロパティを操作する方法**

開発者はAspose.CellsのAPIを使用してドキュメントプロパティを動的に管理できます。この機能により、ファイルが受信された時点、処理された時点、タイムスタンプなどの有用な情報をファイルと一緒に保存できます。

{{% alert color="primary" %}}

C++を使用したAspose.Cells for JavaScriptは、出力ドキュメントにAPIとバージョン番号に関する情報を直接書き込みます。例えば、ドキュメントをPDFにレンダリングするとき、Aspose.Cells for JavaScriptは**アプリケーション**フィールドに「Aspose.Cells」、**PDFプロデューサー**フィールドに「Aspose.Cells v17.9」などを自動的に設定します。

この情報を出力ドキュメントから変更または削除するようC++に指示できないことに注意してください。

{{% /alert %}}

### **ドキュメントプロパティにアクセスする方法**

Aspose.Cells APIは、組み込みとカスタムの両方のタイプのドキュメントプロパティをサポートします。Aspose.Cellsの[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスはExcelファイルを表し、そのようにファイルと同様に、[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスは複数のワークシートを含むことができ、各ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスによって表され、ワークシートのコレクションは[**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)クラスによって表されます。

下記の説明のとおり、[**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)を使用してファイルのドキュメントプロパティにアクセスします。

- 組み込みドキュメントプロパティにアクセスするには、[**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--)を使用します。
- カスタムドキュメントのプロパティにアクセスするには[**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--)を使用します。

[**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--)と[**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--)はどちらも[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/)のインスタンスを返します。このコレクションは[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/)オブジェクトを含み、各オブジェクトは単一の組み込みまたはカスタムドキュメントプロパティを表します。

どのようにプロパティにアクセスするかはアプリケーションの要件次第です。すなわち、例の通り[**DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/)のインデックスまたは名前を使用します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Document Properties</title>
    </head>
    <body>
        <h1>Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Load Document Properties</button>
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object and opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Accessing a custom document property by using the property name
            const customProperty1 = customProperties.get("ContentTypeId");
            // Accessing the same custom document property by using the property index
            const customProperty2 = customProperties.get(0);

            const outputs = [];
            if (customProperty1) {
                outputs.push(`<p>${customProperty1.name} ${customProperty1.value}</p>`);
            }
            if (customProperty2) {
                outputs.push(`<p>${customProperty2.name} ${customProperty2.value}</p>`);
            }
            if (!outputs.length) {
                resultEl.innerHTML = '<p style="color: orange;">No custom document properties found.</p>';
            } else {
                resultEl.innerHTML = outputs.join('');
            }
        });
    </script>
</html>
```

[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/)クラスは、ドキュメントプロパティの名前、値、型を取得できます。

- プロパティ名を取得するには[**DocumentProperty.name()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#name--)を使用します。
- プロパティの値を取得するには、[**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--)を使用します。[**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--)は値をObjectとして返します。
- プロパティの型を取得するには、[**DocumentProperty.type()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#type--)を使用します。これは[**PropertyType**](https://reference.aspose.com/cells/javascript-cpp/propertytype/)列挙値のいずれかを返します。プロパティの型を取得した後、適切な型の値を取得するために**DocumentProperty.ToXXX**メソッドのいずれかを使用してください。これらのメソッドは下表に記載されています。

{{% alert color="primary" %}}

[**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/)クラスはまた、他のデータ型の値を返すメソッドセットも提供します。

{{% /alert %}}

|**メンバー名**|**説明**|**ToXXXメソッド**|
| :- | :- | :- |
|Boolean|プロパティのデータ型はブールです|ToBool|
|Date|プロパティのデータ型は日時です。Microsoft Excelでは日付部分のみが保存され、時刻は保存されません。|ToDateTime|
|Float|プロパティのデータ型はダブルです|ToDouble|
|Number|プロパティのデータ型はInt32です|ToInt|
|String|プロパティのデータ型はstring|ToString|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Retrieve Custom Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            let outputHtml = '<h2>Custom Document Properties</h2>';

            // Accessing a custom document property (first)
            const customProperty1 = customProperties.get(0);
            if (customProperty1) {
                // Storing the value of the document property as an object
                const objectValue = customProperty1.value;
                outputHtml += `<p><strong>${customProperty1.name}</strong> (type: ${customProperty1.type}) : ${objectValue}</p>`;
            } else {
                outputHtml += '<p>No first custom property found.</p>';
            }

            // Accessing a custom document property (second)
            const customProperty2 = customProperties.get(1);
            if (customProperty2) {
                // Checking the type of the document property and then storing the value according to that type
                if (customProperty2.type === AsposeCells.PropertyType.String) {
                    const value = customProperty2.value.toString();
                    outputHtml += `<p>${customProperty2.name} : ${value}</p>`;
                } else {
                    outputHtml += `<p>${customProperty2.name} (type: ${customProperty2.type}) : ${customProperty2.value}</p>`;
                }
            } else {
                outputHtml += '<p>No second custom property found.</p>';
            }

            resultDiv.innerHTML = outputHtml;
        });
    </script>
</html>
```

### **カスタムドキュメントプロパティの追加または削除方法**

このトピックの冒頭で既に説明した通り、ビルトインプロパティはシステム定義されたものであり、開発者は追加または削除することはできませんが、ユーザー定義のカスタムプロパティを追加または削除することは可能です。

### **カスタムプロパティの追加方法**

Aspose.Cells APIは、[**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-)メソッドを公開し、[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/)クラスにカスタムプロパティを追加できるようにしています。[**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-)メソッドは、Excelファイルにプロパティを追加し、新しいドキュメントプロパティの参照を[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/)オブジェクトとして返します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Custom Document Property</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object and opening the Excel file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Retrieve a list of all custom document properties of the Excel file
                const customProperties = workbook.customDocumentProperties;

                // Adding a custom document property to the Excel file
                customProperties.add("Publisher", "Aspose");

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'out_sample-document-properties.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Custom property added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```

### **「コンテンツにリンク」カスタムプロパティの構成方法**

指定された範囲の内容にリンクされたカスタムプロパティを作成するには、[**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-)メソッドを呼び出し、プロパティ名とソースを渡します。プロパティがコンテンツにリンクされているかどうかは、[**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#isLinkedToContent--)プロパティを使用して確認できます。さらに、[**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/)クラスの[**source()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#source--)プロパティを使用してソース範囲を取得可能です。

この例では、シンプルなテンプレートのMicrosoft Excelファイルを使用します。 ワークブックには、**MyRange**と表記された名前付き範囲があり、セルの値を参照しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Custom Document Properties</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.worksheets.customDocumentProperties;

            // Add link to content.
            customProperties.addLinkToContent("Owner", "MyRange");

            // Accessing the custom document property by using the property name
            const customProperty1 = customProperties.get("Owner");

            // Check whether the property is linked to content
            const isLinkedToContent = customProperty1.isLinkedToContent;

            // Get the source for the property
            const source = customProperty1.source;

            // Save the file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = `<p style="color: green;">Operation completed successfully! Property linked: ${isLinkedToContent}. Source: ${source}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

### **カスタムプロパティを削除する方法**

Aspose.Cellsを使用してカスタムプロパティを削除するには、[**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/#remove-string-)メソッドを呼び出し、削除するドキュメントプロパティの名前を渡します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Remove Custom Document Property Example</title>
    </head>
    <body>
        <h1>Remove Custom Document Property Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Removing a custom document property named "Publisher"
            customProperties.remove("Publisher");

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom property removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [ドキュメント情報パネルで表示されるカスタムプロパティの追加](/cells/ja/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [ビルトインドキュメントプロパティのScaleCropおよびLinksUpToDateプロパティを設定する](/cells/ja/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [ビルドインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する](/cells/ja/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [ビルドインドキュメントプロパティを使用してExcelファイルの言語を指定する](/cells/ja/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
