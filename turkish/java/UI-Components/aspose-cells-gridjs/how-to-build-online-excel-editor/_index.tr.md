---
title: Aspose.Cells.GridJs yi Docker da nasıl çalıştırılır
type: docs
weight: 250
url: /tr/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs,docker
description: Bu makale, çevrimiçi excel düzenleyici veya görüntüleme uygulaması oluşturmak için GridJs yi Docker da nasıl çalıştıracağınızı tanıtıyor.
aliases:
  - /java/aspose-cells-gridjs/docker/
  - /java/aspose-cells-gridjs/run-aspose-cells-gridjs-in-docker/
  - /java/aspose-cells-gridjs/run-gridjs-in-docker/
  - /java/aspose-cells-gridjs/how-to-build-online-excel-editor-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-web-spreadsheet-editor-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-web-excel-editor-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-online-excel-viewer-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-web-spreadsheet-viewer-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-web-excel-viewer-using-gridjs/
---

# Docker Kılavuzu

## Önkoşullar

Bilgisayarınıza Docker'ın yüklü olduğundan emin olun. Docker'ı [resmi Docker web sitesinden](https://www.docker.com/get-started) indirip yükleyebilirsiniz.

## Adım 1: Dockerfile Oluşturma

Proje dizininize `Dockerfile` adında bir dosya oluşturun. `Dockerfile`, Docker görüntünüzü nasıl oluşturacağınıza dair talimatlar içermelidir.

## Adım 2: GridJs için Dockerfile Yazma

İşte Java uygulamasıyla GridJs demo için örnek [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile):

```dockerfile
# Use the maven image to build jar file
FROM maven:3.8.6-amazoncorretto-17 AS build
WORKDIR /usr/src/app


# copy local Maven files to container
COPY .mvn .mvn
COPY pom.xml .
COPY src src

# build application with maven
RUN mvn  package -DskipTests


# Use the jdk8 image as the basic docker image
FROM eclipse/ubuntu_jdk8
WORKDIR /app
# copy build jar file to target container 
COPY --from=build /usr/src/app/target/*.jar /app/app.jar

# web port
EXPOSE 8080
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
RUN mkdir -p /app/grid_cache/streamcache
# we provide some sample spread sheet files in demo 
COPY wb/*.xlsx /app/wb/

# set the start command for the docker image 
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app/app.jar"]
```

## Adım 3: Docker Görüntüsünü Oluşturma
Docker Görüntüsü Oluşturma: Terminalden aşağıdaki komutu çalıştırarak Docker görüntünüzü oluşturabilirsiniz:
```bash
docker build -t gridjs-demo-java .
```
docker build komutunu kullanarak gridjs-demo-java yerine kendi istediğiniz adı verebilirsiniz.

## Adım 4: Docker Konteyneri Çalıştırma
İmaj oluşturulduktan sonra aşağıdaki komutu kullanarak bir konteyner çalıştırabilirsiniz:

```bash
docker run -d -p 8080:80   -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-java
```

veya sadece deneme modunda demo'yu çalıştırabilirsiniz:


```bash
docker run -d -p 8080:80  --name gridjs-demo-container  gridjs-demo-java
```

Docker Run Komutu Seçeneklerinin Açıklaması
-d: Konteyneri arka planda çalıştırır.
-p 8080:80: Konteynerdeki 80 portunu ana makinedeki 8080 portuna yönlendir.
-v C:/path/to/license.txt:/app/license: Lisans dosyasının yolunu ana makineden konteyner içindeki dosya yoluna eşler.
--name gridjs-demo-container: Konteynere bir isim atayın.

## Adım 5: Konteynerin Çalıştığını Doğrulama
Konteynerinizin çalışıp çalışmadığını kontrol etmek için aşağıdaki komutu kullanın:

```bash
docker ps
```
Bu, tüm çalışan konteynerleri listeleyecek. Adı ve durumu ile birlikte konteyneriniz görünmelidir.

## Adım 6: Web Uygulamasına Erişim

Bir web tarayıcısı açın ve `http://localhost:8080/gridjsdemo/index` adresine gidin. Uygulamanızın çalıştığını görmelisiniz.

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
docker rmi gridjs-demo-java
```




