---
title: 用JavaScript通过C++从模板文件加载工作簿时筛选数据类型
linktitle: 从模板文件加载工作簿时过滤数据类型
type: docs
weight: 400
url: /zh/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}
有时，你希望在用模板文件构建工作簿时指定加载哪种类型的数据。筛选已加载的数据可以提高特殊用途的性能，尤其是在使用[LightCells API](/cells/zh/javascript-cpp/using-lightcells-api/)时。请使用[**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--)属性实现此目的。
{{% /alert %}}

 以下示例代码仅在加载工作簿时加载形状对象，工作簿来自给定链接中的 [模板文件](5115552.xlsx)。下图显示了 [模板文件](5115552.xlsx) 的内容，并说明因为设置了 [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--) 属性为 [**Shape**](https://reference.aspose.com/cells/javascript-cpp/shape/) ，所以红色和黄色背景的数据不会被加载。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

下面的屏幕截图显示了您可以从给定链接下载的[输出PDF](5115555.pdf)。在这里，您可以看到红色和黄色背景中的数据不存在，但所有形状都在那里。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

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
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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

            // Set the load options, we only want to load shapes and do not want to load data
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.Chart);

            // Create workbook object from uploaded excel file using load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the output in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sampleFilterChars_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
