---  
title: تحسين استخدام الذاكرة عند العمل مع ملفات كبيرة تحتوي على مجموعات بيانات ضخمة عبر Node.js باستخدام C++  
linktitle: تحسين استخدام الذاكرة أثناء العمل مع ملفات كبيرة تحتوي على مجموعات بيانات كبيرة  
type: docs  
weight: 180  
url: /ar/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/  
---  

{{% alert color="primary" %}}  

عند بناء ملف عمل مع مجموعات بيانات كبيرة، أو قراءة ملف Microsoft Excel كبير، فإن إجمالي حجم الذاكرة التي ستستهلكها العملية دائمًا ما يكون مصدر قلق. هناك تدابير يمكن تكييفها لمواجهة التحدي. ي提供 Aspose.Cells for Node.js via C++ بعض الخيارات ذات الصلة واستدعاءات API لتخفيض، تقليل وتحسين استخدام الذاكرة. كما يمكن أن يساعد في جعل العملية أكثر كفاءة وتشغيلًا أسرع.  

استخدام الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) لتحسين استخدام الذاكرة لبيانات الخلايا وتقليل التكلفة الإجمالية للذاكرة. عند بناء مجموعة بيانات كبيرة للخلايا، يمكن أن يوفر مبلغًا معينًا من الذاكرة بالمقارنة بالاستخدام الافتراضي ([**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)).  

{{% /alert %}}  

## **تحسين الذاكرة**  

### **قراءة ملفات Excel الكبيرة**  

توضح المثال التالي كيفية قراءة ملف إكسل كبير بوضع محسن.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the LoadOptions
const opt = new AsposeCells.LoadOptions();
// Set the memory preferences
opt.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Instantiate the Workbook
// Load the Big Excel file having large Data set in it
const wb = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), opt);
```  

### **كتابة ملفات إكسيل الكبيرة**  

المثال التالي يوضح كيفية كتابة مجموعة بيانات كبيرة إلى ورقة عمل بوضع محسن.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Set the memory preferences
wb.getSettings().setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

// To change the memory setting of existing sheets, please change memory setting for them manually:
let cells = wb.getWorksheets().get(0).getCells();
cells.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........

// Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
cells = wb.getWorksheets().add("Sheet2").getCells();
// .........
// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........
```  

## **احترس**  

الخيار الافتراضي، [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)، يُطبق على جميع الإصدارات. في بعض الحالات، مثل بناء ملف عمل يحتوي على مجموعة بيانات كبيرة للخلايا، قد يُحسن خيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) استهلاك الذاكرة ويقلل من تكلفتها على التطبيق. ومع ذلك، قد يؤدي هذا الخيار إلى تدهور الأداء في بعض الحالات الخاصة كما يلي.  

1. **الوصول العشوائي والمتكرر للخلايا**: أكثر ترتيب كفاءة للوصول إلى مجموعة الخلايا هو خلية تلو الأخرى في صف واحد، ثم صف بصف. خاصة، إذا قمت بالوصول إلى الصفوف/الخلايا بواسطة Enumerator المستمد من [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)، [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection)، و[**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)، فسيتم تعظيم الأداء مع [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).  
2. **إدراج وحذف الخلايا والصفوف**: يرجى ملاحظة أنه إذا كانت هناك الكثير من العمليات لإدراج/حذف الخلايا/الصفوف، فإن تدهور الأداء سيكون ملحوظًا لوضع *MemoryPreference* مقارنة بوضع *Normal*.  
3. **العمل على أنواع مختلفة من الخلايا**: إذا كانت معظم الخلايا تحتوي على قيم نصية أو صيغ، فإن تكلفة الذاكرة ستكون نفس وضع *Normal*، ولكن إذا كانت هناك الكثير من الخلايا الفارغة، أو القيم الرقمية، أو القيم البوليانية، وما إلى ذلك، فسيعطي الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) أداءً أفضل.  

