---
title: HTML mit StreamProvider speichern
type: docs
weight: 80
url: /de/net/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}} 

Beim Konvertieren von Excel-Dateien, die Bilder und Formen enthalten, in HTML-Dateien stoßen wir häufig auf die folgenden zwei Probleme:
1. Wo sollten wir die Bilder und Formen speichern, wenn wir die Excel-Datei in eine HTML-Streamdatei speichern.
1. Ersetzen Sie den Standardpfad durch den erwarteten Pfad.

Dieser Artikel erklärt, wie die [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)-Schnittstelle implementiert wird, um die Eigenschaft [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) festzulegen. Durch die Implementierung dieser Schnittstelle können die erstellten Ressourcen während der HTML-Generierung an spezifischen Speicherorten oder in Memory-Streams gespeichert werden.

{{% /alert %}} 

Dies ist der Hauptcode zur Verwendung der Eigenschaft [HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



Hier ist der Code für die Klasse *ExportStreamProvider*, die die [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)-Schnittstelle implementiert, die im obigen Code verwendet wird.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

{{< app/cells/assistant language="csharp" >}}
