---
title: فرز البيانات في العمود بقائمة فرز مخصصة
type: docs
weight: 210
url: /ar/java/sort-data-in-column-with-custom-sort-list/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك فرز البيانات في العمود باستخدام قائمة مخصصة. يمكن القيام بذلك باستخدام [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String) الطريقة. ومع ذلك، تعمل هذه الطريقة فقط إذا كانت العناصر في القائمة المخصصة لا تحتوي على فواصل بينها. إذا كانت تحتوي على فواصل مثل "USA, US", "China, CN" وما إلى ذلك، فيجب عليك استخدام [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String) الطريقة. هنا، الباراميتر الأخير ليس نصا ولكن مصفوفة من السلاسل.

## **فرز البيانات في العمود بقائمة فرز مخصصة**

الكود المثالي التالي يوضح كيفية استخدام الطريقة DataSorter.AddKey(int key, SortOrder order, String[] customList) لفرز البيانات بقائمة فرز مخصصة. يرجى الاطلاع على [ملف الإكسل عينة](50528359.xlsx) المستخدم في هذا الكود و[ملف الإكسل الناتج](50528358.xlsx) المولد منه. الشاشة التالية تظهر تأثير الكود على ملف الإكسل عينة عند التنفيذ.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
