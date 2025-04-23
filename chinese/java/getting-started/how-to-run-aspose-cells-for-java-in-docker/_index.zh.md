---
title: 如何在Docker中运行Aspose.Cells for Java
type: docs
description: 在Linux的Docker容器中运行Aspose.Cells for Java。
weight: 139
url: /zh/java/how-to-run-aspose-cells-in-docker/
---

微服务结合容器化使得很容易结合技术。Docker允许您轻松地将Aspose.Cells功能集成到您的应用程序中，无论您的开发堆栈中使用什么技术。

如果您的目标是微服务或者您的技术栈中主要的技术不是.NET、C++或Java，但您需要Aspose.Cells功能，或者如果您已经在技术栈中使用了Docker，那么您可能对在Docker容器中使用Aspose.Cells for Java感兴趣。

## 先决条件

- 您的系统上必须安装Docker。 

## 创建一个Java应用程序

在这个示例中，您将创建一个简单的xlsx文件，保存并读取它的Java应用程序。然后可以在Docker中构建和运行该应用程序。

### 创建Java应用程序

在Eclipse中使用以下代码创建Java应用程序。在这个示例中，我们使用Aspose.Cells for Java创建一个新的xlsx工作表，并设置其表名和单元格值，然后读取它们并输出它们。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "TestDocker.java" >}}

### 将Java应用程序制作成jar包

下图显示了使用Eclipse的“导出”菜单制作jar包的方法。

**![使用Eclipse制作Jar包](MakeJar.png)**

现在我们使用Aspose.Cells for Java编写了一个Java程序，得到了一个jar包。接下来我们将制作一个dockerfile。

### 配置Dockerfile

下一步是创建和配置Dockerfile。

1. 创建Dockerfile并将其放置在jar包旁边，保持文件名不带扩展名（默认）。
2. 在Dockerfile中指定:

{{< highlight plain >}}
   FROM williamyeh/java8:latest

   VOLUME /tmp

   ADD TestDocker.jar app.jar

   ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
{{< /highlight >}}

### 在Docker中构建和运行应用程序

现在该应用程序可以在Docker中构建和运行了。打开您喜欢的命令提示符，切换到包含Dockerfile的文件夹，运行以下命令:

{{< highlight plain >}}
docker build -t java-app .
{{< /highlight >}}

执行上述命令后，您将得到XLSX工作表的输出和命令行的结果。此时，Java程序已经成功在Linux Docker中运行。
{{< app/cells/assistant language="java" >}}
