---  
title: الجدولات والنطاقات مع Node.js عبر C++  
linktitle: الجداول والنطاقات  
type: docs  
weight: 50  
url: /ar/nodejs-cpp/tables-and-ranges/  
---  

## **مقدمة**  

أحيانًا تقوم بإنشاء جدول في برنامج Microsoft Excel ولا ترغب في الاستمرار في استخدام وظائف الجدول الخاصة به. بدلاً من ذلك، ترغب في شيء يبدو وكأنه جدول. للحفاظ على البيانات في جدول دون فقدان التنسيق، قم بتحويل الجدول إلى نطاق عادي من البيانات.  
يدعم Aspose.Cells هذه الميزة في برنامج Microsoft Excel للجداول وكائنات القوائم.  

## **استخدام Microsoft Excel**  

استخدم ميزة **تحويل إلى نطاق** لتحويل الجدول إلى نطاق بسرعة دون فقدان التنسيق. في Microsoft Excel 2007/2010:  

1. انقر في أي مكان في الجدول للتأكد من أن الخلية النشطة في عمود الجدول.  
1. في علامة التبويب **التصميم**، في مجموعة **الأدوات**، انقر فوق **تحويل إلى نطاق**.  

## **استخدام Aspose.Cells**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");

// Open an existing file that contains a table/list object in it
const wb = new AsposeCells.Workbook(filePath);

// Convert the first table/list object (from the first worksheet) to normal range
wb.getWorksheets().get(0).getListObjects().get(0).convertToRange();

// Save the file
wb.save(path.join(dataDir, "output.xlsx"));
```  

{{% alert color="primary" %}}  

لا تعود ميزات الجداول متاحة بعد تحويل الجدول إلى نطاق. على سبيل المثال، لم تعد رؤوس الصفوف تحتوي على السهام للفرز والتصفية، والإشارات المنظمة (المشار إليها باستخدام أسماء الجدول) التي تم استخدامها في الصيغ تتحول إلى مراجع خلية عادية.  

{{% /alert %}}  

## **تحويل الجدول إلى نطاق بخيارات**  

يوفر Aspose.Cells خيارات إضافية أثناء تحويل الجدول إلى نطاق من خلال فئة [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/). توفر الفئة [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) خاصية [**getLastRow()**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/#getLastRow--) التي تتيح لك تعيين الفهرس الأخير لصف الجدول. سيتم الاحتفاظ بتنسيق الجدول حتى الفهرس المحدد لصف، وسيتم إزالة بقية التنسيق.  

يظهر الشيفرة المثالية أدناه كيفية استخدام الفئة [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");
// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.TableToRangeOptions();
options.setLastRow(5);

// Convert the first table/list object (from the first worksheet) to normal range
workbook.getWorksheets().get(0).getListObjects().get(0).convertToRange(options);

// Save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

