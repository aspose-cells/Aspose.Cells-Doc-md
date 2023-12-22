---
title: الحصول على النمط وتعيينه للخلايا
description: اكتشف كيفية إجراء تنسيق البيانات وتصميمها في Aspose.Cells for .NET، بما في ذلك تنسيق النص وتنسيق الأرقام وتنسيق التاريخ وخيارات التصميم الأخرى. سيساعدك دليلنا على إنشاء جداول بيانات ذات مظهر احترافي بتنسيق جذاب.
keywords: Aspose.Cells for .NET, data formatting, styling, text formatting, number formatting, date formatting, styling options, spreadsheets, attractive formatting, professional-looking.
linktitle: الأنماط
type: docs
weight: 50
url: /ar/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 قدم طريقتين جديدتين لتنسيق الخلايا: Cell.GetStyle وCell.SetStyle. تتناول هذه المقالة طريقة Cell.GetStyle/SetStyle لمساعدتك في تحديد التقنية التي تناسبك بشكل أفضل.

{{% /alert %}} 
##  **التنسيق Cells**
هناك طريقتان لتنسيق الخلية، كما هو موضح أدناه.
###  **باستخدام GetStyle ()**
باستخدام الجزء التالي من التعليمات البرمجية، يتم بدء كائن النمط لكل خلية عند تنسيقها. إذا تم تنسيق عدد كبير من الخلايا، فسيتم استهلاك قدر كبير من الذاكرة لأن كائن النمط كائن كبير. لن يتم تحرير كائنات النمط هذه حتى يتم استدعاء الأسلوب Workbook.Save.



**C#**

{{< highlight "csharp" >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
###  **باستخدام سيت ستايل ()**
النهج الأول سهل ومباشر، فلماذا أضفنا النهج الثاني؟

أضفنا الطريقة الثانية لتحسين استخدام الذاكرة. بعد استخدام الأسلوب Cell.GetStyle لاسترداد كائن النمط، قم بتعديله واستخدام الأسلوب Cell.SetStyle لتعيينه مرة أخرى إلى هذه الخلية. لن يتم الاحتفاظ بكائن النمط هذا وسيجمعه .NET GC عندما لا تتم الإشارة إليه.

عند استدعاء الأسلوب Cell.SetStyle، لا يتم حفظ كائن النمط لكل خلية. بدلاً من ذلك، نقوم بمقارنة كائن النمط هذا بتجميع كائنات النمط الداخلي لمعرفة ما إذا كان يمكن إعادة استخدامه. يتم الاحتفاظ فقط بكائنات النمط التي تختلف عن الكائنات الموجودة لكل كائن مصنف. وهذا يعني أنه لا يوجد سوى عدة مئات من كائنات النمط لكل ملف Excel بدلاً من الآلاف. لكل خلية، يتم الاحتفاظ فقط بفهرس تجمع كائنات النمط.



**C#**

{{< highlight "csharp" >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

##  **مواضيع متقدمة**
- [قم بإنشاء كائن النمط باستخدام فئة CellsFactory](/cells/ar/net/create-style-object-using-cellsfactory-class/)
- [تعديل نمط موجود](/cells/ar/net/modify-an-existing-style/)
- [إعادة استخدام كائنات النمط](/cells/ar/net/reusing-style-objects/)
- [استخدام الأنماط المضمنة](/cells/ar/net/using-built-in-styles/)


