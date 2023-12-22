---
title: الحصول على كافة فهارس الصفوف المخفية بعد تحديث التصفية التلقائية
type: docs
weight: 320
url: /ar/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: تعرف على كيفية الحصول على كافة فهارس الصفوف المخفية بعد تحديث التصفية التلقائية باستخدام Aspose.Cells for .NET API.
keywords: Get All Hidden Rows Indices after Refreshing AutoFilter, Obtain All Hidden Rows Indices after Refreshing AutoFilter, Retrieve All Hidden Rows Indices after Refreshing AutoFilter
---
##  **سيناريوهات الاستخدام المحتملة**

عند تطبيق عامل التصفية التلقائي على خلايا ورقة العمل، يتم إخفاء بعض الصفوف تلقائيًا. ولكن قد يكون الأمر كذلك أن بعض الصفوف مخفية يدويًا بواسطة مستخدم Excel النهائي ولا يتم إخفاؤها بواسطة عامل تصفية تلقائي. ولذلك يصعب معرفة أي من الصفوف تم إخفاؤها بواسطة عامل التصفية التلقائي وأي منها تم إخفاؤه يدويًا بواسطة مستخدم Excel النهائي. Aspose.Cells يتعامل مع هذه المشكلة باستخدام int[][**AutoFilter.Refresh (إخفاء الصفوف المنطقية)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)طريقة. تقوم هذه الطريقة بإرجاع فهارس الصفوف الخاصة بكافة الصفوف التي تم إخفاؤها بواسطة عامل التصفية التلقائي وليس يدويًا بواسطة مستخدم Excel النهائي.

##  **الحصول على كافة فهارس الصفوف المخفية بعد تحديث التصفية التلقائية**

 الرجاء مراجعة نموذج التعليمات البرمجية التالي الذي يقوم بتحميل ملف[عينة من ملف إكسل](64716909.xlsx) الذي يحتوي على بعض الصفوف المخفية يدويًا بواسطة مستخدم Excel النهائي. يطبق الكود عامل التصفية التلقائي ويحدثه باستخدام int[][**AutoFilter.Refresh (إخفاء الصفوف المنطقية)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)الطريقة التي تُرجع فهارس الصفوف لجميع الصفوف المخفية بواسطة عامل التصفية التلقائي. ثم يقوم بطباعة فهارس الصفوف المخفية على وحدة التحكم مع أسماء الخلايا وقيمها.

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

##  **إخراج وحدة التحكم**

{{< highlight "java" >}}

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
