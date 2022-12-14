---
title: Cómo ejecutar Aspose.Cells en Docker
type: docs
description: Ejecute Aspose.Cells en un contenedor Docker para Linux, Windows Server y cualquier sistema operativo.
weight: 139
url: /es/net/how-to-run-aspose-cells-in-docker/
---
Los microservicios, junto con la contenedorización, hacen posible combinar tecnologías fácilmente. Docker le permite integrar fácilmente la funcionalidad Aspose.Cells en su aplicación, independientemente de la tecnología que se encuentre en su pila de desarrollo.

En caso de que esté apuntando a microservicios, o si la tecnología principal en su pila no es .NET, C++ o Java, pero necesita la funcionalidad Aspose.Cells, o si ya usa Docker en su pila, entonces puede estar interesado en utilizar Aspose.Cells en un Docker envase.

## requisitos previos

- Docker debe estar instalado en su sistema. Para obtener información sobre cómo instalar Docker en Windows o Mac, consulte los enlaces en la sección "Ver también".

- Además, tenga en cuenta que Visual Studio 2019, .NET Core 3.1 SDK se usa en el ejemplo que se proporciona a continuación.


## Hello World Aplicación

En este ejemplo, crea una aplicación de consola Hello World simple que hace un "Hello World!" documento y lo guarda en todos los formatos de guardado admitidos. Luego, la aplicación se puede compilar y ejecutar en Docker.

### Creación de la aplicación de consola

Para crear el programa Hello World, siga los pasos a continuación:
1. Una vez que Docker esté instalado, asegúrese de que use contenedores de Linux (predeterminado). Si es necesario, seleccione la opción Cambiar a contenedores de Linux en el menú Docker Desktops.
1. En Visual Studio, cree una aplicación de consola .NET Core.<br>
![todo:imagen_alternativa_texto](create-a-new-project.png)<br>
1. Instale la última versión Aspose.Cells desde NuGet. System.Drawing.Common y System.Text.Encoding.CodePages se instalarán como una dependencia de Aspose.Cells.<br>
![todo:imagen_alternativa_texto](nuget-aspose-cells.png)<br>
1. Dado que la aplicación se ejecutará en Linux, se deben instalar los activos nativos de Linux apropiados. Comience con la imagen base dotnet core sdk 3.1 e instale libgdiplus libc6-dev.
1. Cuando se agreguen todas las dependencias requeridas, escriba un programa simple que cree un "Hello World!" libro de trabajo y lo guarda en todos los formatos de guardado admitidos:<br>
**.NET**<br>
{{< highlight "csharp" >}}
using System;
namespace Aspose.Cells.Docker
{
    class Program
    {
        static void Main(string[] args)
        {
            Workbook workbook = new Workbook();
            workbook.Worksheets[0].Cells[0, 0].PutValue("Hello from Aspose.Cells!!!");
            foreach (SaveFormat sf in Enum.GetValues(typeof(SaveFormat)))
            {
                if (sf != SaveFormat.Unknown)
                {
                    try
                    {
                        // The folder specified will be mounted as a volume when run the application in Docker image.
                        var fileName = string.Format("out{0}", FileFormatUtil.SaveFormatToExtension(sf));
                        workbook.Save(fileName, sf);
                        Console.WriteLine("Saving {0}\t\t[OK]", sf);
                    }
                    catch
                    {
                        Console.WriteLine("Saving {0}\t\t[FAILED]", sf);
                    }
                }
            }
        }
    }
}

{{< /highlight >}}

Tenga en cuenta que la carpeta "TestOut" se especifica como una carpeta de salida para guardar documentos de salida. Al ejecutar la aplicación en Docker, se montará una carpeta en la máquina host en esta carpeta en el contenedor. Esto le permitirá ver fácilmente la salida generada por Aspose.Cells en el contenedor de Docker.

### Configuración de un Dockerfile

El siguiente paso es crear y configurar el Dockerfile.

