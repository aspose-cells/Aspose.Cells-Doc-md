---
title: Read and Write External Connection of XLS and XLSB files with JavaScript via C++
linktitle: Read and Write External Connection of XLS and XLSB files
type: docs
weight: 80
url: /javascript-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/
description: Learn how to read and write external connections of XLS and XLSB files using Aspose.Cells for JavaScript via C++.
---

## **Possible Usage Scenarios**  

Aspose.Cells already supports reading and writing external connections of XLSX files, but now it also supports this feature for XLSB and XLS files. However, the code is the same for all formats.  

## **Read and Write External Connection of XLS/XLSB file**  

The following sample code loads the sample XLSB file (an XLS file can also be loaded) and reads its first external connection, which is actually a Microsoft Access DB connection. It then modifies the [**DBConnection.name**](https://reference.aspose.com/cells/javascript-cpp/dbconnection/#name--) property and saves it as an output XLS/XLSB file. The screenshot shows the effect of the code on the [sample XLSB file](51740722.xlsb) and the [output XLSB file](51740723.xlsb) after its execution. Please also see the console output of the sample code given below for reference.  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **Sample Code**  

The following code shall work for both XLSB and XLS files by loading and saving files with the appropriate extension.  

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (.xls, .xlsx, .xlsb, or .csv).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the source Excel XLSB file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Read the first external connection, which is actually a DB connection
            const dbCon = workbook.dataConnections.get(0);

            // Print the Name, Command and Connection Info of the DB connection
            const outputLines = [];
            outputLines.push("Connection Name: " + dbCon.name);
            outputLines.push("Command: " + dbCon.command);
            outputLines.push("Connection Info: " + dbCon.connectionString);

            // Modify the Connection Name
            dbCon.name = "NewCust";

            // Save the Excel XLSB file
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

## **Console Output**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}