---
title: 用Node.js通过C++取消工作表保护
linktitle: 取消保护工作表
type: docs
weight: 20
url: /zh/nodejs-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

如果开发人员需要在运行时从受保护的工作表中移除保护，以便对文件进行一些更改？这可以很容易地通过Aspose.Cells完成。

{{% /alert %}}

## **取消保护工作表**

### **使用Microsoft Excel**

要取消工作表的保护：

从**工具**菜单中，选择**保护**然后**取消保护工作表**。除非工作表设置了密码，否则保护将会被移除。在这种情况下，会弹出对话框要求输入密码。输入密码后，工作表将被取消保护。

### **使用Aspose.Cells取消简单保护的工作表**

可以通过调用[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类的[**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--)方法来取消保护工作表。一个简单保护的工作表是不设置密码保护的。这类工作表可以通过调用[**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--)方法（不传递参数）来取消保护。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet without a password
worksheet.unprotect();

// Saving the Workbook
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **使用Aspose.Cells取消受密码保护的工作表**

受密码保护的工作表是用密码保护的工作表。这类工作表可以通过调用[**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--)方法的重载版本（带有密码参数）来取消保护。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet with a password
worksheet.unprotect("");

// Save Workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
