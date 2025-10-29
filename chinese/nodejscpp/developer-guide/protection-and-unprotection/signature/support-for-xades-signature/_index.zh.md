---  
title: 支持使用Node.js通过C++进行XAdES签名  
linktitle: 支持对Excel XP以来的高级保护设置  
type: docs  
weight: 110  
url: /zh/nodejs-cpp/support-for-xades-signature/  
description: 这篇文章介绍了如何使用Node.js通过C++和Aspose.Cells支持XAdES签名。  
keywords: 支持XAdES签名的Node.js通过C++，如何使用Node.js通过C++对Excel进行XAdES签名，如何添加XAdES签名到Node.js中的Excel  
---  

## **介绍**  

 Aspose.Cells支持使用XAdES签名对工作簿进行签名。为此，API提供了[**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature)类和[**XAdESType**](https://reference.aspose.com/cells/nodejs-cpp/xadestype)枚举类型。  

## **如何为Excel添加XAdES签名**  

 下列代码片段演示了使用 [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) 类对[源文件](101089323.xlsx)工作簿进行签名。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sourceFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const password = "pfxPassword";

const pfx = path.join(sourceDir, "AsposeDemo.pfx");


const signature = new AsposeCells.DigitalSignature(pfx, "aspose", "testXAdES", new Date());
signature.setXAdESType(AsposeCells.XAdESType.XAdES);
const dsCollection = new AsposeCells.DigitalSignatureCollection();
dsCollection.add(signature);

workbook.setDigitalSignature(dsCollection);

workbook.save(outputDir + "XAdESSignatureSupport_out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
