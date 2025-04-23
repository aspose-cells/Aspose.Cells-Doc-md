---
title: Nur Bereichsstil kopieren
type: docs
weight: 620
url: /de/net/copy-range-style-only/
---

{{% alert color="primary" %}}

[Nur Bereichsdaten kopieren](/cells/de/net/copy-range-data-only/) und [Bereichsdaten mit Format kopieren](/cells/de/net/copy-range-data-with-style/) erklären, wie Daten von einem Bereich in einen anderen kopiert werden können, allein oder einschließlich Formatierung. Es ist auch möglich, nur die Formatierung zu kopieren. Dieser Artikel zeigt wie.

{{% /alert %}} 

Dieses Beispiel erstellt ein Arbeitsblatt, füllt es mit Daten und kopiert nur den Stil eines Bereichs.

1. Erstellen Sie einen Bereich.
1. Erstellen Sie ein [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-Objekt mit angegebenen Formatierungseigenschaften.
1. Wenden Sie die Formatierung des Stils auf den Bereich an.
1. Erstellen Sie einen zweiten Zellenbereich.
1. Kopieren Sie die Formatierung des ersten Bereichs in den zweiten Bereich.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeStyleOnly-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
