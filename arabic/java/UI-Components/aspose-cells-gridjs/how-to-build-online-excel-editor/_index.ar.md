---
title: كيفية تشغيل Aspose.Cells.GridJs في دوكر
type: docs
weight: 250
url: /ar/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs، دوكر
description: يقدم هذا المقال كيفية تشغيل GridJs في دوكر لإنشاء تطبيق محرر أو عارض لجداول البيانات عبر الإنترنت.
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

#دليل دوكر

## متطلبات قبلية

تأكد من تثبيت Docker على جهازك. يمكنك تنزيل وتثبيت Docker من [الموقع الرسمي لدوكر](https://www.docker.com/get-started).

## الخطوة 1: إنشاء ملف Dockerfile

أنشئ ملفًا يحمل اسم `Dockerfile` في مجلد مشروعك (https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs). يجب أن يحتوي `Dockerfile` على تعليمات حول كيفية بناء صورة دوكر الخاصة بك.

## الخطوة 2: كتابة ملف Dockerfile لـ GridJs

فيما يلي [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile) عينة لعرض GridJs مع تطبيق Java:

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

## الخطوة 3: بناء صورة Docker
قم ببناء صورة Docker: من الطرفية، قم بتنفيذ الأمر التالي لبناء صورة Docker الخاصة بك:
```bash
docker build -t gridjs-demo-java .
```
يمكنك استبدال gridjs-demo-java بالاسم الذي ترغب فيه لإعطاء صورة دوكر الخاصة بك.

## الخطوة 4: تشغيل حاوية Docker
بمجرد بناء الصورة، يمكنك تشغيل حاوية باستخدام الأمر التالي:

```bash
docker run -d -p 8080:80 --name gridjs-demo-container  gridjs-demo-java
```
شرح خيارات أمر تشغيل Docker
-d: تشغيل الحاوية في وضع منفصل (في الخلفية).
-p 8080:80: تعيين ميناء 80 في الحاوية إلى الميناء 8080 على جهاز المضيف.
--name gridjs-demo-container: تعيين اسم للحاوية.

## الخطوة 5: التحقق من تشغيل الحاوية
للتحقق مما إذا كانت الحاوية الخاصة بك قيد التشغيل، استخدم الأمر التالي:

```bash
docker ps
```
سيتم إدراج جميع الحاويات الجارية. يجب أن ترى حاويتك مدرجة جنبًا إلى جنب مع اسمها وحالتها.

## الخطوة 6: الوصول إلى تطبيق الويب

افتح متصفح الويب وانتقل إلى ` http://localhost:8080/gridjsdemo/index`. يجب أن ترى تطبيقك يعمل.

## الأوامر الإضافية

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




