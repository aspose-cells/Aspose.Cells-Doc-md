---
title: Uso de Aspose.Cells en plataformas de 32 y 64 bits
type: docs
weight: 10
url: /es/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---
{{% alert color="primary" %}} 

Aspose.Cells es un componente .NET puro que puede simplificar su proceso de implementación mediante la implementación de XCOPY. Para instalar Aspose.Cells, simplemente puede copiar el ensamblaje del componente (Aspose.Cells.dll) en un directorio para su aplicación: la aplicación puede comenzar a usarlo de inmediato. Esto es posible debido a la naturaleza autodescriptiva de los componentes .NET. Este tipo de implementación también tiene un impacto cero en el proceso de instalación.

{{% /alert %}} 
## **Despliegue**
Aspose.Cells admite entornos de 32 y 64 bits. Cuando instala el componente Aspose.Cells for .NET usando el instalador MSI Aspose.Cells, se agregan diferentes archivos DLL a diferentes carpetas en las carpetas Aspose.Cells ${installation_Path}. Consulte la descripción en la tabla de qué carpeta contiene los ensamblajes que necesita usar con una versión particular del marco .NET.

|**Carpeta**|**Descripción**|
|:- |:- |
|red2.0|Contiene ensamblados para usar con .NET Framework 2.0, 3.0, 3.5, 4.0 y Mono. Estos son los ensamblados que normalmente debe usar para entornos de 32 y 64 bits.|
|net2.0_AuthenticodeSigned|Igual que el anterior, pero los ensamblajes están firmados digitalmente con Authenticode. Los ensamblajes firmados pueden cargarse más lentamente que sin Authenticode|
|net3.5_PerfilCliente|Contiene ensamblados para usar con .NET Framework 3.5 o 4.0 Client Profile.|
|red3.5_Perfil del cliente_AuthenticodeFirmado|Igual que el anterior, pero los ensamblajes están firmados digitalmente con Authenticode. Los ensamblados firmados pueden cargarse más lentamente que sin Authenticode.|
|red3.5|Contiene ensamblajes para usar con .NET Framework 3.5 o 4.0.|
|net3.5_AuthenticodeFirmado|Igual que el anterior, pero los ensamblajes están firmados digitalmente con Authenticode. Los ensamblados firmados pueden cargarse más lentamente que sin Authenticode.|
|net4.0|Contiene ensamblajes para usar con .NET Framework 4.0 y 4.5.|
|estándar de red|Contiene ensamblados para usar con .Net Standard 2.0|
|netcoreapp2.1|Contiene ensamblados para usar con .Net core 2.1|
|Xamarin.iOS|Contiene ensamblados para usar con Xamarin.iOS|
|Xamarin.Android|Contiene ensamblados para usar con Xamarin.Android.|
|red5.0|Contiene ensamblados para usar con .net5.0.|
|net6.0|Contiene ensamblados para usar con .net6.0.|
{{% alert color="primary" %}} 

En proyectos VS.NET (por ejemplo, 2005, 2008, 2010, 2012, etc.), al agregar una referencia a Aspose.Cells, el cuadro de diálogo Agregar referencia se refiere a los archivos Aspose.Cells.dll en las carpetas net2.0 o net3.5 respectivamente. (Para obtener más información, lea Referencias Aspose.Cells de un proyecto .NET). Puede cambiar la referencia a la biblioteca según su entorno. Tenga en cuenta que si el marco de destino del proyecto es .NET Framework 3.5/4 Client Profile, use el archivo de componente Aspose.Cells.dll ubicado en la carpeta net_ClientProfile.

{{% /alert %}}
