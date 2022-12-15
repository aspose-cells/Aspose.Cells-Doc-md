---
title: احصل على سلسلة HTML5 من Cell
type: docs
weight: 40
url: /ar/python-java/get-html5-string-from-cell/
---
## **احصل على سلسلة HTML5 من Cell**
باستخدام Aspose.Cells for Python via Java ، يمكنك الحصول على سلسلة HTML من الخلية. يمكن تحقيق ذلك باستخدام ملف[getHtmlString (قيمة منطقية html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) المقدمة من API. إذا نجحت**خاطئة**كمعامل ، سيعود لك HTML عادي ولكن إذا نجحت**حقيقي**كمعامل ، فإنه سيعيد سلسلة HTML5.

نموذج التعليمات البرمجية التالي ينشئ كائن مصنف ويضيف بعض النص في الخلية A1 من ورقة العمل الأولى. ثم تحصل على سلسلة HTML5 و HTML العادية من الخلية A1 باستخدام الامتداد[getHtmlString (قيمة منطقية html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) طريقة وطبعها.
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

التالي هو الناتج الناتج عن مقتطف الشفرة المقدم أعلاه.
## **انتاج |**
{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
