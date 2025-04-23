---
title: Cómo ejecutar los ejemplos
type: docs
weight: 140
url: /es/net/how-to-run-the-examples/
---

## **Requisitos de software**
Asegúrese de cumplir con los siguientes requisitos antes de descargar y ejecutar los ejemplos.

1. Visual Studio 2015 o superior
1. Administrador de paquetes NuGet instalado en Visual Studio. Normalmente ya está instalado en Visual Studio 2015. Para obtener detalles sobre cómo instalar el administrador de paquetes NuGet, consulte: [Instalación de herramientas cliente de NuGet](https://docs.microsoft.com/en-us/nuget/install-nuget-client-tools)
1. Vaya a Herramientas->Opciones->Administrador de paquetes NuGet->Orígenes de paquetes y asegúrese de que la opción **nuget.org** esté seleccionada
1. El proyecto de ejemplo utiliza la función de Restauración automática de paquetes NuGet, por lo tanto, debe tener una conexión a Internet activa. Si no tiene una conexión a Internet activa en la máquina donde se van a ejecutar los ejemplos, consulte [Instalación](/cells/es/net/installation-and-deployment/) y agregue manualmente una referencia a Aspose.Cells.dll en el proyecto de ejemplo.
## **Descargar desde GitHub**
Todos los ejemplos de Aspose.Cells for .NET están alojados en [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET).
## **Ejemplos de Aspose.Cells**
- Puede clonar el repositorio usando su cliente de GitHub favorito o descargar el archivo ZIP desde [aquí](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- Extraiga el contenido del archivo ZIP en cualquier carpeta de su computadora. Todos los ejemplos están ubicados en la carpeta **Ejemplos**.
- Hay un archivo de solución Visual Studio para ejemplos en C# es decir **Aspose.Cells.Examples.CSharp.sln**.
- El proyecto se crea y mantiene en Visual Studio 2015.
- Abra el archivo de solución en Visual Studio y compile el proyecto.
- En la primera ejecución, las dependencias se descargarán automáticamente a través de NuGet. También puede descargar los archivos DLL por separado desde [aquí](https://downloads.aspose.com/cells/net).
- La carpeta **Data** en la carpeta raíz de **Examples** contiene archivos de entrada que son utilizados por los ejemplos en CSharp. Es obligatorio descargar la carpeta **Data** junto con el proyecto de ejemplos.
- Abra **RunExamples.cs**, todos los ejemplos se llaman desde aquí.
- Descomente los ejemplos que desee ejecutar desde el interior del proyecto.
## **Ejemplos Aspose.Cells.GridDesktop**
- Los ejemplos de Aspose.Cells.GridDesktop también están incluidos en el repositorio [Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) y estarán disponibles como parte del archivo ZIP descargable desde [aquí](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- Todos los ejemplos están ubicados en la carpeta **Examples_GridDesktop**.
- Similar a los ejemplos de Aspose.Cells, el nombre del archivo de solución de ejemplos de GridWeb es **Aspose.Cells.GridDesktop.Examples.CSharp.sln**.
- Abra el archivo de solución en Visual Studio y compile el proyecto.
- Todas las dependencias están incluidas como parte del proyecto de ejemplos. También puede descargar los archivos DLL por separado desde [aquí](https://downloads.aspose.com/cells/net).
- La carpeta **Data** en la carpeta raíz de **Examples_GridDesktop** contiene archivos de entrada utilizados por los ejemplos. Es obligatorio descargar la carpeta **Data** junto con el proyecto de ejemplos.
- Abra y ejecute el proyecto.
- Haga clic en el ejemplo en el menú que desea ejecutar desde el formulario.
## **Ejemplos Aspose.Cells.GridWeb**
- Los ejemplos de Aspose.Cells.GridWeb también están incluidos en el repositorio [Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) y estarán disponibles como parte del archivo ZIP descargable desde [aquí](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- Todos los ejemplos están ubicados en la carpeta **Examples_GridWeb**.
- Similar a los ejemplos de Aspose.Cells, el nombre del archivo de solución de ejemplos de GridWeb es **Aspose.Cells.GridWeb.Examples.CSharp.sln**.
- Abra el archivo de solución en Visual Studio y compile el proyecto.
- Todas las dependencias están incluidas como parte de los proyectos de ejemplos. También puede descargar los archivos DLL por separado desde [aquí](https://downloads.aspose.com/cells/net).
- La carpeta **Data** en la carpeta raíz de **Examples_GridWeb** contiene archivos de entrada utilizados por los ejemplos. Es obligatorio descargar la carpeta **Data** junto con el proyecto de ejemplos.
- Abra y ejecute **Examples.aspx** en el proyecto de ejemplos.
- Haz clic en el ejemplo en el navegador que desees ejecutar desde dentro del proyecto.
{{< app/cells/assistant language="csharp" >}}
