---
title: Generieren Sie DataBars-Bilder mit bedingter Formatierung
description: Aspose.Cells ist eine .NET-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Es unterstützt die Generierung bedingt formatierter Datenbalken und Bilder, sodass Benutzer die Anzeige der Tabelle basierend auf dem Wert der Zellen anpassen können. In diesem Artikel wird erläutert, wie Sie mit der Bibliothek Aspose.Cells bedingt formatierte Datenbalken und Bilder generieren.
keywords: Aspose.Cells, Conditional Formatting, Data Bars, Images, Spreadsheets
type: docs
weight: 40
url: /de/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 Manchmal müssen Sie Bilder von DataBars mit bedingter Formatierung generieren. Sie können Aspose.Cells verwenden[**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) Methode, um diese Bilder zu erzeugen. In diesem Artikel wird gezeigt, wie Sie mit Aspose.Cells ein DataBar-Bild generieren.

{{% /alert %}}

 Der folgende Beispielcode generiert das DataBar-Bild von Zelle C1. Zuerst greift es auf das Formatbedingungsobjekt der Zelle zu und dann von diesem Objekt aus auf das[**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar) Objekt und verwendet es[**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)Methode, um das Bild der Zelle zu erzeugen. Schließlich wird das Bild auf der Festplatte gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
