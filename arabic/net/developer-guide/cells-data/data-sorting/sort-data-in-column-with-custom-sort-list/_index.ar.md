---
title: فرز البيانات في العمود بقائمة فرز مخصصة
type: docs
weight: 290
url: /ar/net/sort-data-in-column-with-custom-sort-list/
description: تعلم كيفية فرز البيانات في العمود باستخدام قائمة مخصصة باستخدام واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: فرز البيانات في العمود باستخدام قائمة الفرز المخصصة، فرز البيانات حسب القائمة المخصصة.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك فرز البيانات في العمود باستخدام قائمة مخصصة. يمكن القيام بذلك باستخدام الطريقة [**DataSorter.AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2). ومع ذلك، تعمل هذه الطريقة فقط إذا كانت العناصر في القائمة المخصصة لا تحتوي على فواصل بينها. إذا كانت لديهم فواصل مثل "الولايات المتحدة الأمريكية، US"، "الصين، CN"، إلخ، فيجب عليك استخدام الطريقة [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3). هنا، البرميتر الأخير ليس String بل مصفوفة من النصوص.

## **فرز البيانات في العمود بقائمة فرز مخصصة**

الكود المصدري التالي يشرح كيفية استخدام [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) لفرز البيانات باستخدام قائمة مخصصة. يرجى الاطلاع على [ملف Excel عينة](50528327.xlsx) المستخدم في هذا الكود و [ملف الإخراج Excel](50528328.xlsx) الناتج عنه. توضح اللقطة الناتجة التأثير الناتج عن التعديل على ملف Excel عينة عند تنفيذ الكود.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
{{< app/cells/assistant language="csharp" >}}
