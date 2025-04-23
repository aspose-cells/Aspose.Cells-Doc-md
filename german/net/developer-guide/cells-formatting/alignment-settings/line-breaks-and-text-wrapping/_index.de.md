---
title: Zeilenumbrüche und Textumbruch
description: So implementieren Sie Textumbruch und Wortumbruch mithilfe der Aspose.Cells Bibliothek in C#. Mit der Aspose.Cells Bibliothek können Sie problemlos Text in Zellen einfügen und die Textumbruchmethode festlegen, z. B. manueller Wortumbruch, Wortumbruch usw. Dieses Dokument erläutert, wie man diese Funktionen implementiert, und bietet Beispielscode zur Referenz.
keywords: Aspose.Cells, Zeilenumbrüche, Textumbrüche, Textlayout
type: docs
weight: 60
url: /de/net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Um sicherzustellen, dass der Text in einer Zelle gelesen werden kann, können explizite Zeilenumbrüche und Textumbrüche angewendet werden. Textumbrüche verwandeln eine Zeile in mehrere in einer Zelle, wobei explizite Zeilenumbrüche genau dort eingefügt werden, wo Sie sie haben möchten.

{{% /alert %}}

## **Text in einer Zelle umbrechen**

Um Text in einer Zelle umzubrechen, verwenden Sie die Eigenschaft [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **Explizite Zeilenumbrüche verwenden**

Sie können in C# „\n“ und in VB.NET „vbLf“ verwenden, um explizite Zeilenumbrüche in einer Zelle einzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
