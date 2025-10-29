---
title: 管理包含宏的 Excel 工作簿的 VBA 代码
linktitle: 宏项目
type: docs
weight: 200
url: /zh/javascript-cpp/manage-vba-project/
description: 通过 C++ 使用 Aspose.Cells for JavaScript 添加 VBA 模块并修改 VBA 或宏。
---

## **通过 C++ 用 JavaScript 添加 VBA 模块**
{{% alert color="primary" %}}

Aspose.Cells 允许您使用 C++ 通过 Aspose.Cells for JavaScript 添加新的 VBA 模块和宏代码。请使用 [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#add-worksheet-) 方法在工作簿中添加新的 VBA 模块

{{% /alert %}}

以下示例代码创建一个新工作簿，添加一个 VBA 模块和宏代码，并将输出保存为 XLSM 格式。一旦你用 Microsoft Excel 打开输出的 XLSM 文件并点击 **开发者 > 视觉 Basic** 菜单命令，你将看到名为 "TestModule" 的模块，里面包含以下宏代码。

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add VBA Module</title>
    </head>
    <body>
        <h1>Add VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            // Create new workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add VBA Module
            const idx = workbook.vbaProject.modules.add(worksheet);

            // Access the VBA Module, set its name and codes
            const module = workbook.vbaProject.modules.get(idx);
            module.name = "TestModule";
            module.codes = "Sub ShowMessage()\r\n" +
                           "    MsgBox \"Welcome to Aspose!\"\r\n" +
                           "End Sub";

            // Save the workbook as XLSM and prepare download
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel.sheet.macroEnabled.12" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **通过 C++ 用 JavaScript 修改 VBA 或宏**

{{% alert color="primary" %}} 

您可以使用 Aspose.Cells for JavaScript 通过 C++ 修改 VBA 或宏代码。Aspose.Cells 已添加以下模块和类，用于读取和修改 Excel 文件中的 VBA 项目。

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

本文将向您展示如何使用Aspose.Cells更改源Excel文件中的VBA或宏代码。

{{% /alert %}} 

以下示例代码加载包含 VBA 或宏代码的源 Excel 文件

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

执行Aspose.Cells示例代码后，VBA或宏代码将被修改如下

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

您可以从以下链接下载[源Excel文件](5112508.xlsm)和[输出Excel文件](5112511.xlsm)。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Change VBA Module Code Example</title>
    </head>
    <body>
        <h1>Change VBA Module Code Example</h1>
        <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsm).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access VBA project modules
            const modules = workbook.vbaProject.modules;
            const moduleCount = modules.count;
            for (let i = 0; i < moduleCount; i++) {
                const module = modules.get(i);
                let code = module.codes;
                if (code && code.includes("This is test message.")) {
                    code = code.replace("This is test message.", "This is Aspose.Cells message.");
                    module.codes = code;
                }
            }

            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">VBA module code updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高级主题**
- [在工作簿中添加对VBA项目的库引用](/cells/zh/javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [将宏分配给窗体控件](/cells/zh/javascript-cpp/assign-macro-to-form-control/)
- [检查VBA代码的数字签名是否有效](/cells/zh/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [检查VBA代码是否已签名](/cells/zh/javascript-cpp/check-if-vba-code-is-signed/)
- [检查工作簿中的VBA项目是否已签名](/cells/zh/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [检查VBA项目是否受保护并锁定以供查看](/cells/zh/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [将VBA宏用户表单DesignerStorage从模板复制到目标工作簿](/cells/zh/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [使用证书对VBA代码项目进行数字签名](/cells/zh/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [将VBA证书导出到文件或流](/cells/zh/javascript-cpp/export-vba-certificate-to-file-or-stream/)
- [加载工作簿时过滤VBA项目](/cells/zh/javascript-cpp/filter-vba-project-while-loading-a-workbook/)
- [查找VBA项目是否受保护](/cells/zh/javascript-cpp/find-out-if-vba-project-is-protected/)
- [为Excel工作簿的VBA项目设置密码保护](/cells/zh/javascript-cpp/password-protect-the-vba-project-of-excel-workbook/)
