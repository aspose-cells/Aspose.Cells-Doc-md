---
title: Zeilenumbrüche und Textumbruch
description: Wie man Textumbruch und Zeilenumbruch mit der Aspose.Cells für Python via .NET Bibliothek implementiert. Mit der Aspose.Cells für Python via .NET Bibliothek können Sie Text einfach in Zellen einfügen und die Textumbruch Methode festlegen, z.B. manueller Zeilenumbruch, Zeilenumbruch usw. Dieses Dokument beschreibt, wie diese Funktionen umgesetzt werden und bietet Beispielcode zur Referenz.
keywords: Aspose.Cells für Python via .NET, Zeilenumbrüche, Textumbruch, Textlayout
type: docs
weight: 60
url: /de/python-net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Um sicherzustellen, dass der Text in einer Zelle gelesen werden kann, können explizite Zeilenumbrüche und Textumbrüche angewendet werden. Textumbrüche verwandeln eine Zeile in mehrere in einer Zelle, wobei explizite Zeilenumbrüche genau dort eingefügt werden, wo Sie sie haben möchten.

{{% /alert %}}

## **Text in einer Zelle umbrechen**

Um Text in einer Zelle umzubrechen, verwenden Sie die Eigenschaft [**Style.is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

## **Explizite Zeilenumbrüche verwenden**

Sie können in C# „\n“ und in VB.NET „vbLf“ verwenden, um explizite Zeilenumbrüche in einer Zelle einzufügen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-UseExplicitLineBreaks-1.py" >}}

