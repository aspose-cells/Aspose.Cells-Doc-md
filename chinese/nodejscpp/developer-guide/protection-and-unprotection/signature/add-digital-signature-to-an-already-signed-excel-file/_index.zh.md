---
title: 在使用Node.js通过C++为已签名的Excel文件添加数字签名
linktitle: 向已签名的Excel文件添加数字签名
type: docs
weight: 20
url: /zh/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: 这篇文章介绍了如何使用Aspose.Cells for Node.js via C++和Node.js为已签名的Excel文件添加数字签名。
keywords: 如何在已签名的Excel文件中添加数字签名，使用Node.js通过C++添加数字签名的方法
---

## **可能的使用场景**

 Aspose.Cells for Node.js via C++提供了[**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-)方法，可以用来为已签名的Excel文件添加数字签名。

{{% alert color="primary" %}}

 在为已签名的Excel文档添加数字签名时请注意，如果原始文档由Aspose.Cells生成，则效果良好。但如果由其他引擎（如Microsoft Excel等）生成，Aspose.Cells在加载和重新保存后可能无法保持文件一致，从而使原始签名无效。

{{% /alert %}}

## **如何向已经签名的Excel文件添加数字签名**

 以下示例代码演示了如何使用[**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-)方法为已签名的Excel文件添加数字签名。请查看此代码使用的[示例Excel文件](50528280.xlsx)，该文件已进行数字签名。然后查看由代码生成的[输出Excel文件](50528281.xlsx)。在此代码中使用了名为[AsposeDemo.pfx](50528279.pfx)的演示证书，密码为**aspose**。截图显示了示例代码执行后对示例Excel文件的效果。

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **示例代码**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

const dataDir = path.join(__dirname, "data");
// Certificate file path and password
const certFileName = path.join(dataDir, "AsposeDemo.pfx");
const password = "aspose";

// Load the workbook which is already digitally signed to add new digital signature
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleDigitallySignedByCells.xlsx"));

// Create the digital signature collection
const dsCollection = new AsposeCells.DigitalSignatureCollection();


// Create new digital signature and add it in digital signature collection
const signature = new AsposeCells.DigitalSignature(certFileName, password, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
dsCollection.add(signature);

// Add digital signature collection inside the workbook
workbook.addDigitalSignature(dsCollection);

// Save the workbook and dispose of it.
workbook.save(path.join(__dirname, "outputDigitallySignedByCells.xlsx"));
workbook.dispose();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
