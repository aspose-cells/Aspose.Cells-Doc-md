---
title: فرز البيانات في العمود باستخدام قائمة الفرز المخصصة
type: docs
weight: 290
url: /ar/net/sort-data-in-column-with-custom-sort-list/
---
## **سيناريوهات الاستخدام الممكنة**

 يمكنك فرز البيانات في العمود باستخدام قائمة مخصصة. يمكن القيام بذلك باستخدام[**DataSorter.AddKey (مفتاح int ، ترتيب SortOrder ، قائمة مخصصة للسلسلة)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)طريقة. ومع ذلك ، لا تعمل هذه الطريقة إلا إذا كانت العناصر الموجودة في القائمة المخصصة لا تحتوي على فواصل بداخلها. إذا كانت تحتوي على فواصل مثل "USA، US"، "China، CN" وما إلى ذلك ، فيجب عليك استخدام [** DataSorter.AddKey Method (Int32، SortOrder، String []) **)] (https: // reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) طريقة. هنا ، المعلمة الأخيرة ليست String ولكن مجموعة من السلاسل.

## **فرز البيانات في العمود باستخدام قائمة الفرز المخصصة**

يوضح نموذج الكود التالي كيفية استخدام [** DataSorter.AddKey Method (Int32، SortOrder، String []) **)] (https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey / طرق / 3) طريقة لفرز البيانات باستخدام قائمة الفرز المخصصة. الرجاء مراجعة [نموذج ملف Excel] (50528327.xlsx) المستخدم في هذا الرمز و [ملف Excel الناتج] (50528328.xlsx) الذي تم إنشاؤه بواسطته. تُظهر لقطة الشاشة التالية تأثير الكود على نموذج ملف Excel عند التنفيذ.

![ما يجب القيام به: image_بديل_نص](sort-data-in-column-with-custom-sort-list_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
