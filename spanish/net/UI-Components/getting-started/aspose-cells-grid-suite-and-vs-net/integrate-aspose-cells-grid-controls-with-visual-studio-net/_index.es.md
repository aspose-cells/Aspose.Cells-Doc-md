---
title: Integrar los controles de Aspose.Cells Grid con Visual Studio.NET
type: docs
weight: 10
url: /es/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
description: Este artículo describe cómo usar los controles GridWeb y GridDesktop en Visual Studio .NET.
keywords:  GridWeb,GridDesktop,visual studio,control,integrate
---

{{% alert color="primary" %}} 

Los desarrolladores de Visual Studio.NET pueden arrastrar fácilmente controles desde la **Toolbox** a un formulario de Windows o Web. Aspose.Cells Grid suite se puede descargar con un instalador MSI o como un paquete de DLLs. Este artículo explica qué hacer para asegurarse de que los controles de Aspose.Cells.Grid se puedan usar en Visual Studio.NET cuando se instala utilizando los DLL en lugar del instalador.

{{% /alert %}} 
## **Integrar los controles de Aspose.Cells Grid con Visual Studio.NET**
Para integrar los controles de Aspose.Cells Grid con Visual Studio.NET:

1. Abrir la Toolbox.
1. Seleccionar la pestaña General (o cualquier otra pestaña a la que desee agregar controles).
1. Hacer clic derecho en la pestaña General.
1. En Visual Studio.NET, seleccionar **Choose Items** del menú. Se mostrará el diálogo Customize Toolbox (Este proceso es más o menos el mismo para las nuevas versiones del IDE de VS.NET (por ejemplo, VS.NET 2013/2015 o posteriores)).
1. Hacer clic en **Examinar** y localizar los archivos Aspose.Cells.GridDesktop.dll y Aspose.Cells.GridWeb.dll.
1. Seleccionar los DLL y luego hacer clic en **Abrir**. El diálogo Customize Toolbox ahora contendrá controles de Aspose.Cells Grid Suite. Los controles recién agregados serán resaltados por el diálogo.
1. Hacer clic en **Aceptar** para agregar los controles a su Toolbox de Visual Studio.NET.

los controles de Aspose.Cells Grid se habrán agregado a la pestaña **General** de la Toolbox. Solo el control GridWeb no está activo. Esto se debe a que estamos trabajando en una aplicación de Windows Forms. GridWeb solo está disponible cuando se trabaja en formularios web, mientras que GridDesktop solo se puede usar con formularios de Windows.
