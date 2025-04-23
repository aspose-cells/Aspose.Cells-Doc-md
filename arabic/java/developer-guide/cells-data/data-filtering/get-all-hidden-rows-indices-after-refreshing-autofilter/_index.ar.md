---
title: الحصول على جميع مفرقات الصفوف المخفية بعد تحديث تصفية السيارة.
type: docs
weight: 240
url: /ar/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---

## **سيناريوهات الاستخدام المحتملة**

عند تطبيق تصفية تلقائية على خلايا ورقة العمل، فإن بعض الصفوف تُخفى تلقائيًا. لكن قد يكون الأمر كذلك أن بعض الصفوف يتم إخفاؤها يدويًا مسبقًا من قبل مستخدم نهاية Excel وأنها لم تُخفَ تلقائيًا بواسطة تصفية تلقائية. ولهذا السبب، تتعامل Aspose.Cells مع هذه المشكلة باستخدام طريقة الـ int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh-boolean-). تعيد هذه الطريقة مؤشرات الصفوف لجميع الصفوف التي تم إخفاؤها بواسطة تصفية تلقائية وليست يدويًا بواسطة مستخدم نهاية Excel.

## **الحصول على جميع فهرسات الصفوف المخفية بعد تحديث تصفية السيارة.**

يرجى الرجوع إلى الرمز النموذجي التالي الذي يحمل الملف النموذجي للبيانات [ملف Excel النموذجي](64716913.xlsx) الذي يحتوي على بعض الصفوف المخفية يدويًا من قبل مستخدم نهاية Excel. يُطبق الرمز تصفيةً تلقائية ويقوم بتحديثها باستخدام طريقة int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh-boolean-) التي تُعيد مؤشرات الصفوف المخفية لكافة الصفوف بواسطة تصفية تلقائية. يُطبع بعد توافر ذلك مؤشرات الصفوف المخفية على وحدة التحكم مع أسماء الخلايا والقيم.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

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
{{< app/cells/assistant language="java" >}}
