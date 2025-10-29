---
title: فرز البيانات في عمود مع قائمة فرز مخصصة باستخدام جولانج عبر C++
linktitle: فرز البيانات في العمود بقائمة فرز مخصصة
type: docs
weight: 290
url: /ar/go-cpp/sort-data-in-column-with-custom-sort-list/
description: تعلم كيفية فرز البيانات في العمود باستخدام قائمة مخصصة بواسطة استخدام واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: فرز البيانات في العمود باستخدام قائمة الفرز المخصصة، فرز البيانات حسب القائمة المخصصة.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك فرز البيانات في العمود باستخدام قائمة مخصصة. يمكن القيام بذلك باستخدام [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/). ومع ذلك، فإن هذه الطريقة تعمل فقط إذا لم يكن لدى العناصر في القائمة المخصصة فواصل داخلها. إذا كانت تحتوي على فواصل مثل "USA,US"، "China,CN" وغيرها، فلابد من استخدام [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/). هنا، المعامل الأخير ليس سلسلة نصية بل هو مصفوفة من السلاسل النصية.

## **فرز البيانات في العمود بقائمة فرز مخصصة**

يوضح رمز العينة التالي كيفية استخدام طريقة [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) لفرز البيانات باستخدام القائمة الفرزية المخصصة. يرجى الاطلاع على [ملف إكسل العينة](50528327.xlsx) المستخدم في هذا الرمز و[ملف إكسل الناتج](50528328.xlsx) الناتج عنه. يظهر لقطة الشاشة التالية تأثير الكود على ملف إكسل العينة عند التنفيذ.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SortDataInColumnWithCustomSortList.go" >}}
