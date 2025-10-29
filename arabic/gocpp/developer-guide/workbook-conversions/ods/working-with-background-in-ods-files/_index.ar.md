---
title: العمل مع الخلفية في ملفات ODS باستخدام Golang عبر C++
linktitle: العمل مع الخلفية في ملفات ODS
type: docs
weight: 150
url: /ar/go-cpp/working-with-background-in-ods-files/
description: تعلم كيفية إدارة الخلفيات الملونة والرسومية في ملفات ODS باستخدام Aspose.Cells مع Golang عبر C++.
---

## **الخلفية في ملفات ODS**

يمكن إضافة خلفية إلى الأوراق في ملفات ODS. يمكن أن تكون الخلفية خلفية ملونة أو خلفية رسومية. الخلفية ليست مرئية عند فتح الملف ولكن إذا تمت طباعة الملف كملف PDF، فإن الخلفية مرئية في الملف PDF الناتج. الخلفية أيضًا مرئية في حوار معاينة الطباعة.

يوفر Aspose.Cells القدرة على قراءة معلومات الخلفية وإضافة الخلفية في ملفات ODS.

## **قراءة معلومات الخلفية من ملف ODS**

يوفر Aspose.Cells فئة [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) لإدارة الخلفية في ملفات ODS. يوضح المثال التالي استخدام فئة [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) عن طريق تحميل ملف [المصدر ODS](90112030.ods) وقراءة معلومات الخلفية. يرجى مراجعة إخراج وحدة التحكم الناتج عن الكود للمرجعية.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles.go" >}}
### **مخرجات الوحدة**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **إضافة خلفية ملونة إلى ملف ODS**

يوفر Aspose.Cells فئة [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) لإدارة الخلفية في ملفات ODS. يوضح المثال التالي استخدام خاصية [**OdsPageBackground.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/) لإضافة خلفية ملونة إلى ملف ODS. يرجى مراجعة ملف [النتيجة ODS](90112031.ods) الناتج عن الكود للمرجعية.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-1.go" >}}
## **إضافة خلفية رسومية إلى ملف ODS**

يوفر Aspose.Cells فئة [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) لإدارة الخلفية في ملفات ODS. يوضح المثال التالي استخدام خاصية [**OdsPageBackground.GetGraphicData()**](https://reference.aspose.com/cells/go-cpp/odspagebackground/getgraphicdata/) لإضافة خلفية رسومية إلى ملف ODS. يرجى مراجعة ملف [النتيجة ODS](90112030.ods) الناتج عن الكود للمرجعية.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-2.go" >}}
