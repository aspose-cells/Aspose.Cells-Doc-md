---
title: RuntimeException  Fontconfig başlığı null nasıl düzeltilir
type: docs
weight: 50
url: /tr/java/how-to-fix-runtimeexception-fontconfig-head-is-null/
---

`java.lang.RuntimeException: Fontconfig head is null, check your fonts or fonts configuration` hatası, **Aspose.Cells for Java** sistemde gerekli fontları bulamadığında oluşur. Aspose.Cells, PDF oluşturma, görsel işleme ve sayfa düzeni işlemleri gibi işlemler için font dosyalarına dayanır.

Bu sorunu çözmek için birkaç seçeneğiniz var:

## Headless Modda Çalıştırma

Muhtemelen headless bir ortamda çalışıyorsunuz, bu nedenle Java'yı **headless modda** çalıştıracak şekilde yapılandırmalısınız. Headless mod, Java'nın bir ekran veya grafik ortamına erişimi olmadan çalışmasına izin verir ve Azure veya Docker gibi ortamlar için önemlidir.

Headless modu etkinleştirmek için, Java uygulamanızın başlangıcına aşağıdaki sistem özelliğini ekleyebilirsiniz:

java

```bash
System.setProperty("java.awt.headless", "true");
```

Veya JVM başlatırken komut satırından ayarlayabilirsiniz:

```ini
-Djava.awt.headless=true
```

## Gerekli Yazı tiplerini Kurma

Bir paket yükleyebileceğiniz bir ortamda çalışıyorsanız, temel yazı tiplerinin erişilebilir olmasını sağlamak için font paketleri kurabilirsiniz. Linux sistemleri için şu font paketlerini yükleyebilirsiniz:

**Debian/Ubuntu**:

```bash
sudo apt-get install -y fontconfig ttf-dejavu
```

**Alpine** (minimal Docker kurulumu için):

```bash
apk add --no-cache fontconfig ttf-dejavu
```

**Red Hat/CentOS**:

```bash
sudo yum install -y fontconfig dejavu-sans-fonts
```

## Örnek

Burada, sadece jdk17'nin yüklü olduğu bir Alpine Dockerfile örneği yer almaktadır.

```dockerfile
# Start with the bare Alpine base image
FROM alpine:latest

# Set environment variables for Java
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk \
    PATH=$JAVA_HOME/bin:$PATH

# Install only the minimal OpenJDK 17 package
RUN apk add --no-cache openjdk17-jdk \
    && java -version
```

Aspose.Cells for Java ile Docker kullanın; bu, PDF ve görsellere dönüştürürken aşağıdaki istisnalarla karşılaşacaktır.

```text
Caused by: java.lang.RuntimeException: Fontconfig head is null, check your fonts or fonts configuration
    at java.desktop/sun.awt.FontConfiguration.getVersion(FontConfiguration.java:1271)
    at java.desktop/sun.awt.FontConfiguration.readFontConfigFile(FontConfiguration.java:224)
    at java.desktop/sun.awt.FontConfiguration.init(FontConfiguration.java:106)
    at java.desktop/sun.awt.X11FontManager.createFontConfiguration(X11FontManager.java:706)
    at java.desktop/sun.font.SunFontManager$2.run(SunFontManager.java:358)
    at java.desktop/sun.font.SunFontManager$2.run(SunFontManager.java:315)
    at java.base/java.security.AccessController.doPrivileged(AccessController.java:318)
    at java.desktop/sun.font.SunFontManager.<init>(SunFontManager.java:315)
    at java.desktop/sun.awt.FcFontManager.<init>(FcFontManager.java:35)
    at java.desktop/sun.awt.X11FontManager.<init>(X11FontManager.java:56)
    ... 33 more
```

`fontconfig` ve `ttf-dejavu` paketlerini ekledikten sonra, PDF ve görsel oluşturma işlemleri sorunsuz olacaktır.

```dockerfile
# Start with the bare Alpine base image
FROM alpine:latest

# Set environment variables for Java
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk \
    PATH=$JAVA_HOME/bin:$PATH

# Install only the minimal OpenJDK 17 package
RUN apk add --no-cache openjdk17-jdk \
    && java -version

# Install fontconfig and ttf-dejavu packages to fix RuntimeException: Fontconfig head is null
RUN apk add --no-cache fontconfig ttf-dejavu \
    && fc-cache -f -v
```

{{< app/cells/assistant language="java" >}}
