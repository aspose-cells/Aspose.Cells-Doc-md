---  
title: تحويل مخطط Excel إلى صورة مع Node.js عبر C++  
linktitle: تحويل مخطط Excel إلى صورة  
type: docs  
weight: 20  
url: /ar/nodejs-cpp/convert-an-excel-chart-to-image/  
description: تعلم كيف تحويل مخططات Excel إلى صور باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

الرسوم البيانية ملفتة للنظر من الناحية البصرية وتجعل من السهل على المستخدمين رؤية المقارنات والأنماط والاتجاهات في البيانات. على سبيل المثال، بدلاً من تحليل أعمدة الأرقام في ورقة العمل، يُظهر المخطط في لمحة ما إذا كانت المبيعات في انخفاض أم في ارتفاع، أو كيف تقارن المبيعات الفعلية بالمبيعات المتوقعة. يُطلب من الأشخاص كثيرًا تقديم المعلومات الإحصائية والرسومية بطريقة سهلة الفهم وسهلة الصيانة. تُساعد الصورة في ذلك.  

في بعض الأحيان، تكون المخططات ضرورية في تطبيق أو صفحات ويب. أو قد يكون من الضروري لملف Word، أو ملف PDF، أو عرض PowerPoint أو تطبيق آخر. في كل حالة، ترغب في عرض المخطط كصورة لاستخدامه في مكان آخر.  

{{% /alert %}}  

## **تحويل الرسوم البيانية إلى صور**  

في الأمثلة هنا، يتم تحويل مخطط دائري ومخطط عمود إلى صور.  

### **تحويل مخطط دائري إلى ملف صورة**  

أولاً، أنشئ مخطط دائري في Microsoft Excel ثم قم بتحويله إلى ملف صورة باستخدام Aspose.Cells for Node.js via C++. تنشئ الشفرة في هذا المثال صورة EMF بناءً على المخطط الدائري في ملف Excel النموذجي.  

|**الإخراج: صورة مخطط دائري**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|  

1. أنشئ مخطط دائري في Microsoft Excel:  
   1. افتح برنامج Excel الجديد في Microsoft Excel.  
   1. إدخال بعض البيانات في ورقة العمل.  
   1. أنشئ مخطط دائري بناءً على البيانات.  
   4. حفظ الملف.  

|**الملف المدخل.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|  

1. قم بتنزيل وتثبيت Aspose.Cells:  
   1. [تحميل Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
   1. قم بتثبيته على كمبيوتر التطوير الخاص بك.  

جميع مكونات [Aspose](http://www.aspose.com/) تعمل في وضع التقييم عند التثبيت الأول. وضع التقييم ليس له حد زمني ويضيف فقط علامات مائية إلى مستندات الإخراج.  

1. أنشئ مشروعًا:  
   1. ابدأ بيئة التطوير المتكاملة المفضلة لديك.  
   1. أنشئ تطبيق وحدة تحكم جديد. يستخدم هذا المثال تطبيق Node.js، لكن يمكنك إنشاؤه باستخدام أي بيئة تشغيل جافا سكريبت.  
   1. أضف مرجعًا. يستخدم هذا المشروع Aspose.Cells لذا أضف مرجعًا إلى Aspose.Cells for Node.js via C++.  
   1. كتابة الكود الذي يجد الرسم البياني ويحوله. أدناه الكود المستخدم من قِبَل المكون لإنجاز المهمة. يتم استخدام عدد قليل جدًا من السطور من الكود.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file which contains the pie chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "PieChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "PieChart.out.emf"), AsposeCells.ImageType.Emf);
```  

### **تحويل رسم بياني الأعمدة إلى ملف صورة**  

أولاً، أنشئ مخطط عمودي في Microsoft Excel وقم بتحويله إلى ملف صورة، كما هو موضح أعلاه. بعد تنفيذ الشفرة النموذجية، يتم إنشاء ملف JPEG بناءً على المخطط العمودي في ملف Excel النموذجي.  

|**ملف الإخراج: صورة رسم بياني للأعمدة.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|  

1. إنشاء رسم بياني للأعمدة في Microsoft Excel:  
   1. افتح برنامج Excel الجديد في Microsoft Excel.  
   1. إدخال بعض البيانات في ورقة العمل.  
   1. إنشاء رسم بياني للأعمدة بناءً على البيانات.  
   4. حفظ الملف.  

|**ملف الإدخال.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|  

1. إعداد مشروع، بالمراجع كما هو موضح أعلاه.  
1. تحويل الرسم البياني إلى صورة ديناميكياً. يلي الكود المستخدم من قِبَل المكون لإنجاز المهمة. الكود مماثل للكود السابق:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing excel file which contains the column chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "ColumnChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "ColumnChart.out.jpeg"), AsposeCells.ImageType.Jpeg);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
