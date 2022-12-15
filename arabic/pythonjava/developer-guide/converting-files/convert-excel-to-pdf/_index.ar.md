---
title: تحويل Excel إلى PDF
type: docs
weight: 50
url: /ar/python-java/convert-excel-to-pdf/
description: كيفية تحويل ملفات Excel إلى PDF باستخدام Python. توضح هذه المقالة تحويل ملفات Excel إلى PDF باستخدام Python وسهلة الاستخدام Aspose.Cells via Java API.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---
## **تحويل Excel إلى PDF**

تُستخدم مستندات PDF على نطاق واسع كتنسيق قياسي لتبادل المستندات بين المنظمات والقطاعات الحكومية والأفراد. غالبًا ما يُطلب من مطوري البرامج ابتكار طريقة لتحويل ملفات Excel Microsoft بسهولة إلى مستندات PDF. يوفر Aspose.Cells for Python via Java API القدرة على تحويل ملفات Excel إلى مستندات PDF (بما في ذلك PDF / A). يقوم Aspose.Cell بتحويل جداول البيانات إلى PDF بدرجة عالية من الدقة والإخلاص.

### **التحويل المباشر**

لحفظ ملف Excel مباشرة في PDF ، يمكنك استخدام امتداد[**مصنف**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) طريقة وتمرير[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) كمعامل ثاني.

يوضح مقتطف الشفرة التالي استخدام[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)و ال[**مصنف**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) طريقة لتحويل Excel إلى تنسيق PDF.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **التحويل المتقدم**

للحصول على مزيد من التحكم في التحويل إلى PDF ، يوفر API امتداد الملف[**خيارات PdfSave**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)صف دراسي. ال[**خيارات PdfSave**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)يمكن استخدام فئة لتعيين سمات مختلفة للتحويل. تعيين خصائص مختلفة لملف[**خيارات PdfSave**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)ستمنحك class التحكم في إعدادات الطباعة والخط والأمان والضغط لملف PDF الناتج. الخاصية الأكثر شهرة هي[**امتثال**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)يمكّنك من حفظ ملفات Excel في ملفات PDF متوافقة مع PDF / A.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

 إذا كان جدول البيانات يحتوي على صيغ ، فاتصل بـ[**مصنف .calculateFormula**](https://reference.aspose.com/cells/python/asposecells.api/workbook#calculateFormula()) فقط قبل تحويل جدول البيانات إلى PDF. يضمن ذلك إعادة حساب القيم التابعة للصيغة وتقديم القيم الصحيحة في ملف PDF.

{{% /alert %}}
