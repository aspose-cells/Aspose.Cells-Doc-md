---
title: كيفية تشغيل Aspose.Cells.GridJs في دوكر
type: docs
weight: 250
url: /ar/python-net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs،دوكر
description: تقدم هذه المقالة شرحًا لكيفية تشغيل GridJs في دوكر لبناء محرر أو عارض إكسل على الإنترنت.
aliases:
  - /python-net/aspose-cells-gridjs/docker/
  - /python-net/aspose-cells-gridjs/run-aspose-cells-gridjs-in-docker/
  - /python-net/aspose-cells-gridjs/run-gridjs-in-docker/
  - /python-net/aspose-cells-gridjs/how-to-build-online-excel-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-spreadsheet-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-excel-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-online-excel-viewer-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-spreadsheet-viewer-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-excel-viewer-using-gridjs/
---

# دليل دوكر

## متطلبات قبلية

تأكد من أن لديك Docker مثبت على جهازك. يمكنك تنزيل وتثبيت Docker من [الموقع الرسمي لـ Docker](https://www.docker.com/get-started).

## الخطوة 1: إنشاء ملف Dockerfile

قم بإنشاء ملف باسم `Dockerfile` في [دليل](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/blob/main/Examples_GridJs_Python_Net/) مشروعك. يجب أن يحتوي `Dockerfile` على تعليمات حول كيفية بناء صورة Docker الخاصة بك.

## الخطوة 2: كتابة Dockerfile لـ GridJs

إليك عينة [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/blob/main/Examples_GridJs_Python_Net/Dockerfile) لعرض تجريبي لـ GridJs مع تطبيق بايثون:

```dockerfile
# use Python 3.13 as parent image
FROM python:3.13-slim
# web port
EXPOSE 2022

# Update the package list and install the   package along with additional related packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libicu-dev \
        icu-devtools \
        pkg-config \
        build-essential \
	fontconfig \ 
        libgdiplus && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*

# Set the necessary environment variable  
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu
# Set the System.Globalization.Invariant setting to true
ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true

WORKDIR /app  

# copy all to  /app  
COPY . /app  


RUN pip install --no-cache-dir -r requirements.txt  
# the basic file path which contains the spread sheet files 
RUN mkdir -p /app/wb
# the file path to store the uploaded files
RUN mkdir -p /app/uploads
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache/  
COPY wb/*.xlsx /app/wb/



# start cmd
CMD [ "python", "./main.py" ]
```

## الخطوة 3: بناء صورة Docker
بناء صورة Docker: من الطرفية، نفذ الأمر التالي لبناء صورة Docker الخاصة بك:
```bash
docker build -t gridjs-demo-python .
```
يمكنك استبدال gridjs-demo-python باسم الصورة التي تريد إعطائها لـ Docker الخاص بك.

## الخطوة 4: تشغيل حاوية Docker
بمجرد إنشاء الصورة، يمكنك تشغيل حاوية باستخدام الأمر التالي:

```bash
docker run -d -p 2022:2022   -v C:/path/to/license.txt:/app/license  --name gridjs-demo-container  gridjs-demo-python
```

أو ببساطة تشغيل العرض التوضيحي في وضع التجربة:


```bash
docker run -d -p 2022:2022 --name gridjs-demo-container  gridjs-demo-python
```

شرح خيارات أمر تشغيل Docker
-د: تشغيل الحاوية في الوضع المنفصل (في الخلفية).
-p 2022:2022: ربط المنفذ 2022 في الحاوية إلى المنفذ 2022 على الجهاز المضيف.
-v C:/path/to/license.txt:/app/license: ربط مسار ملف الترخيص على الجهاز المضيف بمسار الملف في الحاوية.
--name gridjs-demo-container: تعيين اسم للحاوية.

## الخطوة 5: التحقق من تشغيل الحاوية
للتحقق من تشغيل الحاوية الخاصة بك، استخدم الأمر التالي:

```bash
docker ps
```
سيقوم هذا الأمر بسرد جميع الحاويات الجارية. يجب أن ترى حاويتك مدرجة مع اسمها وحالتها.

## الخطوة 6: الوصول إلى التطبيق الويب

افتح متصفح ويب واذهب إلى `http://localhost:2022`. يجب أن ترى تطبيقك يعمل.

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
docker rmi gridjs-demo-python
```




