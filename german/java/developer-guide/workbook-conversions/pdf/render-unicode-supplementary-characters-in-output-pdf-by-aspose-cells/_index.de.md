---
title: Unicode Supplementary Zeichen im Ausgabe PDF durch Aspose.Cells rendern
type: docs
weight: 690
url: /de/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}} 

Normale Unicode-Zeichen sind 2 Byte lang, während Unicode-Supplementary-Zeichen 4 Byte lang sind. Aspose.Cells unterstützt jetzt das Rendern dieser 4-Byte-Unicode-Zeichen.

Im Unicode-Standard für Zeichen handelt es sich bei den Supplementary-Zeichen um Zeichen, denen die Codepunkte von U+10000 bis U+10FFFF zugewiesen sind. Mit anderen Worten, dies sind die Unicode-Zeichen größer als U+FFFF.

- In UTF-8 sind diese Zeichen jeweils 4 Bytes lang.
- In UTF-16 benötigen diese Zeichen 2 Ersatzzeichen (16-Bit-Einheiten).

{{% /alert %}} 
## **Rendern von Unicode-Zusatzzeichen im Ausgabe-PDF durch Aspose.Cells**
Der folgende Screenshot zeigt, wie Aspose.Cells die [Excel-Quelldatei](5473390.xlsx) in das [PDF-Ausgabe](5473391.pdf) gerendert hat. Wie Sie sehen können, wurden alle drei Unicode-Zusatzzeichen genauso gerendert wie von Microsoft Excel durchgeführt.

![todo:image_alt_text](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

Sie können diesen Beispielcode verwenden, um die [Excel-Quelldatei](5473390.xlsx) in [PDF-Ausgabe](5473391.pdf) zu konvertieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
