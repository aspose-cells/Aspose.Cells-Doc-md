---
title: Cómo utilizar Aspose.Cells.GridWeb con .NET Core
type: docs
weight: 40
url: /es/net/aspose-cells-gridweb/how-to-use-aspose-cells-gridweb-with-net-core/
keywords: GridWeb,dotnetcore
description: Este artículo presenta cómo usar GridWeb en la aplicación web .net core
---

{{% alert color="primary" %}} 

Este tema explica cómo usar Aspose.Cells.GridWeb con aplicaciones .NET Core usando Visual Studio .NET 2019. Este tema es útil para los desarrolladores principiantes que trabajan con Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Utilizar Aspose.Cells.GridWeb con .NET Core**
Este tema muestra cómo usar Aspose.Cells.GridWeb haciendo un sitio web de ejemplo en Visual Studio 2019. El proceso se ha dividido en pasos.
### **Paso 1: Crear un nuevo proyecto**
1. Abre Visual Studio 2019.
1. Del menú **Archivo**, selecciona **Nuevo**, luego **Proyecto**.
   Se abre el cuadro de diálogo para crear un nuevo proyecto.
1. Selecciona **Aplicación web ASP.NET Core** de las plantillas de proyectos instaladas en Visual Studio y haz clic en **Siguiente**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1. Especifica una ubicación donde se guardará el proyecto y haz clic en **Crear**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1. Selecciona la plantilla **Aplicación web (Modelo-Vista-Controlador)** y asegúrate de que está seleccionado **ASP .NET Core 2.1**. 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1. Haz clic en **Crear**.
### **Paso 2: Comprobando la vista inicial**
Al ejecutar el proyecto recién creado se muestra la plantilla predeterminada en el navegador como se muestra en la imagen a continuación.



![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **Paso 3: Agregando Aspose.Cells.GridWeb**
1. Agrega los siguientes paquetes Nuget al proyecto

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Agregar el Paquete Aspose.Cells.GridWeb

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Agregue lo siguiente al archivo **_ViewImports.cshtml** en la carpeta Views.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

El archivo se verá así después de las modificaciones.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. Coloque el siguiente código en el método Index del HomeController.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

Recuerde actualizar la ruta de SessionStorePath y la ruta ImportExcelFile.

{{% /alert %}} 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1. Agregue el siguiente código en el archivo **Index.cshtml** en el directorio View > Home.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

El archivo se verá así después del cambio.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Agregue soporte para Session y GridScheduedService en el archivo Startup.cs
   1. Agregue el siguiente fragmento de código en el método ConfigureServices.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. Agregue el siguiente fragmento de código en el método Configure.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

Coloque el último acw_client en el directorio: **wwwroot/js** {{% alert color="primary" %}}   {{% /alert %}}
1. Agregue **AcwController** en Controllers para manejar la ruta acw que puede proporcionar todas las operaciones predeterminadas para la acción de edición general.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **Paso 4: Probar la aplicación**
Al ejecutar la aplicación, el resultado será similar al que se muestra en la imagen a continuación.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
