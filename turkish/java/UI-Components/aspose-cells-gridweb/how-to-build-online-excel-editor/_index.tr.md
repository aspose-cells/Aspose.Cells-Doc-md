---
title: Aspose.Cells.GridWeb ı nasıl çalıştıracağınızı ve çevrimiçi elektronik tablo düzenleyicisi veya görüntüleyici uygulamasını nasıl oluşturacağınızı gösterir.
type: docs
weight: 250
url: /tr/java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb, docker
description: Bu makale, çevrimiçi bir excel düzenleyici veya görüntüleyici uygulaması oluşturmak için GridWeb ı docker içinde nasıl çalıştıracağınızı tanıtır.
aliases:
  - /java/aspose-cells-gridweb/docker/
  - /java/aspose-cells-gridweb/run-aspose-cells-gridweb-in-docker/
  - /java/aspose-cells-gridweb/run-gridweb-in-docker/
  - /java/aspose-cells-gridweb/how-to-build-online-excel-editor-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-web-spreadsheet-editor-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-web-excel-editor-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-online-excel-viewer-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-web-spreadsheet-viewer-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-web-excel-viewer-using-gridweb/
---

# Docker Kılavuzu

## Önkoşullar

Makinenize Docker'ın kurulduğundan emin olun. Docker'ı [resmi Docker web sitesinden](https://www.docker.com/get-started) indirip kurabilirsiniz.

## Adım 1: Bir Docker Dosyası Oluşturun

Projedeki [dizin] (https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/) içinde `Dockerfile` adında bir dosya oluşturun. `Dockerfile`, Docker imajınızı nasıl oluşturulacağına dair talimatlar içermelidir.

## Adım 2: GridWeb için Dockerfile Yazın

İşte GridWeb demo için Java uygulamasıyla birlikte bir örnek [`Dockerfile`] (https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile):

```dockerfile
#spring boot3.3 shall use jdk17 above 
FROM openjdk:17-jdk-slim  AS build

# set work dir
WORKDIR /usr/src/app

# copy with maven
COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .
COPY src src

RUN chmod +x mvnw
# build with maven
RUN ./mvnw package -DskipTests


RUN ls -l target

# Stage 2: Create the final image
FROM openjdk:17-jdk-slim

# Set the working directory in the container
WORKDIR /app

# Copy the built JAR file from the build stage
COPY --from=build /usr/src/app/target/*.jar /app/app.jar

# web port
EXPOSE 8080
# Install Fonts because the SDK image contains very few fonts. The command copies font files from local to docker image. Make sure you have a local “fonts” directory that contains all the fonts you need to install. In this example, the local “fonts” directory is put in the same directory as the Dockerfile.
# COPY fonts/* /usr/share/fonts/

# Install necessary dependencies for font management,because we use jdk-slim ,we need to install it
RUN apt-get update && apt-get install -y fontconfig libfreetype6 && rm -rf /var/lib/apt/lists/*

# Set the environment variable for headless mode,no need to use display
ENV JAVA_OPTS="-Djava.awt.headless=true"
# create [log dir](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Examples.GridWeb/springboot3.3demo/src/main/resources/application.properties)
RUN mkdir -p /app/log
# create [cache dir](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Examples.GridWeb/springboot3.3demo/src/main/resources/application.properties)
RUN mkdir -p /app/grid_cache

# RUN ls -l /app/
# run java application
CMD ["sh", "-c", "java $JAVA_OPTS -jar /app/app.jar"]

```

## Adım 3: Docker İmajının Oluşturulması
Docker İmajının Oluşturulması: Terminalden, Docker imajınızı oluşturmak için aşağıdaki komutu çalıştırın:
```bash
docker build -t gridweb-demo-java .
```
gridweb-demo-java'yı Docker imajınıza vermek istediğiniz isimle değiştirebilirsiniz.

## Adım 4: Docker Konteynerinin Çalıştırılması
İmaj oluşturulduktan sonra, aşağıdaki komutu kullanarak bir konteyner çalıştırabilirsiniz:

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
Docker Çalıştır Komutu Seçeneklerinin Açıklaması
-d: Konteyneri geri planda (detached modda) çalıştırın.
-p 8080:8080: Konteynerdeki 8080 bağlantı noktasını ana makinedeki 8080 bağlantı noktasına eşleştirin.
--name gridweb-demo-container: Konteynere bir ad atayın.

## Adım 5: Konteynerin Çalışıp Çalışmadığının Doğrulanması
Konteynerinizin çalışıp çalışmadığını kontrol etmek için aşağıdaki komutu kullanın:

```bash
docker ps
```
Bu tüm çalışan konteynerleri listeler. Konteynerinizin adı ve durumu ile birlikte listelendiğini görmelisiniz.

## Adım 6: Web Uygulamasına Erişim

Bir web tarayıcısı açın ve `http://localhost:8080/gridwebdemo/index` adresine gidin. Uygulamanızın çalıştığını görmelisiniz.



## Ek Komutlar

### Konteynerin Durdurulması

Çalışan bir konteyneri durdurmak için aşağıdaki komutu kullanın:

```bash
docker stop gridweb-demo-container
```

### Bir Konteyneri Kaldırma
Durdurulmuş bir konteyneri kaldırmak için aşağıdaki komutu kullanın:

```bash
docker rm  gridweb-demo-container
```

### Bir Görüntüyü Kaldırma
Bir görüntüyü kaldırmak için aşağıdaki komutu kullanın:

```bash
docker rmi gridweb-demo-java
```




