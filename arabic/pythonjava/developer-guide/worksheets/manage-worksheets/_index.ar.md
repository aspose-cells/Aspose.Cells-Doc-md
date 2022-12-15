---
title: إدارة أوراق العمل
type: docs
weight: 10
url: /ar/python-java/manage-worksheets/
---
إدارة أوراق العمل باستخدام Aspose.Cells for Python via Java سهلة للغاية. في هذه المقالة ، سنشرح أوراق العمل المضافة والوصول إليها وإزالتها باستخدام Aspose.Cells API.
## **إضافة أوراق عمل إلى ملف Excel جديد**
 لإنشاء مصنف جديد ، قم بإنشاء كائن من[دفتر العمل](https://reference.aspose.com/cells/python/asposecells.api/Workbook) صف دراسي. ال[دفتر العمل](https://reference.aspose.com/cells/python/asposecells.api/Workbook) فئة تمثل ملف Excel. ثم باستخدام ملف[يضيف](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\) ) طريقة ال[ورقة العمل](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) ، يتم إضافة أوراق عمل جديدة إلى ملف Excel. أخيرًا ، لحفظ ملف Excel الذي تم إنشاؤه حديثًا ، اتصل بامتداد[حفظ](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\) ) طريقة ال[دفتر العمل](https://reference.aspose.com/cells/python/asposecells.api/Workbook)صف دراسي.

يوضح مقتطف التعليمات البرمجية التالي إنشاء ملف Excel جديد وإضافة ورقة عمل إليه.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **إضافة أوراق عمل إلى جدول بيانات المصمم**
إن إضافة أوراق العمل إلى جدول بيانات المصمم هي نفسها تمامًا مثل إضافة ورقة العمل إلى ملف Excel جديد. الاختلاف الوحيد هو أنه بدلاً من إنشاء ملف Excel جديد ، نفتح ملفًا موجودًا بواسطة ملف[دفتر العمل](https://reference.aspose.com/cells/python/asposecells.api/Workbook)صف دراسي.

يوضح مقتطف الشفرة التالي إضافة ورقة عمل إلى جدول بيانات المصمم.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **الوصول إلى أوراق العمل باستخدام اسم الورقة**
بعد تحميل مصنف ، يمكن للمطورين الوصول إلى أي ورقة عمل باستخدام فهرسها أو اسمها. يوضح مقتطف الشفرة التالي الوصول إلى ورقة عمل باستخدام اسمها.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **إزالة أوراق العمل**
قد تكون هناك أوقات تلتقي فيها بعض الأوراق لتتم إزالتها من المصنف. لهذا ، يوفر API الامتداد[WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)) طريقة. يمكنك تمرير فهرس الورقة أو اسم الورقة للورقة المراد إزالتها. توضح الأمثلة التالية إزالة أوراق العمل باستخدام فهرس الورقة واسم الورقة.
### **إزالة أوراق العمل باستخدام فهرس الورقة**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **إزالة أوراق العمل باستخدام اسم الورقة**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
