---  
title: الحصول على جميع مفرقات الصفوف المخفية بعد تحديث تصفية السيارة. 
type: docs  
weight: 320  
url: /ar/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: تعلم كيفية الحصول على مؤشرات جميع الصفوف المخفية بعد تحديث AutoFilter باستخدام API رقم Aspose.Cells for Node.js via C++.  
keywords: الحصول على جميع مؤشرات الصفوف المخفية بعد تحديث AutoFilter باستخدام Node.js عبر C++، الحصول على جميع مؤشرات الصفوف المخفية بعد تحديث AutoFilter باستخدام Node.js عبر C++، استرجاع جميع مؤشرات الصفوف المخفية بعد تحديث AutoFilter باستخدام Node.js عبر C++  
---  

## **سيناريوهات الاستخدام المحتملة**  

عند تطبيق الفلتر التلقائي على خلايا الورقة، يتم إخفاء بعض الصفوف تلقائيًا. لكن قد يكون بعض الصفوف مخفية يدويًا من قبل مستخدم إكسل ولا يُخفيها الفلتر التلقائي. لذلك، يصعب معرفة الصفوف المخفية بواسطة الفلتر التلقائي والتي هي مخفية يدويًا بواسطة المستخدم. Aspose.Cells for Node.js via C++ يتعامل مع هذه المشكلة باستخدام الـ `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-). ترجع هذه الطريقة مؤشرات الصفوف لجميع الصفوف المخفية بواسطة الفلتر التلقائي وليس يدويًا من قبل المستخدم.  

## **الحصول على جميع فهرسات الصفوف المخفية بعد تحديث تصفية السيارة.**  

يرجى الاطلاع على رمز العينة التالي الذي يحمل [ملف إكسل نموذج](64716909.xlsx) الذي يحتوي على بعض الصفوف التي تم إخفاؤها يدويًا بواسطة مستخدم إكسل. يقوم الرمز بتطبيق الفلتر التلقائي ويحدثه باستخدام طريقة `Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#refresh-boolean-) التي ترجع مؤشرات الصفوف لجميع الصفوف المخفية بواسطة الفلتر التلقائي. ثم يعرض مؤشرات الصفوف المخفية على وحدة التحكم مع أسماء وقيَم الخلايا.  

## **الكود المثالي**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.js" >}}


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
{{< app/cells/assistant language="nodejs-cpp" >}}
