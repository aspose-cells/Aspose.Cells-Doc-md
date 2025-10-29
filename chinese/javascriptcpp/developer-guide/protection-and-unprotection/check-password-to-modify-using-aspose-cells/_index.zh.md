---
title: 使用C++的Aspose.Cells for JavaScript检查修改密码
linktitle: 检查密码修改权限
type: docs
weight: 2400
url: /zh/javascript-cpp/check-password-to-modify-using-aspose-cells/
description: 学习如何使用C++的Aspose.Cells for JavaScript检查修改密码是否匹配。
---

{{% alert color="primary" %}}  
有时，您需要通过程序检查提供的密码是否与“修改密码”匹配。Aspose.Cells 提供了 `WorkbookSettings.writeProtection.validatePassword()` 方法，可以用来验证密码是否正确。  
{{% /alert %}}  

## **在Microsoft Excel中检查修改密码**  

您可以在创建Microsoft Excel工作簿时指定**打开密码**和**修改密码**。请参阅此截图，显示Microsoft Excel提供的界面以指定这些密码。  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **使用C++的Aspose.Cells for JavaScript检查修改密码**  

以下示例加载了 [源Excel文件](5112232.xlsx)，其中设置了打开密码为 1234，修改密码为 5678。代码首先验证 567 是否是正确的修改密码，返回 false，然后验证 5678，返回 true。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Write Protection Passwords</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, SaveFormat, Utils } = AsposeCells;

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

            // Specify password to open inside the load options
            const opts = new LoadOptions();
            opts.password = "1234";

            // Open the source Excel file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Check if 567 is Password to modify
            let ret = workbook.settings.writeProtection.validatePassword("567");
            let outputHtml = `<p>Is 567 correct Password to modify: ${ret}</p>`;

            // Check if 5678 is Password to modify
            ret = workbook.settings.writeProtection.validatePassword("5678");
            outputHtml += `<p>Is 5678 correct Password to modify: ${ret}</p>`;

            document.getElementById('result').innerHTML = outputHtml;
        });
    </script>
</html>
```  

### **控制台输出**  



{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}
