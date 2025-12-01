---
title: How to fix RuntimeException - Fontconfig head is null
type: docs
weight: 50
url: /java/how-to-fix-runtimeexception-fontconfig-head-is-null/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

The error `java.lang.RuntimeException: Fontconfig head is null, check your fonts or fonts configuration` occurs when **Aspose.Cells for Java** cannot locate the required fonts on the system. Aspose.Cells relies on font files for rendering and processing operations such as PDF generation, image rendering, and page layout handling.

To resolve this issue, you have a few options:

## Run in Headless Mode

Since you’re likely running in a headless environment, you should configure Java to run in **headless mode**. Headless mode allows Java to operate without requiring access to a display or graphics environment, which is essential when running in environments like Azure or Docker.

You can enable headless mode by adding the following system property at the start of your Java application:

java

```bash
System.setProperty("java.awt.headless", "true");
```

Or set it via the command line when launching the JVM:

```ini
-Djava.awt.headless=true
```

## Install the Necessary Fonts

If you’re working in an environment where you can install packages, you can install font-related packages to ensure that basic fonts are available. For Linux systems, you could install font packages such as:

**Debian/Ubuntu**:

```bash
sudo apt-get install -y fontconfig ttf-dejavu
```

**Alpine** (for minimal Docker setups):

```bash
apk add --no-cache fontconfig ttf-dejavu
```

**Red Hat/CentOS**:

```bash
sudo yum install -y fontconfig dejavu-sans-fonts
```

## Example

Here is a Dockerfile of Apline with only jdk17 being installed.

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

Use the docker with Aspose.Cells for Java, the following exception will occur while rendering to pdf and image.

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

After addiing `fontconfig` and `ttf-dejavu` packages, it will be OK while rendering to pdf and image.

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
