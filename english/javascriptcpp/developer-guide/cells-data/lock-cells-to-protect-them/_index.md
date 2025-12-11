---
title: How to Lock Cells to Protect Them
type: docs
weight: 130
url: /javascript-cpp/how-to-lock-cells-to-protect-them/
description: This article provides code that shows how to lock cells to protect them using Aspose.Cells for JavaScript via C++.
keywords: JavaScript Lock Cells to Protect Them, How to Lock Cells to Protect Them using JavaScript, Lock Cells to Protect Them in JavaScript.
---

## **Possible Usage Scenarios**
Locking cells to protect them is a common practice in spreadsheet applications, such as Microsoft Excel or Google Sheets, for several important reasons:

1. Preventing Accidental Changes: Locking cells can prevent users from accidentally modifying important data or formulas. This is especially useful in complex spreadsheets where unintentional changes can lead to significant errors.

1. Maintaining Data Integrity: By locking cells, you can ensure that critical data remains consistent and accurate. This is crucial for financial documents, reports, and any other documents where data integrity is essential.

1. Controlled Access: In collaborative environments, locking cells allows you to control who can edit certain parts of a spreadsheet. For example, you might want to allow only certain team members to edit specific cells while keeping the rest of the worksheet protected.

1. Protecting Formulas: Formulas are often crucial for calculations and data analysis. Locking cells that contain formulas ensures that these formulas are not accidentally altered or deleted, which could disrupt the functionality of the entire worksheet.

1. Enforcing Business Rules: In some cases, specific business rules or regulations may require that certain data be protected from modification. Locking cells helps comply with these requirements.

1. Guiding Users: By locking cells and providing clear instructions on which cells can be edited, you can guide users on how to interact with the spreadsheet, reducing confusion and errors.

## **How to Lock Cells to Protect Them in Excel**
Here's how you can lock cells in Microsoft Excel:

1. Select the Cells to Lock: Select the cells you want to lock. If you want to lock the entire sheet, you can skip this step.  
2. Open the Format Cells Dialog: Right‑click on the selected cells and choose **Format Cells**, or press **Ctrl+1**.  
   <br>
   <img src="1.png" width=60% />
3. Lock the Cells: In the Format Cells dialog, go to the **Protection** tab. Check the **Locked** checkbox. Click **OK**.  
4. Protect the Worksheet: Go to the **Review** tab on the Ribbon. Click **Protect Sheet**. Set a password (optional) and choose the permissions you want to allow (e.g., selecting locked cells, formatting cells, etc.). Click **OK**.  
   <br>
   <img src="2.png" width=60% />

## **How to Lock Cells to Protect Them Using JavaScript**

Aspose.Cells is a powerful library for working with Excel files programmatically. To lock cells using Aspose.Cells for JavaScript via C++, you need to follow these steps: load the [sample file](sample.xlsx), unlock all cells first (since, by default, all cells are locked but not enforced until the worksheet is protected), then lock the specific cells you want to protect, and finally protect the worksheet to enforce the locking.

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
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;
        
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unlock all cells first
            const unlockStyle = workbook.createStyle();
            unlockStyle.isLocked = false;

            const styleFlag = new StyleFlag();
            styleFlag.locked = true;
            sheet.cells.applyStyle(unlockStyle, styleFlag);

            // Lock specific cells (e.g., A1 and B2)
            const lockStyle = workbook.createStyle();
            lockStyle.isLocked = true;

            sheet.cells.get("A1").style = lockStyle;
            sheet.cells.get("B2").style = lockStyle;

            // Protect the worksheet to enforce the locking
            sheet.protect(ProtectionType.All);

            // Save the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet protected and cells locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Output Result**
This code ensures that only the specified cells (A1 and B2 in this example) are locked, and the worksheet is protected to enforce these settings. All other cells in the worksheet remain unlocked and editable.

<br>
<img src="3.png" width=60% />