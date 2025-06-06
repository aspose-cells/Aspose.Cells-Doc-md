---
title: الحصول على النمط وتعيينه للخلايا
description: اكتشف كيفية أداء تنسيق البيانات والتصميم في Aspose.Cells لبايثون via .NET، بما في ذلك تنسيق النص، وتنظيم الأرقام، وتنسيق التواريخ، وخيارات التصميم الأخرى. ستساعدك دليلك على إنشاء جداول بيانات بمظهر احترافي مع تنسيقات جذابة.
keywords: Aspose.Cells لبايثون via .NET، تنسيق البيانات، التصمي، تنسيق النص، تنسيق الأرقام، تنسيق التواريخ، خيارات التصميم، جداول البيانات، تنسيقات جذابة، مظهر احترافي.
linktitle: الأنماط
type: docs
weight: 50
url: /ar/python-net/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

أسبوست كيلز للبايثون via .NET قدمت طريقتين جديدتين لتنسيق الخلايا: Cell.GetStyle و Cell.SetStyle. تراجع هذه المقالة نهج Cell.GetStyle/SetStyle لمساعدتك على الحكم على أفضل تقنية تناسبك.

{{% /alert %}} 

## **تنسيق الخلايا**
هناك طريقتان لتنسيق الخلية، كما هو موضح أدناه.

### **استخدام GetStyle()**
مع القطعة التالية من الكود، يتم تشغيل كائن النمط لكل خلية عند تنسيقها. إذا كانت العديد من الخلايا تخضع للتنسيق، فإن كمية كبيرة من الذاكرة يتم استهلاكها لأن كائن النمط هو كائن كبير. لن يتم تحرير هذه الكائنات حتى يتم استدعاء طريقة Workbook.Save.


**بايثون**

{{< highlight python >}}

cell.get_style().font.is_bold = True

{{< /highlight >}}

### **استخدام SetStyle()**
النهج الأول سهل ومباشر, فلماذا أضفنا النهج الثاني؟

أضفنا النهج الثاني لتحسين استخدام الذاكرة. بعد استخدام طريقة Cell.GetStyle لاسترداد كائن النمط، قم بتعديله واستخدم طريقة Cell.SetStyle لتعيينه مرة أخرى لهذه الخلية. لن يتم الاحتفاظ بهذا الكائن وسيقوم .NET بجمع القمامة حينما لا يتم مراجعته.

عند استدعاء طريقة Cell.SetStyle، كائن النمط لا يتم حفظه لكل خلية. بدلاً من ذلك، نقارن هذا الكائن بمجموعة أطراف الكائن الداخلية لنرى ما إذا كان بإمكانه إعادة الاستخدام. يتم الاحتفاظ بكائنات النمط التي تختلف عن القائمة من الكائنات القائمة. وهذا يعني أنه لا يوجد سوى عدد قليل من الكائنات النمط لكل ملف إكسل بدلاً من الآلاف. بالنسبة لكل خلية، يتم الاحتفاظ بفهرس لمجموعة أطراف الكائن النمط.



**بايثون**

{{< highlight python >}}

style = cell.get_style()
style.font.is_bold = True
cell.set_style(style)

{{< /highlight >}}

## **مواضيع متقدمة**
- [انشاء كائن نمط باستخدام فئة CellsFactory](/cells/ar/python-net/create-style-object-using-cellsfactory-class/)
- [تعديل كائن النمط الحالي](/cells/ar/python-net/modify-an-existing-style/)
- [إعادة استخدام كائنات النمط](/cells/ar/python-net/reusing-style-objects/)
- [استخدام الأنماط المدمجة](/cells/ar/python-net/using-built-in-styles/)


