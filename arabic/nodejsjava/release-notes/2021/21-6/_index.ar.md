﻿---
title: Aspose.Cells for Node.js via Java 21.6 ملاحظات الإصدار
type: docs
weight: 7
url: /ar/nodejs-java/aspose-cells-for-node-js-via-java-21-6-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Node.js via Java 21.6](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-21.6/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43466|CellsException: خطأ في ZipFile أثناء استيراد ods|
|CELLSJAVA-43463|المخطط الزمني معطل بعد حفظ الملف|
|CELLSJAVA-43464|لا يسري PivotField.hideItem () في ملف الإخراج|
|CELLSJAVA-43470|يتم قطع النص بعد علامة "br" داخل العلامة "th" عند استيراد مستند HTML|
|CELLSJAVA-43481|الحصول على صيغة خاطئة من خلية|
|CELLSJAVA-43490|لا يمكن استخراج خصائص المستند|
|CELLSJAVA-43491|لا يمكن استخراج قيمة الصيغة التي تستخدم جدول البيانات بشكل صحيح|
|CELLSJAVA-43498|النتيجة المنسقة للقيمة الرقمية غير صحيحة للغة zh_CN|
|CELLSJAVA-43451|يتم عرض محتوى ملف Excel بشكل غير صحيح ولا يعمل العرض التوضيحي ChangeStyle (الربيع) بشكل صحيح|
|CELLSJAVA-43484|تخطيط المحتوى غير متناسق في Excel مع عرض PDF|
|CELLSJAVA-43465|بعض سلاسل الرسم البياني مفقودة أثناء تحويل Excel إلى PDF|
|CELLSJAVA-43468|مشكلة مع معادلة الخط المستقيم في Excel إلى التقديم PDF|
|CELLSJAVA-43432|محتوى المخطط غير متطابق عند إعادة حفظ تنسيق ملف XLS|
|CELLSJAVA-43475|الانحدار: يتم قطع الخلايا الملفوفة بالخط|
|CELLSJAVA-43478|الانحدار: NUMBERS إلى PDF ، ينقصه الكثير من البيانات|
|CELLSJAVA-43485|الانحدار: المحتوى الإضافي عند التصيير PDF من ODS|
|CELLSJAVA-43492| يؤدي تحويل ملف XML (SpreadsheetML) إلى إزالة الإعداد المخفي في "تعريف الاسم" في الإخراج XLS و XLSX|
|CELLSJAVA-43486|NullPointerException عند تحويل مستند HTML إلى مصنف|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على via Java for Node.js Aspose.Cells Aspose.Cells. في منتدى الدعم Aspose.Cells.

### **يغير سلوك Cell. الخاصيةsErrorValue.**

في الإصدارات القديمة ، تنطبق هذه الخاصية فقط على خلايا الصيغة. لجعلها متسقة مع الخصائص الأخرى ، من 21.6 نتحقق من الخلايا غير الصيغة أيضًا وإذا كانت قيمتها قيمة خطأ ، فإننا نرجع أيضًا صحيحًا. يمكن للمستخدم التحقق من Cell.IsFormula أولاً إذا كان يحتاج فقط إلى التحقق من قيمة الخطأ لخلايا الصيغة.

### **يغير سلوك Cell.Value property.**

في الإصدارات القديمة ، تقوم هذه الخاصية دائمًا بإرجاع كائن DateTime إذا تم تنسيق الخلية كوقت تاريخ وقيمتها رقمية. من 21.6 ، تُرجع هذه الخاصية القيمة الرقمية نفسها إذا تجاوزت الحد الأقصى لقيمة DateTime الصالحة. مع هذا التغيير ، يكون الكائن المرتجع متسقًا مع ما هو موضح في شريط صيغة ms excel.

### **إضافة Cell. خاصية قيمة رقمية.**

يوفر طريقة مناسبة وفعالة للمستخدم للتحقق مما إذا كانت قيمة خلية واحدة هي قيمة رقمية (int ، double ، datetime).

### **إضافة طرق محملة بشكل زائد من Cell.SetSharedFormula () / SetArrayFormula () / SetDynamicArrayFormula ().**

دعم لتعيين صيغ الصفيف والصيغ المشتركة بقيم محددة مسبقًا.

### **يضيف تعداد PdfFontEncoding.**

يمثل ترميز خط pdf مضمن.

### **يضيف خاصية PdfSaveOptions.FontEncoding.**

الحصول على أو تعيين ترميز الخطوط المضمنة في ملف pdf.

### **إضافة خاصية SlicerCacheItem.Value.**

إرجاع نص التسمية لعنصر تقطيع الشرائح. يقرأ فقط.

### **يضيف أسلوب GlobalizationSettings.GetProtectionNameOfPivotTable ().**

الحصول على اسم الحماية في PivotTable.

### **يضيف طريقة FileFormatUtil.FileFormatToSaveFormat.**

يحول تنسيق الملف لحفظ التنسيق.
