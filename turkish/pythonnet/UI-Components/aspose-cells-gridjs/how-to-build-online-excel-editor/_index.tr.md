---
title: Aspose.Cells.GridJs yi Docker da nasıl çalıştırılır
type: docs
weight: 250
url: /tr/python-net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs,docker
description: Bu makale, çevrimiçi excel düzenleyici veya görüntüleme uygulaması oluşturmak için GridJs yi Docker da nasıl çalıştıracağınızı tanıtıyor.
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

# Docker Kılavuzu

## Önkoşullar

Bilgisayarınıza Docker'ın yüklü olduğundan emin olun. Docker'ı [resmi Docker web sitesinden](https://www.docker.com/get-started) indirip yükleyebilirsiniz.

## Adım 1: Dockerfile Oluşturma

Proje [kök dizininize](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/blob/main/Examples_GridJs_Python_Net/) bir `Dockerfile` isimli dosya oluşturun. `Dockerfile`, Docker imajınızın nasıl oluşturulacağını anlatan talimatları içermelidir.

## Adım 2: GridJs için Dockerfile Yazma

İşte Python uygulamasıyla GridJs demo için örnek bir [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/blob/main/Examples_GridJs_Python_Net/Dockerfile):

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

## Adım 3: Docker Görüntüsünü Oluşturma
Docker Görüntüsü Oluşturma: Terminalden aşağıdaki komutu çalıştırarak Docker görüntünüzü oluşturabilirsiniz:
```bash
docker build -t gridjs-demo-python .
```
Docker görüntüsü yerine kendi istediğiniz adı verebilirsiniz, gridjs-demo-python yerine başka bir isim kullanabilirsiniz.

## Adım 4: Docker Konteyneri Çalıştırma
İmaj oluşturulduktan sonra aşağıdaki komutu kullanarak bir konteyner çalıştırabilirsiniz:

```bash
docker run -d -p 2022:2022   -v C:/path/to/license.txt:/app/license  --name gridjs-demo-container  gridjs-demo-python
```

veya sadece deneme modunda demo'yu çalıştırabilirsiniz:


```bash
docker run -d -p 2022:2022 --name gridjs-demo-container  gridjs-demo-python
```

Docker Run Komutu Seçeneklerinin Açıklaması
-d: Konteyneri arka planda çalıştırır.
-p 2022:2022: Konteynerdeki 2022 portunu ana makinedeki 2022 portuna bağlar.
-v C:/path/to/license.txt:/app/license: Lisans dosyasının yolunu ana makineden konteyner içindeki dosya yoluna eşler.
--name gridjs-demo-container: Konteynere bir isim atayın.

## Adım 5: Konteynerin Çalıştığını Doğrulama
Konteynerinizin çalışıp çalışmadığını kontrol etmek için aşağıdaki komutu kullanın:

```bash
docker ps
```
Bu, tüm çalışan konteynerleri listeleyecek. Adı ve durumu ile birlikte konteyneriniz görünmelidir.

## Adım 6: Web Uygulamasına Erişim

Bir web tarayıcısı açın ve `http://localhost:2022` adresine gidin. Uygulamanızın çalıştığını görmelisiniz.

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
docker rmi gridjs-demo-python
```




