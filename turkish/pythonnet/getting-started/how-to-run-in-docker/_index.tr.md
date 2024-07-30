---
title: Aspose.Cells i Docker da python via .NET olarak çalıştırma
type: docs
description: "Linux için Docker konteynerinde Aspose.Cells i çalıştırın"
weight: 140
url: /tr/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## Önsöz:

Gitgide daha fazla kullanıcı şirketimizin çeşitli ürünlerini Docker'da kullanıyor ve çeşitli sorunlarla karşılaşıyor. Bu makale, Debian Linux tabanlı bir Docker ortamında Aspose.Cells'i Python via .NET ile nasıl kullanacağınızı kısaca tanıtıyor.

## Örnek:

Kullanımı basit bir örnek ile açıklıyoruz. Bu durumda işlev çok açıktır, yalnızca aspose_test.py içinde Japonca metin içeren bir Excel dosyasını açar. Burada, temel görüntü olarak python:3.11 kullanıyoruz ve ilgili Docker dosyası aşağıdaki gibidir:

{{< highlight plain >}}
FROM python:3.11 AS base

# For drawing,e.g. convert to PDF
RUN apt-get update && apt-get install -y libgdiplus

# Install ICU version supported by .NET Core 3.1
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/i/icu/libicu70_70.1-2_amd64.deb
RUN dpkg -i libicu70_70.1-2_amd64.deb

RUN pip install -i aspose-cells-python
CMD ["python", "aspose_test.py"]
{{< /highlight >}}

Ardından, aşağıdaki komutu çalıştırdığımızda, sonucu elde ederiz:
- Docker İmajı Oluştur

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- Docker İmajını Çalıştır

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

- Not:

Çeşitli dilleri içeren Excel dosyalarını desteklemek için ICU kurmamız gerekmektedir. Python via .NET sarmalayıcısının .NET Core 3.1'e dayandığını göz önünde bulundurarak ve .NET Core 3.1'in ICU için belirli sürüm gereksinimleri olduğunu düşünerek, ICU'nun sürüm 70'i aşmaması gerektiğini belirtir bir sürümünü kurmamız gerekir.


## Ayrıca Bakınız

- [Windows'ta Docker Desktop Kurulumu](https://docs.docker.com/docker-for-windows/install/)
