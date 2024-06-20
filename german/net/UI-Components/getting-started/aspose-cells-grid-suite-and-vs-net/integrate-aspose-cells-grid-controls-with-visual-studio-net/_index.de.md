---
title: Integrieren Sie Aspose.Cells Grid Controls mit Visual Studio.NET
type: docs
weight: 10
url: /de/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
description: In diesem Artikel wird beschrieben, wie die GridWeb und GridDesktop Steuerungen in Visual Studio .NET verwendet werden können.
keywords:  GridWeb,GridDesktop,visual studio,control,integrate
---

{{% alert color="primary" %}} 

Visual Studio.NET-Entwickler können Steuerelemente einfach aus der Toolbox auf ein Windows- oder Webformular ziehen. Das Aspose.Cells Grid Suite kann mit einem MSI-Installationsprogramm oder als Paket von DLLs heruntergeladen werden. Dieser Artikel erläutert, wie sichergestellt werden kann, dass Aspose.Cells.Grid-Steuerungen in Visual Studio.NET verwendet werden können, wenn diese mithilfe der DLLs anstelle des Installationsprogramms installiert wurden.

{{% /alert %}} 
## **Integrieren Sie Aspose.Cells Grid Controls mit Visual Studio.NET**
Um Aspose.Cells Grid-Steuerungen mit Visual Studio.NET zu integrieren:

1. Öffnen Sie die Toolbox.
1. Wählen Sie den Allgemein-Tab (oder einen anderen Tab aus, zu dem Sie Steuerelemente hinzufügen möchten).
1. Klicken Sie mit der rechten Maustaste auf den Allgemein-Tab.
1. Wählen Sie auf Visual Studio.NET **Choose Items** aus dem Menü aus. Der Dialog für die Toolbox anpassen wird angezeigt (Dieser Vorgang ist für neuere VS.NET-IDEs (z. B. VS.NET 2013/2015 oder später) mehr oder weniger der gleiche).
1. Klicken Sie auf **Durchsuchen** und suchen Sie die Dateien Aspose.Cells.GridDesktop.dll und Aspose.Cells.GridWeb.dll.
1. Wählen Sie die DLLs aus und klicken Sie dann auf **Öffnen**. Der Dialog für die Toolbox anpassen enthält jetzt Steuerelemente aus der Aspose.Cells Grid Suite. Die neu hinzugefügten Steuerelemente werden durch den Dialog hervorgehoben.
1. Klicken Sie auf **OK**, um die Steuerelemente Ihrer Visual Studio.NET-Toolbox hinzuzufügen.

Die Aspose.Cells Grid-Steuerungen wurden dem **Allgemein**-Tab der Toolbox hinzugefügt. Nur das GridWeb-Steuerelement ist nicht aktiv. Dies liegt daran, dass wir an einer Windows Forms-Anwendung arbeiten. GridWeb ist nur verfügbar, wenn Sie an Webformularen arbeiten, während GridDesktop nur mit Windows Forms verwendet werden kann.
