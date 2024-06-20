---
title: التحويل بين تنسيقات Excel
type: docs
weight: 20
url: /ar/net/convert-between-excel-formats/
---

## **تحويل Excel إلى PDF**

يتم استخدام ملفات **PDF** على نطاق واسع لتبادل الوثائق بين المؤسسات والقطاعات الحكومية والأفراد. إنها صيغة وثيقة قياسية وغالبًا ما يُطلب من مطوري البرمجيات إيجاد طريقة لتحويل ملفات Microsoft Excel إلى مستندات **PDF**.
تدعم **Aspose.Cells** تحويل ملفات Excel إلى PDF وتحافظ على دقة بصرية عالية أثناء التحويل.

Aspose.Cells for .NET تدعم التحويل من جداول البيانات إلى PDF بشكل مستقل عن البرمجيات الأخرى. يوفر طريقة الحفظ في فئة Workbook العضو الفرعي Save التحويل الأصلي لملفات Excel إلى تنسيق PDF.

التحويل مباشرة من جدول بيانات إلى PDF، بدلاً من استخدام أداة طرف ثالث أو واجهة برمجة تطبيقات خارجية، يحمل العديد من **المزايا**.

1. لا يتطلب التحويل المباشر ملفات مؤقتة لأنه يمكن إجراء العملية بأكملها في الذاكرة.
1. لا يلزم ملف XML بحيث يمكن تحويل الملفات الكبيرة بسهولة.
1. السرعة في التحويل أسرع بكثير.

**لتحويل الملفات إلى صيغة PDF:**

1. قم بإنشاء كائن من فئة **Workbook** عن طريق استدعاء بناءه الفارغ.
1. يمكنك **فتح/تحميل** ملف نموذج موجود أو تخطي هذه الخطوة إذا كنت تقوم بإنشاء الجدول من البداية.
1. قم بعملك المرغوب (إدخال البيانات، تطبيق التنسيق، تعيين الصيغ، إدراج الصور أو أجسام الرسم الأخرى، وما إلى ذلك) على جدول البيانات باستخدام واجهات برمجة التطبيقات API في Aspose.Cells.
1. عند اكتمال كود جدول البيانات، قم باستدعاء **طريقة الحفظ لفئة Workbook** لحفظ جدول البيانات. يجب أن يكون تنسيق الملف هو PDF لذا حدد Pdf (قيمة محددة مسبقًا) من تعداد SaveFormat لإنشاء المستند النهائي بتنسيق PDF.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **تحويل Excel إلى MHTML**

**MHTML** يجمع بين HTML العادي مع الموارد الخارجية (أي المحتوى المرتبط عادةً، مثل الصور والرسوم المتحركة والصوت وما إلى ذلك) في ملف واحد. يتم استخدامها في رسائل البريد الإلكتروني بامتداد ملف .mht.
Aspose.Cells تدعم قراءة وكتابة ملفات MHTML.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **تحويل Excel إلى XPS**

في بعض الأحيان، ترغب في تحويل أو حفظ دفتر عمل يحتوي على عدة أوراق عمل إلى شكل نصي. في حالات الشكل النصي (على سبيل المثال TXT, TabDelim, CSV الخ)، فإن كل من مايكروسوفت إكسل وAspose.Cells تحفظان افتراضيًا محتويات الورقة العمل النشطة فقط.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **تحميل رمز عينة**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
