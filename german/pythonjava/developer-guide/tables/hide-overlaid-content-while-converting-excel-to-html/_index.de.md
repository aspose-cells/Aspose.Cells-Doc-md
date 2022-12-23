---
title: Blenden Sie überlagerte Inhalte aus, während Sie Excel in HTML konvertieren
type: docs
weight: 40
url: /de/python-java/hide-overlaid-content-while-converting-excel-to/
---
## **Blenden Sie überlagerte Inhalte aus, während Sie Excel in HTML konvertieren**
Wenn Sie Ihre Excel-Datei unter HTML speichern, können Sie verschiedene Kreuztypen für Zellstrings angeben. Standardmäßig generiert Aspose.Cells HTML gemäß Microsoft Excel, aber wenn Sie die ändern[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)zu[KREUZ_AUSBLENDEN_RECHTS](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)dann werden alle Zeichenfolgen auf der rechten Seite der Zelle ausgeblendet, die mit der Zellzeichenfolge überlagert oder überlappt sind.

Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](sampleHidingOverlaidContentWithCrossHideRight.xlsx)und speichert es ab[Ausgang HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip)nach dem Einstellen der[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)als[KREUZ_AUSBLENDEN_RECHTS](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). Der Screenshot erklärt wie[KREUZ_AUSBLENDEN_RECHTS](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)wirkt sich auf die Ausgabe HTML der Standardausgabe aus.

![todo: Bild_alt_Text](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
