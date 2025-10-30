---
title: Pivot tabell och källdata
type: docs
weight: 30
url: /sv/javascript-cpp/pivot-table-and-source-data/
---

## **Pivot-tabellens källdata**

Det finns tillfällen då du vill skapa Microsoft Excel-rapporter med pivottabeller som hämtar data från olika datakällor (t.ex. en databas) som inte är kända vid design-tid. Denna artikel ger en metod för att dynamiskt ändra en pivot-tabells datakälla.

### **Ändra en pivot-tabells källdata**

1. Skapa en ny designer-mall.
   1. Skapa en ny designer-mallfil enligt skärmbilden nedan.
   1. Definiera sedan ett namngivet område, **Datakälla**, som hänvisar till detta cellområde.

      **Skapa en designer-mall & definiera ett namngivet område, Datakälla** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Skapa en pivot-tabell baserad på detta namngivna område.
   1. I Microsoft Excel, välj **Data**, sedan **Pivottabell** och **PivotDiagramrapport**.
   1. Skapa en pivottabell baserad på det namngivna området som skapats i det första steget.

      **Skapa en pivottabell baserad på det namngivna området, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Dra det motsvarande fältet till pivottabellraden och kolumnen, skapa sedan den resulterande pivottabellen enligt skärmdumpen nedan.

   **Skapa en pivottabell baserad på ett motsvarande fält** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Högerklicka på pivottabellen och välj **Tabelloptioner**.
   1. Markera **Uppdatera vid öppning** i inställningarna för **Dataalternativ**.

      **Inställning av pivottabellalternativ** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Nu kan du spara den här filen som din designer-mallfil.

1. Försörjning av ny data och ändring av källdata för en pivottabell.
   1. När den designer-mall är skapad, använd följande kod för att ändra källan till pivottabellen.

Genom att köra den här exempelkoden nedan ändras källan till pivottabellen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            // Instantiating a Workbook object using uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Populating new data to the worksheet cells
            worksheet.cells.get("A9").value = "Golf";
            worksheet.cells.get("B9").value = "Qtr4";
            worksheet.cells.get("C9").value = 7000;

            // Changing named range "DataSource"
            const range = worksheet.cells.createRange(0, 0, 9, 3);
            range.name = "DataSource";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
