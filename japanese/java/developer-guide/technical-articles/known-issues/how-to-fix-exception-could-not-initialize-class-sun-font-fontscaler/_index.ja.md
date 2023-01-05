---
title: 例外の修正方法 - クラス sun.font.FontScaler を初期化できませんでした
type: docs
weight: 40
url: /ja/java/how-to-fix-exception-could-not-initialize-class-sun-font-fontscaler/
---
## **考えられる使用シナリオ**
この記事では、クラス sun.font.FontScaler を初期化できませんでしたという例外を修正する方法について説明します。例外はこれに似ています

{{< highlight "java" >}}

 2017-06-12 18:10:16,075 ERROR org.apache.catalina.core.ContainerBase.[jboss.web].[default-host].[/DmMethods].[DoMethod]Servlet.service() for servlet DoMethod threw exception: java.lang.NoClassDefFoundError: Could not initialize class sun.font.FontScaler

at sun.font.TrueTypeFont.getScaler(TrueTypeFont.java:1248) [rt.jar:1.7.0_17]at sun.font.FileFontStrike.(FileFontStrike.java:177) [rt.jar:1.7.0_17]at sun.font.FileFont.createStrike(FileFont.java:95) [rt.jar:1.7.0_17]at sun.font.Font2D.getStrike(Font2D.java:344) [rt.jar:1.7.0_17]at sun.font.Font2D.getStrike(Font2D.java:289) [rt.jar:1.7.0_17]at sun.font.FontDesignMetrics.initMatrixAndMetrics(FontDesignMetrics.java:358) [rt.jar:1.7.0_17]at sun.font.FontDesignMetrics.(FontDesignMetrics.java:350) [rt.jar:1.7.0_17]at sun.font.FontDesignMetrics.getMetrics(FontDesignMetrics.java:302) [rt.jar:1.7.0_17]{{< /highlight >}}
## **システム環境**
システム環境は次のようになります

{{< highlight "java" >}}

 Red Hat Linux 6.3

Java™ SE Runtime Environment (build 1.7.0_17-b02)

Java HotSpot™ 64-Bit Server VM (build 23.7-b01, mixed mode)

{{< /highlight >}}
## **考えられる解決策**
次の JAR をクラスパスに統合することで、問題を解決できる可能性があります。

- ae-awt.jar
## **ae-awt.jar のダウンロード リンク**
- <http://www.java2s.com/Code/JarDownload/ae/ae-awt.jar.zip>


