---
title: العمل مع الخلفية في ملفات ODS
type: docs
weight: 150
url: /ar/net/working-with-background-in-ods-files/
---

## **الخلفية في ملفات ODS**

يمكن إضافة خلفية إلى الأوراق في ملفات ODS. يمكن أن تكون الخلفية خلفية ملونة أو خلفية رسومية. الخلفية ليست مرئية عند فتح الملف ولكن إذا تمت طباعة الملف كملف PDF، فإن الخلفية مرئية في الملف PDF الناتج. الخلفية أيضًا مرئية في حوار معاينة الطباعة.

يوفر Aspose.Cells القدرة على قراءة معلومات الخلفية وإضافة الخلفية في ملفات ODS.

## **قراءة معلومات الخلفية من ملف ODS**

يوفر Aspose.Cells فئة [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) لإدارة الخلفية في ملفات ODS. يُظهر المثال البرمجي التالي استخدام فئة [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) عن طريق تحميل [ODS المصدر](90112030.ods) وقراءة معلومات الخلفية. يُرجى الاطلاع على الإخراج من وحدة التحكم الذي تم إنشاؤه بواسطة الكود للإشارة.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadODSBackground-1.cs" >}}

### **مخرجات الوحدة**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **إضافة خلفية ملونة إلى ملف ODS**

توفر Aspose.Cells الفئة [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) لإدارة الخلفية في ملفات ODS. يوضح الكود العيني التالي استخدام خاصية [**OdsPageBackground.Color**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/color) لإضافة خلفية ملونة إلى ملف ODS. يرجى الرجوع إلى ملف ODS الناتج (90112031.ods) الذي تم إنشاؤه بواسطة الكود للإحالة.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSColoredBackground-1.cs" >}}

## **إضافة خلفية رسومية إلى ملف ODS**

تتيح Aspose.Cells الفئة [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) لإدارة الخلفية في ملفات ODS. يوضح الكود العيني التالي استخدام خاصية [**OdsPageBackground.GraphicData**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/graphicdata) لإضافة خلفية رسومية إلى ملف ODS. يرجى الرجوع إلى ملف ODS الناتج (90112030.ods) الذي تم إنشاؤه بواسطة الكود للإحالة.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSGraphicBackground-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
