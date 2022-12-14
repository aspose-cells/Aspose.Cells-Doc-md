---
title: Speichern Sie HTML mit StreamProvider
type: docs
weight: 80
url: /de/net/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}} 

Beim Konvertieren von Excel-Feldern, die Bilder und Formen enthalten, in HTML-Dateien treten häufig die folgenden zwei Probleme auf:
1. Wo sollen wir die Bilder und Formen speichern, wenn wir eine Excel-Datei im HTML-Stream speichern?
1. Ersetzen Sie den Standardpfad durch den ausgenommenen Pfad.

 In diesem Artikel wird die Implementierung erläutert[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) Schnittstelle zum Einstellen der[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider) Eigentum. Durch die Implementierung dieser Schnittstelle können Sie die erstellten Ressourcen während der HTML-Generierung an Ihren spezifischen Speicherorten oder Speicherströmen speichern.

{{% /alert %}} 

 Dies ist der Hauptcode, der die Verwendung von zeigt[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)Eigentum



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



 Hier ist der Code für*ExportStreamProvider* Klasse, die implementiert[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)Schnittstelle, die im obigen Code verwendet wird.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

