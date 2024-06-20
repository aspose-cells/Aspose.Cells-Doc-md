---
title: إدارة الأوراق العمل
type: docs
weight: 10
url: /ar/python-java/manage-worksheets/
---

إدارة أوراق العمل باستخدام Aspose.Cells for Python via Java سهلة للغاية. في هذه المقالة، سنُظهر كيفية إضافة أوراق عمل جديدة، والوصول إليها، وإزالتها باستخدام واجهة برمجة تطبيقات Aspose.Cells.
## **إضافة ورقات العمل إلى ملف Excel جديد**
لإنشاء كتاب عمل جديد، أنشئ كائن من الفئة [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook). الفئة [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) تمثل ملف Excel. ثم باستخدام طريقة [add](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\)) من [WorksheetCollection](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)، يتم إضافة ورق العمل الجديدة إلى ملف Excel. وأخيرًا، لحفظ ملف Excel الجديد الذي تم إنشاؤه، قم باستدعاء طريقة [save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\)) من الفئة [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook).

يوضح مقتطف الكود التالي إنشاء ملف Excel جديد وإضافة ورق عمل إليه.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **إضافة ورقات عمل إلى جدول التصميم**
إضافة ورق العمل إلى جدول بيانات المصمم هو بالضبط نفس إضافة ورق العمل إلى ملف Excel جديد. الفرق الوحيد هو أننا بدلاً من إنشاء ملف Excel جديد، نفتح ملفًا موجودًا بواسطة فئة [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook).

يوضح مقتطف الكود التالي إضافة ورق عمل إلى جدول بيانات المصمم.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **الوصول إلى الأوراق العمل باستخدام اسم الورقة**
بعد تحميل كتاب العمل، يمكن للمطورين الوصول إلى أي ورق عمل باستخدام فهرسه أو اسمه. يوضح مقتطف الكود التالي الوصول إلى ورقة عمل باستخدام اسمها.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **إزالة أوراق العمل**
قد تكون هناك أوقات عندما يجب إزالة بعض الأوراق من كتاب العمل. لهذا، يوفر الواجهة البرمجية الخاصة به خاصية [WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)). يمكنك تمرير فهرس الورقة أو اسم الورقة التي يجب إزالتها. توضح الأمثلة التالية إزالة أوراق العمل باستخدام فهرس الورقة واسم الورقة.
### **إزالة أوراق العمل باستخدام فهرس الورقة**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **إزالة الأوراق العمل باستخدام اسم الورقة**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
