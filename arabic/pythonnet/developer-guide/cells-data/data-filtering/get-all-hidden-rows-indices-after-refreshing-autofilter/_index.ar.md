---
title: الحصول على جميع مفرقات الصفوف المخفية بعد تحديث تصفية السيارة.
type: docs
weight: 320
url: /ar/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: تعلم كيفية الحصول على جميع مؤشرات الصفوف المخفية بعد تحديث التصفية التلقائية باستخدام Aspose.Cells لغة برمجة Python via .NET.
keywords: مكتبة برمجة Python لإكسيل، الحصول على جميع مؤشرات الصفوف المخفية بعد تحديث التصفية التلقائية بلغة برمجة Python، الحصول على جميع مؤشرات الصفوف المخفية بعد تحديث التصفية التلقائية بلغة برمجة Python، الحصول على جميع مؤشرات الصفوف المخفية بعد تحديث التصفية التلقائية بلغة برمجة Python
---

## **سيناريوهات الاستخدام المحتملة**

عندما تطبق التصفية التلقائية على الخلايا في ورقة العمل، فإن بعض الصفوف تختفي تلقائياً. ولكن قد يكون الوضع أن بعض الصفوف مخفية بالفعل يدوياً من قبل مستخدم إكسل، وأنها لم تكن مخفية بتلقائية بواسطة التصفية التلقائية. لذلك يصعب معرفة الصفوف المخفية بواسطة التصفية التلقائية والتي منها التي تمت إخفاؤها يدوياً بواسطة مستخدم إكسل. Aspose.Cells for Python via .NET تتعامل مع هذه المشكلة باستخدام الطريقة [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool). تُرجع هذه الطريقة مؤشرات الصفوف لكافة الصفوف التي تم إخفاؤها بواسطة التصفية التلقائية وليس يدوياً بواسطة مستخدم إكسل.

## **الحصول على جميع فهرسات الصفوف المخفية بعد تحديث تصفية السيارة.**

يرجى الاطلاع على الكود النموذجي التالي الذي يحمل [ملف إكسيل عينة](64716909.xlsx) الذي يحتوي على بعض الصفوف المخفية يدوياً بواسطة مستخدم إكسل. يطبق الكود التصفية التلقائية ويقوم بتحديثها باستخدام الطريقة [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool) التي تُرجع مؤشرات الصفوف المخفية بواسطة التصفية التلقائية. ثم يقوم بطباعة مؤشرات الصفوف المخفية على وحدة التحكم مع أسماء الخلايا والقيم.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.py" >}}

## **مخرجات الوحدة**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
