---
title: 使用 JavaScript 通过 C++ 从工作簿中提取 OLE 对象
linktitle: 从工作簿中提取OLE对象
type: docs
weight: 110
url: /zh/javascript-cpp/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}
有时，您确实需要从工作簿中提取OLE对象。Aspose.Cells支持提取和保存这些OLE对象。

本文介绍如何在 JavaScript 通过 C++ 中创建应用程序，并用几行代码从工作簿中提取不同的 OLE 对象。
{{% /alert %}}

## **从工作簿中提取OLE对象**

### **创建模板工作簿**

1. 在Microsoft Excel中创建一个工作簿。  
1. 在第一个工作表上添加Microsoft Word文档、Excel工作簿和PDF文档作为OLE对象。

|**带有OLE对象的模板文档（OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

接下来，提取OLE对象并保存到硬盘，保留其各自的文件类型。

### **下载并安装Aspose.Cells**

1. [通过C++下载Aspose.Cells for JavaScript](https://downloads.aspose.com/cells/javascript-cpp)。  
1. 在您的开发计算机上安装它。

所有Aspose组件在安装后都处于评估模式。评估模式没有时间限制，只会在生成的文档中插入水印。

### **创建一个项目**

启动JavaScript环境并创建一个新项目。此示例将展示基于浏览器的应用程序，但你也可以使用任何支持JavaScript的环境。

1. 添加依赖项  
   1. 在你的HTML页面中包含通过C++脚本的Aspose.Cells for JavaScript，并创建一个简单的界面以选择Excel文件并提取OLE对象：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Extract OLE Objects</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLink { display: none; margin-top: 10px; }
            .ole-link { display: block; margin: 6px 0; }
            .info { margin-top: 12px; }
        </style>
    </head>
    <body>
        <h1>Extract OLE Objects</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.xlsb" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            const resultDiv = document.getElementById('result');
            const primaryDownloadLink = document.getElementById('downloadLink');
            resultDiv.innerHTML = '';
            primaryDownloadLink.style.display = 'none';
            primaryDownloadLink.href = '';
            primaryDownloadLink.textContent = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const extractedLinks = [];
            let totalExtracted = 0;

            // Iterate through all worksheets
            const sheetsCount = workbook.worksheets.count;
            for (let s = 0; s < sheetsCount; s++) {
                const worksheet = workbook.worksheets.get(s);

                // Access OLE objects collection on the worksheet
                const oleObjects = worksheet.oleObjects;
                if (!oleObjects) continue;

                const oleCount = oleObjects.count;
                for (let o = 0; o < oleCount; o++) {
                    const ole = oleObjects.get(o);

                    // Attempt to get a filename from ole properties
                    // Applying universal getter->property conversion:
                    // getSourceFullName() -> sourceFullName, getName() -> name, getObjectData() -> objectData
                    let fileName = ole.sourceFullName || ole.name || `ole_object_sheet${s}_idx${o}.bin`;

                    // Ensure filename is just the basename
                    try {
                        // simple basename extraction
                        const parts = fileName.split(/[/\\]/);
                        fileName = parts[parts.length - 1] || fileName;
                    } catch (e) {
                        // if something unexpected, fallback
                        fileName = `ole_object_sheet${s}_idx${o}.bin`;
                    }

                    // Get the raw object data as bytes
                    const objectData = ole.objectData;

                    // Some runtimes may return a typed array, ArrayBuffer or plain JS array.
                    let blobData;
                    if (objectData instanceof ArrayBuffer) {
                        blobData = new Blob([new Uint8Array(objectData)]);
                    } else if (ArrayBuffer.isView(objectData)) {
                        blobData = new Blob([objectData]);
                    } else if (objectData && objectData.buffer && ArrayBuffer.isView(objectData.buffer)) {
                        blobData = new Blob([objectData]);
                    } else if (objectData && objectData.byteLength !== undefined) {
                        // fallback for objects exposing byteLength
                        blobData = new Blob([objectData]);
                    } else {
                        // If objectData is a normal JS array of bytes
                        blobData = new Blob([new Uint8Array(objectData)]);
                    }

                    const url = URL.createObjectURL(blobData);

                    // Create a download link element for this OLE object
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = fileName;
                    a.textContent = `Download extracted OLE object: ${fileName}`;
                    a.className = 'ole-link';
                    resultDiv.appendChild(a);

                    extractedLinks.push({ name: fileName, url });
                    totalExtracted++;
                }
            }

            if (totalExtracted === 0) {
                resultDiv.innerHTML = '<p class="info">No OLE objects were found in the uploaded workbook.</p>';
            } else {
                // Make the first extracted file available via the primary downloadLink element as well
                if (extractedLinks.length) {
                    primaryDownloadLink.href = extractedLinks[0].url;
                    primaryDownloadLink.download = extractedLinks[0].name;
                    primaryDownloadLink.style.display = 'inline-block';
                    primaryDownloadLink.textContent = `Download First Extracted OLE Object: ${extractedLinks[0].name}`;
                }
                const summary = document.createElement('p');
                summary.className = 'info';
                summary.innerHTML = `<strong>Extracted ${totalExtracted} OLE object(s).</strong> Use the links above to download them.`;
                resultDiv.insertBefore(summary, resultDiv.firstChild);
            }
        });
    </script>
