---
title: 使用JavaScript通过C++获取或设置嵌入式OLE对象的类别标识符
linktitle: 获取或设置嵌入式OLE对象的类标识符
type: docs
weight: 200
url: /zh/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: 了解如何在JavaScript中使用Aspose.Cells通过C++获取或设置嵌入OLE对象的类别标识符。
---

## **可能的使用场景**  
Aspose.Cells提供了 [OleObject.classIdentifier](https://reference.aspose.com/cells/javascript-cpp/oleobject/#classIdentifier--) 属性，可以用来获取或设置嵌入OLE对象的类别标识符。OLE对象类别标识符实际上是GUID，即全局唯一标识符。GUID长度始终为16字节，因此类别标识符也是16字节。它们通常存放在Windows注册表中，向主应用程序提供如何打开包含各种嵌入资源的OLE对象的信息。

## **获取或设置嵌入的OLE对象的类标识符**  
下面的截图显示了从[示例Excel文件](5115190.xls)中读取的OLE对象类标识符（GUID）。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **示例代码**  
请参见用[示例Excel文件](5115190.xls)执行的以下示例代码及其控制台输出，输出打印了OLE对象的类标识符（GUID），与截图中显示的完全相同。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract OLE Object Class Identifier (GUID)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access its first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first ole object inside the worksheet
            const oleObject = worksheet.oleObjects.get(0);

            // Convert 16-bytes array into GUID
            const bytes = new Uint8Array(oleObject.classIdentifier);
            const guid = bytes.reduce((acc, byte) => acc + String.fromCharCode(byte), '');

            // Print the GUID
            console.log(guid.toUpperCase());
            resultDiv.innerHTML = `<p style="color: green;">GUID: ${guid.toUpperCase()}</p>`;
        });
    </script>
</html>
```  
### **控制台输出**  
以上示例代码执行后生成的控制台输出。

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}
