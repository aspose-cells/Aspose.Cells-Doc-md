---
title: Deaktivieren Sie Downlevel Revealed Comments beim Speichern als HTML mit C++
linktitle: Downlevel Revealed Comments deaktivieren
type: docs
weight: 20
url: /de/cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Eliminieren Sie Downlevel Revealed Comments beim Speichern von Excel Dateien als HTML mit Aspose.Cells in C++.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei als HTML speichern, zeigt Aspose.Cells Downlevel Conditional Comments. Diese bedingten Kommentare sind hauptsächlich für ältere Versionen des Internet Explorers relevant und für moderne Webbrowser irrelevant. Sie können sie im Detail unter dem folgenden Link lesen.

- [Bedingter Kommentar - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells ermöglicht es Ihnen, diese Downlevel Revealed Comments zu eliminieren, indem Sie die [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/)-Eigenschaft auf **true** setzen.

## **Beim Speichern als HTML-Wrap Kommentare ausblenden**

Das folgende Beispiel zeigt die Verwendung der [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisabledownlevelrevealedcomments/)-Eigenschaft. Das Bild zeigt die Wirkung dieser Eigenschaft, wenn sie nicht auf true gesetzt ist. Bitte laden Sie die in diesem Code verwendete Beispiel-Excel-Datei ([50528257.xlsx](50528257.xlsx)) und den generierten [Ausgabe-HTML-Code](50528258.zip) herunter.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample workbook
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(sourceDir + u"sampleDisableDownlevelRevealedComments.xlsx");

    // Disable DisableDownlevelRevealedComments
    HtmlSaveOptions opts;
    opts.SetDisableDownlevelRevealedComments(true);

    // Save the workbook in html
    wb.Save(outputDir + u"outputDisableDownlevelRevealedComments_true.html", opts);

    std::cout << "Workbook saved successfully with DisableDownlevelRevealedComments enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
