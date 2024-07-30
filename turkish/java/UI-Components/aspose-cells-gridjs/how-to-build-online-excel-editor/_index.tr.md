---
title: nasıl çalıştırılacağını Aspose.Cells.GridJs docker içinde
type: docs
weight: 250
url: /tr/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs,docker
description: Bu makale GridJs i docker içinde çalıştırarak çevrimiçi bir excel düzenleyici veya görüntüleyici uygulaması oluşturmayı tanıtır.
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

Makinenize Docker'ın kurulduğundan emin olun. Docker'ı [resmi Docker web sitesinden](https://www.docker.com/get-started) indirip kurabilirsiniz.

## Adım 1: Bir Docker Dosyası Oluşturun

Projektnizde `Dockerfile` adında bir dosya oluşturun. `Dockerfile`, Docker görüntünüzü nasıl oluşturacağınıza dair talimatları içermelidir.

## Adım 2: GridJs için Dockerfile Oluşturma

İşte Java uygulamasıyla GridJS demosu için örnek bir [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile):

```dockerfile
# Use the jdk8 image
FROM eclipse/ubuntu_jdk8
WORKDIR /usr/src/app


# copy local Maven files to container
COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .
COPY src src

# build application with maven
RUN ./mvnw package -DskipTests

# Set the user
USER root

#RUN ls -l *

# copy the build output jar to container
COPY  target/*.jar /app/app.jar

# delete build source to reduce storage usage
RUN rm -rf target && rm -rf .mvn && rm -rf src
# web port
EXPOSE 8080
# if you want display better like in windows ,you need to install kinds of fonts in /usr/share/fonts/ 
# then the application can parse and render the fonts which is used in the spread sheet file
# here we don't provide extra fonts resource
# Install Fonts because the SDK image contains very few fonts. The command copies font files from local to docker image. Make sure you have a local “fonts” directory that contains all the fonts you need to install. In this example, the local “fonts” directory is put in the same directory as the Dockerfile.
# COPY fonts/* /usr/share/fonts/
# the basic file path which contains the spread sheet files 
RUN mkdir -p /app/wb
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache/streamcache
# we provide some sample spread sheet files in demo 
COPY wb/*.xlsx /app/wb/

# set the start command for the docker image 
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app/app.jar"]
```

## Adım 3: Docker İmajının Oluşturulması
Docker İmajının Oluşturulması: Terminalden, Docker imajınızı oluşturmak için aşağıdaki komutu çalıştırın:
```bash
docker build -t gridjs-demo-java .
```
gridjs-demo-java yerine Docker görüntünüze vermek istediğiniz ismi kullanabilirsiniz.

## Adım 4: Docker Konteynerinin Çalıştırılması
İmaj oluşturulduktan sonra, aşağıdaki komutu kullanarak bir konteyner çalıştırabilirsiniz:

```bash
docker run -d -p 8080:80 --name gridjs-demo-container  gridjs-demo-java
```
Docker Çalıştır Komutu Seçeneklerinin Açıklaması
-d: Konteyneri geri planda (detached modda) çalıştırın.
-p 8080:80: Konteynerdeki 80 portunu ana bilgisayarınızdaki 8080 porta eşleştirin.
--name gridjs-demo-container: Konteynere bir isim verin.

## Adım 5: Konteynerin Çalışıp Çalışmadığının Doğrulanması
Konteynerinizin çalışıp çalışmadığını kontrol etmek için aşağıdaki komutu kullanın:

```bash
docker ps
```
Bu tüm çalışan konteynerleri listeler. Konteynerinizin adı ve durumu ile birlikte listelendiğini görmelisiniz.

## Adım 6: Web Uygulamasına Erişim

Bir web tarayıcısı açın ve ` http://localhost:8080/gridjsdemo/index` adresine gidin. Uygulamanızın çalıştığını görmelisiniz.

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
docker rmi gridjs-demo-java
```