1. Cree el Dockerfile y colóquelo junto al archivo de solución de su aplicación. Mantenga este nombre de archivo sin extensión (el predeterminado).
1. En el Dockerfile, especifique:

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

Lo anterior es un Dockerfile simple, que contiene las siguientes instrucciones:

- La imagen del SDK que se utilizará. Aquí está la imagen de .Net Core SDK 3.1. Docker lo descargará cuando se ejecute la compilación. La versión de SDK se especifica como una etiqueta.
- Instale Fuentes porque la imagen del SDK contiene muy pocas fuentes. El comando copia los archivos de fuentes de la imagen local a la ventana acoplable. Asegúrese de tener un directorio local de "fuentes" que contenga todas las fuentes que necesita instalar. En este ejemplo, el directorio local de "fuentes" se coloca en el mismo directorio que el Dockerfile.
- El directorio de trabajo, que se especifica en la línea siguiente.
- El comando para copiar todo al contenedor, publicar la aplicación y especificar el punto de entrada.
- El comando para instalar libgdiplus se ejecuta en el contenedor. Esto es requerido por System.Drawing.Common.

### Creación y ejecución de la aplicación en Docker

Ahora la aplicación se puede compilar y ejecutar en Docker. Abra su símbolo del sistema favorito, cambie el directorio a la carpeta con la aplicación (carpeta donde se encuentran el archivo de la solución y el Dockerfile) y ejecute el siguiente comando:

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

La primera vez que se ejecuta este comando, puede llevar más tiempo, ya que Docker necesita descargar las imágenes requeridas. Una vez completado el comando anterior, ejecute el siguiente comando:

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

Preste atención al argumento de montaje porque, como se mencionó anteriormente, una carpeta en la máquina host se monta en la carpeta del contenedor, para ver fácilmente los resultados de la ejecución de la aplicación. Las rutas en Linux distinguen entre mayúsculas y minúsculas.

{{% /alert %}}

## Imágenes de apoyo Aspose.Cells

- Aspose.Cells for .NET El estándar no admite EMF ni TIFF en Linux.


## Más ejemplos

***1. Para ejecutar la aplicación en Windows Server 2019***

- Dockerfile

{{< highlight "plain" >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

- Crear imagen acoplable

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Ejecutar imagen de Docker

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. Para ejecutar la aplicación en Linux***

- Escriba un programa simple que configure la carpeta de fuentes, cree un "Hello World!" libro de trabajo y lo guarda.

{{< highlight "csharp" >}}
namespace Aspose.Cells.Docker.Fonts
{
    using System;
    using System.IO;

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Set font folders on linux.
                string[] fonts = { "/Fonts" };
                FontConfigs.SetFontFolders(fonts, true);
                // build workbook
                Workbook workbook = new Workbook();
                MemoryStream memoryStream = new MemoryStream();
                workbook.Worksheets[0].Cells[0, 0].PutValue("Hello from Aspose.Cells!!!");
                Style style = workbook.CreateStyle();
                style.Font.Name = "Arial";
                style.Font.Size = 16;
                workbook.Worksheets[0].Cells[0, 0].SetStyle(style);
                workbook.Save("/TestOut/TestFontsOut.xlsx");
            }
            catch (Exception e)
            {
                Console.WriteLine("Saving outfonts.xlsx\t\t[FAILED],{0}", e.Message);
            }
           
        }
    }
}

{{< /highlight >}}
- Dockerfile

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.Fonts.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.Fonts.dll"]{{< /highlight >}}

- Crear imagen acoplable

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Ejecutar imagen de Docker

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## Ver también

- [Instale Docker Desktop en Windows](https://docs.docker.com/docker-for-windows/install/)
- [Instalar Docker Desktop en Mac](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Núcleo 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- [Cambiar a contenedores de Linux](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers) opción
-  Información adicional sobre[.NET SDK básico](https://hub.docker.com/_/microsoft-dotnet-sdk)
