---
title: GridWeb简介
type: docs
weight: 10
url: /zh/java/introduction-of-gridweb/
---
## **GridWeb基础知识**
Aspose.Cells.GridWeb是一种基于GUI的Web控件，可以嵌入到JSP Web页面或Java服务器中的任何HTML页面中。 
{{% alert color="primary" %}} 

使用起来简单易用。

它可以帮助您快速构建在线电子表格文件编辑器。

它还支持导入和导出各种电子表格格式文件，与MS Excel文件完全兼容。

## **Aspose.Cells.GridWeb - 演示**
{{% alert color="primary" %}} 

为了让您快速上手，我们提供了许多代码示例和演示，展示了如何使用Aspose.Cells.GridWeb API。

请从以下链接下载演示：
[Aspose.Cells.GridWeb 演示](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


## **如何运行Aspose.Cells for GridWeb Java演示**
{{% alert color="primary" %}} 

Aspose.Cells for GridWeb Java演示很容易运行。您只需在Web服务器中部署gridwebdemo.war文件。请从此链接下载演示。

本文介绍了如何在Apache Tomcat服务器中运行Aspose.Cells for GridWeb Java演示。

{{% /alert %}} 
### **逐步指南以运行GridWeb Java演示**
1. 在任何目录（例如C:\Tomcat）中解压缩apache-tomcat-7.0.52.zip 

![todo:image_alt_text](introduction-of-gridweb_1.png)



下图显示了Apache Tomcat服务器的解压缩目录和文件 

![todo:image_alt_text](introduction-of-gridweb_2.png)



您可能还需要设置环境变量CATALINA_HOME 

![todo:image_alt_text](introduction-of-gridweb_3.png)

1. 打开tomcat-users.xml文件 

![todo:image_alt_text](introduction-of-gridweb_4.png)

1. 添加此用户

{{< highlight java >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



这里的用户名是tomcat，密码是secret 

![todo:image_alt_text](introduction-of-gridweb_5.png)

1. 运行startup.bat文件
   它将运行Apache Tomcat服务器 

![todo:image_alt_text](introduction-of-gridweb_6.png)



Tomcat服务器在命令窗口中运行 

![todo:image_alt_text](introduction-of-gridweb_7.png)

1. 现在打开浏览器，输入 **localhost:8080**。
   显示Apache Tomcat网页。 

   **Apache Tomcat网页** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1. 点击**Manager App**，输入用户名和密码。(如上：tomcat, secret) 

![todo:image_alt_text](introduction-of-gridweb_9.png)

1. 滚动到**要部署的WAR文件**部分，浏览**gridwebdemo.war**文件。
1. 点击**部署**。 

![todo:image_alt_text](introduction-of-gridweb_10.png)

1. 浏览**gridwebdemo.war**文件。 

![todo:image_alt_text](introduction-of-gridweb_11.png)

1. 点击**部署**。 

![todo:image_alt_text](introduction-of-gridweb_12.png)

1. 部署后，点击**/gridwebdemo**，开始运行示例。 

![todo:image_alt_text](introduction-of-gridweb_13.png)


显示GridWeb演示页面。 

**GridWeb演示页面** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1. 点击任何示例并运行。 

   **创建内容演示正在运行** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**工作表演示正在运行** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**HeaderBar和CommandButton演示正在运行** 

![todo:image_alt_text](introduction-of-gridweb_17.png)


{{% /alert %}} 
## **浏览器能力和Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb是基于GUI的Web控件，可嵌入JSP网页中，类似其他Web控件。Web控件最重要的事情是提供跨浏览器支持。Aspose.Cells.GridWeb提供跨浏览器支持。
### **对比**
Aspose.Cells.GridWeb在Microsoft的Internet Explorer (IE)上得到充分支持。然而，在其他浏览器上，它有一些局限性。本主题详细比较了不同浏览器支持哪些功能。

| **客户端功能** | **Microsoft Internet Explorer** | **Google Chrome** | **Mozilla Firefox** | **Opera** |
| :- | :- | :- | :- | :- |
|单元格的上下文菜单|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|客户端验证|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|双击事件|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|下拉列表（*组合框模式*）|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|下拉列表（*弹出菜单模式*）|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|公式输入/编辑|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|冻结或取消冻结行/列|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|超链接（*单元格命令模式*）|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|超链接（*URL模式*）|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|合并或取消合并单元格|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|多个单元格复制/粘贴|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|多个单元格输入/编辑，单个提交|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|数字格式|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|工作表分页|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|只读单元格|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|只读行/列|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|使用正则表达式进行数据验证|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|调整列宽度|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|调整行高度|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|插入/删除行和列|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|滚动内容|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|滚动工作表标签|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|设置单元格边框|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|设置单元格字体设置|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Context menu of a cell can only be activated by clicking the Client side menu button.
