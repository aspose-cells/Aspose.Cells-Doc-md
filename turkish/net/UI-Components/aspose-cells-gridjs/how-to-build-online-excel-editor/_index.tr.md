---
title: Aspose.Cells.GridJs yi Docker da nasıl çalıştırılır
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs,docker
description: Bu makale, çevrimiçi excel düzenleyici veya görüntüleme uygulaması oluşturmak için GridJs yi Docker da nasıl çalıştıracağınızı tanıtıyor.
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

Bilgisayarınıza Docker'ın yüklü olduğundan emin olun. Docker'ı [resmi Docker web sitesinden](https://www.docker.com/get-started) indirip yükleyebilirsiniz.

## Adım 1: Dockerfile Oluşturma

Proje [klasörünüzde](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/) `Dockerfile` adlı bir dosya oluşturun. `Dockerfile` Docker görüntünüzü nasıl oluşturacağınızı talimatlar içermelidir.

## Adım 2: GridJs için Dockerfile Yazma

İşte ASP.NET Core uygulamasıyla GridJs demo'su için örnek [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Dockerfile):

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
# the file path to store the uploaded files
RUN mkdir -p /app/uploads
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache
# we provide some sample spread sheet files in demo 
COPY wb/*.xlsx /app/wb/

COPY --from=publish /app/publish .

# set the start command for the docker image 
ENTRYPOINT ["dotnet", "gridjs-demo-.net6.dll"]
```

## Adım 3: Docker Görüntüsünü Oluşturma
Docker Görüntüsü Oluşturma: Terminalden aşağıdaki komutu çalıştırarak Docker görüntünüzü oluşturabilirsiniz:
```bash
docker build -t gridjs-demo-net6 .
```
docker image adını, örneğin gridjs-demo-net6, istediğiniz gibi değiştirebilirsiniz.

## Adım 4: Docker Konteyneri Çalıştırma
İmaj oluşturulduktan sonra aşağıdaki komutu kullanarak bir konteyner çalıştırabilirsiniz:

```bash
docker run -d -p 24262:80 -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-net6
```

veya sadece deneme modunda demo'yu çalıştırabilirsiniz:


```bash
docker run -d -p 24262:80 --name gridjs-demo-container  gridjs-demo-net6
```


Docker Run Komutu Seçeneklerinin Açıklaması
-d: Konteyneri arka planda çalıştırır.
-p 24262:80: Port 80'i konteynerde, 24262'de ana makinede eşler.
-v C:/path/to/license.txt:/app/license: Lisans dosyasının yolunu ana makineden konteyner içindeki dosya yoluna eşler.
--name gridjs-demo-container: Konteynere bir isim atayın.

## Adım 5: Konteynerin Çalıştığını Doğrulama
Konteynerinizin çalışıp çalışmadığını kontrol etmek için aşağıdaki komutu kullanın:

```bash
docker ps
```
Bu, tüm çalışan konteynerleri listeleyecek. Adı ve durumu ile birlikte konteyneriniz görünmelidir.

## Adım 6: Web Uygulamasına Erişim

Bir web tarayıcısı açın ve `http://localhost:24262/GridJs2/List` adresine gidin. Uygulamanızın çalıştığını görmelisiniz.

## Ek Komutlar

### Konteyneri Durdurma

Çalışan bir konteyneri durdurmak için aşağıdaki komutu kullanın:

```bash
docker stop gridjs-demo-container
```

### Bir Konteyner Kaldırma
Durdurulmuş bir konteyneri kaldırmak için aşağıdaki komutu kullanın:

```bash
docker rm  gridjs-demo-container
```

### Bir İmaj Kaldırma
Bir imajı kaldırmak için aşağıdaki komutu kullanın:

```bash
docker rmi gridjs-demo-net6
```




