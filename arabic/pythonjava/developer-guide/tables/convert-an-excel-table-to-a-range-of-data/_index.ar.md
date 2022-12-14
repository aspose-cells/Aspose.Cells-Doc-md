---
title: تحويل جدول Excel إلى نطاق من البيانات
type: docs
weight: 10
url: /ar/python-java/convert-an-excel-table-to-a-range-of-data/
---
## **تحويل جدول Excel إلى نطاق من البيانات**
 يوفر Aspose.Cells لـ Python عبر Java خيار تحويل جدول Excel إلى نطاق من البيانات. لهذا ، يوفر API امتداد[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\) ) طريقة. يوضح مقتطف الشفرة التالي استخدام[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)لتحويل جدول Excel إلى نطاق من البيانات.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **تحويل جدول Excel إلى نطاق مع خيارات**
يمكنك توفير خيارات إضافية أثناء تحويل جدول إلى نطاق بامتداد[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) صف دراسي. يمكنك تمرير مثيل من[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)فئة ل[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) لتحديد خيارات إضافية. يوضح مقتطف الشفرة التالي استخدام ملف[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)فئة لتعيين فهرس الصف الأخير من الجدول. سيتم الاحتفاظ بتنسيق الجدول حتى فهرس الصف المحدد وستتم إزالة باقي التنسيق.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
