---
title: JavaScriptを使用したスプレッドシートレンダリングのためのフォント設定例
linktitle: スプレッドシートのレンダリングのためのフォントの設定
type: docs
weight: 10
url: /ja/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Aspose.Cells for JavaScriptを使用してスプレッドシートのフォントを設定する方法。最適な変換品質のためにフォントが利用可能であることを確認してください。
---

## **可能な使用シナリオ**

Aspose.Cells APIは、スプレッドシートを画像形式でレンダリングしたり、PDFやXPS形式に変換したりする機能を提供します。変換の精度を最大化するためには、スプレッドシートで使用されるフォントがOSの標準フォントディレクトリに存在する必要があります。必要なフォントがない場合、Aspose.Cells APIは利用可能なフォントに置き換えようとします。

## **フォントの選択**

Aspose.Cells API が裏で行うプロセスは以下の通りです。

1. API は、スプレッドシートで使用されている正確なフォント名と一致するフォントをファイルシステムで検索しようとします。
1. API が正確な同じ名前のフォントを見つけられない場合、ワークブックの [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) プロパティで指定されたデフォルトフォントを使用しようとします。
1. API がワークブックの [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) プロパティで定義されたフォントを見つけられない場合、[**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) または [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) プロパティで指定されたフォントを使用しようとします。
1. API が [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) または [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) プロパティで定義されたフォントを見つけられない場合、[**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--) プロパティで指定されたフォントを使用しようとします。
1. API が [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--) プロパティで定義されたフォントを見つけられない場合、利用可能なすべてのフォントから最適なフォントを選択しようとします。
1. 最終的に API がファイルシステムでフォントを見つけられない場合、Arial を使用してスプレッドシートをレンダリングします。

## **カスタムフォントフォルダの設定**

Aspose.Cells APIは、必要なフォントが存在しない場合の代替フォントの指定も可能です。ユーザーはフォント名のリストを用意して、元々必要だったフォントの代わりに指定できます。このために、Aspose.Cells APIは[**FontConfigs**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs)メソッドを公開しており、これは2つのパラメータを受け取ります。最初のパラメータは**string**型で、置換するフォント名を指定します。2つ目のパラメータは**string**型の配列で、元のフォントの代わりに使用するフォント名のリストを提供します。

