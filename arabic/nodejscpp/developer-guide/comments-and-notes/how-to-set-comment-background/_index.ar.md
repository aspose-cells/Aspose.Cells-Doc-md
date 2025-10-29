---
title: كيفية تغير خلفية التعليق في Excel باستخدام Node.js عبر C++
linktitle: خلفية التعليق
type: docs
weight: 190
url: /ar/nodejs-cpp/how-to-set-comment-background/
description: كيفية تغيير لون التعليق وإدراج صورة أو صورة في التعليق في Excel باستخدام Aspose.Cells for Node.js via C++.
keywords: إضافة صورة داخلية ولون خلفية التعليق في Excel عبر Node.js بواسطة C++
---

{{% alert color="primary" %}}
يتم إضافة التعليقات إلى الخلايا لتسجيل ملاحظات، من تفاصيل كيفية عمل صيغة، من أين يأتي قيمة معينة، أو أسئلة من المراجعين. تلعب التعليقات دورًا مهمًا جدًا عندما يناقش عدة أشخاص أو يراجعون نفس المستند في أوقات مختلفة. كيف يمكن تمييز تعليقات الأشخاص المختلفين؟ نعم، يمكننا تعيين لون خلفية مختلف لكل تعليق. ولكن عندما نحتاج إلى معالجة الكثير من المستندات والكثير من التعليقات، فإن القيام بذلك يدويًا يعد كارثة. لحسن الحظ، يوفر [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) API يتيح لك القيام بذلك برمجياً.
{{% /alert %}}

## **كيفية تغيير اللون في التعليق في إكسل**

عندما لا تحتاج إلى لون خلفية افتراضي للتعليقات، قد ترغب في استبداله بلون تهتم به. كيف أغير لون خلفية صندوق التعليقات في Excel؟

سيقوم الكود التالي بإرشادك كيفية استخدام [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) لإضافة لون خلفية مفضلة إلى التعليقات باختيارك الخاص.

لقد أعددنا لك [ملف نموذجي](exmaple.xlsx). يُستخدم هذا الملف لتهيئة كائن Workbook في الشيفرة أدناه.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Initialize a new workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "example.xlsx"));

// Accessing the newly added comment
const comment = workbook.getWorksheets().get(0).getComments().get(0);

// change background color
const shape = comment.getCommentShape();
shape.getFill().getSolidFill().setColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "result.xlsx"));
```

قم بتشغيل الكود أعلاه وستحصل على ملف [output file](result.xlsx).

## **كيفية إدراج صورة أو صورة في التعليق في إكسل**

يتيح Microsoft Excel للمستخدمين تخصيص مظهر وأسلوب جداول البيانات إلى حد كبير. من الممكن أيضًا إضافة صور خلفية إلى التعليقات. يمكن أن يكون إضافة صورة خلفية اختيارًا جماليًا أو يُستخدم لتعزيز العلامة التجارية.

ينشئ الكود أدناه ملف XLSX من الصفر باستخدام API [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/)، ويضيف تعليقًا بخلفية صورة إلى الخلية A1.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
const workbook = new AsposeCells.Workbook();

// Get a reference of comments collection with the first sheet
const comments = workbook.getWorksheets().get(0).getComments();

// Add a comment to cell A1
const commentIndex = comments.add(0, 0);
const comment = comments.get(commentIndex);
comment.setNote("First note.");
comment.getFont().setName("Times New Roman");

// Load an image into stream
const fs = require("fs");
const bmp = fs.readFileSync(path.join(dataDir, "image2.jpg"));
const ms = Buffer.from(bmp);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(ms);

// Save the workbook
const outputFilePath = path.join(dataDir, "commentwithpicture1.out.xlsx");
workbook.save(outputFilePath, AsposeCells.SaveFormat.Xlsx);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
