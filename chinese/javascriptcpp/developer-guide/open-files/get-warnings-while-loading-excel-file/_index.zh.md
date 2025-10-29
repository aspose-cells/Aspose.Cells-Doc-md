---
title: 用JavaScript通过C++在加载Excel文件时获取警告信息
linktitle: 加载Excel文件时获取警告
type: docs
weight: 110
url: /zh/javascript-cpp/get-warnings-while-loading-excel-file/
description: 学习如何在用C++调用Aspose.Cells for JavaScript加载Excel文件时捕获警告。有效处理损坏但可加载的工作簿。
---

## **可能的使用场景**

 有时，用户尝试加载一个或有损坏但仍可加载的工作簿。在这种情况下，Aspose.Cells 在加载工作簿时会发出警告。您可以通过实现 [**IWarningCallback**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback) 接口并设置 [**LoadOptions.warningCallback**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#warningCallback--) 属性来捕获这些警告。

## **加载 Excel 文件时获取警告**

 以下示例代码说明了如何在加载Excel文件时获取警告。代码加载会在加载时抛出 [**DuplicateDefinedName**](https://reference.aspose.com/cells/javascript-cpp/warningtype) 警告的 [示例Excel文件](sampleDuplicateDefinedName.xlsx)。这个警告由 [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback/#warning-warninginfo-) 方法捕获，并在控制台输出警告信息。随后，代码将工作簿保存为 [输出Excel文件](outputDuplicateDefinedName.xlsx)。如果在Microsoft Excel中打开该示例文件，也会显示类似的警告。请同时查看下面的控制台输出以获取更多信息。

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Warning Callback Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Warning Callback Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, WarningType } = AsposeCells;

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

        // Implement IWarningCallback interface to catch warnings while loading workbook
        class WarningCallback extends AsposeCells.IWarningCallback {
            warning(warningInfo) {
                if (warningInfo.type === AsposeCells.WarningType.DuplicateDefinedName) {
                    console.log("Duplicate Defined Name Warning: " + warningInfo.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options and set the WarningCallback property 
            // to catch warnings while loading workbook
            const options = new LoadOptions();
            options.warningCallback = new WarningCallback();

            // Load the source excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDuplicateDefinedName.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully. Check console for warnings.</p>';
        });
    </script>
</html>
```

## **控制台输出**



{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
