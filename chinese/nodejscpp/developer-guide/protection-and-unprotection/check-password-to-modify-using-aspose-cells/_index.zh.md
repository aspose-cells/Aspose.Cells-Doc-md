---  
title: 使用 Aspose.Cells for Node.js via C++ 检查修改密码  
linktitle: 检查密码修改权限  
type: docs  
weight: 2400  
url: /zh/nodejs-cpp/check-password-to-modify-using-aspose-cells/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 检查修改密码是否匹配。  
---  

{{% alert color="primary" %}}  
有时，您需要通过程序检查提供的密码是否与“修改密码”匹配。Aspose.Cells 提供了 `WorkbookSettings.writeProtection.validatePassword()` 方法，可以用来验证密码是否正确。  
{{% /alert %}}  

## **在Microsoft Excel中检查修改密码**  

您可以在创建Microsoft Excel工作簿时指定**打开密码**和**修改密码**。请参阅此截图，显示Microsoft Excel提供的界面以指定这些密码。  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **使用 Aspose.Cells for Node.js via C++ 检查修改密码**  

以下示例加载了 [源Excel文件](5112232.xlsx)，其中设置了打开密码为 1234，修改密码为 5678。代码首先验证 567 是否是正确的修改密码，返回 false，然后验证 5678，返回 true。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify password to open inside the load options
const opts = new AsposeCells.LoadOptions();
opts.setPassword("1234");

// Open the source Excel file with load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleBook.xlsx"), opts);

// Check if 567 is Password to modify
let ret = workbook.getSettings().getWriteProtection().validatePassword("567");
console.log("Is 567 correct Password to modify: " + ret);

// Check if 5678 is Password to modify
ret = workbook.getSettings().getWriteProtection().validatePassword("5678");
console.log("Is 5678 correct Password to modify: " + ret);
```  

### **控制台输出**  

这是加载了[源 Excel](5112232.xlsx) 文件后的上述示例代码的控制台输出。  

{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
