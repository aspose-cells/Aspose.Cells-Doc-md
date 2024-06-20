---
title: Ausgeblendeten Inhalt beim Konvertieren von Excel in HTML ausblenden
type: docs
weight: 40
url: /de/python-java/hide-overlaid-content-while-converting-excel-to/
---

## **Ausgeblendeten Inhalt beim Konvertieren von Excel in HTML ausblenden**
Wenn Sie Ihre Excel-Datei als HTML speichern, können Sie verschiedene Kreuzungstypen für Zellzeichenfolgen angeben. Standardmäßig generiert Aspose.Cells HTML gemäß Microsoft Excel, aber wenn Sie die [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) auf [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) ändern, werden alle Zeichenfolgen am rechten Rand der Zelle ausgeblendet, die mit der Zellzeichenfolge überlagert oder überlappend sind.

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](sampleHidingOverlaidContentWithCrossHideRight.xlsx) und speichert sie als [Ausgabe-HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip) nach dem Setzen des [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) als [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). Der Screenshot erklärt, wie [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) das Ausgabe-HTML vom Standardausgabe beeinflusst.

![todo:image_alt_text](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
