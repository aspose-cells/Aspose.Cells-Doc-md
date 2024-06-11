---
title: 如何解决异常 - 无法初始化sun.font.FontScaler类
type: docs
weight: 40
url: /zh/java/how-to-fix-exception-could-not-initialize-class-sun-font-fontscaler/
---

## **可能的使用场景**
本文将解释如何解决异常 - 无法初始化sun.font.FontScaler类。异常看起来类似于这样

{{< highlight java >}}

 2017-06-12 18:10:16,075 ERROR org.apache.catalina.core.ContainerBase.[jboss.web].[default-host].[/DmMethods].[DoMethod] Servlet.service() for servlet DoMethod threw exception: java.lang.NoClassDefFoundError: Could not initialize class sun.font.FontScaler

at sun.font.TrueTypeFont.getScaler(TrueTypeFont.java:1248) [rt.jar:1.7.0_17]

at sun.font.FileFontStrike.(FileFontStrike.java:177) [rt.jar:1.7.0_17]

at sun.font.FileFont.createStrike(FileFont.java:95) [rt.jar:1.7.0_17]

at sun.font.Font2D.getStrike(Font2D.java:344) [rt.jar:1.7.0_17]

at sun.font.Font2D.getStrike(Font2D.java:289) [rt.jar:1.7.0_17]

at sun.font.FontDesignMetrics.initMatrixAndMetrics(FontDesignMetrics.java:358) [rt.jar:1.7.0_17]

at sun.font.FontDesignMetrics.(FontDesignMetrics.java:350) [rt.jar:1.7.0_17]

at sun.font.FontDesignMetrics.getMetrics(FontDesignMetrics.java:302) [rt.jar:1.7.0_17]

{{< /highlight >}}
## **系统环境**
系统环境可能如下所示

{{< highlight java >}}

 Red Hat Linux 6.3

Java™ SE Runtime Environment (build 1.7.0_17-b02)

Java HotSpot™ 64-Bit Server VM (build 23.7-b01, mixed mode)

{{< /highlight >}}
## **可能的解决方案**
您可能可以通过将以下JAR集成到类路径中来解决问题：

- ae-awt.jar
## **ae-awt.jar的下载链接**
- <http://www.java2s.com/Code/JarDownload/ae/ae-awt.jar.zip>