</html>
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Extract OLE Objects from Workbook</title>
    </head>
    <body>
        <h1>Extract OLE Objects from Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="extractBtn">Extract OLE Objects</button>
        <div id="result"></div>
        <div id="downloads"></div>

        <script src="aspose.cells.js"></script>
        <script type="text/javascript">
            const { Workbook, FileFormatType, SaveFormat } = AsposeCells;

            AsposeCells.onReady().then(() => {
                console.log("Aspose.Cells initialized");
            });

            document.getElementById('extractBtn').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                const result = document.getElementById('result');
                const downloads = document.getElementById('downloads');
                downloads.innerHTML = '';
                if (!fileInput.files.length) {
                    result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Get the OleObject collection in the first worksheet.
                const worksheet = workbook.worksheets.get(0);
                const oles = worksheet.oleObjects;

                const count = oles.count;
                if (count === 0) {
                    result.innerHTML = '<p>No OLE objects found in the workbook.</p>';
                    return;
                }

                result.innerHTML = `<p>Found ${count} OLE object(s). Preparing downloads...</p>`;

                for (let i = 0; i < count; i++) {
                    const ole = oles.get(i);
                    // Specify each file format based on the ole object format type.
                    let ext = 'bin';
                    switch (ole.fileFormatType) {
                        case FileFormatType.Doc:
                            ext = 'doc';
                            break;
                        case FileFormatType.Excel97To2003:
                            ext = 'xls';
                            break;
                        case FileFormatType.Xlsx:
                            ext = 'xlsx';
                            break;
                        case FileFormatType.Ppt:
                            ext = 'ppt';
                            break;
                        case FileFormatType.Pdf:
                            ext = 'pdf';
                            break;
                        case FileFormatType.Unknown:
                            ext = 'jpg';
                            break;
                        default:
                            ext = 'bin';
                            break;
                    }

                    const fileName = `outOle${i}.${ext}`;

                    // Save the ole object as a new excel file if the object type is xlsx.
                    if (ole.fileFormatType === FileFormatType.Xlsx) {
                        const ms = ole.objectData;
                        if (ms != null) {
                            const oleBook = new Workbook(ms);
                            oleBook.settings.isHidden = false;
                            const outData = oleBook.save(SaveFormat.Xlsx);
                            const blob = new Blob([outData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
                            const a = document.createElement('a');
                            a.href = URL.createObjectURL(blob);
                            a.download = fileName;
                            a.textContent = `Download ${fileName}`;
                            downloads.appendChild(a);
                            downloads.appendChild(document.createElement('br'));
                        }
                    } else {
                        const data = ole.objectData;
                        if (data != null) {
                            const blob = new Blob([data]);
                            const a = document.createElement('a');
                            a.href = URL.createObjectURL(blob);
                            a.download = fileName;
                            a.textContent = `Download ${fileName}`;
                            downloads.appendChild(a);
                            downloads.appendChild(document.createElement('br'));
                        }
                    }
                }

                result.innerHTML += '<p style="color: green;">Extraction completed! Use the links above to download the extracted files.</p>';
            });
        </script>
    </body>
</html>
