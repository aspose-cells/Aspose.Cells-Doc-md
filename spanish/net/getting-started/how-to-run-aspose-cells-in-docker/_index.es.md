---
title: Cómo Ejecutar Aspose.Cells en Docker
type: docs
description: "Ejecutar Aspose.Cells en un contenedor de Docker para Linux, Windows Server y cualquier SO."
weight: 139
url: /es/net/how-to-run-aspose-cells-in-docker/
---

Los microservicios, en conjunto con la contenerización, hacen posible combinar fácilmente tecnologías. Docker te permite integrar fácilmente la funcionalidad de Aspose.Cells en tu aplicación, independientemente de la tecnología que esté en tu pila de desarrollo.

En caso de que estés apuntando a microservicios, o si la tecnología principal en tu pila no es .NET, C++ o Java, pero necesitas la funcionalidad de Aspose.Cells, o si ya estás usando Docker en tu pila, entonces es posible que te interese utilizar Aspose.Cells en un contenedor Docker.

## Requisitos previos

- Docker debe estar instalado en tu sistema. Para obtener información sobre cómo instalar Docker en Windows o Mac, consulta los enlaces en la sección 'Ver también'.

- Además, ten en cuenta que en el ejemplo se utiliza Visual Studio 2019 y el SDK de .NET Core 3.1.


## Aplicación Hola Mundo

En este ejemplo, creas una sencilla aplicación de consola Hola Mundo que crea un documento '¡Hola Mundo!' y lo guarda en todos los formatos de guardado admitidos. La aplicación luego se puede construir y ejecutar en Docker.

### Creación de la aplicación de consola

Para crear el programa Hola Mundo, sigue los pasos a continuación:
1. Una vez instalado Docker, asegúrate de que esté utilizando contenedores Linux (por defecto). Si es necesario, selecciona la opción Cambiar a contenedores Linux desde el menú de Docker Desktop.
1. In Visual Studio, create a .NET Core console application.<br>
![todo:image_alt_text](create-a-new-project.png)<br>
1. Install the latest Aspose.Cells version from NuGet. System.Drawing.Common and System.Text.Encoding.CodePages will be installed as a dependency of Aspose.Cells.<br>
![todo:image_alt_text](nuget-aspose-cells.png)<br>
1. Dado que la aplicación se ejecutará en Linux, es necesario instalar los archivos nativos apropiados para Linux. Comienza con la imagen base del SDK de dotnet core 3.1 e instala libgdiplus libc6-dev.
1. When all required dependencies are added, write a simple program that creates a “Hello World!” workbook and saves it in all supported save formats:<br>
**.NET**<br>
{{< highlight csharp >}}
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

Ten en cuenta que la carpeta 'TestOut' se especifica como una carpeta de salida para guardar los documentos de salida. Al ejecutar la aplicación en Docker, se montará una carpeta de la máquina host en esta carpeta en el contenedor. Esto te permitirá ver fácilmente la salida generada por Aspose.Cells en el contenedor Docker.

### Configuración de un Dockerfile

El siguiente paso es crear y configurar el Dockerfile.

1. Crea el Dockerfile y colócalo junto al archivo de solución de tu aplicación. Mantén el nombre de este archivo sin extensión (el predeterminado).
1. En el Dockerfile, especifica:

{{< highlight plain >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

El anterior es un Dockerfile sencillo, que contiene las siguientes instrucciones:

- La imagen del SDK que se va a utilizar. Aquí se trata de la imagen .Net Core SDK 3.1. Docker la descargará cuando se ejecute la construcción. La versión del SDK se especifica como una etiqueta.
- Instalar fuentes, porque la imagen del SDK contiene muy pocas fuentes. El comando copia los archivos de fuente desde local a la imagen de Docker. Asegúrate de tener un directorio local 'fuentes' que contenga todas las fuentes que necesitas instalar. En este ejemplo, el directorio local 'fuentes' se coloca en el mismo directorio que el Dockerfile.
- El directorio de trabajo, el cual se especifica en la siguiente línea.
- El comando para copiar todo al contenedor, publicar la aplicación y especificar el punto de entrada.
- El comando para instalar libgdiplus se ejecuta en el contenedor. Esto es requerido por System.Drawing.Common.

### Construyendo y Ejecutando la Aplicación en Docker

Ahora la aplicación puede ser construida y ejecutada en Docker. Abra su terminal de comandos favorita, cambie al directorio con la aplicación (carpeta donde se encuentran el archivo de solución y el Dockerfile) y ejecute el siguiente comando:

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

La primera vez que se ejecuta este comando puede tardar más tiempo, ya que Docker necesita descargar las imágenes requeridas. Una vez que el comando anterior se haya completado, ejecute el siguiente comando:

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

Preste atención al argumento de montaje, porque, como se mencionó anteriormente, una carpeta en la máquina host se monta en la carpeta del contenedor, para ver fácilmente los resultados de la ejecución de la aplicación. Las rutas en Linux distinguen entre mayúsculas y minúsculas.

{{% /alert %}}

## Imágenes que Soportan Aspose.Cells

- Aspose.Cells for .NET Standard no soporta EMF y TIFF en Linux.


## Más Ejemplos

***1. Para ejecutar la aplicación en Windows Server 2019***

- Dockerfile

{{< highlight plain >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

- Construir Imagen de Docker

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Ejecutar Imagen de Docker

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. Para ejecutar la aplicación en Linux***

- Escribir un programa simple que configure la carpeta de fuentes, cree un libro de trabajo de “¡Hola Mundo!” y lo guarde.

{{< highlight csharp >}}
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

{{< highlight plain >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.Fonts.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.Fonts.dll"]
{{< /highlight >}}

- Construir Imagen de Docker

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Ejecutar Imagen de Docker

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## Ver También

- [Instalar Docker Desktop en Windows](https://docs.docker.com/docker-for-windows/install/)
- [Instalar Docker Desktop en Mac](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- Opción [Cambiar a contenedores de Linux](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers)
- Información adicional sobre [.NET Core SDK](https://hub.docker.com/_/microsoft-dotnet-sdk)
{{< app/cells/assistant language="csharp" >}}
