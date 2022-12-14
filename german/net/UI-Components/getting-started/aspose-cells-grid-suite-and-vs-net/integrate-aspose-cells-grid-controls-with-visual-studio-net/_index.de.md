---
title: Integrieren Sie Aspose.Cells-Rastersteuerelemente in Visual Studio.NET
type: docs
weight: 10
url: /de/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
---
{{% alert color="primary" %}} 

 Visual Studio.NET-Entwickler können Steuerelemente einfach aus der ziehen**Werkzeugkasten** auf ein Windows oder Webformular. Aspose.Cells Die Grid-Suite kann mit einem MSI-Installationsprogramm oder als Satz von DLL-Paketen heruntergeladen werden. In diesem Artikel wird erläutert, was zu tun ist, um sicherzustellen, dass Aspose.Cells.Grid-Steuerelemente in Visual Studio.NET verwendet werden können, wenn es mithilfe der DLLs anstelle des Installationsprogramms installiert wird.

{{% /alert %}} 
## **Integrieren Sie Aspose.Cells-Rastersteuerelemente in Visual Studio.NET**
So integrieren Sie Aspose.Cells Grid-Steuerelemente in Visual Studio.NET:

1. Öffnen Sie die Werkzeugkiste.
1. Wählen Sie die Registerkarte Allgemein (oder eine andere Registerkarte, der Sie Steuerelemente hinzufügen möchten).
1. Klicken Sie mit der rechten Maustaste auf die Registerkarte Allgemein.
1.  In Visual Studio.NET 2003: Auswählen**Elemente hinzufügen/entfernen** aus dem Menü.
1. Wählen Sie in Visual Studio.NET 2005 aus**Wählen Sie Artikel** aus dem Menü. Das Dialogfeld Customize Toolbox wird angezeigt (Dieser Prozess ist mehr oder weniger derselbe für neuere VS.NET-IDEs (z. B. VS.NET 2013/2015 oder höher)).
1.  Klicken**Durchsuche** und suchen Sie die Dateien Aspose.Cells.GridDesktop.dll und Aspose.Cells.GridWeb.dll.
1.  Wählen Sie die DLLs aus und klicken Sie dann auf**Offen**. Das Dialogfeld Customize Toolbox enthält jetzt Steuerelemente aus Aspose.Cells Grid Suite. Die neu hinzugefügten Steuerelemente werden im Dialogfeld hervorgehoben.
1.  Klicken**OK** um die Steuerelemente zu Ihrer Visual Studio.NET-Toolbox hinzuzufügen.

 die Aspose.Cells Grid Controls wurden der Toolbox hinzugefügt**Allgemein** Tab. Nur das GridWeb-Steuerelement ist nicht aktiv. Dies liegt daran, dass wir an einer Windows Forms-Anwendung arbeiten. GridWeb ist nur verfügbar, wenn Sie an Webformularen arbeiten, während GridDesktop nur mit Windows-Formularen verwendet werden kann.
