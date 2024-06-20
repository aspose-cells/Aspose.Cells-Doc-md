---
title: تحويل Excel إلى ODS
type: docs
weight: 40
url: /ar/python-java/convert-excel-to-ods/
---

## **تحويل Excel إلى ODS**
تم إنشاء ملفات ODS بواسطة برنامج Calc الذي يعد جزءًا من مجموعة Apache OpenOffice. تخزن ملفات ODS البيانات المنظمة في صفوف وأعمدة وتتم تنسيقها باستخدام المعيار القائم على XML لمستند OASIS OpenDocument.

يدعم Aspose.Cells للبايثون via Java العمل مع ملفات ODS. يوضح الأمثلة التالية تحويل Excel إلى ملف ODS.
### **التحويل المباشر**
أبسط طريقة لتحويل ملف Excel إلى ODS هي تحميل الدفتر وحفظه عن طريق تمرير [SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) كالمعامل الثاني لطريقة [Workbook.save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)).

يوضح مقتطف الكود التالي تحويل Excel مباشرة إلى ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **حفظ مستند ODS في مواصفات ODF 1.1 أو 1.2**
يدعم Aspose.Cells للبايثون via Java حفظ ملفات ODS في مواصفات ODF 1.1 و ODF 1.2. يوفر الواجهة البرمجية [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) لهذا الغرض. ضبط هذا الخاصية على **true** سيقوم بحفظ الملف بمواصفات ODF 1.1. القيمة الافتراضية لـ [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) هي **false**، لذا يتم حفظ ملف ODS دون إعدادات خاصة مع مواصفات ODF 1.2.

يوضح مقتطف الكود التالي حفظ ملفات ODS بمواصفات ODF 1.1 و 1.2.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
