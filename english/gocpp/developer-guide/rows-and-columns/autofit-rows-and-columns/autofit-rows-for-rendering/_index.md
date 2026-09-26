---
title: AutoFit Rows for Rendering with Golang via C++
linktitle: AutoFit Rows for Rendering
type: docs
weight: 130
url: /go-cpp/autofit-rows-for-rendering/
description: Learn how to autofit rows for rendering in Excel files using Aspose.Cells with Golang via C++.
---

Generally, when you want to display all the text in a cell, you can autofit the row in Normal view with 100 % zoom in Microsoft Excel. This allows the text to be fully visible in Normal view, and even when you print or save the file as a PDF, the text will be displayed correctly.

However, in some cases, autofitting the row works fine in Normal view, but when you switch to Print View or save the file as a PDF, the text gets clipped. Please check the source file [Book1.xlsx](Book1.xlsx) and screenshots.

![text is clipped in print view](text_clipped_in_printview.png)

If you want to prevent text **from** being clipped in the saved PDF file, you can autofit the row with the [AutoFitterOptions.GetForRendering()](https://reference.aspose.com/cells/go-cpp/autofitteroptions/getforrendering/) option.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutofitRowsForRendering.go" >}}

Now, the text is not clipped in the output PDF file.

![text is not clipped in saved PDF](text_not_clipped_in_saved_pdf.png)
{{< app/cells/assistant language="go" >}}
