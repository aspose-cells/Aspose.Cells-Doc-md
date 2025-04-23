---
title: Comment résoudre l exception RuntimeException  Fontconfig head est null
type: docs
weight: 50
url: /fr/java/how-to-fix-runtimeexception-fontconfig-head-is-null/
---

L'erreur `java.lang.RuntimeException : Fontconfig head is null, vérifiez vos polices ou votre configuration de polices` se produit lorsque **Aspose.Cells for Java** ne peut pas localiser les polices requises sur le système. Aspose.Cells dépend des fichiers de police pour rendre et traiter des opérations telles que la génération de PDF, le rendu d'image et la gestion de la mise en page.

Pour résoudre ce problème, vous avez plusieurs options :

## Exécuter en mode Headless

Étant donné que vous exécutez probablement dans un environnement sans interface graphique, vous devriez configurer Java pour fonctionner en **mode headless**. Le mode headless permet à Java de fonctionner sans accès à un affichage ou à un environnement graphique, ce qui est essentiel lors de l'exécution dans des environnements comme Azure ou Docker.

Vous pouvez activer le mode headless en ajoutant la propriété système suivante au début de votre application Java :

java

```bash
System.setProperty("java.awt.headless", "true");
```

Ou la définir via la ligne de commande lors du lancement du JVM :

```ini
-Djava.awt.headless=true
```

## Installer les polices nécessaires

Si vous travaillez dans un environnement où vous pouvez installer des paquets, vous pouvez installer des paquets liés aux polices pour vous assurer que les polices de base soient disponibles. Pour les systèmes Linux, vous pourriez installer des paquets comme :

**Debian/Ubuntu** :

```bash
sudo apt-get install -y fontconfig ttf-dejavu
```

**Alpine** (pour des configurations Docker minimales) :

```bash
apk add --no-cache fontconfig ttf-dejavu
```

**Red Hat/CentOS** :

```bash
sudo yum install -y fontconfig dejavu-sans-fonts
```

## Exemple

Voici un Dockerfile d'Alpine avec uniquement jdk17 installé.

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

Utilisez le docker avec Aspose.Cells for Java, l'exception suivante se produira lors du rendu en PDF et image.

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

Après avoir ajouté les paquets `fontconfig` et `ttf-dejavu`, le rendu en PDF et image sera correct.

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
