---
title: إدراج القُطار
linktitle: قاطعات
type: docs
weight: 170
url: /ar/nodejs-cpp/create-slicer/
description: إدارة فلاتر التقسيمات في ملفات إكسل بواسطة Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**

يستخدم فاصل التصفية لتصفية البيانات بسرعة. يمكن استخدامه لتصفية البيانات سواء في جدول أو في جدول محوري. يتيح لك Microsoft Excel إنشاء فاصل تصفية عن طريق اختيار جدول أو جدول محوري ثم النقر على *إدراج > فاصل تصفية*. Aspose.Cells for Node.js via C++ يتيح أيضًا إنشاء فاصل تصفية باستخدام طريقة [**Worksheet.getSlicers().add()**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#add-pivottable-string-string-).

## **إنشاء مُقطَّع إلى جدول محوري**

يرجى الاطلاع على الكود التجريبي التالي. يقوم بتحميل ملف إكسل النموذجي الذي يحتوي على الجدول المحوري. ثم يقوم بإنشاء الفاصل بناءً على أول حقل جدول محوري أساسي. وأخيرًا، يحفظ المصنف بتنسيق [XLSX المخرجة](67338470.xlsx) و [XLSB المخرجة](67338471.xlsx). تظهر لقطة الشاشة التالية الفاصل الذي أنشأه Aspose.Cells for Node.js via C++ في ملف إكسل الناتج.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **الكود المثالي**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToPivotTable.js" >}}

## **إنشاء مُقطَّع إلى جدول Excel**

يرجى الاطلاع على رمز العينة التالي. يقوم بتحميل ملف Excel العيني ([sampleCreateSlicerToExcelTable.xlsx](sampleCreateSlicerToExcelTable.xlsx)) الذي يحتوي على جدول. ثم يقوم بإنشاء المُقطَّع بناءً على العمود الأول. أخيرًا، يحفظ برنامج العمل بتنسيق [XLSX](outputCreateSlicerToExcelTable.xlsx).

### **الكود المثالي**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToExcelTable-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
