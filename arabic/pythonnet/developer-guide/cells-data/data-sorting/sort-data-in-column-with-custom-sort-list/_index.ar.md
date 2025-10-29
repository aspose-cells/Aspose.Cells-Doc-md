---
title: فرز البيانات في العمود بقائمة فرز مخصصة
type: docs
weight: 290
url: /ar/python-net/sort-data-in-column-with-custom-sort-list/
description: تعلم كيفية فرز البيانات في العمود باستخدام قائمة مخصصة باستخدام Aspose.Cells for Python via .NET API.
keywords: مكتبة Python Excel، فرز البيانات في العمود باستخدام قائمة الفرز المخصصة في Python، فرز البيانات في Python حسب قائمة مخصصة.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك فرز البيانات في العمود باستخدام قائمة مخصصة. يمكن القيام بذلك باستخدام الطريقة [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list). ومع ذلك، تعمل هذه الطريقة فقط إذا لم تحتوي العناصر في القائمة المخصصة على فاصلات بينها. إذا كانت تحتوي على فواصل مثل "الولايات المتحدة الأمريكية، الولايات المتحدة"، "الصين، CN" وما إلى ذلك، فيجب أن تستخدم الطريقة [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list). هنا، البرميتر الأخير ليس سلسلة ولكن مصفوفة من السلاسل.

## **فرز البيانات في العمود بقائمة فرز مخصصة**

يشرح الكود العيني التالي كيفية استخدام الطريقة [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) لفرز البيانات بقائمة فرز مخصصة. يرجى الاطلاع على [ملف Excel عيني](50528327.xlsx) المستخدم في هذا الكود و[ملف Excel الناتج](50528328.xlsx) الذي تم إنشاؤه عن طريقه. تُظهر اللقطة الشاشة التالية تأثير الكود على ملف Excel العيني عند تنفيذه.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithCustomSortList.py" >}}
{{< app/cells/assistant language="python-net" >}}
