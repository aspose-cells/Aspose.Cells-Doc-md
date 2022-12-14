---
title: Speichern Sie HTML mit StreamProvider
type: docs
weight: 120
url: /de/java/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}}

Beim Konvertieren von Excel-Feldern, die Bilder und Formen enthalten, in HTML-Dateien treten häufig die folgenden zwei Probleme auf:
1. Wo sollen wir die Bilder und Formen speichern, wenn wir eine Excel-Datei im HTML-Stream speichern?
1. Ersetzen Sie den Standardpfad durch den ausgenommenen Pfad.

 In diesem Artikel wird die Implementierung erläutert[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) Schnittstelle zum Einstellen der[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) Eigentum. Durch die Implementierung dieser Schnittstelle können Sie die erstellten Ressourcen während der HTML-Generierung an Ihren spezifischen Speicherorten oder Speicherströmen speichern.

{{% /alert %}}

## Beispielcode

 Dies ist der Hauptcode, der die Verwendung von zeigt[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)Eigentum

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

 Hier ist der Code für*ExportStreamProvider* Klasse, die implementiert[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)Schnittstelle, die im obigen Code verwendet wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

