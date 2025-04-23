---
title: Come risolvere RuntimeException  Fontconfig head is null
type: docs
weight: 50
url: /it/java/how-to-fix-runtimeexception-fontconfig-head-is-null/
---

L'errore `java.lang.RuntimeException: Fontconfig head is null, check your fonts or fonts configuration` si verifica quando **Aspose.Cells for Java** non riesce a localizzare i font necessari sul sistema. Aspose.Cells si appoggia sui file di font per operazioni di rendering e elaborazione come generazione PDF, rendering di immagini e gestione del layout di pagina.

Per risolvere questo problema, hai alcune opzioni:

## Esegui in Modalità Headless

Poiché molto probabilmente operi in un ambiente senza interfaccia grafica, dovresti configurare Java per funzionare in **modalità headless**. La modalità headless permette a Java di operare senza richiedere l'accesso a uno schermo o a un ambiente grafico, essenziale quando si lavora in ambienti come Azure o Docker.

Puoi abilitare la modalità headless aggiungendo la seguente proprietà di sistema all'avvio della tua applicazione Java:

java

```bash
System.setProperty("java.awt.headless", "true");
```

Oppure impostandola tramite la riga di comando al lancio della JVM:

```ini
-Djava.awt.headless=true
```

## Installa i Font Necessari

Se lavori in un ambiente dove puoi installare pacchetti, puoi installare pacchetti relativi ai font per assicurarti che i font di base siano disponibili. Per i sistemi Linux, puoi installare pacchetti di font come:

**Debian/Ubuntu**:

```bash
sudo apt-get install -y fontconfig ttf-dejavu
```

**Alpine** (per setup Docker minimalisti):

```bash
apk add --no-cache fontconfig ttf-dejavu
```

**Red Hat/CentOS**:

```bash
sudo yum install -y fontconfig dejavu-sans-fonts
```

## Esempio

Ecco un esempio di Dockerfile di Alpine con solo l'installazione di jdk17.

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

Usa il docker con Aspose.Cells for Java, si verificherà la seguente eccezione durante il rendering in PDF e immagine.

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

Dopo aver aggiunto i pacchetti `fontconfig` e `ttf-dejavu`, il rendering in PDF e immagine sarà OK.

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
