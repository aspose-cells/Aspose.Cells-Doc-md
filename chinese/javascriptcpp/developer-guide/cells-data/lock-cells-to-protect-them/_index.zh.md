---
title: 如何锁定单元格以保护它们
type: docs
weight: 130
url: /zh/javascript-cpp/how-to-lock-cells-to-protect-them/
description: 本文介绍了如何使用C++中的Aspose.Cells for JavaScript锁定单元格以保护它们的示例代码。
keywords: JavaScript锁定单元格以保护它们，如何使用JavaScript锁定单元格，JavaScript中锁定单元格以保护它们。
---

## **可能的使用场景**
锁定单元格以保护它们是在电子表格应用程序中常见的做法，原因包括：

1. 防止意外更改：锁定单元格可以防止用户无意中修改重要数据或公式。在复杂的电子表格中尤其有用，因为不小心的更改会导致重大错误。

1. 保持数据完整性：通过锁定单元格，可以确保关键数据保持一致和准确。这对于财务文件、报告以及任何需要数据完整性的文件来说都是至关重要的。

1. 受控访问：在协作环境中，锁定单元格允许你控制谁可以编辑电子表格的某些部分。例如，你可能只允许特定团队成员编辑特定单元格，而保持其他区域受保护。

1. 保护公式：公式常用于计算与数据分析。锁定包含公式的单元格可以确保这些公式不被意外更改或删除，从而保持整个工作表的功能。

1. 强制执行业务规则：在某些情况下，特定的业务规则或规定可能要求保护某些数据，防止修改。锁定单元格可以帮助满足这些要求。

1. 引导用户：通过锁定单元格并提供明确指示哪些单元格可以编辑，可以引导用户如何与电子表格交互，减少混淆和错误。

## **如何在Excel中锁定单元格以保护它们**
下面介绍在Microsoft Excel中锁定单元格的方法：

1. 选择要锁定的单元格：选择你想要锁定的单元格。如果要锁定整个工作表，可以跳过此步骤。
1. 打开“格式单元格”对话框：右键点击所选单元格，选择“设置单元格格式”，或按Ctrl+1。
<br>
<img src="1.png" width=60% />
1. 锁定单元格：在“设置单元格格式”对话框中，转到“保护”选项卡。勾选“锁定”复选框。点击“确定”。
1. 保护工作表：在功能区的“审阅”选项卡中，点击“保护工作表”。设置密码（可选）并选择你想允许的权限（例如选择锁定单元格、设置单元格格式等）。点击“确定”。
<br>
<img src="2.png" width=60% />

## **如何使用JavaScript锁定单元格以保护它们**

Aspose.Cells是一个用于以编程方式处理Excel文件的强大库。要通过C++使用Aspose.Cells for JavaScript锁定单元格，您需要遵循以下步骤：加载[示例文件](sample.xlsx)，首先取消所有单元格锁定（因为默认情况下所有单元格都被锁定但未生效，直到工作表被保护），然后锁定您要保护的特定单元格，最后保护工作表以强制执行锁定。

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


## **输出结果**
此代码确保只有指定的单元格（此例中的A1和B2）被锁定，并对工作表进行保护以强制执行这些设置。工作表中的其他单元格保持未锁定且可编辑。

<br>
<img src="3.png" width=60% />