1.[**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-): このメソッドは1つのフォルダだけを設定する場合に有用です。
1.[**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-): このメソッドは、フォントが複数のフォルダに存在し、ユーザーがすべてのフォルダを単一のフォルダにまとめるのではなく、それぞれ別々に設定したい場合に有用です。
1.[**FontConfigs.fontSources(FontSourceBase[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources-fontsourcebasearray-): このメカニズムは、ユーザーが複数のフォルダからフォントを読み込む場合や、単一のフォントファイルやバイト配列からフォントデータを読み込みたい場合に有用です。

{{% alert color="primary" %}}

両方の[**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-)および[**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-)メソッドは、2番目のパラメータとしてBoolean型を受け付けます。2番目のパラメータに**true**を渡すと、Aspose.Cells APIはフォントファイルをサブフォルダーで検索します。

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Font Configuration Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Font Configuration Example</h1>
        <p>Select an Excel file (optional) and font resources to configure Aspose.Cells font sources in the browser.</p>

        <label>Excel File (optional):</label>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>

        <label>Font File (.ttf/.otf) (optional):</label>
        <input type="file" id="fontFileInput" accept=".ttf,.otf" />
        <br/><br/>

        <label>Font Folder (optional, select a folder):</label>
        <input type="file" id="fontFolderInput" webkitdirectory directory multiple />
        <br/><br/>

        <button id="runExample">Configure Fonts</button>
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
            const fontFileInput = document.getElementById('fontFileInput');
            const fontFolderInput = document.getElementById('fontFolderInput');
            const resultDiv = document.getElementById('result');

            // Basic validation: ensure at least one font resource is provided (file or folder)
            if (!fontFileInput.files.length && !fontFolderInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select at least one font file or a font folder.</p>';
                return;
            }

            // Defining string variables to store paths/names to font folders & font file
            // (In browser environment we use simple names or uploaded file names)
            const fontFolder1 = "Arial";
            const fontFolder2 = "Calibri";
            const fontFile = "arial.ttf";

            // Setting first font folder (converted from setFontFolder)
            AsposeCells.FontConfigs.fontFolder = fontFolder1;
            // Preserve the subfolder-search flag from original API call as a separate property
            AsposeCells.FontConfigs.fontFolderSearchSubFolders = true;

            // Setting both font folders (converted from setFontFolders)
            AsposeCells.FontConfigs.fontFolders = [fontFolder1, fontFolder2];
            // Preserve the subfolder-search flag as a separate property
            AsposeCells.FontConfigs.fontFoldersSearchSubFolders = false;

            // Defining FolderFontSource
            const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

            // Defining FileFontSource
            const sourceFile = new AsposeCells.FileFontSource(fontFile);

            // Defining MemoryFontSource
            let memoryFontBytes = new Uint8Array([]);
            if (fontFileInput.files.length) {
                const ff = fontFileInput.files[0];
                const arrayBuffer = await ff.arrayBuffer();
                memoryFontBytes = new Uint8Array(arrayBuffer);
            } else if (fontFolderInput.files.length) {
                // If a folder was provided, try to find a .ttf/.otf inside it and use the first found
                const files = Array.from(fontFolderInput.files);
                const fontCandidate = files.find(f => f.name.toLowerCase().endsWith('.ttf') || f.name.toLowerCase().endsWith('.otf'));
                if (fontCandidate) {
                    const arrayBuffer = await fontCandidate.arrayBuffer();
                    memoryFontBytes = new Uint8Array(arrayBuffer);
                }
            }
            const sourceMemory = new AsposeCells.MemoryFontSource(memoryFontBytes);

            // Setting font sources (converted from setFontSources)
            AsposeCells.FontConfigs.fontSources = [sourceFolder, sourceFile, sourceMemory];

            // Provide feedback to the user
            resultDiv.innerHTML = '<p style="color: green;">Font configuration applied successfully.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

上記のいずれかの方法を、アプリケーションの開始時に（つまり、Aspose.Cellsの他のオブジェクトを呼び出す前に）使用してください。

{{% /alert %}} {{% alert color="primary" %}}

フォントソースを設定するために上記のすべての方法を使用した場合、最後に設定したもののみが有効になります。

{{% /alert %}}

## **フォントの代替メカニズム**

Aspose.Cells API は、変換時に必要なフォントが利用できない場合に備えて、代替フォントを指定する機能も提供しています。ユーザーは、オリジナルのフォントの代わりに使用可能なフォント名のリストを指定できます。このために、Aspose.Cells API では [**FontConfigs.fontSubstitutes(string, string[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-stringarray-) メソッドを公開しており、2つのパラメータを受け取ります。最初のパラメータは **string** 型で、代替フォントの名前を指定します。二つ目のパラメータは **string** の配列で、代替フォント名のリストを提供します。

以下は単純な使用シナリオです。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Substituting the Arial font with Times New Roman & Calibri
            // Converted from: AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
            AsposeCells.FontConfigs.fontSubstitutes = { "Arial": ["Times New Roman", "Calibri"] };

            // Saving the (possibly modified) workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the processed file.</p>';
        });
    </script>
</html>
```

## **情報収集**

上記の方法に加え、Aspose.Cells APIは設定されたソースと置換に関する情報を収集する手段も提供しています。

1. [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--)メソッドは、指定されたフォントソースのリストを含む[**FontSourceBase**](https://reference.aspose.com/cells/javascript-cpp/fontsourcebase)型の配列を返します。ソースが設定されていない場合、[**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--)メソッドは空の配列を返します。
1. [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-)メソッドは、置換が設定されているフォント名を指定できる**string**型のパラメータを受け取ります。指定されたフォントに対して置換が設定されていない場合、[**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-)メソッドはnullを返します。

## **高度なトピック**
- [スプレッドシートを画像にレンダリングする際のデフォルトフォントの設定](/cells/ja/javascript-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [PdfSaveOptionsおよびImageOrPrintOptionsのDefaultFontプロパティを優先するために設定します](/cells/ja/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [サポートされるフォント形式](/cells/ja/javascript-cpp/supported-font-formats/)
- [ワークシートを画像に変換 - レンダリングされた画像のピクセル形式を設定する](/cells/ja/javascript-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
