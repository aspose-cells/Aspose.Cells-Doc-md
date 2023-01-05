---
title: فرز البيانات في العمود باستخدام قائمة الفرز المخصصة
type: docs
weight: 210
url: /ar/java/sort-data-in-column-with-custom-sort-list/
---
## **سيناريوهات الاستخدام الممكنة**

يمكنك فرز البيانات في العمود باستخدام قائمة مخصصة. يمكن القيام بذلك باستخدام[DataSorter.AddKey (مفتاح int ، ترتيب SortOrder ، قائمة مخصصة للسلسلة)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) طريقة. ومع ذلك ، لا تعمل هذه الطريقة إلا إذا كانت العناصر الموجودة في القائمة المخصصة لا تحتوي على فواصل بداخلها. إذا كانت تحتوي على فواصل مثل "USA، US"، "China، CN" وما إلى ذلك ، فيجب عليك استخدام[DataSorter.AddKey (مفتاح int ، ترتيب SortOrder ، قائمة مخصصة للسلسلة)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) طريقة. هنا ، المعلمة الأخيرة ليست String ولكن مجموعة من السلاسل.

## **فرز البيانات في العمود باستخدام قائمة الفرز المخصصة**

يوضح نموذج التعليمات البرمجية التالي كيفية استخدام DataSorter.AddKey (مفتاح int ، ترتيب SortOrder ، أسلوب String [] customList) لفرز البيانات باستخدام قائمة الفرز المخصصة. الرجاء مراجعة[نموذج لملف Excel](50528359.xlsx)المستخدمة في هذا الرمز و[إخراج ملف Excel](50528358.xlsx)ولدت به. تُظهر لقطة الشاشة التالية تأثير الكود على نموذج ملف Excel عند التنفيذ.

![ما يجب القيام به: image_بديل_نص](sort-data-in-column-with-custom-sort-list_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
