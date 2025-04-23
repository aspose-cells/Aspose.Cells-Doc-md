---
title: Aspose.Cells for Python via Java ü Gunicorn+Flask ortamında nasıl kullanılır
type: docs
weight: 40
url: /tr/python-java/aspose-cells-python-java-in-gunicorn-flask/
description: Bu bölüm, Aspose.Cells for Python via Java bileşenlerini ve diğer Excel Python işlem kütüphanelerini karşılaştırır.
keywords: Python Excel, Excel Python, Excel Python via Java, Python via Java Excel, Neden Aspose.Cells for Python via Java, Neden xlrd xlwt xlutils xlwings openpyxl xlswriter win32com DataNitro pandas değil.
---

{{% alert color="primary" %}}

Bu başlangıç konusu, geliştiricilerin Aspose.Cells for Python via Java kullanarak basit bir uygulama (Merhaba Dünya) oluşturabileceğini gösterir. Uygulama, belirli bir hücrede Merhaba Dünya yazısı ile Microsoft Excel dosyası oluşturur.

{{% /alert %}}



## **Tam ortam hazırlama**

Bu kılavuzun çalışma ortamı Ubuntu: 20.04'tür, gerçek durumunuza göre ayarlayabilirsiniz. Örneklerin düzgün çalışmasını sağlamak için ortamda bazı gerekli araçların kurulması gerekir. İşte işlemi tamamlamanıza yardımcı olacak kısa adım adım rehber. Lütfen bu sadece kaba bir rehberdir ve sisteminiz ve ihtiyaçlarınıza göre detaylar değişebilir.

### Python

Kurulmamışsa, aşağıdaki gibi yükleyin:
```
sudo apt install python3 python3-pip # Ubuntu/Debian
#sudo yum install python3 python3-pip # CentOS/RHEL
```
Sürüm Kontrolü
```
python3 --version
pip3 --version
```

### Java
Kurulmamışsa, aşağıdaki gibi yükleyin:
```
sudo apt install openjdk-11-jdk # Ubuntu/Debian
#sudo yum install java-17-openjdk # CentOS/RHEL
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
```
Sürüm Kontrolü
```
java -version
```

### virtualenv sanal ortam
Sanal ortam, ihtiyacınıza göre kurulur. Hem geliştirme hem de üretim ortamında proje bağımlılıklarını yönetmek için sanal ortamların kullanılması önerilir.
Lütfen kurulum için aşağıdaki komutu izleyin:
```
sudo apt install python3-venv # Ubuntu/Debian
#sudo yum install python3-venv # CentOS/RHEL
```
Sanal ortam oluşturun
```
python3 -m venv myenv # Create a virtual environment named myenv in the current directory
```
Sanal ortamı başlatın
```
source myenv/bin/activate
```

***Uyarı: Bir sanal ortam kullanılıyorsa, aşağıdaki işlemler ilk önce ilgili sanal ortamın aktif edilmesini gerektirir***

### Flask
Yüklenmediyse, lütfen yüklemek için aşağıdaki komutu izleyin:
```
pip install Flask
```

### Gunicorn
Yüklenmediyse, lütfen yüklemek için aşağıdaki komutu izleyin:
```
pip install gunicorn
```

### Jpype
Yüklenmediyse, lütfen yüklemek için aşağıdaki komutu izleyin:
```
pip install jpype1
```

### aspose-cells
Yüklenmediyse, lütfen yüklemek için aşağıdaki komutu izleyin:
```
pip install aspose-cells
```

## **Merhaba Dünya Uygulamasını Oluşturma**

Aspose.Cells API'sını kullanarak Merhaba Dünya uygulamasını oluşturmak için:

1. [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) sınıfının bir örneğini oluşturun.
1. Lisansı uygulayın:
   1. Bir lisans satın aldıysanız, uygulamanızda Aspose.Cells'in tam işlevselliğine erişmek için lisansı kullanın.
   1. Bileşenin değerlendirme sürümünü kullanıyorsanız (lisanssız Aspose.Cells kullanıyorsanız), bu adımı atlayın.
1. Yeni bir Microsoft Excel dosyası oluşturun veya belirli metinleri eklemek/güncellemek istediğiniz mevcut bir dosyayı açın.
1. Microsoft Excel dosyasının bir çalışma sayfasının herhangi bir hücresine erişin.
1. Erişilen bir hücreye **Merhaba Dünya!** kelimesini ekleyin.
1. Değiştirilmiş Microsoft Excel dosyasını oluşturun.

Aşağıdaki örnekler yukarıdaki adımları göstermektedir.

### **Bir Workbook Oluşturma**

Aşağıdaki örnek, sıfırdan yeni bir çalışma kitabı oluşturur, ilk çalışma sayfasındaki A1 hücresine "Merhaba Dünya!" yazıp dosyayı kaydeder.

Varsayalım ki bir test yolu "/app". Bu test yolu altında aşağıdaki çalışmaları tamamlayacağız.

#### Flask uygulama dosyaları: hello.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask1.py" >}}


#### Özel Gunicorn başlatma sınıfı dosyası: custom_gunicorn.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask2.py" >}}

#### Servisi başlat

Tüm gerekli paketlerin yüklü olduğunu doğrulayın, ardından servisi başlatın.

Python3-venv sanal ortamını kullanıyorsanız, test yolunda bir sanal ortam oluşturmanız, başlatmanız ve ardından tüm gerekli araç paketlerini yüklemeniz gerekir.

``` 
python custom_gunicorn.py Or python3 custom_gunicorn.py
``` 

#### Sonuçları kontrol edin

1 Tarayıcıyı açın ve http://127.0.0.1:5000/ adresini ziyaret edin.

2 Girmek istediğiniz dosya adını giriş kutusuna yazın.

3 'Generate' (Oluştur) düğmesine tıklayarak dosyayı kaydedin.

Bunu yaptıktan sonra, şu anda test yolu altında girdiğiniz içeriğe göre adlandırılmış bir Excel dosyası alacaksınız. Ön izleme etkisi aşağıdaki gibidir:

![todo:image_alt_text](HelloWorldFileInFlask.png)


## Docker Kullanımı

Veya yukarıdaki işlemleri bir docker konteynerine koyabilirsiniz. Örneği kullanmak için Docker'ı ortam oluşturma amacıyla çok basit bir şekilde kullanabilirsiniz. Sadece yukarıdaki işlemleri Dockerfile dosyasına yerleştirin.

İşte bir Dockerfile dosyası referans olarak. Gerekli bazı araç takımlarını listeler.

### Dockerfile

``` 
FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    openjdk-11-jdk \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python3", "custom_gunicorn.py"]
```

### requirements.txt

Bu dosya esas olarak Python projelerine bağımlılık ortamı sağlamak için kullanılır. Bu dosyadaki sürümü ihtiyaçlarınıza göre değiştirebilirsiniz.

```
aspose-cells==24.11.0
jpype1==1.5.1
Flask==3.0.3
gunicorn==23.0.0
```
### Ana dosyalar

Ana dosya yapısı şu şekildedir:
```
app/
|-requirements.txt
|-hello.py
|-custom_gunicorn.py
```

### Konteyneri başlat

Aşağıdaki komutu kullanarak konteyneri başlatabilirsiniz
```
docker run --rm -p 127.0.0.1:5000:5000 gunicorn_flask:v1.0 # gunicorn_flask:v1.0 - Image built by Dockerfile
```
