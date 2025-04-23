---
title: Aspose.Cells.GridWeb i Docker da nasıl çalıştırılır
type: docs
weight: 250
url: /tr/net/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb,docker
description: Bu makale, Docker da GridWeb i çalıştırarak çevrimiçi excel düzenleyici veya görüntüleme uygulaması oluşturmayı anlatıyor.
aliases:
  - /net/aspose-cells-gridweb/docker/
  - /net/aspose-cells-gridweb/run-aspose-cells-gridweb-in-docker/
  - /net/aspose-cells-gridweb/run-gridweb-in-docker/
  - /net/aspose-cells-gridweb/how-to-build-online-excel-editor-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-spreadsheet-editor-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-excel-editor-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-online-excel-viewer-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-spreadsheet-viewer-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-excel-viewer-using-gridweb/
---

# Docker Kılavuzu

## Önkoşullar

Bilgisayarınıza Docker'ın yüklü olduğundan emin olun. Docker'ı [resmi Docker web sitesinden](https://www.docker.com/get-started) indirip yükleyebilirsiniz.

## Adım 1: Dockerfile Oluşturma

Proje dizininizde bir `Dockerfile` adlı dosya oluşturun. `Dockerfile` Docker imajınızı nasıl inşa edeceğinizi belirten talimatlar içermelidir. https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/

## Adım 2: GridWeb için Dockerfile yazın

İşte ASP.NET Core uygulamasıyla GridWeb demosu için örnek bir [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/Dockerfile):

```dockerfile
# Use the official .NET6.0 runtime as a parent image
FROM mcr.microsoft.com/dotnet/aspnet:6.0-focal AS base
WORKDIR /app  
EXPOSE 80 


# Use the official .NET6.0 SDK as build enviroment
FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build

WORKDIR /src  
#we shall use .net6.0 project
COPY ["GridWeb.Demo.NET6.0.csproj", "."]
RUN dotnet restore "./GridWeb.Demo.NET6.0.csproj"

# Copy everything else and build
COPY . .
WORKDIR "/src/."
RUN dotnet build "GridWeb.Demo.NET6.0.csproj" -c Release -o /app/build

# Publish the app
FROM build AS publish
RUN dotnet publish "GridWeb.Demo.NET6.0.csproj" -c Release -o /app/publish

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
# the cache file path for GridWeb
RUN mkdir -p /app/filecache
# the cache picture path for GridWeb
RUN mkdir -p /app/piccache
COPY wwwroot/wb/*.xlsx /app/wb/

COPY --from=publish /app/publish .

# set the start command for the docker image 
ENTRYPOINT ["dotnet", "GridWeb.Demo.NET6.0.dll"]
```

## Adım 3: Docker Görüntüsünü Oluşturma
Docker Görüntüsü Oluşturma: Terminalden aşağıdaki komutu çalıştırarak Docker görüntünüzü oluşturabilirsiniz:
```bash
docker build -t gridweb-demo-net6 .
```
docker görüntünüzü vermek istediğiniz isimle gridweb-demo-net6 yerine değiştirebilirsiniz.

## Adım 4: Docker Konteyneri Çalıştırma
İmaj oluşturulduktan sonra aşağıdaki komutu kullanarak bir konteyner çalıştırabilirsiniz:

```bash
docker run -d -p 24262:80 --name gridweb-demo-container  gridweb-demo-net6
```
Docker Run Komutu Seçeneklerinin Açıklaması
-d: Konteyneri arka planda çalıştırır.
-p 24262:80: Port 80'i konteynerde, 24262'de ana makinede eşler.
--name gridweb-demo-container: Konteynerin adını belirleyin.

## Adım 5: Konteynerin Çalıştığını Doğrulama
Konteynerinizin çalışıp çalışmadığını kontrol etmek için aşağıdaki komutu kullanın:

```bash
docker ps
```
Bu, tüm çalışan konteynerleri listeleyecek. Adı ve durumu ile birlikte konteyneriniz görünmelidir.

## Adım 6: Web Uygulamasına Erişim

Bir web tarayıcısı açın ve `http://localhost:24262/` adresine gidin. Uygulamanızın çalıştığını göreceksiniz.

GridWeb için genel geliştirme kılavuzunu göreceksiniz. 

Sayfadaki [demo](http://localhost:24262/grid/index1 "demo") bağlantısına tıklayın, elektronik tablo dosyası üzerinde düzenleme işlemi yapabilirsiniz.

## Ek Komutlar

### Konteyneri Durdurma

Çalışan bir konteyneri durdurmak için aşağıdaki komutu kullanın:

```bash
docker stop gridweb-demo-container
```

### Bir Konteyner Kaldırma
Durdurulmuş bir konteyneri kaldırmak için aşağıdaki komutu kullanın:

```bash
docker rm  gridweb-demo-container
```

### Bir İmaj Kaldırma
Bir imajı kaldırmak için aşağıdaki komutu kullanın:

```bash
docker rmi gridweb-demo-net6
```




