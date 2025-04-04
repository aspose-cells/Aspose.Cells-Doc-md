---
title: AutoFit Rows for Rendering
type: docs
weight: 130
url: /net/autofit-rows-for-rendering/
---

Generally, when you want to display all the text in a cell, you can autofit row in Normal view with 100% zoom in Microsoft Excel. This allows the text to be fully visible in Normal view, and even when you print or save the file as a PDF, the text will be displayed correctly.

However, in some cases, autofitting row works fine in Normal view, but when you switch to print view or save the file as a PDF, the text gets clipped. Please check the source file [Book1.xlsx](Book1.xlsx) and screenshots.

![text is clipped in printview](text_clipped_in_printview.png)

If you want to prevent text being clipped in the saved PDF file, you can autofit row with the [AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/forrendering/) option.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Autofit-AutofitRowsForRendering.cs" >}}

Now, the text is not clipped in the output PDF file.

![text is not clipped in saved pdf](text_not_clipped_in_saved_pdf.png)
{{< app/cells/assistant language="csharp" >}}