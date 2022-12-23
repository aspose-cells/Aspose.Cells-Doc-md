---
title: تحويل Excel إلى ODS
type: docs
weight: 40
url: /ar/python-java/convert-excel-to-ods/
---
## **تحويل Excel إلى ODS**
يتم إنشاء ملفات ODS بواسطة برنامج Calc وهو جزء من Apache OpenOffice Suite. تقوم ملفات ODS بتخزين البيانات المنظمة في صفوف وأعمدة ومنسقة باستخدام معيار OASIS OpenDocument المستند إلى XML.

Aspose.Cells for Python via Java يدعم عمل ملفات ODS. توضح الأمثلة التالية تحويل Excel إلى ملف ODS.
### **التحويل المباشر**
إن أبسط طريقة لتحويل ملف Excel إلى ODS هي تحميل المصنف وحفظه بالتمرير[حفظ تنسيق ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) كمعامل ثاني لملف[مصنف](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)) طريقة.

يوضح مقتطف الكود التالي تحويل Excel مباشرة إلى ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **احفظ المستند ODS في مواصفات ODF 1.1 أو 1.2**
Aspose.Cells for Python via Java يدعم حفظ ملفات ODS في مواصفات ODF 1.1 و ODF 1.2. لهذا ، يوفر API[OdsSaveOptions.setStrictSchema11 ()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) خاصية. تعيين هذه الخاصية إلى**حقيقي** سيحفظ الملف بمواصفات ODF 1.1. القيمة الافتراضية لـ[OdsSaveOptions.setStrictSchema11 ()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) يكون**خاطئة**، لذلك يتم حفظ الملف ODS المحفوظ بدون إعدادات خاصة بمواصفات ODF 1.2.

يوضح مقتطف الكود التالي حفظ ملفات ODS بمواصفات ODF 1.1 و 1.2.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
