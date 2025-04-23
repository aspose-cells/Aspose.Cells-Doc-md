---
title: دمج العديد من سجلات العمل في سجل عمل واحد
linktitle: مدمج السجل
type: docs
weight: 66
url: /ar/python-net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى دمج دفاتِر ملاحظات تحتوي على محتوى متنوع مثل الصور والرسوم البيانية والبيانات في دفاتر عمل واحدة. يدعم Aspose.Cells لبايثون via .NET هذه الميزة. يوضح هذا المقال كيفية إنشاء تطبيق سطر أوامر في Visual Studio ودمج دفاتر ملاحظات باستخدام Aspose.Cells لبايثون via .NET بقليل من الأسطر البسيطة من الكود.

{{% /alert %}}

## **دمج أسجل العمل مع الصور والرسوم البيانية**

يقوم رمز المثال بدمج كتابي عمل في كتاب عمل واحد باستخدام Aspose.Cells for Python via .NET. يقوم الكود بتحميل كتب العمل المصدرية، ويستخدم الطريقة [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) لدمجها ويحفظ كتاب العمل الناتج.

### **السجلات المصدر**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **مصنفات الإخراج**

- [combined.xlsx](5473095.xlsx)

### **لقطات الشاشة**

أدناه تظهر لقطات من المصنفات الأصلية والمخرّجة.

{{% alert color="primary" %}}

يمكنك استخدام أي مصنف أصلي. هذه الصور مجرد لأغراض توضيحية.

{{% /alert %}}

**الورقة العمل الأولى لمصنف الرسوم البيانية - مكدسة** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**الورقة العمل الثانية لمصنف الرسوم البيانية - خطية** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**الورقة العمل الأولى لمصنف الصور - صورة** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**كل الورقات الثلاثة في مصنف الدمج - مكدسة، خطية، صورة** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CombineMultipleWorkbooksSingleWorkbook-1.py" >}}

## **مواضيع متقدمة**
- [دمج الورقات المتعددة في ورقة عمل واحدة](/cells/ar/python-net/combine-multiple-worksheets-into-a-single-worksheet/)
- [دمج الملفات](/cells/ar/python-net/merge-files/)

