---
title: الحصول على سلسلة HTML5 من الخلية باستخدام Golang عبر C++
linktitle: الحصول على سلسلة HTML5 من الخلية
type: docs
weight: 90
url: /ar/go-cpp/get-html5-string-from-cell/
description: تعلم كيفية الحصول على سلسلة HTML5 من خلية باستخدام API Aspose.Cells for C++.
keywords: الحصول على سلسلة HTML5 من الخلية، الحصول على سلسلة HTML5 من الخلية، إدارة سلسلة HTML5 للخلية
---

## **سيناريوهات الاستخدام المحتملة**

تُعيد Aspose.Cells سلسلة HTML للخلية باستخدام الطريقة [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) التي تقبل معلمة منطقية. إذا قمت بتمرير **false** كمعامل، فسيتم إرجاع HTML عادي، وإذا قمت بتمرير **true**، فسيتم إرجاع سلسلة HTML5.

## ** الحصول على سلسلة HTML5 من الخلية**

يقوم الكود النموذجي التالي بإنشاء كائن جدول بيانات ويضيف بعض النص في الخلية A1 للورقة العمل الأولى. يتم الحصول بعد ذلك على السلسلة العادية لـ HTML وسلسلة HTML5 من الخلية A1 باستخدام الأسلوب  [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) ويتم طباعتها على وحدة التحكم.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetHtml5StringFromCell.go" >}}
## **مخرجات الوحدة**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
