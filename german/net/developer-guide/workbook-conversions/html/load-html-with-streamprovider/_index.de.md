---
title: HTML in Excel mit StreamProvider laden
type: docs
weight: 80
url: /de/net/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

Beim Laden von HTML-Dateien, die externe Ressourcen enthalten, stoßen wir oft auf die folgenden beiden Probleme:
1. Wenn der HTML-Stream geladen wird, können die Bilder und externen Ressourcen, auf die die HTML-Datei verweist, nicht über relative Pfade erhalten werden.
1. Externe Ressourcenpfade, auf die in HTML-Dateien verwiesen wird, müssen zugeordnet werden

In diesem Artikel wird erklärt, wie die [IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) Schnittstelle zur Festlegung der [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) Eigenschaft implementiert werden. Durch die Implementierung dieser Schnittstelle können Sie externe Ressourcen beim Laden von Html-Streams laden oder diese externen Ressourcen sind relativ.

{{% /alert %}} 

Dies ist der Hauptcode, der die Verwendung der [HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) Eigenschaft zeigt



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
{{< app/cells/assistant language="csharp" >}}
