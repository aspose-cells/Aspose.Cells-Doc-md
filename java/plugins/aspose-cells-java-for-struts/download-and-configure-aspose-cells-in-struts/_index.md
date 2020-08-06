---
title: Download and Configure Aspose.Cells in Struts
type: docs
weight: 10
url: /java/download-and-configure-aspose-cells-in-struts/
---

## **Downloading Aspose.Cells Java for Struts 1.3**
You can downloaded the pre-built (binary) .war file from the latest releases hosted on [codeplex](http://aspose-cellsforstruts.codeplex.com/releases).

-OR-

You can download / check out the project source codes from the following locations:

- [CodePlex](https://asposecellsforstruts.codeplex.com)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Struts)
## **Building Aspose.Cells Java for Struts 1.3 from Source Codes**
After checking out source codes from any of the above repository, apply the following mvn commands:

{{< highlight java >}}

 $ mvn -U clean package 

{{< /highlight >}}

This will build "Strutsbookapp.war" in the target tolder.

To deploy the .war file just copy it to the running Apache tomcat server webapp directory.
