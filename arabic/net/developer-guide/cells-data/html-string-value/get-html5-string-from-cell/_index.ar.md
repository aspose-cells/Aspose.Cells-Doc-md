---
title: احصل على سلسلة HTML5 من Cell
type: docs
weight: 90
url: /ar/net/get-html5-string-from-cell/
---
## **سيناريوهات الاستخدام الممكنة**

Aspose.Cells تقوم بارجاع سلسلة HTML للخلية باستخدام[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) الطريقة التي تقبل معلمة منطقية. إذا مررت**خاطئة**كمعامل ، فإنه سيعيد HTML عادي ولكن إذا قمت بتمريره**حقيقي** كمعامل ، فإنه سيعيد سلسلة HTML5.

## **احصل على سلسلة HTML5 من Cell**

نموذج التعليمات البرمجية التالي ينشئ كائن مصنف ويضيف بعض النص في الخلية A1 من ورقة العمل الأولى. ثم تحصل على سلسلة HTML5 و HTML العادية من الخلية A1 باستخدام الامتداد[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)الطريقة وطباعتها على وحدة التحكم.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
