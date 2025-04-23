---
title: العمل مع الخلفية في ملفات ODS
type: docs
weight: 170
url: /ar/java/working-with-background-in-ods-files/
---

## **الخلفية في ملفات ODS**

يمكن إضافة خلفية إلى الصفحات في ملفات ODS. يمكن أن تكون الخلفية إما خلفية لونية أو خلفية رسومية. لا يظهر الخلفية عند فتح الملف ولكن إذا تمت طباعة الملف كملف PDF، فإن الخلفية مرئية في ملف PDF المُنشأ. كما أن الخلفية مرئية في معاينة الطباعة.

توفر Aspose.Cells القدرة على قراءة معلومات الخلفية وإضافة خلفية في ملفات ODS.

## **قراءة معلومات الخلفية من ملف OSD**

توفر Aspose.Cells فئة [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) لإدارة الخلفية في ملفات ODS  . يوضح الكود النموذجي التالي استخدام فئة [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) عن طريق تحميل ملف OSD المصدر وقراءة معلومات الخلفية. يرجى الرجوع إلى إخراج الكونسول الذي تم إنشاؤه بواسطة الكود للرجوع إلى الأمر.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **مخرجات الوحدة**

{{< highlight java >}}

Background Type: GRAPHIC

Backgorund Position: CENTER_CENTER

{{< /highlight >}}

## **إضافة خلفية ملونة إلى ملف ODS**

توفر Aspose.Cells فئة [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) لإدارة الخلفية في ملفات ODS  . يوضح الكود النموذجي التالي استخدام خاصية [**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color) لإضافة خلفية ملونة إلى ملف ODS. يرجى الرجوع إلى الملف ODS الناتج الذي تم إنشاؤه بواسطة الكود للرجوع إلى الأمر.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **إضافة خلفية رسومية إلى ملف ODS**

توفر Aspose.Cells فئة [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) لإدارة الخلفية في ملفات ODS  . يوضح الكود النموذجي التالي استخدام خاصية [**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData) لإضافة خلفية جرافيكية إلى ملف ODS. يرجى الرجوع إلى الملف ODS الناتج الذي تم إنشاؤه بواسطة الكود للرجوع إلى الأمر.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
{{< app/cells/assistant language="java" >}}
