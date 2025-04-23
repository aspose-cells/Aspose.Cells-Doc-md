---
title: فرز البيانات في العمود بقائمة فرز مخصصة
type: docs
weight: 290
url: /ar/nodejs-cpp/sort-data-in-column-with-custom-sort-list/
description: تعلم كيفية فرز البيانات في العمود باستخدام قائمة مخصصة بواسطة API رقم Aspose.Cells for Node.js via C++.
keywords: فرز البيانات في العمود باستخدام قائمة الفرز المخصصة، فرز البيانات حسب القائمة المخصصة.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك فرز البيانات في العمود باستخدام قائمة مخصصة. يتم ذلك باستخدام [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-string-) طريقة. ومع ذلك، تعمل هذه الطريقة فقط إذا لم تكن العناصر في القائمة المخصصة تحتوي على فواصل داخلها. إذا كانت تحتوي على فواصل مثل "الولايات المتحدة الأمريكية،US"، "الصين،CN"، إلخ، فالإجراء الصحيح هو استخدام [**DataSorter.addKey(number, SortOrder, string[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-) طريقة. هنا، المعامل الأخير ليس String وإنما مصفوفة من السلاسل.

## **فرز البيانات في العمود بقائمة فرز مخصصة**

الكود التالي يوضح كيفية استخدام [**DataSorter.addKey(number, SortOrder, string[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-) لطريقة فرز البيانات باستخدام قائمة فرز مخصصة. يرجى الاطلاع على ملف Excel النموذجي [المستخدم في هذا الكود](50528327.xlsx) وملف Excel الناتج [الذي تم إنشاؤه به](50528328.xlsx). تعرض لقطة الشاشة التالية تأثير الكود على ملف Excel النموذجي عند التنفيذ.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithCustomSortList.js" >}}

