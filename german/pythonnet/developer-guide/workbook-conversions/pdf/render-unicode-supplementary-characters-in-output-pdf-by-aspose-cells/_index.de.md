---
title: Unicode Supplementary Zeichen im Ausgabe PDF mit Aspose.Cells für Python via .NET rendern
type: docs
weight: 350
url: /de/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Erfahren Sie, wie Sie Unicode Supplementary Zeichen beim Konvertieren von Excel zu PDF mit Aspose.Cells für Python via .NET API rendern.
keywords: Python Render Unicode Supplementary characters beim Speichern in PDF, Unicode Supplementary characters beim Speichern von Excel in PDF mit Python drucken, Python Unicode Supplementary characters anzeigen beim Konvertieren von Excel in PDF, Unicode Supplementary characters für Excel zu PDF ausgeben
---

{{% alert color="primary" %}}

Normale Unicode-Zeichen sind 2 Bytes lang, während Unicode-Supplementary-Zeichen 4 Bytes lang sind. Aspose.Cells für Python via .NET unterstützt jetzt das Rendern dieser 4-Byte-Unicode-Zeichen.

Im Unicode-Standard für Zeichen handelt es sich bei den Supplementary-Zeichen um Zeichen, denen die Codepunkte von U+10000 bis U+10FFFF zugewiesen sind. Mit anderen Worten, dies sind die Unicode-Zeichen größer als U+FFFF.

- In UTF-8 sind diese Zeichen jeweils 4 Bytes lang.
- In UTF-16 benötigen diese Zeichen 2 Ersatzzeichen (16-Bit-Einheiten).

{{% /alert %}}

## Render Unicode-Supplementary-Zeichen im Ausgabe-PDF mit Aspose.Cells für Python via .NET

Der folgende Screenshot zeigt, wie Aspose.Cells für Python via .NET die [Quell-Excel-Datei](5115563.xlsx) in das [Ausgabe-PDF](5115564.pdf) gerendert hat. Wie Sie sehen können, wurden alle drei Unicode-Supplementary-Zeichen genau wie von Microsoft Excel gerendert.

![todo:image_alt_text](output.png)

## Beispielcode

Sie können diesen Beispiellcode verwenden, um die [Quellexceldatei](5115563.xlsx) in die [Ausgabepdf](5115564.pdf) zu konvertieren.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
{{< app/cells/assistant language="python-net" >}}
