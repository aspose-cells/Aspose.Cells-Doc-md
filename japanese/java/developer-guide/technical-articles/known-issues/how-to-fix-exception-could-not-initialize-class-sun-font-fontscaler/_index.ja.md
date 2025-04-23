---
title: 例外  sun.font.FontScaler の初期化できません
type: docs
weight: 40
url: /ja/java/how-to-fix-exception-could-not-initialize-class-sun-font-fontscaler/
---

## **可能な使用シナリオ**
この記事では、例外 - sun.font.FontScaler の初期化方法について説明します。例外は次のようなものに似ています

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
## **システム環境**
システム環境は次のようなものがあるかもしれません

{{< highlight java >}}

 Red Hat Linux 6.3

Java™ SE Runtime Environment (build 1.7.0_17-b02)

Java HotSpot™ 64-Bit Server VM (build 23.7-b01, mixed mode)

{{< /highlight >}}
## **可能な解決策**
以下のJARをクラスパスに統合することで問題を解決できる可能性があります

- ae-awt.jar
## **ae-awt.jarのダウンロードリンク**
- <http://www.java2s.com/Code/JarDownload/ae/ae-awt.jar.zip>


{{< app/cells/assistant language="java" >}}
