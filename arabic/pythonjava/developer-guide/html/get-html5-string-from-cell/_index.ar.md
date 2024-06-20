---
title: الحصول على سلسلة HTML5 من الخلية
type: docs
weight: 40
url: /ar/python-java/get-html5-string-from-cell/
---

## **الحصول على سلسلة HTML5 من الخلية**
باستخدام Aspose.Cells for Python via Java، يمكنك الحصول على سلسلة HTML من الخلية. يمكن تحقيق ذلك باستخدام الطريقة getHtmlString(boolean html5) (https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) المقدمة من الواجهة برمجة التطبيقات (API). إذا قمت بتمرير قيمة False كمعلمة، فسيعيد لك HTML عادي ولكن إذا قمت بتمرير True كمعلمة، فسيعيد لك سلسلة HTML5.

يقوم الكود النموذجي التالي بإنشاء كائن دفتر العمل وإضافة نص معين في الخلية A1 من الصفحة النموذجية الأولى. ثم يحصل على سلسلة HTML العادية وسلسلة HTML5 من الخلية A1 باستخدام الطريقة getHtmlString(boolean html5) (https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) ويقوم بطباعتهم.
## **الكود المثالي**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

الناتج التي تولّده مقتطف كود المعطى أعلاه هو
## **الناتج**
{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
