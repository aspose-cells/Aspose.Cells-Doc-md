---
title: Cómo usar Aspose.Cells.GridWeb con .NET Core
type: docs
weight: 40
url: /es/net/how-to-use-aspose-cells-gridweb-with-net-core/
---
{{% alert color="primary" %}} 

Este tema explica cómo usar Aspose.Cells.GridWeb con aplicaciones .NET Core usando Visual Studio.NET 2019. Este tema es útil para los desarrolladores principiantes que trabajan con Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Use Aspose.Cells.GridWeb con .NET Core**
Este tema muestra cómo usar Aspose.Cells.GridWeb creando un sitio web de muestra en Visual Studio 2019. El proceso se ha dividido en pasos.
### **Paso 1: Creación de un nuevo proyecto**
1. Abra Visual Studio 2019.
1.  Desde el**Expediente** menú, seleccione**Nuevo** , después**Proyecto**.
 Se abre el cuadro de diálogo Crear un nuevo proyecto.
1.  Seleccione**ASP.NET Aplicación web principal** desde las plantillas de proyecto instaladas de Visual Studio y haga clic en**próximo**.

![todo:imagen_alternativa_texto](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1.  Especifique una ubicación donde la ubicación y el nombre del proyecto y haga clic en**Crear**.

![todo:imagen_alternativa_texto](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1.  Selecciona el**Aplicación Web (Modelo-Vista-Controlador)** plantilla y asegúrese de que**ASP .NET Núcleo 2.1** es seleccionado.

![todo:imagen_alternativa_texto](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1.  Hacer clic**Crear**.
### **Paso 2: Comprobación de la vista inicial**
Al ejecutar el proyecto recién creado, se muestra la plantilla predeterminada en el navegador, como se muestra en la imagen a continuación.



![todo:imagen_alternativa_texto](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **Paso 3: Agregar Aspose.Cells.GridWeb**
1. Agregue los siguientes paquetes Nuget al proyecto

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Agregar Aspose.Cells.Paquete GridWeb

![todo:imagen_alternativa_texto](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Agregue lo siguiente al archivo **_ViewImports.cshtml** en la carpeta Vistas.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

El archivo se verá así después de las modificaciones.

![todo:imagen_alternativa_texto](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. Coloque el siguiente código en el método Index de HomeController.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

Recuerde actualizar SessionStorePath y la ruta ImportExcelFile.

{{% /alert %}} 

![todo:imagen_alternativa_texto](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1.  Agregue el siguiente código en el**Índice.cshtml** archivo en el directorio Ver > Inicio.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

El archivo se verá así después del cambio.

![todo:imagen_alternativa_texto](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Agregue soporte de sesión y GridScheduedService en el archivo Startup.cs
 1. Agregue el siguiente fragmento de código en el método ConfigureServices.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:imagen_alternativa_texto](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. Agregue el siguiente fragmento de código en el método Configure.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:imagen_alternativa_texto](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. Coloque el acw_client más reciente en el directorio: **wwwroot/js** {{% alert color="primary" %}} {{% /alert %}}
1.  Agregar**AcwControlador**en Controladores para manejar el mapa de ruta acw que puede proporcionar todas las operaciones predeterminadas para la acción de edición general.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:imagen_alternativa_texto](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **Paso 4: prueba la aplicación**
Al ejecutar la aplicación, el resultado será similar al que se muestra en la imagen a continuación.

![todo:imagen_alternativa_texto](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
