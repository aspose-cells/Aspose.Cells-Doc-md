---
title: تعطيل CSS عند الحفظ إلى HTML
type: docs
weight: 320
url: /ar/net/disable-css-while-saving-to-html/
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف إكسل إلى HTML صفحة واحدة، عادةً ستُدمج عناصر CSS داخل ملف HTML وستكون موجودة في قسم HEAD. إذا قمت بإرفاق هذا الملف كمحتوى/جسم رسالة بريد إلكتروني، سيتم حذف عناصر CSS بواسطة معظم العملاء البريد الإلكتروني، مما يؤدي إلى عرض غير صحيح. تُقدم نسخة 24.12 من Aspose.Cells خيارًا يتيح تعطيل CSS بشكل اختياري، مما يسمح بتطبيق الأنماط مباشرة داخل عناصر HTML نفسها. إذا رغبت في تعيين HTML كمحتوى/جسم البريد الإلكتروني، يرجى استخدام الخاصية [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disablecss) وتعيينها إلى **true**.



## **تعطيل CSS عند الحفظ إلى HTML**

يعرض المثال التالي رمز الاستخدام الخاص بملكية [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disablecss). 



## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-DisableCss-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
