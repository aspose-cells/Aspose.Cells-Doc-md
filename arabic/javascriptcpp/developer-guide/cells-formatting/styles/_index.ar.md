---
title: الحصول على النمط وتعيينه للخلايا
description: اكتشف كيفية أداء تنسيق البيانات وتخصيصها في Aspose.Cells for JavaScript عبر C++، بما في ذلك تنسيق النص، تنسيق الأرقام، تنسيق التاريخ، وغيرها من خيارات التخصيص. دليلنا سيساعدك على إنشاء جداول بيانات ذات مظهر احترافي مع تنسيق جذاب.
keywords: Aspose.Cells for JavaScript عبر C++، تنسيق البيانات، التخصيص، تنسيق النص، تنسيق الأرقام، تنسيق التاريخ، خيارات التخصيص، جداول البيانات، تنسيق جذاب، مظهر احترافي.
linktitle: الأنماط
type: docs
weight: 50
url: /ar/javascript-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

 قدم Aspose.Cells for JavaScript عبر C++ طريقتين جديدتين لتنسيق الخلايا: Cell.style و Cell.style. تتناول هذه المقالة منهجية Cell.style/style لمساعدتك على تحديد التقنية التي تناسبك أفضل.

{{% /alert %}} 
## **تنسيق الخلايا**
هناك طريقتان لتنسيق الخلية، كما هو موضح أدناه.
### ** باستخدام النمط**
باستخدام قطعة الكود التالية، يتم تهيئة كائن Style لكل خلية عند تنسيقها. إذا تم تنسيق العديد من الخلايا، فإنه يُستهلك قدر كبير من الذاكرة لأن كائن Style كبير. لن يتم تحرير هذه الكائنات إلا عند استدعاء طريقة Workbook.save.

**JavaScript**

{{< highlight javascript >}}
cell.style.font.isBold = true;
{{< /highlight >}}
### ** باستخدام النمط**
النهج الأول سهل ومباشر, فلماذا أضفنا النهج الثاني؟

 أضفنا المقاربة الثانية لتحسين استخدام الذاكرة. بعد استخدام الخاصية Cell.style لاسترجاع كائن Style، قم بتعديله وتعيينه مرة أخرى إلى هذه الخلية باستخدام الخاصية Cell.style. لن يتم الاحتفاظ بهذا كائن Style وسيقوم جامع القمامة في جافا سكريبت بجمعه عند عدم الإشارة إليه.

 عند تعيين خاصية Cell.style، لا يتم حفظ كائن Style لكل خلية. بدلاً من ذلك، نقارن هذا الكائن بكومة كائنات Style الداخلية لنرى إذا يمكن إعادة استخدامه. يتم الاحتفاظ فقط بكائنات Style التي تختلف عن الموجودة حالياً لكل كائن Workbook. هذا يعني أن هناك فقط عدة مئات من كائنات Style لكل ملف Excel بدلاً من الآلاف. لكل خلية، يتم الاحتفاظ فقط بفهرس إلى كومة كائنات Style.

**JavaScript**

{{< highlight javascript >}}
let style = cell.style;

style.font.isBold = true;

cell.style = style;
{{< /highlight >}}

## **مواضيع متقدمة**
- [انشاء كائن نمط باستخدام فئة CellsFactory](/cells/ar/javascript-cpp/create-style-object-using-cellsfactory-class/)
- [تعديل كائن النمط الحالي](/cells/ar/javascript-cpp/modify-an-existing-style/)
- [إعادة استخدام كائنات النمط](/cells/ar/javascript-cpp/reusing-style-objects/)
- [استخدام الأنماط المدمجة](/cells/ar/javascript-cpp/using-built-in-styles/)
