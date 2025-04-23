---
title: Instalar Aspose Cells a través de NuGet
type: docs
weight: 30
url: /es/net/installation/
---


## **Instale Aspose.Cells for .NET a través de NuGet**
NuGet es la forma más fácil de descargar e instalar las API de Aspose para .NET. Abra Microsoft Visual Studio y el administrador de paquetes de NuGet. Busque "aspose" para encontrar la API deseada. Haga clic en "Instalar", la API seleccionada se descargarán y se referenciarán en su proyecto.

Nota: Puede visitar la página web de nuget para aspose.cells para obtener más información: 
[Paquete NuGet Aspose.Cells for .NET](https://www.nuget.org/packages/Aspose.Cells/)

### **Instalar Aspose.Cells usando el GUI del Administrador de Paquetes**
Siga estos pasos para referenciar el componente Aspose.Cells usando el GUI del administrador de paquetes:

- Abra su solución/proyecto en Visual Studio.
- Haga clic en **Herramientas** -> **Administrador de paquetes de bibliotecas** -> **Administrar paquetes NuGet** desde la Solución. También puede acceder fácilmente a la misma opción a través del Explorador de soluciones. Haga clic derecho en la solución o proyecto y seleccione **Administrador de paquetes NuGet** desde el menú contextual.
- Seleccione **En línea** en el menú de la izquierda y escriba "Aspose.Cells" en el cuadro de búsqueda para encontrar el paquete Aspose.Cells .NET.
- Haga clic en el botón **Instalar** junto a la entrada Aspose.Cells for .NET para instalar la última versión en su proyecto.
### **Instalar Aspose.Cells usando la Consola del Administrador de Paquetes**
Puede seguir los siguientes pasos para referenciar el componente Aspose.Cells usando la consola del administrador de paquetes:

- Abra su solución/proyecto en Visual Studio.
- Seleccione **Herramientas** -> **Administrador de paquetes de bibliotecas** -> **Consola del Administrador de Paquetes** en el menú para abrir la consola del administrador de paquetes.
  - Escriba el comando "Install-Package Aspose.Cells" y presione enter para instalar la última versión completa en su aplicación. Alternativamente, puede agregar el sufijo "-prerelease" al comando para especificar que se instale también la última versión que incluya correcciones.
- Verá que aparece el aviso "Descargando Aspose.Cells..." en la parte inferior izquierda de la ventana, indicando que la descarga está en proceso.
- Una vez descargado, verá los siguientes mensajes de confirmación. Si no está familiarizado con el EULA de Aspose, es una buena idea leer la licencia referenciada en la URL.
- Ahora debería encontrar que Aspose.Cells se ha agregado y referenciado con éxito en su aplicación.
## **Referenciar Aspose.Cells desde un Proyecto .NET**
Para utilizar Aspose.Cells en una aplicación, agregue una referencia. Para agregar una referencia usando Visual Studio:

1. En el **Explorador de soluciones**, expanda el nodo del proyecto al que desea agregar una referencia.
1. Haga clic derecho en el nodo **Referencias** del proyecto y seleccione **Agregar referencia** en el menú.
1. En el cuadro de diálogo **Agregar referencia**, seleccione la pestaña .NET (seleccionada por defecto). Si instaló usando el instalador MSI, Aspose.Cells aparecerá en el panel superior.
1. Selecciónelo y haga clic en **Seleccionar**.

Si solo has descargado o desempaquetado el archivo DLL:

1. Ubica el archivo Aspose.Cells.dll usando el botón **Examinar**. Aspose.Cells debería aparecer en el panel **Componentes Seleccionados** de la ventana de diálogo.
1. Haz clic en **OK**. La referencia a Aspose.Cells aparecerá bajo el nodo **Referencias** del proyecto.
### **Haciendo referencia al componente desde un proyecto de VS.NET 2010 Client Profile**
Si el framework de destino de tu proyecto es .NET Framework 3.5/4 Client Profile, utiliza el archivo del componente Aspose.Cells.dll ubicado en la carpeta net_ClientProfile de tu directorio de instalación. Por ejemplo:

- En el **Explorador de soluciones** de VS.NET 2010 para tu proyecto, haz clic derecho en **Referencias** y selecciona **Agregar referencia**.
- Selecciona la pestaña **Examinar** en el diálogo y haz clic en el menú desplegable **Buscar**.
- Encuentra y selecciona el archivo del componente Aspose.Cells.dll en tu directorio de instalación, por ejemplo: .../Archivos de programa/Aspose/Aspose.Cells for .NET/Bin/net_ClientProfile/ **(Asegúrate de haber instalado el producto usando el instalador MSI en tu máquina.)**
- Haz clic en **OK** para cerrar el diálogo

{{% alert color="primary" %}} 

Si el framework de destino de tu proyecto de VS.NET 2010 es ".NET Framework 4" u otro, simplemente utiliza el archivo del componente Aspose.Cells.dll ubicado en la carpeta net4.0/net2.0.

{{% /alert %}} 
## **Haciendo referencia a los controles de cuadrícula de Aspose.Cells desde un proyecto .NET**
Para usar un control de cuadrícula en tu aplicación, agrega una referencia a él. Para hacer referencia a un control de cuadrícula en Visual Studio, realiza lo siguiente:

- En **Explorador de soluciones**, expande el nodo del proyecto al que deseas agregar una referencia.
- Haz clic con el botón derecho en el nodo **Referencias** del proyecto y selecciona **Agregar referencia** en el menú.
- En el cuadro de diálogo **Agregar referencia**, selecciona la pestaña **.NET** (seleccionada por defecto). Si has utilizado el instalador MSI para instalar Aspose.Cells for .NET, Aspose.Cells.GridDesktop y Aspose.Cells.GridWeb aparecerán en el panel superior.
- Selecciona ambos y haz clic en **Seleccionar**.
- Las referencias a Aspose.Cells.GridDesktop y Aspose.Cells.GridWeb aparecerán bajo el nodo Referencias del proyecto.

Si solo has descargado y desempaquetado el archivo DLL:

- Localiza los archivos Aspose.Cells.GridDesktop.dll y Aspose.Cells.GridWeb.dll usando el botón Examinar. El conjunto de controles de cuadrícula de Aspose.Cells ha sido referenciado y debería aparecer en el panel **Componentes Seleccionados** de la ventana de diálogo.
- Haz clic en **OK.**
## **Desinstalando Aspose.Cells for .NET**
Si ha utilizado el instalador MSI para implementar Aspose.Cells for .NET, siga estos pasos para eliminar por completo el componente y los controles, las demos asociadas y la documentación:

- Desde el menú **Inicio**, seleccione **Configuración**, seguido de **Panel de Control**.
- Haga clic en **Agregar o quitar programas**.
- Seleccione Aspose.Cells for .NET (versión).
- Haga clic en **Cambiar/Quitar** para eliminar Aspose.Cells.
{{< app/cells/assistant language="csharp" >}}
