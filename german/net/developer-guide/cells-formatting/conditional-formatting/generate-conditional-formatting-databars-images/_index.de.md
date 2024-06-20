---
title: Generieren von Miniaturbildern für bedingte Formatierung DataBars
description: Aspose.Cells ist eine .NET Bibliothek zum Arbeiten mit Tabellendateien. Sie unterstützt die Generierung von bedingt formatierten Datenleisten und Bildern, was es Benutzern ermöglicht, die Anzeige der Tabelle basierend auf dem Wert der Zellen anzupassen. Dieser Artikel wird einführen, wie die Aspose.Cells Bibliothek verwendet wird, um bedingt formatierte Datenleisten und Bilder zu generieren.
keywords: Aspose.Cells, Bedingte Formatierung, Datenleisten, Bilder, Tabellendokumente
type: docs
weight: 40
url: /de/net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Manchmal muss man Bilder von bedingten Formatierungen DataBars generieren. Sie können die Methode von Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) verwenden, um diese Bilder zu generieren. In diesem Artikel wird gezeigt, wie man ein DataBar-Bild mit Aspose.Cells generiert.

{{% /alert %}}

Der folgende Beispielcode generiert das DataBar-Bild der Zelle C1. Zuerst greift er auf das Formatbedingungsobjekt der Zelle zu, und dann greift er von diesem Objekt aus auf das [**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar)-Objekt zu und verwendet dessen [**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)-Methode, um das Bild der Zelle zu generieren. Schließlich speichert er das Bild auf der Festplatte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
