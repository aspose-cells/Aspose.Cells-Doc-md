---
title: منع تصدير محتويات ورقة عمل مخفية عند الحفظ إلى HTML
type: docs
weight: 210
url: /ar/python-net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

يمكنك حفظ سجلات العمل في Excel إلى HTML. ومع ذلك، إذا كانت سجلات العمل تحتوي على أوراق عمل مخفية، فإن Aspose.Cells بشكل افتراضي يصدر محتويات ورقة العمل المخفية إلى دليل الإخراج الخاص ب HTML (_files) الذي يحتوي على ملفات مثل أوراق العمل، الصور، tabstrip.htm، stylesheet.css إلخ. في بعض الأحيان، سيصدر محتوى أوراق العمل المخفية بهذه الطريقة ليس مناسبًا. على سبيل المثال، إذا كانت ورقة العمل المخفية تحتوي على صور يجب عدم تصديرها إلى دليل _files.

{{% /alert %}}

يوفر Aspose.Cells خاصية [**HtmlSaveOptions.export_hidden_worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_hidden_worksheet). بشكل افتراضي، يتم تعيينها على **true** ويتم صدور أوراق العمل المخفية إلى HTML. إذا قمت بتعيينها على **false**، فإن Aspose.Cells لن يصدر محتويات ورقة العمل المخفية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-PreventExportingHiddenContentWhileSavingAsHTML.py" >}}

{{< app/cells/assistant language="python-net" >}}
