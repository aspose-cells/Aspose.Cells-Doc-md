---
title: الحصول على سلسلة HTML5 من الخلية
type: docs
weight: 90
url: /ar/java/get-html5-string-from-cell/
---

## **سيناريوهات الاستخدام المحتملة**

تقوم Aspose.Cells بإرجاع سلسلة HTML للخلية باستخدام الطريقة [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString). إذا قمت بتمرير **false** كمعلمة، فسترجع لك نص HTML عادي ولكن إذا قمت بتمرير **true** كمعلمة، فسترجع سلسلة HTML5.

## **الحصول على سلسلة HTML5 من الخلية**

الكود العيني التالي يقوم بإنشاء كائن دفتر العمل وإضافة نص معين في الخلية A1 من ورقة العمل الأولى. ثم يحصل على سلسلة HTML عادية وسلسلة HTML5 من الخلية A1 باستخدام الطريقة [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString) ويقوم بطباعتها على وحدة التحكم.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
