---
title: تحويل جدول Excel إلى مجموعة من البيانات
type: docs
weight: 10
url: /ar/python-java/convert-an-excel-table-to-a-range-of-data/
---

## **تحويل جدول Excel إلى مجموعة بيانات**
يوفر Aspose.Cells for Python via Java الخيار لتحويل جدول Excel إلى مجموعة بيانات. لذلك، توفر الواجهة البرمجية أسلوب [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)). يُظهر الشيفرة البرمجية التالية استخدام أسلوب [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) لتحويل جدول Excel إلى مجموعة بيانات.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **تحويل جدول Excel إلى نطاق مع الخيارات**
يمكنك تقديم خيارات إضافية أثناء تحويل الجدول إلى نطاق باستخدام فئة [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions). يمكنك تمرير مثيلًا من فئة [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) إلى طريقة [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) لتحديد الخيارات الإضافية. يوضح مقتطف الكود التالي استخدام فئة [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) لتعيين فهرس الصف الأخير للجدول. سيتم الاحتفاظ بتنسيق الجدول حتى الفهرس المحدد للصف وسيتم إزالة بقية التنسيق.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
