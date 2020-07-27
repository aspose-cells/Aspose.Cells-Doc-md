+++
title = "How to fix exception - Could not initialize class sun.font.FontScaler" 
description = "" 
weight = 16585 
+++

Aspose.Cells for Java : How to fix exception - Could not initialize class sun.font.FontScaler  

# Aspose.Cells for Java : How to fix exception - Could not initialize class sun.font.FontScaler


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#Howtofixexception-Couldnotinitializeclasssun.font.FontScaler-PossibleUsageScenarios)
*   2 [System Environment](#Howtofixexception-Couldnotinitializeclasssun.font.FontScaler-SystemEnvironment)
*   3 [Possible Solution](#Howtofixexception-Couldnotinitializeclasssun.font.FontScaler-PossibleSolution)
*   4 [Download Link of the ae-awt.jar](#Howtofixexception-Couldnotinitializeclasssun.font.FontScaler-DownloadLinkoftheae-awt.jar)
{{< /panel >}}
 

## Possible Usage Scenarios

This article will explain how to fix exception - Could not initialize class sun.font.FontScaler. The exception looks something similar to this

2017-06-12 18:10:16,075 ERROR org.apache.catalina.core.ContainerBase.\[jboss.web\].\[default-host\].\[/DmMethods\].\[DoMethod\] Servlet.service() for servlet DoMethod threw exception: java.lang.NoClassDefFoundError: Could not initialize class sun.font.FontScalerat sun.font.TrueTypeFont.getScaler(TrueTypeFont.java:1248) \[rt.jar:1.7.0\_17\]at sun.font.FileFontStrike.(FileFontStrike.java:177) \[rt.jar:1.7.0\_17\]at sun.font.FileFont.createStrike(FileFont.java:95) \[rt.jar:1.7.0\_17\]at sun.font.Font2D.getStrike(Font2D.java:344) \[rt.jar:1.7.0\_17\]at sun.font.Font2D.getStrike(Font2D.java:289) \[rt.jar:1.7.0\_17\]at sun.font.FontDesignMetrics.initMatrixAndMetrics(FontDesignMetrics.java:358) \[rt.jar:1.7.0\_17\]at sun.font.FontDesignMetrics.(FontDesignMetrics.java:350) \[rt.jar:1.7.0\_17\]at sun.font.FontDesignMetrics.getMetrics(FontDesignMetrics.java:302) \[rt.jar:1.7.0\_17\]

## System Environment

The system environment could be something like this

Red Hat Linux 6.3Java™ SE Runtime Environment (build 1.7.0\_17-b02)Java HotSpot™ 64-Bit Server VM (build 23.7-b01, mixed mode)

## Possible Solution

You are likely to resolve the problem by integrating the following JAR into your classpath:

*   ae-awt.jar

## Download Link of the ae-awt.jar

*   [http://www.java2s.com/Code/JarDownload/ae/ae-awt.jar.zip](http://www.java2s.com/Code/JarDownload/ae/ae-awt.jar.zip)

