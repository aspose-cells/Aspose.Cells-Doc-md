---
title: تحويل ملف إكسل إلى تنسيق PDF متوافق مع PDFA 1a باستخدام Golang عبر C++
linktitle: تحويل ملف Excel إلى صيغة PDF متوافقة مع PDFA 1a
type: docs
weight: 130
url: /ar/go-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: تعلم كيفية تحويل ملفات إكسل إلى تنسيق PDF / A 1a متوافق باستخدام Aspose.Cells مع Golang عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

 PDF/A هو نوع فريد من PDF مصمم للحفاظ طويل الأمد على المستندات. PDF / A هو إصدار قياسي من تنسيق المستندات المحمولة (PDF) وهو تنسيق أرشيفي لـ PDF يدمج جميع الخطوط المستخدمة في المستند داخل ملف PDF. يختلف PDF / A عن PDF من خلال حظر الميزات، مثل ربط الخطوط (مقابل تضمين الخطوط) والتشفير. يمكّنك Aspose.Cells من حفظ ملفات Excel بصيغة PDF / A متوافقة (PDF / A-1a، PDF / A-1b، PDF / A-2a، PDF / A-2b، PDF / A-2u، PDF / A-3a، PDF / A-2ab، وPDF / A-3u مدعومة). يصف هذا الموضوع كيف تحفظ دفتر عمل Excel إلى ملف PDF متوافق مع PDF / A (PDF / A-1a).

## **تحويل ملف Excel إلى تنسيق PDF متوافق مع PDF/A-1a**

يمكن للمطورين استخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) لضبط سمات مختلفة للتحويل. ضبط خصائص مختلفة من فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) يمنحك السيطرة على إعدادات الطباعة، الخط، الأمان، والضغط لملف PDF الناتج. الخاصية الأهم هي [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/) التي تمكنك من حفظ ملفات Excel إلى ملفات PDF / A متوافقة.

يشرح الكود النموذجي التالي كيفية تحويل ملف Excel إلى تنسيق PDF متوافق مع PDF/A-1a. يرجى الاطلاع على [المخرج PDF](outputCompliancePdfA1a.pdf) بالإضافة إلى لقطة الشاشة للرجوع إليها.

## **لقطة شاشة**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelFileToPdfFormatCompatibleWithPdfa1a.go" >}}
