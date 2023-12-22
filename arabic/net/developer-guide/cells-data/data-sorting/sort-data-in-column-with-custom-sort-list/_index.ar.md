---
title: فرز البيانات في العمود باستخدام قائمة الفرز المخصصة
type: docs
weight: 290
url: /ar/net/sort-data-in-column-with-custom-sort-list/
description: تعرف على كيفية فرز البيانات في العمود باستخدام قائمة مخصصة باستخدام Aspose.Cells for .NET API.
keywords: Sort Data in Column with Custom Sort List, Sort data by custom list.
---
##  **سيناريوهات الاستخدام المحتملة**

 يمكنك فرز البيانات في العمود باستخدام قائمة مخصصة. يمكن القيام بذلك باستخدام[**DataSorter.AddKey (مفتاح int، ترتيب SortOrder، قائمة سلسلة مخصصة)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)طريقة. ومع ذلك، تعمل هذه الطريقة فقط إذا كانت العناصر الموجودة في القائمة المخصصة لا تحتوي على فواصل بداخلها. إذا كانت تحتوي على فواصل مثل "USA,US" و"China,CN" وما إلى ذلك، فيجب عليك استخدام [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. طريقة aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3). هنا، المعلمة الأخيرة ليست سلسلة ولكن مجموعة من السلاسل.

##  **فرز البيانات في العمود باستخدام قائمة الفرز المخصصة**

يشرح نموذج التعليمات البرمجية التالي كيفية استخدام [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey /methods/3) طريقة لفرز البيانات باستخدام قائمة الفرز المخصصة. الرجاء مراجعة[عينة من ملف إكسل](50528327.xlsx) المستخدمة في هذا الرمز و[إخراج ملف إكسل](50528328.xlsx) المتولدة عنها. توضح لقطة الشاشة التالية تأثير التعليمات البرمجية على نموذج ملف Excel عند التنفيذ.

![ما يجب القيام به:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
