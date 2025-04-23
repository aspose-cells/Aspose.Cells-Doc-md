---
title: Docker da Aspose.Cells for Java Nasıl Çalıştırılır
type: docs
description: Linux için Docker konteynerinde Aspose.Cells for Java çalıştırın.
weight: 139
url: /tr/java/how-to-run-aspose-cells-in-docker/
---

Mikrohizmetler, konteynerleştirme ile birleştirildiğinde, teknolojileri kolayca birleştirmeyi mümkün kılar. Docker, geliştirme yığınızda hangi teknolojinin olduğundan bağımsız olarak Aspose.Cells işlevselliğini kolayca entegre etmenize olanak tanır.

Eğer mikroservislere hedefleniyorsa veya yığınınızın ana teknolojisi .NET, C++ veya Java değilse, ancak Aspose.Cells işlevselliğine ihtiyacınız varsa veya yığınızda zaten Docker kullanıyorsanız, o zaman Docker konteynerinde Aspose.Cells for Java kullanımını düşünebilirsiniz.

## Önkoşullar

- Sisteminizde Docker'ın kurulu olması gerekir. 

## Java Uygulaması Oluşturun

Bu örnekte, basit bir xlsx dosyası oluşturan, kaydeden ve okuyan bir Java uygulaması oluşturursunuz. Uygulama daha sonra Docker'da derlenip çalıştırılabilir.

### Java Uygulaması Oluşturma

Aşağıdaki kodu kullanarak Eclipse'te Java Uygulamasını oluşturun. Bu örnekte, Aspose.Cells for Java ile yeni bir xlsx çalışma sayfası oluşturup adını ve hücre değerlerini ayarlayıp, ardından onları okuyup çıktılarını alıyoruz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "TestDocker.java" >}}

### Java Uygulamasını jar paketine dönüştürme

Aşağıdaki şekil Eclipse'in "Dışa Aktar" menüsünü kullanarak bir jar paketi oluşturmanın bir yolunu göstermektedir.

**![Eclipse kullanarak Jar Oluştur](MakeJar.png)**

Artık Aspose.Cells for Java kullanarak bir Java programı yazdık ve bir jar paketi elde ettik. Şimdi bir dockerfile yapacağız.

### Bir Dockerfile Yaplandırma

Bir sonraki adım, Dockerfile'ı oluşturmak ve yapılandırmaktır.

1. Dockerfile oluşturun ve jar paketinin yanına yerleştirin. Bu dosya adını uzantısız bırakın (varsayılan).
2. Dockerfile'da şunları belirtin:

{{< highlight plain >}}
   FROM williamyeh/java8:latest

   VOLUME /tmp

   ADD TestDocker.jar app.jar

   ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
{{< /highlight >}}

### Docker'da Uygulamanın Derlenmesi ve Çalıştırılması

Şimdi uygulama Docker'da derlenebilir ve çalıştırılabilir. Favori komut istemcinizde, Dockerfile'ın bulunduğu klasöre geçin ve aşağıdaki komutu çalıştırın:

{{< highlight plain >}}
docker build -t java-app .
{{< /highlight >}}

Yukarıdaki komutu çalıştırdıktan sonra, XLSX çalışma sayfasının çıktısını ve komut satırının sonucunu elde edersiniz. Bu noktada, bir Java programı Linux Docker'da başarıyla çalıştırılmış olacaktır.
{{< app/cells/assistant language="java" >}}
