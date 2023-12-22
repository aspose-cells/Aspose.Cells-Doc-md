---
title: احصل على سلسلة HTML5 من Cell
type: docs
weight: 90
url: /ar/net/get-html5-string-from-cell/
description: تعرف على كيفية الحصول على سلسلة HTML5 من Cell إلى Aspose.Cells for .NET API.
keywords: Get HTML5 string from Cell, Obtain HTML5 string from Cell, Manage HTML5 string of Cell
---
##  **سيناريوهات الاستخدام المحتملة**

Aspose.Cells تقوم بإرجاع السلسلة HTML للخلية باستخدام[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) الطريقة التي تقبل معلمة منطقية. إذا نجحت**خطأ شنيع** كمعلمة، فإنه سيعود عادي HTML ولكن إذا نجحت**حقيقي** كمعلمة، فإنه سيتم إرجاع سلسلة HTML5.

##  **احصل على سلسلة HTML5 من Cell**

يقوم نموذج التعليمات البرمجية التالي بإنشاء كائن مصنف وإضافة بعض النص في الخلية A1 من ورقة العمل الأولى. ثم يحصل على سلسلة Normal HTML وHTML5 من الخلية A1 باستخدام[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)الطريقة وطباعتها على وحدة التحكم.

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

##  **إخراج وحدة التحكم**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
