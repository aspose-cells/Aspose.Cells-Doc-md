---
title: Wie behebt man RuntimeException  Fontconfig Head ist null
type: docs
weight: 50
url: /de/java/how-to-fix-runtimeexception-fontconfig-head-is-null/
---

Der Fehler `java.lang.RuntimeException: Fontconfig head is null, check your fonts or fonts configuration` tritt auf, wenn **Aspose.Cells for Java** die erforderlichen Schriftarten auf dem System nicht finden kann. Aspose.Cells ist auf Schriftdateien angewiesen, um Operationen wie PDF-Erstellung, Bildrendering und Seitenlayout zu verarbeiten.

Um dieses Problem zu beheben, haben Sie einige Optionen:

## Im Headless-Modus ausführen

Da Sie wahrscheinlich in einer headless-Umgebung laufen, sollten Sie Java so konfigurieren, dass es im **Headless-Modus** läuft. Der Headless-Modus ermöglicht Java, ohne Zugriff auf eine Anzeige oder eine Grafikumgebung zu arbeiten, was beim Betrieb in Umgebungen wie Azure oder Docker wesentlich ist.

Sie können den Headless-Modus aktivieren, indem Sie die folgende Systemeigenschaft zu Beginn Ihrer Java-Anwendung hinzufügen:

java

```bash
System.setProperty("java.awt.headless", "true");
```

Oder setzen Sie ihn beim Starten des JVM über die Befehlszeile:

```ini
-Djava.awt.headless=true
```

## Installieren Sie die erforderlichen Schriftarten

Wenn Sie in einer Umgebung arbeiten, in der Sie Pakete installieren können, können Sie Schriftartenbezogene Pakete installieren, um sicherzustellen, dass grundlegende Schriftarten verfügbar sind. Für Linux-Systeme könnten Sie Schriftartenpakete wie installieren:

**Debian/Ubuntu**:

```bash
sudo apt-get install -y fontconfig ttf-dejavu
```

**Alpine** (für minimalistische Docker-Setups):

```bash
apk add --no-cache fontconfig ttf-dejavu
```

**Red Hat/CentOS**:

```bash
sudo yum install -y fontconfig dejavu-sans-fonts
```

## Beispiel

Hier ist eine Dockerdatei von Alpine mit nur JDK17 installiert.

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

Verwenden Sie den Docker mit Aspose.Cells for Java, dabei tritt beim Rendern in PDF und Bild die folgende Ausnahme auf.

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

Nach der Installation der Pakete `fontconfig` und `ttf-dejavu` funktioniert das Rendern in PDF und Bild ohne Probleme.

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
