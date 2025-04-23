---
title: الحصول على جميع مفرقات الصفوف المخفية بعد تحديث تصفية السيارة.
type: docs
weight: 320
url: /ar/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: تعلم كيفية الحصول على كافة فهارس الصفوف المخفية بعد تحديث التصفية التلقائية باستخدام Aspose.Cells for .NET API.
keywords: الحصول على كافة فهارس الصفوف المخفية بعد تحديث التصفية التلقائية، الحصول على كافة فهارس الصفوف المخفية بعد تحديث التصفية التلقائية، استرداد كافة فهارس الصفوف المخفية بعد تحديث التصفية التلقائية
---

## **سيناريوهات الاستخدام المحتملة**

عند تطبيق تصفية تلقائية على خلايا الورقة، يتم إخفاء بعض الصفوف تلقائيًا. ولكن قد يكون الحال أن بعض الصفوف قد تم إخفاؤها يدويًا بالفعل من قبل مستخدم اكسل ولا تكون قد تمت إخفاؤها بواسطة التصفية التلقائية. لذلك من الصعب معرفة أي من الصفوف تم إخفاؤها بواسطة التصفية التلقائية وأي منهم تم إخفاؤها يدويًا من قبل مستخدم اكسل. وتتعامل Aspose.Cells مع هذه المشكلة باستخدام الطريقة int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1). تُرجع هذه الطريقة فهارس الصفوف لكافة الصفوف التي تم إخفاؤها بواسطة التصفية التلقائية وليس يدويًا بواسطة مستخدم اكسل.

## **الحصول على جميع فهرسات الصفوف المخفية بعد تحديث تصفية السيارة.**

يرجى الاطلاع على الكود النموذجي التالي الذي يحمل [ملف اكسل عينة](64716909.xlsx) الذي يحتوي على بعض الصفوف التي تم إخفاؤها يدويًا بواسطة مستخدم اكسل. يُطبق الكود تصفية تلقائية ويقوم بتحديثها باستخدام الطريقة int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1) التي ترجع فهارس الصفوف المخفية بواسطة التصفية التلقائية. ثم يُطبع الفهارس للصفوف المخفية على وحدة التحكم مع أسماء الخلايا والقيم.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
