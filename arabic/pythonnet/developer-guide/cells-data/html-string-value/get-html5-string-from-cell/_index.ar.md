---
title: الحصول على سلسلة HTML5 من الخلية
type: docs
weight: 90
url: /ar/python-net/get-html5-string-from-cell/
description: تعلم كيفية الحصول على سلسلة HTML5 من الخلية من خلال API Aspose.Cells for Python via .NET.
keywords: مكتبة Python Excel، الحصول على سلسلة HTML5 من الخلية باستخدام Python، الحصول على سلسلة HTML5 من الخلية باستخدام Python، إدارة سلسلة HTML5 للخلية في Python.
---

## **سيناريوهات الاستخدام المحتملة**

يُمكن أن يُرجع Aspose.Cells for Python via .NET سلسلة HTML من الخلية باستخدام الطريقة [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) التي تقبل معلمة منطقية. إذا قمت بتمرير **false** كمعلمة، سيُرجع HTML عادي ولكن إذا قمت بتمرير **true** كمعلمة، سيُرجع سلسلة HTML5.

## **الحصول على سلسلة HTML5 من الخلية**

يقوم الكود النموذجي التالي بإنشاء كائن جدول بيانات ويضيف بعض النص في الخلية A1 للورقة العمل الأولى. يتم الحصول بعد ذلك على السلسلة العادية لـ HTML وسلسلة HTML5 من الخلية A1 باستخدام الأسلوب  [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) ويتم طباعتها على وحدة التحكم.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetHTML5StringFromCell.py" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
