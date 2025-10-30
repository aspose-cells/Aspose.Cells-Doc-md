---
title: JavaScriptを使ったXLSおよびXLSBファイルの外部接続の読み書き（C++経由）
linktitle: XLSおよびXLSBファイルの外部接続の読み取りと書き込み
type: docs
weight: 80
url: /ja/javascript-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/
description: Aspose.Cells for JavaScriptを使ったC++によるXLSおよびXLSBファイルの外部接続の読み書き方法を学びます。
---

## **可能な使用シナリオ**  

Aspose.Cellsは既にXLSXファイルの外部接続の読み書きをサポートしていますが、今度はXLSBおよびXLSファイルもサポートします。コードはすべてのフォーマットタイプで同じです。  

## **XLS/XLSBファイルの外部接続の読み取りと書き込み**  

次のサンプルコードは、サンプルXLSBファイル（XLSもロード可能）をロードし、その最初の外部接続（実際にはMicrosoft AccessのDB接続）を読み取ります。その後、[**DBConnection.name**](https://reference.aspose.com/cells/javascript-cpp/dbconnection/#name--)プロパティを変更し、出力XLS/XLSBファイルとして保存します。スクリーンショットは、[サンプルXLSBファイル](51740722.xlsb)と[出力XLSBファイル](51740723.xlsb)のコード実行後の効果を示しています。参考のため、以下のサンプルコードのコンソール出力もご覧ください。  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **サンプルコード**  

このコードは、適切な拡張子のファイルを読み込んで保存することにより、XLSBおよびXLSファイルの両方で動作します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read and Modify External DB Connection (XLSB)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (.xlsb).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the source Excel Xlsb file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Read the first external connection which is actually a DB-Connection
            const dbCon = workbook.dataConnections.get(0);

            // Print the Name, Command and Connection Info of the DB-Connection
            const outputLines = [];
            outputLines.push("Connection Name: " + dbCon.name);
            outputLines.push("Command: " + dbCon.command);
            outputLines.push("Connection Info: " + dbCon.connectionString);

            // Modify the Connection Name
            dbCon.name = "NewCust";

            // Save the Excel Xlsb file
            const outputData = workbook.save(SaveFormat.Xlsb);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExternalConnection_XLSB.xlsb';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<pre style="color: green;">' + outputLines.join('\n') + '\n\nModified connection name to: NewCust</pre>';
        });
    </script>
</html>
```  

## **コンソール出力**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}
