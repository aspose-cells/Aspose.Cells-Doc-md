---  
title: تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة
type: docs  
weight: 280  
url: /ar/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/  
description: تعلم كيفية تطبيق فلتر متقدم في Microsoft Excel لعرض السجلات التي تلبّي معايير معقدة باستخدام API رقم Aspose.Cells for Node.js via C++.  
keywords: تطبيق فلتر متقدم عبر Node.js باستخدام C++، ضبط فلتر متقدم عبر Node.js باستخدام C++، أضف فلتر متقدم عبر Node.js باستخدام C++، إنشاء فلتر متقدم عبر Node.js باستخدام C++، كيفية إضافة فلتر متقدم إلى نطاق عبر Node.js باستخدام C++  
---  

## **سيناريوهات الاستخدام المحتملة**  

يسمح لك Microsoft Excel بتطبيق *التصفية المتقدمة* على بيانات ورقة العمل لعرض السجلات التي تلبي معايير معقدة. يمكنك تطبيق التصفية المتقدمة باستخدام أمر *البيانات > متقدمة* كما هو موضح في لقطة الشاشة هذه.  

![todo:image_alt_text](1.png)  

Aspose.Cells for Node.js via C++ يسمح لك أيضًا بتطبيق الفلتر المتقدم باستخدام طريقة [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-). تمامًا مثل Microsoft Excel، يقبل المعلمات التالية.  

**isFilter**  

يشير ما إذا كان يتم تصفية القائمة في المكان.  

**listRange**  

نطاق القائمة.  

**criteriaRange**  

نطاق المعيار.  

**copyTo**  

نطاق نسخ البيانات إليه.  

**uniqueRecordOnly**  

عرض أو نسخ الصفوف الفريدة فقط.  

## **تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة**  

الكود النموذجي التالي يطبق التصفية المتقدمة على ملف Excel [ملف Excel النموذجي](48496692.xlsx) ويولد ملف [ملف إخراج Excel](48496691.xlsx). تُظهر لقطة الشاشة كلا الملفين للمقارنة. كما ترى في لقطة الشاشة، تم تصفية البيانات داخل ملف الإخراج وفقًا لمعايير معقدة.  

![todo:image_alt_text](2.png)  

## **الكود المثالي**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-AdvancedFilter.js" >}}


