---
title: كيفية إصلاح الاستثناء - تعذرت تهيئة الفئة sun.font.FontScaler
type: docs
weight: 40
url: /ar/java/how-to-fix-exception-could-not-initialize-class-sun-font-fontscaler/
---
## **سيناريوهات الاستخدام الممكنة**
تشرح هذه المقالة كيفية إصلاح الاستثناء - لا يمكن تهيئة فئة sun.font.FontScaler. يبدو الاستثناء شيئًا مشابهًا لهذا

{{< highlight "java" >}}

 2017-06-12 18:10:16,075 ERROR org.apache.catalina.core.ContainerBase.[jboss.web].[default-host].[/DmMethods].[DoMethod]Servlet.service() for servlet DoMethod threw exception: java.lang.NoClassDefFoundError: Could not initialize class sun.font.FontScaler

at sun.font.TrueTypeFont.getScaler(TrueTypeFont.java:1248) [rt.jar:1.7.0_17]at sun.font.FileFontStrike.(FileFontStrike.java:177) [rt.jar:1.7.0_17]at sun.font.FileFont.createStrike(FileFont.java:95) [rt.jar:1.7.0_17]at sun.font.Font2D.getStrike(Font2D.java:344) [rt.jar:1.7.0_17]at sun.font.Font2D.getStrike(Font2D.java:289) [rt.jar:1.7.0_17]at sun.font.FontDesignMetrics.initMatrixAndMetrics(FontDesignMetrics.java:358) [rt.jar:1.7.0_17]at sun.font.FontDesignMetrics.(FontDesignMetrics.java:350) [rt.jar:1.7.0_17]at sun.font.FontDesignMetrics.getMetrics(FontDesignMetrics.java:302) [rt.jar:1.7.0_17]{{< /highlight >}}
## **بيئة النظام**
يمكن أن تكون بيئة النظام شيئًا من هذا القبيل

{{< highlight "java" >}}

 Red Hat Linux 6.3

Java™ SE Runtime Environment (build 1.7.0_17-b02)

Java HotSpot™ 64-Bit Server VM (build 23.7-b01, mixed mode)

{{< /highlight >}}
## **حل ممكن**
من المحتمل أن تحل المشكلة من خلال دمج JAR التالية في مسار الفصل الخاص بك:

- ae-awt.jar
## **رابط تحميل ملف ae-awt.jar**
- <http://www.java2s.com/Code/JarDownload/ae/ae-awt.jar.zip>


