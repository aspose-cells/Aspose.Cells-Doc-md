---
title: دمج دفاتر عمل متعددة في دفتر عمل واحد مع Golang عبر C++
linktitle: مدمج السجل
type: docs
weight: 66
url: /ar/go-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: تعلم كيفية دمج دفاتر عمل متعددة في دفتر واحد باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى دمج دفاتر عمل تحتوي على محتوى مختلف مثل الصور، المخططات، والبيانات إلى دفتر عمل واحد. يدعم Aspose.Cells هذه الميزة. تظهر هذه المقالة كيفية إنشاء تطبيق وحدة التحكم في Visual Studio ودمج دفاتر العمل ببضع أسطر برمجية بسيطة باستخدام Aspose.Cells.

{{% /alert %}}

## **دمج أسجل العمل مع الصور والرسوم البيانية**

يقوم الكود المثالي بدمج سجلي عمل في سجل عمل واحد باستخدام Aspose.Cells. الكود يحمل سجلي العمل المصدر ويستخدم الطريقة [**Workbook::Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) لدمجهم ويحفظ سجل العمل الناتج.

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeWorkbooks.go" >}}
## **مواضيع متقدمة**
- [دمج الورقات المتعددة في ورقة عمل واحدة](/cells/ar/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [دمج الملفات](/cells/ar/cpp/merge-files/)
