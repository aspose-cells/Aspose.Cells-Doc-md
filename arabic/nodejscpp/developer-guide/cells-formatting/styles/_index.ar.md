---
title: الحصول على النمط وتعيينه للخلايا
description: اكتشف كيفية أداء تنسيق البيانات وتنسيقها بسهولة في Aspose.Cells for Node.js via C++، بما في ذلك تنسيق النص، وتنسيق الأرقام، وتنسيق التاريخ، وخيارات التنسيق الأخرى. ستساعدك أدلاحنا على إنشاء جداول بيانات ذات مظهر احترافي مع تنسيق جذاب.
keywords: Aspose.Cells for Node.js via C++، تنسيق البيانات، التشكيل، تنسيق النص، تنسيق الأرقام، تنسيق التاريخ، خيارات التنسيق، جداول البيانات، تنسيق جذاب، مظهر احترافي.
linktitle: الأنماط
type: docs
weight: 50
url: /ar/nodejs-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

قدم Aspose.Cells for Node.js via C++ طريقتين جديدتين لتنسيق الخلايا: Cell.getStyle و Cell.setStyle. تستعرض هذه المقالة طريقة Cell.getStyle/setStyle لمساعدتك في اختيار التقنية التي تناسبك أكثر.

{{% /alert %}} 
## **تنسيق الخلايا**
هناك طريقتان لتنسيق الخلية، كما هو موضح أدناه.
### **باستخدام getStyle()**
باستخدام قطعة الكود التالية، يتم تهيئة كائن Style لكل خلية عند تنسيقها. إذا تم تنسيق العديد من الخلايا، فإنه يُستهلك قدر كبير من الذاكرة لأن كائن Style كبير. لن يتم تحرير هذه الكائنات إلا عند استدعاء طريقة Workbook.save.

**JavaScript**

{{< highlight javascript >}}
cell.getStyle().getFont().setIsBold(true);
{{< /highlight >}}
### **باستخدام setStyle()**
النهج الأول سهل ومباشر, فلماذا أضفنا النهج الثاني؟

لقد أضفنا الطريقة الثانية لتحسين استخدام الذاكرة. بعد استخدام طريقة Cell.getStyle لاسترداد كائن Style، قم بتعديله واستخدم طريقة Cell.setStyle لإعادته إلى هذه الخانة. لن يتم الاحتفاظ بهذا كائن Style، وسيتم جمع القمامة الخاص بجافا سكريبت عندما لا يكون مرجعًا.

عند استدعاء طريقة Cell.setStyle، لا يتم حفظ كائن Style لكل خلية على حدة. بدلاً من ذلك، نقارن كائن Style هذا مع مجموعة “مسبقة التصنيف” من الكائنات Style الداخلية لنرى إذا كان يمكن إعادة استخدامه. يتم الاحتفاظ فقط بكائنات Style التي تختلف عن الكائنات الموجودة. هذا يعني أن هناك بضع مئات فقط من كائنات Style لكل ملف Excel بدلاً من الآلاف. يتم الاحتفاظ فقط بمؤشر إلى مجموعة كائنات Style لكل خلية.

**JavaScript**

{{< highlight javascript >}}
let style = cell.getStyle();

style.getFont().setIsBold(true);

cell.setStyle(style);
{{< /highlight >}}

## **مواضيع متقدمة**
- [انشاء كائن نمط باستخدام فئة CellsFactory](/cells/ar/nodejs-cpp/create-style-object-using-cellsfactory-class/)
- [تعديل كائن النمط الحالي](/cells/ar/nodejs-cpp/modify-an-existing-style/)
- [إعادة استخدام كائنات النمط](/cells/ar/nodejs-cpp/reusing-style-objects/)
- [استخدام الأنماط المدمجة](/cells/ar/nodejs-cpp/using-built-in-styles/)

{{< app/cells/assistant language="nodejs-cpp" >}}
