---
title: 管理包含宏的 Excel 工作簿的 VBA 代码
linktitle: 宏项目
type: docs
weight: 200
url: /zh/nodejs-cpp/manage-vba-project/
description: 添加VBA模块并使用Aspose.Cells for Node.js via C++修改VBA或宏代码。
---

## **在 Node.js 中添加 VBA 模块**
{{% alert color="primary" %}}

Aspose.Cells允许你使用Aspose.Cells for Node.js via C++添加新的VBA模块和宏代码。请使用[**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#add-worksheet-)方法在工作簿中添加新的VBA模块。

{{% /alert %}}

以下示例代码创建一个新工作簿，添加一个 VBA 模块和宏代码，并将输出保存为 XLSM 格式。一旦你用 Microsoft Excel 打开输出的 XLSM 文件并点击 **开发者 > 视觉 Basic** 菜单命令，你将看到名为 "TestModule" 的模块，里面包含以下宏代码。

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}

以下是生成带有 VBA 模块和宏代码的输出 XLSM 文件的示例代码。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add VBA Module
const idx = workbook.getVbaProject().getModules().add(worksheet);

// Access the VBA Module, set its name and codes
const module = workbook.getVbaProject().getModules().get(idx);
module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```

## **在 Node.js 中修改 VBA 或宏**

{{% alert color="primary" %}} 

你可以使用Aspose.Cells for Node.js via C++修改VBA或宏代码。Aspose.Cells已添加以下模块和类来读取和修改Excel文件中的VBA项目。

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

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsm"));

// Change the VBA Module Code
const modules = workbook.getVbaProject().getModules();
const moduleCount = modules.getCount();
for (let i = 0; i < moduleCount; i++) {
const module = modules.get(i);
const code = module.getCodes();
if (code.includes("This is test message.")) 
{
code = code.replace("This is test message.", "This is Aspose.Cells message.");
module.setCodes(code);
}
}


// Save the output Excel file
workbook.save(path.join(dataDir, "output_out.xlsm"));
```

## **高级主题**
- [在工作簿中添加对VBA项目的库引用](/cells/zh/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [将宏分配给窗体控件](/cells/zh/nodejs-cpp/assign-macro-to-form-control/)
- [检查VBA代码的数字签名是否有效](/cells/zh/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [检查VBA代码是否已签名](/cells/zh/nodejs-cpp/check-if-vba-code-is-signed/)
- [检查工作簿中的VBA项目是否已签名](/cells/zh/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [检查VBA项目是否受保护并锁定以供查看](/cells/zh/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [将VBA宏用户表单DesignerStorage从模板复制到目标工作簿](/cells/zh/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [使用证书对VBA代码项目进行数字签名](/cells/zh/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [将VBA证书导出到文件或流](/cells/zh/nodejs-cpp/export-vba-certificate-to-file-or-stream/)
- [加载工作簿时过滤VBA项目](/cells/zh/nodejs-cpp/filter-vba-project-while-loading-a-workbook/)
- [查找VBA项目是否受保护](/cells/zh/nodejs-cpp/find-out-if-vba-project-is-protected/)
- [为Excel工作簿的VBA项目设置密码保护](/cells/zh/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="nodejs-cpp" >}}
