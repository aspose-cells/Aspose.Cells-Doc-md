---
title: nasıl çalıştırılacağını Aspose.Cells.GridJs docker içinde
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs,docker
description: Bu makale GridJs i docker içinde çalıştırarak çevrimiçi bir excel düzenleyici veya görüntüleyici uygulaması oluşturmayı tanıtır.
aliases:
  - /net/aspose-cells-gridjs/docker/
  - /net/aspose-cells-gridjs/run-aspose-cells-gridjs-in-docker/
  - /net/aspose-cells-gridjs/run-gridjs-in-docker/
  - /net/aspose-cells-gridjs/how-to-build-online-excel-editor-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-spreadsheet-editor-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-excel-editor-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-online-excel-viewer-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-spreadsheet-viewer-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-excel-viewer-using-gridjs/
---

# Docker Kılavuzu

## Önkoşullar

Makinenize Docker'ın kurulduğundan emin olun. Docker'ı [resmi Docker web sitesinden](https://www.docker.com/get-started) indirip kurabilirsiniz.

## Adım 1: Bir Docker Dosyası Oluşturun

Projende `Dockerfile` adında bir dosya oluşturun [dizin](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/) içinde. `Dockerfile`, Docker imajınızı nasıl oluşturulacağına dair talimatlar içermelidir.

## Adım 2: GridJs için Dockerfile Oluşturma

İşte ASP.NET Core uygulamasıyla GridJs demosu için örnek bir [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Dockerfile):

```dockerfile
# Use the official .NET6.0 runtime as a parent image
FROM mcr.microsoft.com/dotnet/aspnet:6.0-focal AS base
WORKDIR /app  
EXPOSE 80 


# Use the official .NET6.0 SDK as build enviroment
FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build

WORKDIR /src  
#we shall use .net6.0 project
COPY ["gridjs-demo-.net6.csproj", "."]
RUN dotnet restore "./gridjs-demo-.net6.csproj"

# Copy everything else and build
COPY . .
WORKDIR "/src/."
RUN dotnet build "gridjs-demo-.net6.csproj" -c Release -o /app/build

# Publish the app
FROM build AS publish
RUN dotnet publish "gridjs-demo-.net6.csproj" -c Release -o /app/publish

# Final stage/image
FROM base AS final
WORKDIR /app
# if you want display better like in windows ,you need to install kinds of fonts in /usr/share/fonts/ 
# then the application can parse and render the fonts which is used in the spread sheet file
# here we don't provide extra fonts resource
# Install Fonts because the SDK image contains very few fonts. The command copies font files from local to docker image. Make sure you have a local “fonts” directory that contains all the fonts you need to install. In this example, the local “fonts” directory is put in the same directory as the Dockerfile.
# COPY fonts/* /usr/share/fonts/
# the basic file path which contains the spread sheet files 
RUN mkdir -p /app/wb
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache
# we provide some sample spread sheet files in demo 
COPY wb/*.xlsx /app/wb/

COPY --from=publish /app/publish .

# set the start command for the docker image 
ENTRYPOINT ["dotnet", "gridjs-demo-.net6.dll"]
```

## Adım 3: Docker İmajının Oluşturulması
Docker İmajının Oluşturulması: Terminalden, Docker imajınızı oluşturmak için aşağıdaki komutu çalıştırın:
```bash
docker build -t gridjs-demo-net6 .
```
docker imajınızı oluşturmak için aşağıdaki komutu çalıştırın:

## Adım 4: Docker Konteynerinin Çalıştırılması
İmaj oluşturulduktan sonra, aşağıdaki komutu kullanarak bir konteyner çalıştırabilirsiniz:

```bash
docker run -d -p 24262:80 --name gridjs-demo-container  gridjs-demo-net6
```
Docker Çalıştır Komutu Seçeneklerinin Açıklaması
-d: Konteyneri geri planda (detached modda) çalıştırın.
-p 24262:80: Konteynerdeki 80 numaralı limanı ana makinedeki 24262 numaralı limana eşleştirin.
--name gridjs-demo-container: Konteynere bir isim verin.

## Adım 5: Konteynerin Çalışıp Çalışmadığının Doğrulanması
Konteynerinizin çalışıp çalışmadığını kontrol etmek için aşağıdaki komutu kullanın:

```bash
docker ps
```
Bu tüm çalışan konteynerleri listeler. Konteynerinizin adı ve durumu ile birlikte listelendiğini görmelisiniz.

## Adım 6: Web Uygulamasına Erişim

Bir web tarayıcısı açın ve `http://localhost:24262/GridJs2/List` adresine gidin. Uygulamanızın çalıştığını görmelisiniz.

## Ek Komutlar

### Konteynerin Durdurulması

Çalışan bir konteyneri durdurmak için aşağıdaki komutu kullanın:

```bash
docker stop gridjs-demo-container
```

### Bir Konteyneri Kaldırma
Durdurulmuş bir konteyneri kaldırmak için aşağıdaki komutu kullanın:

```bash
docker rm  gridjs-demo-container
```

### Bir Görüntüyü Kaldırma
Bir görüntüyü kaldırmak için aşağıdaki komutu kullanın:

```bash
docker rmi gridjs-demo-net6
```




