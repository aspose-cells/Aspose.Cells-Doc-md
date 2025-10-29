---
title: الحصول على سلسلة HTML5 من الخلية
type: docs
weight: 90
url: /ar/nodejs-cpp/get-html5-string-from-cell/
description: تعلم كيفية الحصول على سلسلة HTML5 من الخلية عبر واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: الحصول على سلسلة HTML5 من الخلية عبر Node.js باستخدام C++، الحصول على سلسلة HTML5 من الخلية عبر Node.js باستخدام C++، إدارة سلسلة HTML5 للخلية عبر Node.js باستخدام C++
---

## **سيناريوهات الاستخدام المحتملة**

يعيد Aspose.Cells السلسلة HTML للخلية باستخدام طريقة [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) التي تقبل معيار boolean. إذا مررت **false** كمعامل، فسيعود بـ HTML عادي، وإذا مررت **true**، فسيعود بسلسلة HTML5.

## **الحصول على سلسلة HTML5 من الخلية**

يقوم رمز العينة التالي بإنشاء كائن دفتر عمل ويضيف بعض النص إلى الخلية A1 من ورقة العمل الأولى. ثم يحصل على سلاسل HTML العادية وHTML5 من الخلية A1 باستخدام طريقة [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) ويطبعها على وحدة التحكم.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-HtmlStringValue-GetHtml5String.js" >}}


## **مخرجات الوحدة**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
