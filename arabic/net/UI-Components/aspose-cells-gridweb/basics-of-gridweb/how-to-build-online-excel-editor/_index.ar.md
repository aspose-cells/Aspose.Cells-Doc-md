---
title: كيفية تشغيل Aspose.Cells.GridWeb في دوكر
type: docs
weight: 250
url: /ar/net/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb، دوكر
description: يقدم هذا المقال كيفية تشغيل GridWeb في دوكر لبناء تطبيق محرر أو معاينة Excel عبر الإنترنت.
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

#دليل دوكر

## متطلبات قبلية

تأكد من تثبيت Docker على جهازك. يمكنك تنزيل وتثبيت Docker من [الموقع الرسمي لدوكر](https://www.docker.com/get-started).

## الخطوة 1: إنشاء ملف Dockerfile

أنشئ ملفًا بالاسم `Dockerfile` في [دليل المشروع](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/). يجب أن يحتوي `Dockerfile` على تعليمات حول كيفية بناء صورة Docker الخاصة بك.

## الخطوة 2: كتابة Dockerfile لـ GridWeb

فيما يلي [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/Dockerfile) عيني لعرض GridWeb مع تطبيق ASP.NET Core:

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

## الخطوة 3: بناء صورة Docker
قم ببناء صورة Docker: من الطرفية، قم بتنفيذ الأمر التالي لبناء صورة Docker الخاصة بك:
```bash
docker build -t gridweb-demo-net6 .
```
يمكنك استبدال gridweb-demo-net6 بالاسم الذي ترغب في منحه لصورة Docker الخاصة بك.

## الخطوة 4: تشغيل حاوية Docker
بمجرد بناء الصورة، يمكنك تشغيل حاوية باستخدام الأمر التالي:

```bash
docker run -d -p 24262:80 --name gridweb-demo-container  gridweb-demo-net6
```
شرح خيارات أمر تشغيل Docker
-d: تشغيل الحاوية في وضع منفصل (في الخلفية).
-p 24262:80: ربط المنفذ 80 في الحاوية بالمنفذ 24262 على جهاز المضيف.
--name gridweb-demo-container: قم بتعيين اسم للحاوية.

## الخطوة 5: التحقق من تشغيل الحاوية
للتحقق مما إذا كانت الحاوية الخاصة بك قيد التشغيل، استخدم الأمر التالي:

```bash
docker ps
```
سيتم إدراج جميع الحاويات الجارية. يجب أن ترى حاويتك مدرجة جنبًا إلى جنب مع اسمها وحالتها.

## الخطوة 6: الوصول إلى تطبيق الويب

افتح متصفح الويب وانتقل إلى `http://localhost:24262/`. يجب رؤية تطبيقك يعمل.

ستتعرف على دليل التطوير العام لـ GridWeb 

انقر [الديمو](http://localhost:24262/grid/index1 "الديمو") في الصفحة، يمكنك تنفيذ عملية تحرير لملف جدول البيانات.

## الأوامر الإضافية

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
docker rmi gridweb-demo-net6
```




