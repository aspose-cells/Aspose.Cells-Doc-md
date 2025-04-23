---
title: Generieren von Miniaturbildern für bedingte Formatierung DataBars
description: Aspose.Cells für Python via .NET ist eine Python Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Sie unterstützt die Erstellung bedingt formatierter Datenbalken und Bilder, was es den Nutzern ermöglicht, die Anzeige der Tabelle basierend auf den Zellenwerten anzupassen. Dieser Artikel stellt die Verwendung der Aspose.Cells für Python Bibliothek vor, um bedingt formatierte Datenbalken und Bilder zu generieren.
keywords: Aspose.Cells für Python via .NET, Bedingte Formatierung, Datenbalken, Bilder, Tabellen
type: docs
weight: 40
url: /de/python-net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Manchmal müssen Bilder von bedingten Formatierungs-Datenbalken generiert werden. Sie können die Aspose.Cells [**DataBar.to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image) Methode verwenden, um diese Bilder zu erstellen. Dieser Artikel zeigt, wie man mit Aspose.Cells für Python via .NET einen DataBar-Bild erzeugt.

{{% /alert %}}

Der folgende Beispielcode generiert das DataBar-Bild der Zelle C1. Zuerst greift er auf das Formatbedingungsobjekt der Zelle zu, und dann greift er von diesem Objekt aus auf das [**DataBar**](https://reference.aspose.com/cells/python-net/aspose.cells/databar)-Objekt zu und verwendet dessen [**to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image)-Methode, um das Bild der Zelle zu generieren. Schließlich speichert er das Bild auf der Festplatte.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GenerateDatabarImage-1.py" >}}
