---
title: Verwenden Sie Ihre eigenen Symbole anstelle der standardmäßigen GridWeb Symbole
type: docs
weight: 10
url: /de/net/aspose-cells-gridweb/use-your-own-icons-instead-of-the-default-icons/
keywords: GridWeb, Symbol, Symbole
description: Dieser Artikel beschreibt, wie Symbole in GridWeb verwendet werden.
---

{{% alert color="primary" %}} 

Manchmal möchten Sie möglicherweise Ihre eigenen Symbole (Bilder) anstelle der standardmäßigen Symbole der Aspose.Cells.GridWeb-Steuerung verwenden. Dieser Artikel erklärt, wie das gemacht werden kann.

{{% /alert %}} 

Die standardmäßigen Symbole der Steuerung befinden sich im URL-Pfad "/acw_client/". Der Dateipfad ist standardmäßig "C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client". In diesem Ordner finden Sie Dateien wie submit.gif, save.gif usw. Wenn Sie diese Bilder durch eigene ersetzen möchten, fügen Sie einen Konfigurationsabschnitt zur Web.config-Datei Ihrer Webanwendung hinzu.

**XML**

{{< highlight csharp >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

Sie haben möglicherweise bemerkt, dass diese Konfiguration nur den Bildpfad der Steuerung betrifft und den Client-Skript-Pfad der Steuerung nicht beeinflusst. Wenn Sie beispielsweise Ihre Seite mit der GridWeb-Steuerung ausführen und die Quelldatei im Browser überprüfen, finden Sie möglicherweise, dass die acw_client _path-Eigenschaft des DIV-Elements der Tabelle immer noch sagt: "/IhreApp/webform1.aspx/". In einigen Fällen müssen Sie möglicherweise den Client-Skript-Pfad neu definieren. Um die Steuerung zu zwingen, den neu definierten Bildpfad als Client-Skript-Pfad zu verwenden, fügen Sie eine weitere Konfigurationseinstellung im appSettings-Bereich hinzu.
**XML**

{{< highlight csharp >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

Diese Konfiguration wirkt sich nur auf die lizenzierte Steuerung aus.

{{% /alert %}}
