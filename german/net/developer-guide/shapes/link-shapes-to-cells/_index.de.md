---
title: Wie man Excel Formen mit Arbeitsblattzellen verknüpft
linktitle: Excel Formen mit Zellen verknüpfen
type: docs
description: "Wie man Excel Formen mit Arbeitsblattzellen verknüpft"
weight: 3300
url: /de/net/link-shapes-to-cells/
---

{{% alert color="primary" %}}

Manchmal müssen Sie den Inhalt einer Arbeitsblattzelle in einer Form, Textbox oder Diagrammelement anzeigen. Wenn die Daten in einer Zelle oder einem Zellbereich geändert werden, müssen Sie den Zellinhalt mit dem Inhalt einer Form, Textbox oder eines Diagrammelements synchronisieren. Dazu können Sie eine Form, Textbox oder Diagrammelement mit den Zellen verknüpfen, die die gewünschten Daten enthalten.

{{% /alert %}}

## So verknüpfen Sie Formen mit Zellen in MS Excel

Die folgende Abbildung zeigt, wie man eine verknüpfte Zelle für eine Form einstellt.

![todo:image_alt_text](link-shapes-to-cells-1.png)

1. Wählen Sie eine Form aus. Die Formelleiste ist normalerweise leer.

2. Geben Sie die Formel der Form ein, zum Beispiel "=A1"

## Wie man Formen in Aspose.Cells mit Zellen verknüpft

Der folgende Code zeigt, wie die Aspose.Cells-Bibliothek verwendet wird, um eine Verknüpfung für eine Form oder Textbox zu setzen, damit der Zellinhalt dynamisch angezeigt wird.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-1.cs"  >}}

## Erweiterte Nutzung

Wenn Sie möchten, dass der Text der Form aus zwei oder mehr Zellen besteht oder wenn Sie den gewünschten Inhalt anhand einer Formel auswählen möchten, erfüllt der obige Beispielcode möglicherweise nicht Ihre Bedürfnisse. In diesem Fall müssen Sie etwas Fortgeschritteneres tun. Sie müssen zuerst die Formel, die das gewünschte Ergebnis liefert, in eine Zelle einfügen und dann die Form mit der Zelle, die die Formel enthält, verknüpfen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-2.cs"  >}}

{{< app/cells/assistant language="csharp" >}}
