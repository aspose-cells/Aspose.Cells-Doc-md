---
title: تحويل ملف Excel إلى صيغة PDF متوافقة مع PDFA 1a
type: docs
weight: 80
url: /ar/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **سيناريوهات الاستخدام المحتملة**

PDF/A هو نكهة فريدة من PDF مصممة للحفاظ على الوثائق على المدى الطويل. PDF/A هو إصدار من الشكل المحمول للوثائق (PDF) الذي يستند إلى المعايير الدولية (ISO) وهو شكل أرشيفي لـ PDF يضم جميع الخطوط المستخدمة في الوثيقة داخل ملف PDF. يختلف PDF/A عن PDF عن طريق حظر بعض الميزات مثل الربط بالخط (بدلاً من تضمين الخط) والتشفير. تتيح Aspose.Cells لك حفظ ملفات Excel كملفات PDF متوافقة مع PDF/A (تدعم PDF/A-1a وPDF/A-1b وPDF/A-2a وPDF/A-2b وPDF/A-2u وPDF/A-3a وPDF/A-2ab وPDF/A-3u). يصف هذا الموضوع كيفية حفظ سجل العمل الخاص بـ Excel كملف PDF متوافق مع PDF/A (PDF/A-1a).

## **تحويل ملف Excel إلى تنسيق PDF متوافق مع PDF/A-1a**

يمكن للمطورين استخدام الفئة [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) لضبط خصائص مختلفة للتحويل. ضبط خصائص مختلفة للفئة [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) يمنحك السيطرة على إعدادات الطباعة، الخط، الأمان والضغط لملف PDF الناتج. الخاصية الأهم هي [PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance) التي تمكّنك من حفظ ملفات إكسيل إلى ملفات PDF متوافقة بمعيار PDF/A.

يشرح الكود النموذجي التالي كيفية تحويل ملف Excel إلى تنسيق PDF متوافق مع PDF/A-1a. يرجى الاطلاع على [المخرج PDF](outputCompliancePdfA1a.pdf) بالإضافة إلى لقطة الشاشة للرجوع إليها.

## **لقطة شاشة**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
