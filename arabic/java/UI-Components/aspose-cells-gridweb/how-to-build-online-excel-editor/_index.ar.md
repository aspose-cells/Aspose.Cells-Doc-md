---
title: كيفية تشغيل Aspose.Cells.GridWeb لبناء محرر أو عارض جداول البيانات على الإنترنت في Docker
type: docs
weight: 250
url: /ar/java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb، Docker
description: يقدم هذا المقال كيفية تشغيل GridWeb في حاوية Docker لبناء محرر أو عارض ملفات إكسل عبر الإنترنت.
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

# دليل دوكر

## متطلبات قبلية

تأكد من أن لديك Docker مثبت على جهازك. يمكنك تنزيل وتثبيت Docker من [الموقع الرسمي لـ Docker](https://www.docker.com/get-started).

## الخطوة 1: إنشاء ملف Dockerfile

قم بإنشاء ملف باسم `Dockerfile` في [دليل](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/) مشروعك. يجب أن يحتوي `Dockerfile` على تعليمات حول كيفية بناء صورة Docker الخاصة بك.

## الخطوة 2: كتابة Dockerfile لـ GridWeb

إليك نموذج [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile) لعرض GridWeb مع تطبيق جافا:

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
# create [log dir](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridWeb/springboot3.3demo/src/main/resources/application.properties)
RUN mkdir -p /app/log
# create [cache dir](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridWeb/springboot3.3demo/src/main/resources/application.properties)
RUN mkdir -p /app/grid_cache

# RUN ls -l /app/
# run java application
CMD ["sh", "-c", "java $JAVA_OPTS -jar /app/app.jar"]

```

## الخطوة 3: بناء صورة Docker
بناء صورة Docker: من الطرفية، نفذ الأمر التالي لبناء صورة Docker الخاصة بك:
```bash
docker build -t gridweb-demo-java .
```
يمكنك استبدال gridweb-demo-java باسم تريد إعطاء الصورة الخاصة بك في Docker.

## الخطوة 4: تشغيل حاوية Docker
بمجرد إنشاء الصورة، يمكنك تشغيل حاوية باستخدام الأمر التالي:

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
شرح خيارات أمر تشغيل Docker
-د: تشغيل الحاوية في الوضع المنفصل (في الخلفية).
-p 8080:8080: ربط المنفذ 8080 في الحاوية إلى المنفذ 8080 على جهاز المضيف.
--name gridweb-demo-container: تعيين اسم للحاوية.

## الخطوة 5: التحقق من تشغيل الحاوية
للتحقق من تشغيل الحاوية الخاصة بك، استخدم الأمر التالي:

```bash
docker ps
```
سيقوم هذا الأمر بسرد جميع الحاويات الجارية. يجب أن ترى حاويتك مدرجة مع اسمها وحالتها.

## الخطوة 6: الوصول إلى التطبيق الويب

افتح متصفح ويب واذهب إلى `http://localhost:8080/gridwebdemo/index`. ينبغي أن ترى تطبيقك يعمل.



## أوامر إضافية

### إيقاف الحاوية

لإيقاف حاوية جارية، استخدم الأمر التالي:

```bash
docker stop gridweb-demo-container
```

### إزالة حاوية
لإزالة حاوية متوقفة، استخدم الأمر التالي:

```bash
docker rm  gridweb-demo-container
```

### إزالة صورة
لإزالة صورة، استخدم الأمر التالي:

```bash
docker rmi gridweb-demo-java
```




