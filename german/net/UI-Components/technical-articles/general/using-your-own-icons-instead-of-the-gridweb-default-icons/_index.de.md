---
title: Verwenden Ihrer eigenen Symbole anstelle der GridWeb-Standardsymbole
type: docs
weight: 10
url: /de/net/using-your-own-icons-instead-of-the-gridweb-default-icons/
---
{{% alert color="primary" %}} 

Manchmal möchten Sie möglicherweise Ihre eigenen Symbole (Bilder) anstelle der Standardsymbole des Steuerelements Aspose.Cells.GridWeb verwenden. Dieser Artikel erklärt, wie das geht.

{{% /alert %}} 

Die Standardsymbole des Steuerelements befinden sich im URL-Pfad „/acw_client/". Der Dateipfad kann lauten: "C:\Programme\Aspose\Aspose.Cells for .NET\acw_client" standardmäßig. In diesem Ordner finden Sie Dateien wie submit.gif, save.gif usw. Wenn Sie diese Bilder durch Ihre eigenen ersetzen möchten, fügen Sie einen Konfigurationsabschnitt zur Datei web.config Ihrer Webanwendung hinzu.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

Sie haben vielleicht bemerkt, dass diese Konfiguration nur den Bildpfad des Steuerelements betrifft und nicht den Client-Skriptpfad des Steuerelements. Wenn Sie beispielsweise Ihre Seite mit dem GridWeb-Steuerelement ausführen und die Quelldatei im Browser überprüfen, stellen Sie möglicherweise fest, dass die acw_ Klient_path-Eigenschaft des DIV-Elements des Grids sagt immer noch: „/yourApp/webform1.aspx/“. In einigen Fällen müssen Sie möglicherweise den Client-Skriptpfad neu definieren. Um das Steuerelement zu zwingen, den neu definierten Bildpfad als Client-Skriptpfad zu verwenden, fügen Sie eine weitere Konfigurationseinstellung im Abschnitt „appSettings“ hinzu
**XML**

{{< highlight "csharp" >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

Diese Konfiguration wird nur mit der lizenzierten Steuerung wirksam.

{{% /alert %}}
