---
title: احصل على سلسلة HTML5 من Cell
type: docs
weight: 90
url: /ar/java/get-html5-string-from-cell/
---
## **سيناريوهات الاستخدام الممكنة**

Aspose.Cells تقوم بارجاع سلسلة HTML للخلية باستخدام[**getHtmlString (قيمة منطقية html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)طريقة. إذا مررت**خاطئة**كمعامل ، سيعود لك HTML عادي ولكن إذا نجحت**حقيقي**كمعامل ، فإنه سيعيد سلسلة HTML5.

## **احصل على سلسلة HTML5 من Cell**

نموذج التعليمات البرمجية التالي ينشئ كائن مصنف ويضيف بعض النص في الخلية A1 من ورقة العمل الأولى. ثم تحصل على سلسلة HTML5 و HTML العادية من الخلية A1 باستخدام الامتداد[**getHtmlString (قيمة منطقية html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)الطريقة وطباعتها على وحدة التحكم.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **إخراج وحدة التحكم**

{{< highlight "java" >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
