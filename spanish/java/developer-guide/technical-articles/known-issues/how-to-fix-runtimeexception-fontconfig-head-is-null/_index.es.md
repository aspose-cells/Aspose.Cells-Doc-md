---
title: Cómo solucionar RuntimeException  Fontconfig head es nulo
type: docs
weight: 50
url: /es/java/how-to-fix-runtimeexception-fontconfig-head-is-null/
---

El error `java.lang.RuntimeException: Fontconfig head is null, check your fonts or fonts configuration` ocurre cuando **Aspose.Cells for Java** no puede localizar las fuentes requeridas en el sistema. Aspose.Cells confía en archivos de fuentes para operaciones de renderizado y procesamiento como la generación de PDF, renderizado de imágenes y manejo de diseño de página.

Para resolver este problema, tienes algunas opciones:

## Ejecutar en modo sin cabeza

Dado que probablemente estás ejecutando en un entorno sin cabeza, debes configurar Java para que se ejecute en **modo sin cabeza**. El modo sin cabeza permite que Java opere sin requerir acceso a una pantalla o entorno gráfico, lo cual es esencial cuando se ejecuta en entornos como Azure o Docker.

Puedes habilitar el modo sin cabeza agregando la siguiente propiedad del sistema al inicio de tu aplicación Java:

java

```bash
System.setProperty("java.awt.headless", "true");
```

O configúrelo mediante la línea de comandos al iniciar la JVM:

```ini
-Djava.awt.headless=true
```

## Instalar las fuentes necesarias

Si trabaja en un entorno donde puede instalar paquetes, puede instalar paquetes relacionados con fuentes para garantizar que estén disponibles las fuentes básicas. Para sistemas Linux, puede instalar paquetes de fuentes como:

**Debian/Ubuntu**:

```bash
sudo apt-get install -y fontconfig ttf-dejavu
```

**Alpine** (para configuraciones mínimas de Docker):

```bash
apk add --no-cache fontconfig ttf-dejavu
```

**Red Hat/CentOS**:

```bash
sudo yum install -y fontconfig dejavu-sans-fonts
```

## Ejemplo

Aquí tienes un Dockerfile de Alpine con solo jdk17 instalado.

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

Usa el Docker con Aspose.Cells for Java, ocurrirá la siguiente excepción al renderizar a PDF e imagen.

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

Después de agregar los paquetes `fontconfig` y `ttf-dejavu`, será correcto al renderizar a PDF e imagen.

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
