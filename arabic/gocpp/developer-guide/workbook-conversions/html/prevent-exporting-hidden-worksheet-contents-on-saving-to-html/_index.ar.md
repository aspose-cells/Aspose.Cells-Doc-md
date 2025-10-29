---
title: منعه من تصدير محتوى ورقة العمل المخفي عند الحفظ إلى HTML باستخدام جولانغ عبر C++
linktitle: منع تصدير محتوى ورقة العمل المخفي
type: docs
weight: 210
url: /ar/go-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: تعلم كيف تمنع تصدير محتوى ورقة العمل المخفي عند حفظ ملفات إكسل إلى HTML باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يمكنك حفظ سجلات العمل في Excel إلى HTML. ومع ذلك، إذا كانت سجلات العمل تحتوي على أوراق عمل مخفية، فإن Aspose.Cells بشكل افتراضي يصدر محتويات ورقة العمل المخفية إلى دليل الإخراج الخاص ب HTML (_files) الذي يحتوي على ملفات مثل أوراق العمل، الصور، tabstrip.htm، stylesheet.css إلخ. في بعض الأحيان، سيصدر محتوى أوراق العمل المخفية بهذه الطريقة ليس مناسبًا. على سبيل المثال، إذا كانت ورقة العمل المخفية تحتوي على صور يجب عدم تصديرها إلى دليل _files.

{{% /alert %}}

يوفر Aspose.Cells خاصية [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexporthiddenworksheet/). بشكل افتراضي، يتم تعيينها على **true** ويتم صدور أوراق العمل المخفية إلى HTML. إذا قمت بتعيينها على **false**، فإن Aspose.Cells لن يصدر محتويات ورقة العمل المخفية.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreventExportingHiddenWorksheetContentsOnSavingToHtml.go" >}}
