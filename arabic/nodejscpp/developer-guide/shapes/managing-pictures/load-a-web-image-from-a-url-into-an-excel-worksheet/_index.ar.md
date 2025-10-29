---  
title: تحميل صورة ويب من عنوان URL إلى ورقة إكسل باستخدام Node.js عبر C++  
linktitle: تحميل صورة ويب من عنوان URL إلى ورقة عمل إكسل  
type: docs  
weight: 30  
url: /ar/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/  
description: كيفية تحويل صورة من URL إلى صورة فعلية في إكسل باستخدام Aspose.Cells for Node.js via C++.  
keywords: إظهار الصورة من URL في إكسل، عنوان URL للصورة في إكسل، عرض الصورة في إكسل من URL، إدراج صورة من URL في إكسل، تحويل URL إلى صورة في إكسل، صورة من URL في إكسل، تحميل صورة من URL في إكسل، Node.js، إكسل  
---  

## تحميل صورة من عنوان URL إلى ورقة عمل إكسل  

 يوفر Aspose.Cells for Node.js via C++ طريقة سهلة وبسيطة لتحميل الصور من عناوين URL إلى أوراق عمل إكسل. يشرح هذا المقال كيفية تنزيل بيانات الصورة إلى تيار ثم إدراجها في ورقة العمل باستخدام API الخاص بـ Aspose.Cells. باستخدام هذه الطريقة، تصبح الصور جزءًا من ملف إكسل ولا يتم تحميلها كل مرة يتم فيها فتح ورقة العمل.  

## كود عينة  

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
 قد تكون هناك حالات ترغب فيها دائمًا في الحصول على الصورة المحدثة من عنوان URL. لتحقيق ذلك، يمكنك اتباع التعليمات الواردة في مقالة [إدراج صورة مرتبطة من عنوان ويب](/cells/ar/nodejs-cpp/insert-a-linked-picture-from-web-address/). باتباع هذه الطريقة، يتم تحميل الصورة من URL في كل مرة تُفتح فيها ورقة العمل.  
{{% /alert %}}  


{{< app/cells/assistant language="nodejs-cpp" >}}
