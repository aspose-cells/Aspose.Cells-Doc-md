---
title: دمج الأوراق العمل المتعددة في ورقة عمل واحدة
type: docs
weight: 70
url: /ar/java/combine-multiple-worksheets-into-a-single-worksheet/
description: دمج أوراق العمل المتعددة في ورقة عمل واحدة باستخدام كود Java وAspose.Cells for Java API.
keywords: دمج أوراق العمل المتعددة في ورقة عمل واحدة أحيانًا تكون بحاجة إلى دمج أوراق العمل المتعددة في ورقة عمل واحدة. يمكن تحقيق ذلك بسهولة باستخدام واجهة برمجة التطبيقات لـ Aspose.Cells. سيوضح لك هذا المقال مثال على الكود الذي يقوم بقراءة الدفتر النشط ويدمج بيانات جميع أوراق العمل النشطة في ورقة عمل واحدة داخل دفتر العمل الوجهة.
---

{{% alert color="primary" %}}

في بعض الأحيان، قد تحتاج إلى دمج أوراق العمل المتعددة في ورقة عمل واحدة. يمكن بسهولة تحقيق ذلك باستخدام واجهة برمجة التطبيقات Aspose.Cells. سيوضح لك هذا المقال مثالًا على الكود الذي يقوم بقراءة دفتر عمل المصدر ويدمج البيانات من جميع أوراق العمل المصدر في ورقة عمل واحدة داخل دفتر عمل الوجهة.

{{% /alert %}}

## **كيفية دمج أوراق العمل**

يستخدم النموذج أدناه الـ [**Range.copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#copy-com.aspose.cells.Range-) لنسخ جميع صفحات العمل الأصلية إلى ورقة واحدة داخل دفتر عمل الوجهة.

### **دفتر العمل المصدر**

يمكنك استخدام أي دفتر عمل مصدر. لهذا المثال، نحن نستخدم دفتر عمل مصدر يحتوي على ثلاثة أوراق عمل.

**ورقة العمل 1**

![todo:image_alt_text](combine-multiple-worksheets-into-a-single-worksheet_1.jpg)

**ورقة العمل 2**

![todo:image_alt_text](combine-multiple-worksheets-into-a-single-worksheet_2.jpg)

**ورقة العمل 3**

![todo:image_alt_text](combine-multiple-worksheets-into-a-single-worksheet_3.jpg)

### **دفتر العمل الناتج**

توفير تعليمات البرمجة التالية يوفر دفتر عمل يحتوي على ورقة واحدة تحتوي على البيانات من كل من الأوراق الثلاثة.

**الورقة العمل الناتجة الآن تحتوي على البيانات من جميع الأوراق الثلاثة المصدرية**

![todo:image_alt_text](combine-multiple-worksheets-into-a-single-worksheet_4.jpg)

## **تحميل دفتر عمل مصدر ودفتر عمل الناتج**

- [دفتر العمل المصدر](5473078.xlsx)
- [دفتر العمل الناتج](5473079.xlsx)

### **رمز عينة لدمج أوراق عمل متعددة في ورقة عمل واحدة**

الكود المصدري التالي يظهر كيفية دمج عدة أوراق عمل في ورقة عمل واحدة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CombineMultipleWorksheets-CombineMultipleWorksheets.java" >}}

## **موارد إضافية**

{{% alert color="primary" %}}

قد تجد المقالة [دمج ملفات عمل متعددة في دفتر عمل واحد](/cells/ar/java/combine-multiple-workbooks-into-a-single-workbook/) مفيدة للحصول على المزيد من المعلومات.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
