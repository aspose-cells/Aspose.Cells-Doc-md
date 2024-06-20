---
title: الحصول على سلسلة HTML5 من الخلية
type: docs
weight: 90
url: /ar/net/get-html5-string-from-cell/
description: تعلم كيفية الحصول على سلسلة HTML5 من الخلية من خلال واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: الحصول على سلسلة HTML5 من الخلية، الحصول على سلسلة HTML5 من الخلية، إدارة سلسلة HTML5 للخلية
---

## **سيناريوهات الاستخدام المحتملة**

تعيد Aspose.Cells سلسلة HTML للخلية باستخدام الطريقة [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) التي تقبل معلمة منطقية. إذا قمت بتمرير **false** كمعلمة، ستعيد HTML عادي ولكن إذا قمت بتمرير **true** كمعلمة، ستقوم بإرجاع سلسلة HTML5.

## **الحصول على سلسلة HTML5 من الخلية**

يقوم الكود النموذجي التالي بإنشاء كائن جدول بيانات ويضيف بعض النص في الخلية A1 للورقة العمل الأولى. يتم الحصول بعد ذلك على السلسلة العادية لـ HTML وسلسلة HTML5 من الخلية A1 باستخدام الأسلوب  [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) ويتم طباعتها على وحدة التحكم.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
