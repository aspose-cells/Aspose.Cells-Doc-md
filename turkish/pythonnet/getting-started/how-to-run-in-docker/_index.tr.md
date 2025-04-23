---
title: Docker da Aspose.Cells for Python via .NET Çalıştırma
type: docs
description: "Linux için Docker konteynerinde Aspose.Cells çalıştırma"
weight: 140
url: /tr/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## Preface:

Daha fazla kullanıcı şirketimizin çeşitli ürünlerini Docker ortamında kullanıyor ve çeşitli sorunlarla karşılaşıyor. Bu makale, Debian Linux tabanlı bir Docker ortamında Aspose.Cells for Python via .NET'nin nasıl kullanılacağını kısaca tanıtacaktır.

## Örnek:

Kullanimı basit bir örnekle gösteriyoruz. Bu durumda, fonksiyonellik oldukça basit, yalnızca aspose_test.py dosyasındaki Japonca metin içeren bir Excel dosyasını açıyoruz. Burada, temel imaj olarak python:3.11 kullanıyoruz ve ilgili Dockerfile aşağıdaki gibidir:

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

Daha sonra, aşağıdaki komutu çalıştırdığımızda, nihai sonucu elde ediyoruz:
- Docker İmajı Oluştur

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- Docker İmajını Çalıştır

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

- Not:

Çeşitli diller içeren Excel dosyalarının açılışını desteklemek için ICU'yu kurmamız gerekiyor. Python via .NET bağlamasının .NET Core 3.1'e dayandığını ve .NET Core 3.1’in ICU için belirli sürüm gereksinimleri olduğunu göz önünde bulundurarak, sürüm 70'i aşmayan belirli bir ICU sürümünü kurmamız gerekiyor.


## Ayrıca Bakınız

- [Windows'ta Docker Desktop Kurulumu](https://docs.docker.com/docker-for-windows/install/)
