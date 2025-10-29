---  
title: 使用Node.js通过C++将网页图片加载到Excel工作表中  
linktitle: 将网络图片从URL加载到Excel工作表  
type: docs  
weight: 30  
url: /zh/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/  
description: 如何使用Aspose.Cells for Node.js via C++将URL中的图片转换为实际Excel图片。  
keywords: excel显示url中的图片，excel URL转图片，显示图片在Excel中，Excel插入URL图片，转换URL为Excel图片，Excel中的URL图片，从URL加载图片，Node.js，Excel  
---  

## 从URL加载图像到Excel工作表  

Aspose.Cells for Node.js via C++提供了一种简单易用的方法，将URL中的图片加载到Excel工作表中。本文介绍了将图片数据下载到流中，然后使用Aspose.Cells API将其插入到工作表中的方法。采用这种方式，图片成为Excel文件的一部分，每次打开工作表时都无需重新下载。  

## 示例代码  

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");
const https = require("https");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "webimagebook.out.xlsx");
const url = "https://www.aspose.com/Images/aspose-logo.jpg"; // Changed http to https

let objImage;

https.get(url, (res) => {
const chunks = [];

res.on("data", (chunk) => {
chunks.push(chunk);
```  

{{% alert color="primary" %}}  
可能存在你总是希望从URL获取最新图片的情况。为实现此目标，可按照[从网页地址插入链接图片](/cells/zh/nodejs-cpp/insert-a-linked-picture-from-web-address/)文章中的指导操作。通过此方法，每次打开工作表时，图片都将从URL重新加载。  
{{% /alert %}}  


{{< app/cells/assistant language="nodejs-cpp" >}}
