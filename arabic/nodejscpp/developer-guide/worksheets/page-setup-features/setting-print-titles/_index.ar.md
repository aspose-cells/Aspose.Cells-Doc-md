---  
title: كيف تعيين عناوين الطباعة باستخدام Node.js عبر C++  
linktitle: كيفية ضبط عناوين الطباعة  
type: docs  
weight: 200  
url: /ar/nodejs-cpp/how-to-set-print-titles/  
description: يوضح هذا المقال كيف يمكنك تعيين عناوين الطباعة باستخدام مكتبة Aspose.Cells لـ Node.js عبر C++.  
keywords: طباعة الصفوف والأعمدة بشكل متكرر، كيفيّة تعيين عناوين الطباعة في Node.js، تعيين ومسح عناوين الطباعة باستخدام Node.js، كيفية مسح عناوين الطباعة في Node.js، كيفية إضافة عناوين الطباعة باستخدام Node.js، كيفية إزالة عناوين الطباعة باستخدام Node.js، كيفيّة تعيين عناوين الطباعة في Excel، كيفية مسح عناوين الطباعة في Excel.  
---  

## **سيناريوهات الاستخدام المحتملة**  

ضبط عناوين الطباعة في إكسل يضمن تكرار صفوف أو أعمدة معينة في كل صفحة مطبوعة، وهو مفيد بشكل خاص للجداول الكبيرة التي تمتد عبر صفحات متعددة. إليك بعض الأسباب التي قد تدفعك لضبط عناوين الطباعة:  

1. تحسين قابلية القراءة: تساعد عناوين الطباعة القراء على فهم البيانات من خلال إبقاء العناوين مرئية على جميع الصفحات، مما يجعل من الأسهل تفسير المعلومات على كل صفحة دون الحاجة للرجوع إلى الصفحة الأولى.  

1. تقديم مظهر احترافي: عرض العناوين أو التسميات بشكل متكرر على كل صفحة يخلق مظهرًا أكثر أناقة واحترافية للمستندات المطبوعة.  

1. تحسين التنقل: بالنسبة للمستندات التي تحتوي على بيانات موسعة، يساعد تكرار العناوين في كل صفحة على التنقل بسرعة والوصول إلى المعلومات، ويقلل من الحاجة للرجوع بين الصفحات.  

1. تقليل الأخطاء: عندما تكون العناوين موجودة على كل صفحة، يقل احتمال سوء التفسير أو أخطاء الإدخال، حيث يمكن للمستخدمين رؤية سياق البيانات بسهولة.  

1. التناسق: ضمان أن المعلومات المهمة، مثل عناوين الأعمدة أو تسميات الصفوف، دائمًا مرئية يحافظ على التناسق والوضوح Throughout المستند.  

## **كيفية ضبط عناوين الطباعة في إكسل**  

 لضبط عناوين الطباعة في إكسل، اتبع الخطوات التالية:  

1. افتح علامة تبويب تخطيط الصفحة: انقر على علامة التبويب "تخطيط الصفحة" في الشريط أعلى نافذة إكسل.  
1. الوصول إلى عناوين الطباعة: في مجموعة "إعداد الصفحة"، انقر على "عناوين الطباعة".  
1. تعيين الصفوف للتكرار: في مربع حوار "إعداد الصفحة"، انتقل إلى علامة التبويب "ورقة». في قسم "عناوين الطباعة"، حدد الصفوف التي تريد تكرارها في الأعلى بالنقر على المربع بجانب "تكرار الصفوف في أعلى" واختيار الصفوف التي تريد تكرارها.  
1. تعيين الأعمدة للتكرار (إن لزم الأمر): بالمثل، يمكنك تحديد الأعمدة للتكرار على اليسار عن طريق النقر على المربع بجانب "تكرار الأعمدة على اليسار" واختيار الأعمدة التي تريد تكرارها.  
<br>  
<img src="3.png" width=60% />  

1. أكد والطباعة: انقر على "موافق" لتطبيق الإعدادات. عند طباعة ورقة العمل، ستظهر الصفوف أو الأعمدة المحددة على كل صفحة مطبوعة.  

## **كيفية مسح عناوين الطباعة في إكسل**  

لمسح عناوين الطباعة في إكسل، تحتاج إلى إزالة الصفوف أو الأعمدة التي تم تعيينها للتكرار على كل صفحة مطبوعة. إليك الطريقة:  

1. افتح علامة تبويب تخطيط الصفحة: انقر على علامة التبويب "تخطيط الصفحة" في الشريط أعلى نافذة إكسل.  
1. الوصول إلى عناوين الطباعة: في مجموعة "إعداد الصفحة"، انقر على "عناوين الطباعة".  
1. مسح عناوين الطباعة: في مربع حوار "إعداد الصفحة"، انتقل إلى علامة التبويب "ورقة". امسح مربعات النص لـ "الصفوف لإعادة التكرار في الأعلى" و"الأعمدة لإعادة التكرار على اليسار" عن طريق حذف أي محتوى داخلها.  
<br>  
<img src="4.png" width=60% />  

1. أكد وأغلق: انقر على "موافق" لتطبيق التغييرات.  

## **كيفية تعيين عناوين الطباعة باستخدام Aspose.Cells for Node.js via C++**  

لتعيين عناوين الطباعة في ورقة عمل محددة: أولاً، قم بتحميل [ملف العينة](input.xlsx)، ثم تحتاج إلى تعديل خصائص [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) و [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) من كائن [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) للورقة المرغوبة. تعيين هذه الخصائص إلى سلسلة نطاق سيحدد عناوين الطباعة.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set rows to repeat at the top (e.g., rows 1 and 2)
worksheet.getPageSetup().setPrintTitleRows("$1:$2");

// Set columns to repeat at the left (e.g., columns A and B)
worksheet.getPageSetup().setPrintTitleColumns("$A:$B");

// Save the workbook
workbook.save("set_print_titles.pdf");
```  

نتيجة الإخراج:  
<br>  
<img src="1.png" width=60% />  

## **كيفية مسح عناوين الطباعة باستخدام Aspose.Cells for Node.js via C++**  

لمسح عناوين الطباعة في ورقة عمل محددة: أولاً، قم بتحميل [ملف العينة](input.xlsx)، ثم تحتاج إلى تعديل خصائص [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) و [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) من كائن [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) للورقة المرغوبة. تعيين هذه الخصائص إلى سلسلة فارغة سيمسح عناوين الطباعة.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Clear the rows and columns set to repeat
worksheet.getPageSetup().setPrintTitleRows("");
worksheet.getPageSetup().setPrintTitleColumns("");

// Save the workbook
workbook.save("clear_print_titles.pdf");
```  

نتيجة الإخراج:  
<br>  
<img src="2.png" width=60% />  

