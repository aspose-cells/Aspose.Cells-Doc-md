---
title: So beheben Sie die Ausnahme – Die Klasse sun.font.FontScaler konnte nicht initialisiert werden
type: docs
weight: 40
url: /de/java/how-to-fix-exception-could-not-initialize-class-sun-font-fontscaler/
---
## **Mögliche Nutzungsszenarien**
In diesem Artikel wird erläutert, wie die Ausnahme behoben wird – Die Klasse sun.font.FontScaler konnte nicht initialisiert werden. Die Ausnahme sieht in etwa so aus

{{< highlight "java" >}}

 2017-06-12 18:10:16,075 ERROR org.apache.catalina.core.ContainerBase.[jboss.web].[default-host].[/DmMethods].[DoMethod]Servlet.service() for servlet DoMethod threw exception: java.lang.NoClassDefFoundError: Could not initialize class sun.font.FontScaler

at sun.font.TrueTypeFont.getScaler(TrueTypeFont.java:1248) [rt.jar:1.7.0_17]at sun.font.FileFontStrike.(FileFontStrike.java:177) [rt.jar:1.7.0_17]at sun.font.FileFont.createStrike(FileFont.java:95) [rt.jar:1.7.0_17]at sun.font.Font2D.getStrike(Font2D.java:344) [rt.jar:1.7.0_17]at sun.font.Font2D.getStrike(Font2D.java:289) [rt.jar:1.7.0_17]at sun.font.FontDesignMetrics.initMatrixAndMetrics(FontDesignMetrics.java:358) [rt.jar:1.7.0_17]at sun.font.FontDesignMetrics.(FontDesignMetrics.java:350) [rt.jar:1.7.0_17]at sun.font.FontDesignMetrics.getMetrics(FontDesignMetrics.java:302) [rt.jar:1.7.0_17]{{< /highlight >}}
## **Systemumgebung**
Die Systemumgebung könnte in etwa so aussehen

{{< highlight "java" >}}

 Red Hat Linux 6.3

Java™ SE Runtime Environment (build 1.7.0_17-b02)

Java HotSpot™ 64-Bit Server VM (build 23.7-b01, mixed mode)

{{< /highlight >}}
## **Mögliche Lösung**
Sie werden das Problem wahrscheinlich lösen, indem Sie das folgende JAR in Ihren Klassenpfad integrieren:

- ae-awt.jar
## **Download-Link der ae-awt.jar**
- <http://www.java2s.com/Code/JarDownload/ae/ae-awt.jar.zip>


