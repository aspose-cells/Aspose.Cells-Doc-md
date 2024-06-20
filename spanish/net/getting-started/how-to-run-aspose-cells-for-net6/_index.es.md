---
title: Cómo ejecutar Aspose.Cells para .Net6
type: docs
description: "Cómo ejecutar Aspose.Cells para .Net6."
weight: 138
url: /es/net/how-to-run-aspose-cells-for-net6/
---

## Resumen

Para las plataformas .NET6 (o posterior), en comparación con plataformas anteriores (.netcore31 o antes), una diferencia importante es sobre la biblioteca gráfica. 
En este [Documento oficial de Microsoft](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), explica que para .NET6 o versiones posteriores la biblioteca gráfica "System.Drawing.Common" solo será compatible en Windows, y da recomendaciones para reemplazar la biblioteca gráfica.

Para el producto Apose.Cells, hemos realizado la evaluación y completado la migración de la biblioteca de gráficos. Utilizamos SkiaSharp en lugar de System.Drawing.Common en sistemas no Windows, como se sugiere en la documentación oficial de Microsoft. Tenga en cuenta que este cambio crítico entrará en vigor en Aspose.Cells 22.10.1 o posterior para .Net6.

Para .netcore31 o antes, por compatibilidad y estabilidad, actualmente seguimos utilizando la biblioteca gráfica "System.Drawing.Common". Las dependencias para .netcore31 o antes son las siguientes:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 5.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

## Ejecutar Aspose.Cells para .Net6 en Windows

Primero puedes crear una aplicación .net6 con VS2022, luego puedes elegir las siguientes opciones de instalación:

### Instalar a través de NuGet

1. Busca Aspose.Cells en NuGet: [Paquete NuGet Aspose.Cells for .NET](https://www.nuget.org/packages/Aspose.Cells/). 
También puedes instalar Aspose.Cells desde el administrador de paquetes NuGet en VS2022.

2. "SkiaSharp" o "System.Drawing.Common" se instalarán automáticamente como dependencia de Aspose.Cells 22.10.1 o posterior para plataformas .Net6, que dependen de la configuración "Sistema Operativo Destino" en tu proyecto.
- Establece el "Sistema Operativo Destino" en "Windows" para tu proyecto, utilizarás "System.Drawing.Common" como dependencia en tu sistema Windows para el proyecto .Net6. En esta configuración, el resultado del dibujo es más similar a .netcore31 o antes.
**![Configurar sistema operativo destino](TargetOS.png)**
- Establece el "Sistema Operativo Destino" en "Ninguno" u otras opciones para tu proyecto, utilizarás "SkiaSharp" como dependencia en tu sistema Windows para el proyecto .Net6. *Por favor, ten en cuenta que la versión que usa "SkiaSharp" como dependencia no admite la función de impresión en impresora.*

### Instalar a través de msi o DLL

1. [Descarga Aspose.Cells.msi o DLL](https://releases.aspose.com/cells/net/)

2. Abre el directorio de instalación o el directorio del DLL, luego selecciona el paso 3 o 4 a continuación:

3. localiza el subdirectorio "net6.0-windows", añade el Aspose.Cells.dll en él a tu aplicación .net6. Añade manualmente los siguientes paquetes NuGet a tu proyecto .net6:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages, 4.7.0.

De esta forma, utilizarás "System.Drawing.Common" como dependencia en tu sistema Windows para el proyecto .Net6. En esta configuración, el resultado del dibujo es más similar a .netcore31 o antes.

4. localiza el subdirectorio "net6.0", añade el Aspose.Cells.dll en él a tu aplicación .net6. Añade manualmente los siguientes paquetes NuGet a tu proyecto .net6:
- SkiaSharp, 2.88.6.
- System.Security.Cryptography.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages, 4.7.0.

De esta manera, usará "SkiaSharp" como una dependencia en su sistema Windows para el proyecto .Net6. *Por favor, tenga en cuenta que la versión que utiliza "SkiaSharp" como dependencia no admite la función de impresión a la impresora.*
## Ejecute Aspose.Cells para .Net6 en Linux

Consulte el método de instalación en Windows, solo puede seleccionar SkiaSharp como una dependencia de la biblioteca gráfica en el sistema Linux.

Debe realizar las siguientes operaciones adicionales para garantizar el uso adecuado de SkiaSharp en Linux:

1. Ejecute el siguiente comando en su Sistema Linux:
```
apt-get update && apt-get install -y libfontconfig1
```
O
```
apk update && apk add fontconfig 
```

2. Agregue los paquetes nuget "SkiaSharp.NativeAssets.Linux 2.88.6" a su proyecto .net6.

3. O puede optar por agregar los paquetes nuget "SkiaSharp.NativeAssets.Linux.NoDependencies 2.88.6" a su proyecto .net6, en lugar de los dos pasos anteriores.

### Ejemplo de Dockerfile para Ubuntu

1. Agregue los paquetes nuget "SkiaSharp.NativeAssets.Linux 2.88.6" a su proyecto .net6.

2. Utilice el siguiente Dockerfile:
{{< highlight plain >}}
# Ubuntu 20.04
FROM mcr.microsoft.com/dotnet/runtime:6.0-focal AS base
WORKDIR /app

# add "libfontconfig1" package if using "SkiaSharp.NativeAssets.Linux" in your project
# Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apt-get update && apt-get install -y libfontconfig1

# Copy fonts from local to docker
# For example, put a "fonts" folder in your project folder, and put the font files in it,
# then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build
WORKDIR /src
COPY ["Ubuntu_Docker.csproj", "."]
RUN dotnet restore "./Ubuntu_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Ubuntu_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ubuntu_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ubuntu_Docker.dll"]
{{< /highlight >}}

### Ejemplo de Dockerfile para Alpine

1. Agregue los paquetes nuget "SkiaSharp.NativeAssets.Linux 2.88.6" a su proyecto .net6.

2. Utilice el siguiente Dockerfile:
{{< highlight plain >}}
#Alpine 3.16
FROM mcr.microsoft.com/dotnet/runtime:6.0-alpine3.16 AS base
WORKDIR /app

# add "fontconfig" package if using "SkiaSharp.NativeAssets.Linux" in your project
# Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apk update && apk add fontconfig 

# Copy fonts from local to docker
# For example, put a "fonts" folder in your project folder, and put the font files in it,
# then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-alpine3.16 AS build
WORKDIR /src
COPY ["Alpine_Docker.csproj", "."]
RUN dotnet restore "./Alpine_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Alpine_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Alpine_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Alpine_Docker.dll"]
{{< /highlight >}}
