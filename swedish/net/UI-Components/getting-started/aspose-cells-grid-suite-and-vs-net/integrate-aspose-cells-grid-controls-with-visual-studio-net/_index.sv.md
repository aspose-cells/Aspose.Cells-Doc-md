---
title: Integrera Aspose.Cells Grid kontroller med Visual Studio.NET
type: docs
weight: 10
url: /sv/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
description: Denna artikel beskriver hur man använder GridWeb och GridDesktop kontroller i Visual Studio .NET.
keywords:  GridWeb,GridDesktop,visual studio,control,integrate
---

{{% alert color="primary" %}} 

Visual Studio.NET-utvecklare kan enkelt dra kontroller från verktygslådan till en Windows- eller Web-blankett. Aspose.Cells Grid-suite kan laddas ner med en MSI-installatör eller som en uppsättning DLL-filer. Den här artikeln förklarar vad man ska göra för att se till att Aspose.Cells Grid-kontroller kan användas i Visual Studio.NET när de är installerade med DLL-filer istället för installatören.

{{% /alert %}} 
## **Integrera Aspose.Cells Grid-kontroller med Visual Studio.NET**
För att integrera Aspose.Cells Grid-kontroller med Visual Studio.NET:

1. Öppna verktygslådan.
1. Välj fliken Allmänt (eller någon annan flik du vill lägga till kontroller på).
1. Högerklicka på fliken Allmänt.
1. På Visual Studio.NET, välj **Välj objekt** från menyn. Anpassa verktygslådan-dialogrutan kommer att visas (Denna process är mer eller mindre densamma för nyare VS.NET IDEs (t.ex. VS.NET 2013/2015 eller senare)).
1. Klicka på **Bläddra** och hitta filerna Aspose.Cells.GridDesktop.dll och Aspose.Cells.GridWeb.dll.
1. Välj DLL-filerna och klicka sedan på **Öppna**. Anpassa verktygslådan-dialogrutan kommer nu innehålla kontroller från Aspose.Cells Grid Suite. De nyss tillagda kontrollerna kommer att markeras av dialogrutan.
1. Klicka på **OK** för att lägga till kontrollerna i din Visual Studio.NET-verktygslåda.

Aspose.Cells Grid-kontroller kommer att ha lagts till i verktygslådans **Allmänt** flik. Endast GridWeb-kontrollen är inte aktiv. Detta beror på att vi arbetar med en Windows Forms-applikation. GridWeb är endast tillgänglig när man arbetar med Web Forms medan GridDesktop kan användas endast med Windows-formulär.
