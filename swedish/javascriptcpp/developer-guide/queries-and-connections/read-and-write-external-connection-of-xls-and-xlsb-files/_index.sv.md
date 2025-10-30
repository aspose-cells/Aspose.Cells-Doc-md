---
title: Läs och skriv extern anslutning av XLS och XLSB filer med JavaScript via C++
linktitle: Läs och skriv extern anslutning för XLS och XLSB filer
type: docs
weight: 80
url: /sv/javascript-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/
description: Lär dig hur du läser och skriver externa anslutningar av XLS och XLSB filer med hjälp av Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

Aspose.Cells stöder redan att läsa och skriva externa anslutningar av XLSX-filer, men nu stödjer den även denna funktion för XLSB- och XLS-filer. Koden är densamma för alla format.  

## **Läs och skriv extern anslutning för XLS/XLSB-fil**  

Följande exempel laddar en exempel XLSB-fil (XLS kan också laddas) och läser dess första externa anslutning, som är en Microsoft Access DB-anslutning. Den modifierar sedan `[**DBConnection.name**](https://reference.aspose.com/cells/javascript-cpp/dbconnection/#name--)`-egenskapen och sparar den som en output XLS/XLSB-fil. Skärmbilden visar effekten av koden på [exempel XLSB-fil](51740722.xlsb) och [utdata XLSB-fil](51740723.xlsb) efter körning. Se även konsolutmatningen nedan för referens.  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **Exempelkod**  

Följande kod ska fungera för både XLSB- och XLS-filer genom att ladda och spara filer med rätt tillägg.  

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

## **Konsoloutput**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}
