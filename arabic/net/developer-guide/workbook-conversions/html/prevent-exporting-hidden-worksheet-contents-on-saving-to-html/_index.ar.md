---
title: منع تصدير محتويات ورقة العمل المخفية عند الحفظ إلى HTML
type: docs
weight: 210
url: /ar/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

يمكنك حفظ مصنفات Excel في HTML. ومع ذلك ، إذا كان المصنف يحتوي على أوراق عمل مخفية ، فإن Aspose.Cells يقوم افتراضيًا بتصدير محتويات ورقة العمل المخفية إلى إخراج HTML (_ files) الذي يحتوي على ملفات مثل أوراق العمل والصور و tabstrip.htm و stylesheet.css وما إلى ذلك. في بعض الأحيان ، لا يكون تصدير محتوى أوراق العمل المخفية بهذه الطريقة مناسبًا. على سبيل المثال ، إذا كانت ورقة العمل المخفية تحتوي على صور لا ينبغي تصديرها إلى ملف_دليل الملفات.

{{% /alert %}}

 يوفر Aspose.Cells ملف[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet) خاصية. بشكل افتراضي ، يتم تعيينه على**حقيقي** ويتم تصدير أوراق العمل المخفية إلى HTML. إذا قمت بتعيينها**خاطئة**، لن يقوم Aspose.Cells بتصدير محتويات ورقة العمل المخفية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

