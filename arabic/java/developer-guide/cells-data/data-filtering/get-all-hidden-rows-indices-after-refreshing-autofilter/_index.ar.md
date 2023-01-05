---
title: احصل على جميع مؤشرات الصفوف المخفية بعد تحديث التصفية التلقائية
type: docs
weight: 240
url: /ar/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---
## **سيناريوهات الاستخدام الممكنة**

عند تطبيق مرشح تلقائي على خلايا ورقة العمل ، يتم إخفاء بعض الصفوف تلقائيًا. ولكن قد يكون الأمر كذلك أن بعض الصفوف مخفية بالفعل يدويًا بواسطة مستخدم Excel النهائي ولا يتم إخفاؤها بواسطة عامل التصفية التلقائي. لذلك ، يصعب معرفة الصفوف المخفية بواسطة عامل التصفية التلقائي وأي منها مخفي يدويًا بواسطة مستخدم Excel النهائي. Aspose.Cells يتعامل مع هذه المشكلة باستخدام int [][**AutoFilter.refresh (إخفاء الصفوف المنطقية)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)) طريقة. تقوم هذه الطريقة بإرجاع فهارس الصفوف لجميع الصفوف المخفية بواسطة عامل التصفية التلقائي وليس يدويًا بواسطة مستخدم Excel النهائي.

## **احصل على جميع مؤشرات الصفوف المخفية بعد تحديث التصفية التلقائية**

الرجاء مراجعة نموذج التعليمات البرمجية التالي الذي يقوم بتحميل ملف[نموذج لملف Excel](64716913.xlsx)والذي يحتوي على بعض الصفوف المخفية يدويًا بواسطة مستخدم Excel النهائي. يطبق الكود المرشح التلقائي ويقوم بتحديثه باستخدام int [][**AutoFilter.refresh (إخفاء الصفوف المنطقية)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)) طريقة تُرجع فهارس الصفوف لجميع الصفوف المخفية بواسطة المرشح التلقائي. ثم يقوم بطباعة فهارس الصفوف المخفية على وحدة التحكم مع أسماء الخلايا وقيمها.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

## **إخراج وحدة التحكم**

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
