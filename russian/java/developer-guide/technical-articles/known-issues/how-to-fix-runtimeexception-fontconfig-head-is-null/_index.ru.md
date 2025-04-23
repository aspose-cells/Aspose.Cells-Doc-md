---
title: Как исправить RuntimeException  Fontconfig head is null
type: docs
weight: 50
url: /ru/java/how-to-fix-runtimeexception-fontconfig-head-is-null/
---

Ошибка `java.lang.RuntimeException: Fontconfig head is null, check your fonts or fonts configuration` возникает, когда **Aspose.Cells for Java** не может найти необходимые шрифты в системе. Aspose.Cells полагается на файлы шрифтов для рендеринга и обработки таких операций, как создание PDF, отображение изображений и обработка компоновки страниц.

Чтобы решить эту проблему, у вас есть несколько вариантов:

## Запуск в безголовом режиме

Поскольку, вероятно, вы работаете в безголовой среде, необходимо настроить Java на работу в **безголовом режиме**. Безголовый режим позволяет Java работать без доступа к дисплею или графической среде, что важно при запуске в таких средах, как Azure или Docker.

Вы можете включить безголовый режим, добавив следующую системную свойство в начале вашего Java-приложения:

java

```bash
System.setProperty("java.awt.headless", "true");
```

Или установите его через командную строку при запуске JVM:

```ini
-Djava.awt.headless=true
```

## Установка необходимых шрифтов

Если вы работаете в среде, где можете устанавливать пакеты, вы можете установить соответствующие шрифтовые пакеты, чтобы обеспечить наличие основных шрифтов. Для систем Linux можно установить такие пакеты, как:

**Debian/Ubuntu**:

```bash
sudo apt-get install -y fontconfig ttf-dejavu
```

**Alpine** (для минимальных Docker-настроек):

```bash
apk add --no-cache fontconfig ttf-dejavu
```

**Red Hat/CentOS**:

```bash
sudo yum install -y fontconfig dejavu-sans-fonts
```

## Пример

Вот Dockerfile Alpine с установленным только JDK 17.

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

Используйте Docker с образом Aspose.Cells for Java, при рендеринге в PDF и изображение возникнет следующая ошибка.

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

После добавления пакетов `fontconfig` и `ttf-dejavu` всё будет работать без ошибок при рендеринге в PDF и изображения.

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
