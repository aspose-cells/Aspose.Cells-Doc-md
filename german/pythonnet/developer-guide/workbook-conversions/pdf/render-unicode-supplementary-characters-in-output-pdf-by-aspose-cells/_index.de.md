---
title: Rendern Sie Unicode-Ergänzungszeichen in der Ausgabe PDF durch Aspose.Cells for Python via .NET
type: docs
weight: 350
url: /de/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Erfahren Sie, wie Sie Unicode-Ergänzungszeichen beim Konvertieren von Excel in PDF mit Aspose.Cells for Python via .NET API rendern.
keywords: Python Render Unicode Supplementary characters while saving file to PDF, Print Unicode Supplementary characters while saving Excel to PDF using Python, Python Show Unicode Supplementary characters when converting Excel to PDF, Output Unicode Supplementary characters for excel to pdf
---
{{% alert color="primary" %}}

Normale Unicode-Zeichen sind 2 Byte lang, während Unicode-Ergänzungszeichen 4 Byte lang sind. Aspose.Cells for Python via .NET unterstützt jetzt die Darstellung dieser 4-Byte-Unicode-Zeichen.

Im Unicode-Zeichenstandard sind Zusatzzeichen die Zeichen, denen Codepunkte von U+10000 bis U+10FFFF zugewiesen sind. Mit anderen Worten: Dies sind die Unicode-Zeichen, die größer als U+FFFF sind.

- In UTF-8 sind diese Zeichen jeweils 4 Byte lang.
- In UTF-16 erfordern diese Zeichen zwei Ersatzzeichen (16-Bit-Einheiten).

{{% /alert %}}

##  Rendern Sie Unicode-Ergänzungszeichen in der Ausgabe PDF durch Aspose.Cells for Python via .NET

 Der folgende Screenshot zeigt, wie Aspose.Cells for Python via .NET das gerendert hat[Quell-Excel-Datei](5115563.xlsx) in die[Ausgabe PDF](5115564.pdf). Wie Sie sehen können, wurden alle drei Unicode-Ergänzungszeichen genauso gerendert wie von Microsoft Excel.

![todo:image_alt_text](output.png)

##  Beispielcode

Sie können diesen Beispielcode zum Konvertieren verwenden[Quell-Excel-Datei](5115563.xlsx) hinein[Ausgabe PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
