---
title: كيفية إصلاح استثناء Runtime  رأس Fontconfig فارغ
type: docs
weight: 50
url: /ar/java/how-to-fix-runtimeexception-fontconfig-head-is-null/
---

يحدث خطأ `java.lang.RuntimeException: Fontconfig head is null, check your fonts or fonts configuration` عندما لا تتمكن **Aspose.Cells for Java** من تحديد مواضع الخطوط المطلوبة على النظام. تعتمد Aspose.Cells على ملفات الخطوط للأعمال مثل التوليد PDF، ومعالجة الصور، وإدارة تخطيط الصفحات.

لحل هذه المشكلة، لديك بعض الخيارات:

## تشغيل في وضع Headless

نظرًا لأنه من المرجح أن تعمل في بيئة بدون واجهة، يجب تكوين Java للعمل في وضع **headless**. يسمح وضع headless لـ Java بالعمل بدون الحاجة للوصول إلى شاشة أو بيئة رسومية، وهو ضروري عند التشغيل في بيئات مثل Azure أو Docker.

يمكنك تمكين وضع headless عن طريق إضافة خاصية النظام التالية عند بدء تطبيق Java الخاص بك:

java

```bash
System.setProperty("java.awt.headless", "true");
```

أو تعيينها عبر سطر الأوامر عند تشغيل JVM:

```ini
-Djava.awt.headless=true
```

## تثبيت الخطوط الضرورية

إذا كنت تعمل في بيئة يمكنك فيها تثبيت الحزم، يمكنك تثبيت حزم الخطوط الأساسية لضمان توفر الخطوط الأساسية. لنظام Linux، يمكنك تثبيت حزم الخطوط مثل:

**ديبيان/أوبونتو**:

```bash
sudo apt-get install -y fontconfig ttf-dejavu
```

**ألبية** (للإعدادات المصغرة لـ Docker):

```bash
apk add --no-cache fontconfig ttf-dejavu
```

**ريد هات/سينتوس**:

```bash
sudo yum install -y fontconfig dejavu-sans-fonts
```

## مثال

إليك ملف Docker الخاص بـ Alpine مع تثبيت jdk17 فقط.

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

استخدم Docker مع Aspose.Cells for Java، ستحدث الاستثناءات التالية أثناء التحويل إلى PDF وصورة.

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

بعد إضافة حزمتَي `fontconfig` و `ttf-dejavu`، سيكون الأمر حسنًا أثناء التحويل إلى PDF وصورة.

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
