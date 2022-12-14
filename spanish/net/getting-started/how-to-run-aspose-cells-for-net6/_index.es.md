---
title: Cómo ejecutar Aspose.Cells para .Net6
type: docs
description: Cómo ejecutar Aspose.Cells para .Net6
weight: 138
url: /es/net/how-to-run-aspose-cells-for-net6/
---
## Visión general

 Para las plataformas .NET6 (o posteriores), en comparación con las plataformas anteriores (.netcore31 o anteriores), una diferencia importante es la biblioteca de gráficos.
 En este oficial[Microsoft Documento](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), explica que para .NET6 o versiones posteriores, la biblioteca de gráficos "System.Drawing.Common" solo se admitirá en Windows y brinda recomendaciones para reemplazar la biblioteca de gráficos.

Para el producto Apose.Cells, realizamos la evaluación y completamos la migración de la biblioteca de gráficos. Usamos SkiaSharp en lugar de System.Drawing.Common en sistemas que no son Windows, como se sugiere en la documentación oficial de Microsoft. Tenga en cuenta que este cambio crítico entrará en vigencia en Aspose.Cells 22.10.1 o posterior para .Net6.

Para .netcore31 o anterior, por compatibilidad y estabilidad, actualmente todavía usamos la biblioteca de gráficos "System.Drawing.Common". Las dependencias para .netcore31 o anterior son las siguientes:
- Sistema.Dibujo.Común, 4.7.0.
- Sistema.Seguridad.Criptografía.Pkcs, 5.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

## Ejecute Aspose.Cells para .Net6 en Windows

Primero puede crear una aplicación .net6 con VS2022, luego puede elegir las siguientes opciones de instalación:

### Instalar a través de nuget

1.  Buscar Aspose.Cells desde NuGet:[Aspose.Cells for .NET NuGet Paquete](https://www.nuget.org/packages/Aspose.Cells/). 
También puede instalar Aspose.Cells desde el administrador de paquetes Nuget en VS2022.

2. "SkiaSharp" o "System.Drawing.Common" se instalarán automáticamente como una dependencia de Aspose.Cells 22.10.1 o posterior para plataformas .Net6, que depende de la configuración de "Target OS" en su proyecto.
- Establezca el "SO de destino" en "Windows" para su proyecto, utilizará "System.Drawing.Common" como una dependencia en su sistema de Windows para el proyecto .Net6. En esta configuración, el resultado del dibujo se acerca más a .netcore31 o antes.
**![Configurar sistema operativo de destino](TargetOS.png)**
- Establezca el "SO de destino" en "Ninguno" u otras opciones para su proyecto, utilizará "SkiaSharp" como una dependencia en su sistema de Windows para el proyecto .Net6. Tenga en cuenta que actualmente SkiaSharp no admite formatos como EMF en Windows.

### Instalar a través de msi o DLL

1. [Descargar Aspose.Cells.msi o DLL](https://releases.aspose.com/cells/net/)

2. Abra el directorio de instalación o el directorio DLL, luego seleccione el paso 3 o 4 a continuación:

3. Localice el subdirectorio "net6.0-windows", agregue Aspose.Cells.dll a su aplicación .net6. Agregue manualmente los siguientes paquetes nuget a su proyecto .net6:
- Sistema.Dibujo.Común, 4.7.0.
- Sistema.Seguridad.Criptografía.Pkcs, 6.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

De esta manera, usará "System.Drawing.Common" como una dependencia en su sistema de Windows para el proyecto .Net6. En esta configuración, el resultado del dibujo se acerca más a .netcore31 o antes.

4. Localice el subdirectorio "net6.0", agregue Aspose.Cells.dll a su aplicación .net6. Agregue manualmente los siguientes paquetes nuget a su proyecto .net6:
- SkiaSharp, 2.88.3.
- Sistema.Seguridad.Criptografía.Pkcs, 6.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

De esta forma, usará "SkiaSharp" como una dependencia en su sistema Windows para el proyecto .Net6. Tenga en cuenta que actualmente SkiaSharp no admite formatos como EMF en Windows.

## Ejecute Aspose.Cells para .Net6 en Linux

Consulte el método de instalación en Windows, solo puede seleccionar SkiaSharp como dependencia de la biblioteca de gráficos en el sistema Linux.

Debe realizar las siguientes operaciones adicionales para garantizar el uso adecuado de SkiaSharp en Linux:

1. Ejecute el siguiente comando en su sistema Linux:
```
apt-get update && apt-get install -y libfontconfig1
```
O
```
apk update && apk add fontconfig 
```

2. Agregue los paquetes nuget "SkiaSharp.NativeAssets.Linux 2.88.3" a su proyecto .net6.

3. O puede optar por agregar nuget paquetes "SkiaSharp.NativeAssets.Linux.NoDependencies 2.88.3" a su proyecto .net6, en lugar de los dos pasos anteriores.

### Ejemplo de Dockerfile para Ubuntu

1. Agregue los paquetes nuget "SkiaSharp.NativeAssets.Linux 2.88.3" a su proyecto .net6.

2. Use el siguiente Dockerfile:
{{< highlight "plain" >}}
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
COPY ["Ubuntu_Docker.csproj", "."]RUN dotnet restore "./Ubuntu_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Ubuntu_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ubuntu_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ubuntu_Docker.dll"]{{< /highlight >}}

### Ejemplo de Dockerfile para Alpine

1. Agregue los paquetes nuget "SkiaSharp.NativeAssets.Linux 2.88.3" a su proyecto .net6.

2. Use el siguiente Dockerfile:
{{< highlight "plain" >}}
# Alpine 3.16
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
COPY ["Alpine_Docker.csproj", "."]RUN dotnet restore "./Alpine_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Alpine_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Alpine_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Alpine_Docker.dll"]{{< /highlight >}}
