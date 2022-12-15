---
title: Integrera Aspose.Cells Grid Controls med Visual Studio.NET
type: docs
weight: 10
url: /sv/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
---
{{% alert color="primary" %}} 

 Visual Studio.NET-utvecklare kan enkelt dra kontroller från**Verktygslåda** på ett Windows eller webbformulär. Aspose.Cells Grid suite kan laddas ner med ett MSI-installationsprogram eller som en uppsättning DLL-paket. Den här artikeln förklarar vad du ska göra för att se till att Aspose.Cells.Grid-kontroller kan användas i Visual Studio.NET när det är installerat med DLL-filer istället för installationsprogrammet.

{{% /alert %}} 
## **Integrera Aspose.Cells Grid Controls med Visual Studio.NET**
Så här integrerar du Aspose.Cells Grid-kontroller med Visual Studio.NET:

1. Öppna verktygslådan.
1. Välj fliken Allmänt (eller någon annan flik som du vill lägga till kontroller på).
1. Högerklicka på fliken Allmänt.
1.  På Visual Studio.NET 2003: Välj**Lägg till/ta bort objekt** från menyn.
1. På Visual Studio.NET 2005 väljer du**Välj objekt** från menyn. Dialogrutan Anpassa verktygslåda kommer att visas (denna process är ungefär densamma för nyare VS.NET IDE:er (t.ex. VS.NET 2013/2015 eller senare)).
1.  Klick**Bläddra** och leta upp filerna Aspose.Cells.GridDesktop.dll och Aspose.Cells.GridWeb.dll.
1.  Välj DLL:erna och klicka sedan**Öppna**. Dialogrutan Anpassa verktygslåda kommer nu att innehålla kontroller från Aspose.Cells Grid Suite. De nyligen tillagda kontrollerna kommer att markeras av dialogrutan.
1.  Klick**OK** för att lägga till kontrollerna i din Visual Studio.NET Toolbox.

 Aspose.Cells Grid Controls kommer att ha lagts till i verktygslådan**Allmän** flik. Endast GridWeb-kontrollen är inte aktiv. Detta beror på att vi arbetar med en Windows Forms ansökan. GridWeb är endast tillgängligt när du arbetar med webbformulär medan GridDesktop endast kan användas med Windows-formulär.
