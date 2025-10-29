---
title: العمل مع الخلفية في ملفات ODS
type: docs
weight: 150
url: /ar/python-net/working-with-background-in-ods-files/
description: كيفية العمل مع الخلفية في ملفات ODS باستخدام واجهة برمجة التطبيقات Aspose.Cells for Python via .NET.
keywords: العمل مع الخلفية في ملفات ODS بواسطة بايثون، قراءة معلومات الخلفية من ملف ODS بايثون via NET، إضافة خلفية ملونة إلى ملف ODS باستخدام بايثون via NET، بايثون via NET إضافة خلفية رسومية إلى ملف ODS.
---

## **الخلفية في ملفات ODS**

يمكن إضافة خلفية إلى الأوراق في ملفات ODS. يمكن أن تكون الخلفية خلفية ملونة أو خلفية رسومية. الخلفية ليست مرئية عند فتح الملف ولكن إذا تمت طباعة الملف كملف PDF، فإن الخلفية مرئية في الملف PDF الناتج. الخلفية أيضًا مرئية في حوار معاينة الطباعة.

تقدم Aspose.Cells for Python via .NET القدرة على قراءة معلومات الخلفية وإضافة الخلفية في ملفات ODS.

## **قراءة معلومات الخلفية من ملف ODS**

Aspose.Cells for Python via .NET يوفر الفئة [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) لإدارة الخلفية في ملفات ODS. يوضح الكود النموذجي التالي استخدام الفئة [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) بتحميل ملف ODS المصدر وقراءة معلومات الخلفية. يرجى الاطلاع على ناتج وحدة التحكم الذي يتم إنشاؤه بواسطة الكود للإشارة.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ReadODSBackground-1.py" >}}

### **مخرجات الوحدة**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **إضافة خلفية ملونة إلى ملف ODS**

Aspose.Cells for Python via .NET يوفر الفئة [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) لإدارة الخلفية في ملفات ODS. يوضح الكود النموذجي التالي استخدام الخاصية [**OdsPageBackground.color**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/color/) لإضافة خلفية ملونة إلى ملف ODS. يرجى الاطلاع على ملف ODS الناتج الذي أُنشئ بواسطة الكود للإشارة.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSColoredBackground-1.py" >}}

## **إضافة خلفية رسومية إلى ملف ODS**

Aspose.Cells for Python via .NET يوفر الفئة [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) لإدارة الخلفية في ملفات ODS. يوضح الكود النموذجي التالي استخدام الخاصية [**OdsPageBackground.graphic_data**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/graphic_data/) لإضافة خلفية صورية إلى ملف ODS. يُرجى الاطلاع على ملف ODS الناتج الذي تم إنشاؤه بواسطة الكود للإشارة.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSGraphicBackground-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
