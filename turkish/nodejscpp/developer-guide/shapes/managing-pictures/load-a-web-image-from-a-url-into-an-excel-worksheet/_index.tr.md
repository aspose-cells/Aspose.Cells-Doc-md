---  
title: Web den resim yükleme ve Excel çalışma sayfasına aktarma araştırması  
linktitle: Bir URL den Web Resmini Excel Çalışma Sayfasına Yükleme  
type: docs  
weight: 30  
url: /tr/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/  
description: Bir Resmi URL den gerçek Excel resmi haline dönüştürme nasıl yapılır, öğrenin (Aspose.Cells for Node.js via C++).  
keywords: excel url den resim gösterme, excel url den resim ekleme, excel den url ile resim gösterme, excel url den resim ekleme, url den resim dönüştürme, excel url den resim, url den resim yükleme in excel, Node.js, Excel  
---  

## Bir URL'den Bir Resmi Excel Çalışma Sayfasına Yükleme  

Aspose.Cells for Node.js via C++, URL'lerden resim yüklemek ve Excel Çalışma Sayfalarına eklemek için basit ve kolay bir yol sağlar. Bu makale, resim verilerini bir akışa indirip sonra Aspose.Cells API kullanarak çalışma sayfasına nasıl ekleyeceğinizi açıklar. Bu yöntemi kullanarak, resimler Excel dosyasının bir parçası olur ve her çalışma sayfası açıldığında yeniden indirilmez.  

## Örnek Kod  

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
Her zaman güncellenmiş resmi URL'den almak istiyorsanız, [Bağlantılı Resim Ekleme Web Adresinden] ( /cells/tr/nodejs-cpp/insert-a-linked-picture-from-web-address/) makalesindeki talimatları takip edebilirsiniz. Bu yöntemle, çalışma sayfası her açıldığında resim URL'den yüklenir.  
{{% /alert %}}  


{{< app/cells/assistant language="nodejs-cpp" >}}
