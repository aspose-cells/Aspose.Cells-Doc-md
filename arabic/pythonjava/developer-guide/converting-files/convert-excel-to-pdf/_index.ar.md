---
title: تحويل Excel إلى PDF
type: docs
weight: 50
url: /ar/python-java/convert-excel-to-pdf/
description: كيفية تحويل Excel إلى PDF باستخدام Python. توضح هذه المقالة تحويل ملفات Excel إلى PDF باستخدام Python وسهل الاستخدام Aspose.Cells for Python via Java API.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---
## **تحويل Excel إلى PDF**

يتم استخدام وثائق PDF على نطاق واسع كتنسيق قياسي لتبادل الوثائق بين المنظمات والقطاعات الحكومية والأفراد. غالبًا ما يُطلب من مطوري البرامج ابتكار طريقة لتحويل ملفات Excel Microsoft بسهولة إلى مستندات PDF. Aspose.Cells for Python via Java API يوفر القدرة على تحويل ملفات Excel إلى وثائق PDF (بما في ذلك PDF / A). يقوم Aspose.Cell بتحويل جداول البيانات إلى PDF بدرجة عالية من الدقة والإخلاص.

### **التحويل المباشر**

لحفظ ملف Excel مباشرة في PDF ، يمكنك استخدام امتداد[**مصنف**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) طريقة وتمرير[**حفظ تنسيق PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) كمعامل ثاني.

يوضح مقتطف الشفرة التالي استخدام[**حفظ تنسيق PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)و ال[**مصنف**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) طريقة لتحويل Excel إلى تنسيق PDF.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **التحويل المتقدم**

للحصول على مزيد من التحكم في التحويل إلى PDF ، يوفر API تنسيق[**خيارات PdfSave**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)صف دراسي. ال[**خيارات PdfSave**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)يمكن استخدام فئة لتعيين سمات مختلفة للتحويل. تعيين خصائص مختلفة لملف[**خيارات PdfSave**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)ستمنحك class التحكم في إعدادات الطباعة والخط والأمان والضغط لملف PDF الناتج. الخاصية الأكثر شهرة هي[**الالتزام**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)التي تمكنك من حفظ ملفات Excel في PDF / A متوافق مع ملفات PDF.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

 إذا كان جدول البيانات يحتوي على صيغ ، فاتصل بـ[**مصنف .calculateFormula**](https://reference.aspose.com/cells/python/asposecells.api/workbook#calculateFormula()) قبل تحويل جدول البيانات إلى PDF. هذا يضمن إعادة حساب القيم التابعة للصيغة وتقديم القيم الصحيحة في PDF.

{{% /alert %}}
