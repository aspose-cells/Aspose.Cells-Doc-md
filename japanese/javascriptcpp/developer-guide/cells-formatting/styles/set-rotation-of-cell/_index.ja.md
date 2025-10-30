---
title: セルのテキストの回転方法
linktitle: セルのテキストの回転方法  
type: docs  
weight: 80  
url: /ja/javascript-cpp/how-to-rotate-text-of-cell/  
description: C++を使用したAspose.Cells for JavaScriptでセルのテキスト回転をプログラムで行う方法を学びます。  
keywords: C++を使用したJavaScriptでセルのテキストを回転させる、ワークブック内のセルのテキストをプログラムで回転角度設定、Excelでセルのテキスト回転を行う方法  
---

## **C++を使用したAspose.Cells for JavaScriptでセルのテキストを回転させる**

Aspose.Cellsは、Excelスプレッドシートをプログラム的に操作できる強力なJavaScriptコンポーネントです。Aspose.Cellsの機能の一つにセルの回転があり、これによりテキストの方向をカスタマイズし、データの視覚的提示を向上させることができます。本書では、Aspose.Cellsを使用したセルの回転方法について解説します。

## **Excel でセルのテキストを回転する方法**
Excel でセルを回転するには、次の手順を使用できます:
1. Excel を開き、回転させたいセルまたは範囲を選択します。
1. 選択したセルで右クリックし、コンテキストメニューから「セルの書式設定」を選択します。または、Excel リボンの「ホーム」タブで、「セル」グループの「書式」ドロップダウンをクリックし、「セルの書式設定」を選択します。
1. 「セルの書式設定」ダイアログボックスで、「配置」タブに移動します。
1. 「方向」セクションで、テキストの回転オプションが表示されます。『度』ボックスに、希望の回転角度を直接入力できます。正の値はテキストを反時計回りに、負の値は時計回りに回転させます。
<br>
![todo:image_alt_text](alignment.png)
1. 希望の回転を選択したら、「OK」をクリックして変更を適用します。選択したセルは、選択した回転角度または方向に基づいて回転されます。

## **Aspose.Cells APIを使用してセルのテキストを回転する方法**

[**Style.rotationAngle(number)**](https://reference.aspose.com/cells/javascript-cpp/style/#rotationAngle-number-)プロパティを使用すると、セルを回転させることが簡単になります。Aspose.Cellsでセルを回転させるには、次の手順に従う必要があります:
1. Excelワークブックをロードする  
<br>
まず、Aspose.Cellsを使用してExcelワークブックをロードする必要があります。Workbookクラスを使用して既存のExcelファイルを開くか、新しいファイルを作成できます。 

1. ワークシートにアクセスする  
<br>
ワークブックがロードされたら、セルを回転させたいワークシートにアクセスする必要があります。ワークシートはインデックスまたは名前でアクセスできます。 

1. セルのテキストを回転させる  
<br>
ワークシートにアクセスできるようになったので、希望のセルのStyleオブジェクトを変更することでセルを回転させることができます。Styleオブジェクトを使用すると、回転を含むさまざまな書式設定オプションを設定できます。 

1. ワークブックを保存する  
<br>
セルを回転させた後、変更されたワークブックをSaveメソッドを使用してファイルまたはストリームに保存できます。

## **JavaScriptサンプルコード**

以下のコードをご覧ください。これはワークブックオブジェクトを作成し、複数のセルに異なる回転角度を設定しています。スクリーンショットは、サンプルコードの実行後の結果を示しています。
<br>
<img src="rotation.png" width=80% />

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Rotate Text in Cells Example</h1>
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
            // Creating a new Workbook (blank)
            const workbook = new Workbook();

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Row index of the cell
            let row = 0;
            // Column index of the cell
            let column = 0; 

            let a1 = worksheet.cells.get(row, column);
            a1.putValue("a1 rotate text");
            let a1Style = a1.style;

            // Set the rotation angle in degrees
            a1Style.rotationAngle = 45; 
            a1.style = a1Style;

            // set Column index of the cell
            column = 1;
            let b1 = worksheet.cells.get(row, column);
            b1.putValue("b1 rotate text");
            let b1Style = b1.style;

            // Set the rotation angle in degrees
            b1Style.rotationAngle = 255;
            b1.style = b1Style;

            // set Column index of the cell
            column = 2;
            let c1 = worksheet.cells.get(row, column);
            c1.putValue("c1 rotate text");
            let c1Style = c1.style;

            // Set the rotation angle in degrees
            c1Style.rotationAngle = -90;
            c1.style = c1Style;

            // set Column index of the cell
            column = 3;
            let d1 = worksheet.cells.get(row, column);
            d1.putValue("d1 rotate text");
            let d1Style = d1.style;

            // Set the rotation angle in degrees
            d1Style.rotationAngle = -90;
            d1.style = d1Style;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
