---
title: Zeilenumbrüche und Textumbruch mit Golang über C++
description: So implementieren Sie Textumbruch und Wortumbruch mit der Aspose.Cells Bibliothek in C++. Durch die Verwendung der Aspose.Cells Bibliothek können Sie Text in Zellen einfach einfügen und die Textumbruchmethode festlegen, z.B. manueller Wortumbruch, Wortumbruch usw. Dieses Dokument beschreibt, wie diese Funktionen implementiert werden, und stellt Beispielcode zu Ihrer Verfügung.
keywords: Aspose.Cells, Zeilenumbrüche, Textumbrüche, Textlayout
type: docs
weight: 60
url: /de/go-cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Um sicherzustellen, dass der Text in einer Zelle gelesen werden kann, können explizite Zeilenumbrüche und Textumbrüche angewendet werden. Textumbrüche verwandeln eine Zeile in mehrere in einer Zelle, wobei explizite Zeilenumbrüche genau dort eingefügt werden, wo Sie sie haben möchten.

{{% /alert %}}

## **Text in einer Zelle umbrechen**

Um Text in einer Zelle umzubrechen, verwenden Sie die [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/)-Eigenschaft.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping.go" >}}
## **Explizite Zeilenumbrüche verwenden**

Sie können '\n' in C++ verwenden, um explizite Zeilenumbrüche in einer Zelle einzufügen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping-1.go" >}}
