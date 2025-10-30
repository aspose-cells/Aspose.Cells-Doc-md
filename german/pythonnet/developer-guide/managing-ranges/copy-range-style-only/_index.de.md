---
title: Nur Bereichsstil kopieren
type: docs
weight: 620
url: /de/python-net/copy-range-style-only/
description: Dieser Artikel beschreibt, wie Sie nur den Bereichsstil mit der Aspose.Cells for Python via .NET Bibliothek kopieren können.
keywords: Python Excel Bibliothek, Python Wie man nur den Bereichsstil kopiert, Python Wie man nur den Bereichsstil mit Python Excel Bibliothek kopiert.
---

{{% alert color="primary" %}}

[Kopieren von Bereichsdaten nur](/cells/de/python-net/copy-range-data-only/) und [Kopieren von Bereichsdaten mit Stil](/cells/de/python-net/copy-range-data-with-style/) erklären, wie Daten aus einem Bereich allein oder einschließlich der Formatierung in einen anderen Bereich kopiert werden können. Es ist auch möglich, nur die Formatierung zu kopieren. Dieser Artikel zeigt, wie das funktioniert.

{{% /alert %}} 

Dieses Beispiel erstellt ein Arbeitsblatt, füllt es mit Daten und kopiert nur den Stil eines Bereichs.

1. Erstellen Sie einen Bereich.
1. Erstellen Sie ein [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-Objekt mit angegebenen Formatierungseigenschaften.
1. Wenden Sie die Formatierung des Stils auf den Bereich an.
1. Erstellen Sie einen zweiten Zellenbereich.
1. Kopieren Sie die Formatierung des ersten Bereichs in den zweiten Bereich.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeStyleOnly-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
