---  
title: 使用Node.js通过C++设置强加密类型  
linktitle: 设置强加密类型  
type: docs  
weight: 60  
url: /zh/nodejs-cpp/setting-strong-encryption-type/  
description: 学习如何使用Aspose.Cells for Node.js via C++为Excel文件设置强加密类型。  
---  

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) 可以让您为电子表格加密并设置密码保护。它使用 Crypto Service Provider 提供的算法。Crypto Service Provider (或 CSP) 是一组具有不同属性的加密算法。默认的 CSP 是“办公室 97/2000 兼容”。这是一个带有一些公开已知安全问题的 CSP。使用“弱加密 (XOR)”或“办公室 97/2000 兼容”加密类型的电子表格很容易被破解。

为了解决这个问题，可以使用 Microsoft Excel 提供的强加密类型之一。可以将加密类型更改为最强的可用 CSP。对于强加密，需要最小 128 位密钥长度，例如，“Microsoft Strong Cryptographic Provider”。

您还可以使用 Aspose.Cells API 对 Excel 文件应用强加密类型进行加密和密码保护。

{{% /alert %}}  
## **在 Microsoft Excel 中应用加密**  
在 Microsoft Excel (例如 2007) 中实现文件加密:

1. 从** 工具** 菜单中选择 **选项**。  
1. 选择**安全**选项卡。  
1. 为**打开密码**字段输入一个值。  
1. 点击“高级”。  
1. 选择加密类型并确认密码。  

## **使用 Aspose.Cells 应用加密**  
下面的代码示例对文件应用强加密并设置密码。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password protect the file.
workbook.getSettings().setPassword("1234");

// Save the Excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```  

