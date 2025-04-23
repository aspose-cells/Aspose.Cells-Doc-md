---
title: Generieren von Miniaturbildern für bedingte Formatierung DataBars
linktitle: Generieren von Miniaturbildern für bedingte Formatierung DataBars
description: Aspose.Cells ist eine Node.js Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien. Es unterstützt die Erstellung von bedingt formatierten Datenbalken und Bildern, die es Benutzern ermöglichen, die Anzeige der Tabelle basierend auf dem Zellwert anzupassen. Dieser Artikel zeigt, wie man die Aspose.Cells Bibliothek nutzt, um bedingt formatierte Datenbalken und Bilder zu generieren.
keywords: Aspose.Cells, Bedingte Formatierung, Datenbalken, Bilder, Tabellenkalkulationen, Node.js via C++
type: docs
weight: 40
url: /de/nodejs-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Manchmal muss man Bilder von bedingten Formatierungen DataBars generieren. Sie können die Methode von Aspose.Cells [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) verwenden, um diese Bilder zu generieren. In diesem Artikel wird gezeigt, wie man ein DataBar-Bild mit Aspose.Cells generiert.

{{% /alert %}}

Der folgende Beispielcode generiert das DataBar-Bild der Zelle C1. Zuerst greift es auf das Formatierungsbedingungsobjekt der Zelle zu, dann aus diesem Objekt auf das [**DataBar**](https://reference.aspose.com/cells/nodejs-cpp/databar)-Objekt und verwendet seine [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-)-Methode, um das Bild der Zelle zu erstellen. Schließlich wird das Bild auf der Festplatte gespeichert.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-GenerateConditionalFormattingDataBars.js" >}}

