---
title: Erstellen von DataBars Bildern für bedingte Formatierung mit Golang über C++
linktitle: Generieren von Miniaturbildern für bedingte Formatierung DataBars
description: Aspose.Cells ist eine C++ Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Es unterstützt die Generierung bedingt formatierter Datenbalken und Bilder, sodass Benutzer die Anzeige der Tabelle basierend auf dem Zellwert anpassen können. Dieser Artikel zeigt, wie man die Aspose.Cells Bibliothek zur Erzeugung bedingt formatierter Datenbalken und Bilder nutzt.
keywords: Aspose.Cells, Bedingte Formatierung, Datenleisten, Bilder, Tabellendokumente
type: docs
weight: 40
url: /de/go-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Manchmal muss man Bilder von bedingten Formatierungen DataBars generieren. Sie können die Methode von Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) verwenden, um diese Bilder zu generieren. In diesem Artikel wird gezeigt, wie man ein DataBar-Bild mit Aspose.Cells generiert.

{{% /alert %}}

Der folgende Beispielcode generiert das DataBar-Bild der Zelle C1. Zuerst greift es auf das Formatierungsbedingungsobjekt der Zelle zu, dann aus diesem Objekt auf das [**DataBar**](https://reference.aspose.com/cells/go-cpp/databar/)-Objekt und verwendet seine [**ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/)-Methode, um das Bild der Zelle zu erstellen. Schließlich wird das Bild auf der Festplatte gespeichert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GenerateConditionalFormattingDatabarsImages.go" >}}
