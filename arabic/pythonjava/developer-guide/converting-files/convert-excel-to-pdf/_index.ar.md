---
title: تحويل Excel إلى PDF
type: docs
weight: 50
url: /ar/python-java/convert-excel-to-pdf/
description: كيفية تحويل Excel إلى PDF باستخدام Python. يوضح هذا المقال كيفية تحويل ملفات Excel إلى PDF باستخدام Python واجهة برمجة التطبيقات سهلة الاستخدام Aspose.Cells للبايثون via Java.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---

## **تحويل Excel إلى PDF**

تستخدم المستندات البي دي إف على نطاق واسع كتنسيق قياسي لتبادل المستندات بين المؤسسات والقطاعات الحكومية والأفراد. غالباً ما يُطلب من مطوري البرامج وضع طريقة لتحويل ملفات مايكروسوفت إكسل بسهولة إلى مستندات بي دي إف. توفر واجهة برمجة تطبيقات Aspose.Cells للبايثون via Java القدرة على تحويل ملفات Excel إلى مستندات بي دي إف (بما في ذلك PDF/A). يُحول Aspose.Cells الجداول الإلكترونية إلى PDF بدرجة عالية من الدقة والموافقة.

### **التحويل المباشر**

لحفظ ملف Excel مباشرةً إلى ملف PDF، يمكنك استخدام الـ [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) وتمرير الـ [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) كالمعلمة الثانية.

المقتطف التالي يبرز استخدام [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) والطريقة [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) لتحويل Excel إلى تنسيق PDF.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **التحويل المتقدم**

للحصول على مزيد من التحكم في تحويل إلى PDF، يوفر الواجهة البرمجية التطبيقية فئة  [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) . يمكن استخدام فئة  [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)  لتعيين خصائص مختلفة للتحويل. تعيين خصائص مختلفة لفئة  [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)  سوف يمنحك التحكم في إعدادات  الطباعة، الخط، الأمان، والضغط لملف PDF الناتج. أبرز الخاصية هي  [**Compliance**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)  التي تمكنك من حفظ ملفات Excel إلى ملفات PDF/A متوافقة.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، قم بالاستدعاء الطريقة [**Workbook.calculateFormula**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#calculateFormula()) قبل عرض الجدول إلى PDF. يضمن هذا إعادة حساب القيم المعتمدة على الصيغ وعرض القيم الصحيحة في PDF.

{{% /alert %}}
