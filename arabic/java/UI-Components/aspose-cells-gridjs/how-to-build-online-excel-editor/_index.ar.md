---
title: كيفية تشغيل Aspose.Cells.GridJs في دوكر
type: docs
weight: 250
url: /ar/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs،دوكر
description: تقدم هذه المقالة شرحًا لكيفية تشغيل GridJs في دوكر لبناء محرر أو عارض إكسل على الإنترنت.
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

# دليل دوكر

## متطلبات قبلية

تأكد من أن لديك Docker مثبت على جهازك. يمكنك تنزيل وتثبيت Docker من [الموقع الرسمي لـ Docker](https://www.docker.com/get-started).

## الخطوة 1: إنشاء ملف Dockerfile

أنشئ ملفًا باسم `Dockerfile` في مجلد مشروعك [الدليل](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs). يجب أن يحتوي `Dockerfile` على تعليمات حول كيفية بناء الصورة الخاصة بك في Docker.

## الخطوة 2: كتابة Dockerfile لـ GridJs

إليك مثال [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile) لعرض GridJs مع تطبيق جافا:

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

## الخطوة 3: بناء صورة Docker
بناء صورة Docker: من الطرفية، نفذ الأمر التالي لبناء صورة Docker الخاصة بك:
```bash
docker build -t gridjs-demo-java .
```
يمكنك استبدال gridjs-demo-java باسم الصورة التي ترغب في إعطائها لـ Docker الخاص بك.

## الخطوة 4: تشغيل حاوية Docker
بمجرد إنشاء الصورة، يمكنك تشغيل حاوية باستخدام الأمر التالي:

```bash
docker run -d -p 8080:80   -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-java
```

أو ببساطة تشغيل العرض التوضيحي في وضع التجربة:


```bash
docker run -d -p 8080:80  --name gridjs-demo-container  gridjs-demo-java
```

شرح خيارات أمر تشغيل Docker
-د: تشغيل الحاوية في الوضع المنفصل (في الخلفية).
-p 8080: يربط منفذ 80 في الحاوية بمنفذ 8080 على الجهاز المضيف.
-v C:/path/to/license.txt:/app/license: ربط مسار ملف الترخيص على الجهاز المضيف بمسار الملف في الحاوية.
--name gridjs-demo-container: تعيين اسم للحاوية.

## الخطوة 5: التحقق من تشغيل الحاوية
للتحقق من تشغيل الحاوية الخاصة بك، استخدم الأمر التالي:

```bash
docker ps
```
سيقوم هذا الأمر بسرد جميع الحاويات الجارية. يجب أن ترى حاويتك مدرجة مع اسمها وحالتها.

## الخطوة 6: الوصول إلى التطبيق الويب

افتح متصفح ويب واذهب إلى ` http://localhost:8080/gridjsdemo/index`. يجب أن ترى تطبيقك يعمل.

## أوامر إضافية

### إيقاف الحاوية

لإيقاف حاوية جارية، استخدم الأمر التالي:

```bash
docker stop gridjs-demo-container
```

### إزالة حاوية
لإزالة حاوية متوقفة، استخدم الأمر التالي:

```bash
docker rm  gridjs-demo-container
```

### إزالة صورة
لإزالة صورة، استخدم الأمر التالي:

```bash
docker rmi gridjs-demo-java
```




