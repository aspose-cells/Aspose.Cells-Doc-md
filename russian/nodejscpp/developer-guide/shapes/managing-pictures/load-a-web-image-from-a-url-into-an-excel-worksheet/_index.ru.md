---  
title: Загрузка веб изображения по URL в лист Excel с помощью Node.js via C++  
linktitle: Загрузка веб изображения из URL в рабочий лист Excel  
type: docs  
weight: 30  
url: /ru/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/  
description: Как преобразовать изображение по URL в реальное изображение Excel с помощью Aspose.Cells for Node.js via C++.  
keywords: excel отображение изображения по URL, excel url к изображению, отображение изображения в excel из url, вставка изображения из url в excel, преобразование url в изображение в excel, excel изображение из url, загрузка изображения из url в excel, Node.js, Excel  
---  

## Загрузка изображения из URL в рабочий лист Excel  

Aspose.Cells for Node.js via C++ предоставляет простой и удобный способ загрузки изображений по URL в листы Excel. Эта статья объясняет, как скачивать данные изображения в поток, а затем вставлять их в лист с помощью API Aspose.Cells. Используя этот метод, изображения становятся частью файла Excel и не скачиваются при каждом открытии листа.  

## Образец кода  

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
Могут быть случаи, когда вы всегда хотите получить обновленное изображение с URL. Для достижения этого следуйте инструкциям, приведенным в статье [Вставка связанного изображения из веб-адреса](/cells/ru/nodejs-cpp/insert-a-linked-picture-from-web-address/). Следуя этому методу, изображение загружается с URL каждый раз при открытии листа.  
{{% /alert %}}  


