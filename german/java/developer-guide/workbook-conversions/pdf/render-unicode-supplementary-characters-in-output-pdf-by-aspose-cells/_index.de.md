---
title: Rendert Unicode-Ergänzungszeichen in der Ausgabe PDF durch Aspose.Cells
type: docs
weight: 690
url: /de/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---
{{% alert color="primary" %}} 

Normale Unicode-Zeichen sind 2 Byte lang, während Unicode-Ergänzungszeichen 4 Byte lang sind. Aspose.Cells unterstützt jetzt die Wiedergabe dieser 4-Byte-Unicode-Zeichen.

Im Unicode-Zeichenstandard sind ergänzende Zeichen die Zeichen, denen Codepunkte von U+10000 bis U+10FFFF zugewiesen wurden. Mit anderen Worten, dies sind die Unicode-Zeichen, die größer als U+FFFF sind.

- In UTF-8 sind diese Zeichen jeweils 4 Byte lang.
- In UTF-16 erfordern diese Zeichen 2 Ersatzzeichen (16-Bit-Einheiten).

{{% /alert %}} 
## **Rendert Unicode-Ergänzungszeichen in der Ausgabe PDF durch Aspose.Cells**
 Der folgende Screenshot zeigt, wie Aspose.Cells die gerendert[Excel-Quelldatei](5473390.xlsx) in die[Ausgang PDF](5473391.pdf). Wie Sie sehen können, wurden alle drei Unicode-Ergänzungszeichen genau so gerendert wie von Microsoft Excel.

![todo: Bild_alt_Text](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

Sie können diesen Beispielcode verwenden, um die zu konvertieren[Excel-Quelldatei](5473390.xlsx) hinein[Ausgang PDF](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
