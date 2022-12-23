---
title: التحويل بين تنسيقات Excel
type: docs
weight: 20
url: /ar/net/convert-between-excel-formats/
---
## **تحويل ملف Excel إلى PDF**

**PDF** تستخدم الملفات على نطاق واسع لتبادل الوثائق بين المنظمات والقطاعات الحكومية والأفراد. إنه تنسيق مستند قياسي وغالبًا ما يُطلب من مطوري البرامج إيجاد طريقة لتحويل ملفات Excel Microsoft إلى**PDF** مستندات.
**Aspose.Cells** يدعم تحويل ملفات Excel إلى PDF ويحافظ على دقة بصرية عالية في التحويل.

Aspose.Cells for .NET يدعم التحويل من جداول البيانات إلى PDF بشكل مستقل عن البرامج الأخرى. احفظ ملف Excel في PDF باستخدام طريقة Save لفئة المصنف. توفر طريقة الحفظ عضو التعداد SaveFormat.Pdf الذي يحول ملفات Excel الأصلية إلى تنسيق PDF.

**التحويل** مباشرة من جدول البيانات إلى PDF ، بدلاً من استخدام أداة خارجية أو API خارجي ، لديه العديد من**مزايا**:

1. لا يتطلب التحويل المباشر ملفات مؤقتة لأن العملية برمتها يمكن إجراؤها في الذاكرة.
1. ليست هناك حاجة إلى ملف XML بحيث يمكن بسهولة تحويل الملفات الكبيرة.
1. سرعة التحويل أسرع بكثير.

**لتحويل الملفات إلى PDF:**

1.  إنشاء كائن من**دفتر العمل** فئة عن طريق استدعاء مُنشئها الفارغ.
1.  يمكنك**فتح / تحميل** ملف قالب موجود أو تخطي هذه الخطوة إذا كنت تقوم بإنشاء المصنف من البداية.
1. قم بالعمل المطلوب (إدخال البيانات ، وتطبيق التنسيق ، وتعيين الصيغ ، وإدراج الصور أو الكائنات الرسومية الأخرى ، وما إلى ذلك) على جدول البيانات باستخدام واجهات برمجة التطبيقات Aspose.Cells '.
1.  عند اكتمال كود جدول البيانات ، اتصل بـ**طريقة حفظ فئة المصنف** لحفظ جدول البيانات. يجب أن يكون تنسيق الملف PDF ، لذا حدد Pdf (قيمة محددة مسبقًا) من تعداد SaveFormat لإنشاء مستند PDF النهائي.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **تحويل ملف Excel إلى MHTML**

**MHTML** يجمع بين HTML العادي والموارد الخارجية (أي المحتوى المرتبط عادةً ، مثل الصور والرسوم المتحركة والصوت وما إلى ذلك) في ملف واحد. يتم استخدامها لرسائل البريد الإلكتروني بامتداد الملف .mht.
يدعم Aspose.Cells قراءة وكتابة ملفات MHTML.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **تحويل ملف Excel إلى XPS**

في بعض الأحيان ، تريد تحويل مصنف أو حفظه باستخدام أوراق عمل متعددة إلى تنسيق نصي. بالنسبة لتنسيقات النص (على سبيل المثال TXT ، TabDelim ، CSV إلخ.) ، افتراضيًا ، يتم حفظ محتويات ورقة العمل النشطة فقط Microsoft Excel و Aspose.Cells.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **تنزيل نموذج التعليمات البرمجية**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
