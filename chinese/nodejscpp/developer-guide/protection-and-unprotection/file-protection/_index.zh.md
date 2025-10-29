---  
title: 使用Node.js通过C++加密和解密Excel文件  
linktitle: 加密和解密Excel文件  
type: docs  
weight: 10  
url: /zh/nodejs-cpp/encrypt-and-decrypt-excel-files/  
description: 如何使用Node.js通过C++加密和解密Excel文件。锁定和解锁Excel文件。  
---  

{{% alert color="primary" %}}  
Microsoft Excel (97 - 365) 可以让您对电子表格进行加密和密码保护。它使用加密服务提供商（CSP）提供的算法，即一组具有不同属性的加密算法。默认的CSP是'Office 97/2000兼容'或'弱加密（XOR）'。选择适当的加密密钥长度很重要。有些CSP不支持超过40或56位。这被视为弱加密。对于强加密，需要最小128位的密钥长度。而且，Microsoft Windows中还包含提供强加密类型的CSP，例如 'Microsoft Strong Cryptographic Provider'。举例来说，128位加密是银行用于与其网上银行系统进行加密连接的加密级别。  

Aspose.Cells允许您使用所需的加密类型对Microsoft Excel文件进行加密和密码保护。  
{{% /alert %}}  

## **使用Microsoft Excel**  

在Microsoft Excel（例如Microsoft Excel 2003）中设置文件加密设置:  

1. 从**工具**菜单中选择**选项**。会出现一个对话框。  
 2. 选择**安全性**标签。  
 3. 输入密码并点击**高级**  
 4. 选择加密类型并确认密码。  

## ** 使用Aspose.Cells for Node.js via C++加密Excel文件**  

 以下示例演示了如何用 Aspose.Cells API 对Excel文件进行加密和密码保护。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify XOR encryption type.
workbook.setEncryptionOptions(AsposeCells.EncryptionType.XOR, 40);

// Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password protect the file.
workbook.getSettings().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```  

### ** 指定密码修改选项**  

下面的示例显示了如何使用Aspose.Cells API为现有文件设置**修改密码** Microsoft Excel选项。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```  


## ** 使用Aspose.Cells for Node.js via C++解密Excel文件**  
 很容易用 Aspose.Cells API 打开受密码保护的Excel文件并解密，如以下代码所示：  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open encrypted file with password.
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("password");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);

// Remove password.
workbook.getSettings().setPassword(null);

// Save the file.
workbook.save(filePath);
```  


## **高级主题**  
- [加密和解密ODS文件](/cells/zh/nodejs-cpp/encrypt-and-decrypt-ods-files/)  
- [设置强加密类型](/cells/zh/nodejs-cpp/setting-strong-encryption-type/)  
- [在保护工作簿时指定作者](/cells/zh/nodejs-cpp/specify-author-while-write-protecting-workbook/)  
- [验证已加密文件的密码](/cells/zh/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
