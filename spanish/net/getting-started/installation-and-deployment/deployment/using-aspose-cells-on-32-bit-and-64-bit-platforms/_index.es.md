---
title: Usar Aspose.Cells en plataformas de 32 bits y 64 bits
type: docs
weight: 10
url: /es/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---

{{% alert color="primary" %}} 

Aspose.Cells es un componente puro de .NET que puede simplificar su proceso de implementación mediante la implementación de XCOPY. Para instalar Aspose.Cells, simplemente puede copiar el ensamblado del componente (Aspose.Cells.dll) en un directorio para su aplicación: la aplicación puede comenzar a usarlo de inmediato. Esto es posible debido a la naturaleza auto-descriptiva de los componentes .NET. Este tipo de implementación tampoco tiene ningún impacto en el proceso de instalación.

{{% /alert %}} 
## **Despliegue**
Aspose.Cells admite entornos de 32 bits y 64 bits. Cuando instala el componente Aspose.Cells for .NET mediante el instalador MSI de Aspose.Cells, se añaden DLL diferentes a diferentes carpetas en la(s) carpeta(s) de Aspose.Cells ${installation_Path}. Consulte la descripción en la tabla para saber qué carpeta contiene los ensamblados que necesita usar con una versión concreta del .NET Framework.

|**Carpeta**|**Descripción**|
| :- | :- |
|net2.0|Contiene ensamblajes para usar con .NET Framework 2.0, 3.0, 3.5, 4.0 y Mono. Estos son los ensamblajes que normalmente debería usar para entornos de 32 bits y 64 bits.|
|net2.0_AuthenticodeSigned|Igual que arriba, pero los ensamblajes están firmados digitalmente con Authenticode. Los ensamblajes firmados pueden cargar más lento que sin Authenticode|
|net3.5_ClientProfile|Contiene ensamblajes para usar con .NET Framework 3.5 o 4.0 Client Profile.|
|net3.5_ClientProfile_AuthenticodeSigned|Igual que arriba, pero los ensamblajes están firmados digitalmente con Authenticode. Los ensamblajes firmados pueden cargar más lento que sin Authenticode.|
|net3.5|Contiene ensamblajes para usar con .NET Framework 3.5 o 4.0.|
|net3.5_AuthenticodeSigned|Igual que arriba, pero los ensamblajes están firmados digitalmente con Authenticode. Los ensamblajes firmados pueden cargar más lento que sin Authenticode.|
|net4.0|Contiene ensamblajes para usar con .NET Framework 4.0 y 4.5.|
|netStandard|Contiene ensamblajes para usar con .Net Standard 2.0|
|netcoreapp2.1|Contiene ensamblajes para usar con .Net core 2.1|
|Xamarin.iOS|Contiene ensamblajes para usar con Xamarin.iOS|
|Xamarin.Android|Contiene ensamblajes para usar con Xamarin.Android|
|net5.0|Contiene ensamblajes para usar con .net5.0.|
|net6.0|Contiene ensamblajes para usar con .net6.0.|
{{% alert color="primary" %}} 

En VS.NET (por ejemplo 2005, 2008, 2010, 2012, etc.) proyectos, al agregar una referencia a Aspose.Cells, el cuadro de diálogo Agregar referencia se refiere a los archivos Aspose.Cells.dll en la carpeta net2.0 o net3.5 respectivamente. (Para más información, lea la referencia a Aspose.Cells desde un proyecto .NET). Puede cambiar la referencia a la biblioteca de acuerdo a su entorno. Por favor note que si el marco de destino del proyecto es .NET Framework 3.5/4 Client Profile, use el archivo de componente Aspose.Cells.dll ubicado en la carpeta net_ClientProfile.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
