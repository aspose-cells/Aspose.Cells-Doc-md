---
title: XLS ve XLSB dosyalarının Dış Bağlantısını JavaScript ile C++ kullanarak Oku ve Yaz
linktitle: XLS ve XLSB dosyalarının Dış Bağlantısını Okuma ve Yazma
type: docs
weight: 80
url: /tr/javascript-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/
description: C++ kullanarak Aspose.Cells for JavaScript ile XLS ve XLSB dosyalarının dış bağlantılarını nasıl okuyup yazacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**  

Aspose.Cells, XLSX dosyalarının harici bağlantılarını okuma ve yazma desteğini zaten sağlar, ancak şimdi XLSB ve XLS dosyaları için de bu özelliği destekler. Ancak, kod tüm format türleri için aynıdır.  

## **XLS/XLSB Dosyasının Dış Bağlantısını Okuma ve Yazma**  

Aşağıdaki örnek kod, örnek XLSB dosyasını yükler (XLS de yüklenebilir) ve aslında bir Microsoft Access DB Bağlantısı olan ilk harici bağlantıyı okur. Daha sonra, [**DBConnection.name**](https://reference.aspose.com/cells/javascript-cpp/dbconnection/#name--) özelliğini değiştirir ve çıktıyı XLS/XLSB dosyası olarak kaydeder. Ekran görüntüsü, kodun çalışması sonrası [örnek XLSB dosyası](51740722.xlsb) ve [çıkış XLSB dosyası](51740723.xlsb) üzerindeki etkisini gösterir. Lütfen aşağıdaki örnek kodun konsol çıkışını da referans için inceleyin.  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **Örnek Kod**  

Aşağıdaki kod, uygun uzantısıyla dosyaların yüklenmesini ve kaydedilmesini sağlayarak hem XLSB hem de XLS dosyaları için çalışacaktır.  

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

## **Konsol Çıktısı**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}
