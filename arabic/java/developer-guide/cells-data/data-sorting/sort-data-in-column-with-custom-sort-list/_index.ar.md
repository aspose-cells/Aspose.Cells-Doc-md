---
title: فرز البيانات في العمود بقائمة فرز مخصصة
type: docs
weight: 210
url: /ar/java/sort-data-in-column-with-custom-sort-list/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك فرز البيانات في العمود باستخدام قائمة مخصصة. يمكن ذلك باستخدام [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-java.lang.String-) . ومع ذلك، تعمل هذه الطريقة فقط إذا لم تحتوي العناصر في القائمة المخصصة على فواصل داخلها. إذا كانت تحتوي على فواصل مثل "USA, US"، "China, CN" إلخ، يجب عليك استخدام [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-java.lang.String-) . هنا، المعامل الأخير ليس String بل مصفوفة من Strings.

## **فرز البيانات في العمود بقائمة فرز مخصصة**

الكود المثالي التالي يوضح كيفية استخدام الطريقة DataSorter.AddKey(int key, SortOrder order, String[] customList) لفرز البيانات بقائمة فرز مخصصة. يرجى الاطلاع على [ملف الإكسل عينة](50528359.xlsx) المستخدم في هذا الكود و[ملف الإكسل الناتج](50528358.xlsx) المولد منه. الشاشة التالية تظهر تأثير الكود على ملف الإكسل عينة عند التنفيذ.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
{{< app/cells/assistant language="java" >}}
