---
title: GridWeb简介
type: docs
weight: 10
url: /zh/java/introduction-of-gridweb/
---
## **如何运行 Aspose.Cells for GridWeb Java Demos**
{{% alert color="primary" %}} 

 Aspose.Cells for GridWeb Java 演示很容易运行。你只需要部署**gridwebdemo.war**在您的网络服务器中。请从这里下载演示[关联](https://forum.aspose.com/uploads/discourse_instance3/22292).

本文介绍如何在 Apache Tomcat Server 中运行 Aspose.Cells for GridWeb Java Demos。

{{% /alert %}} 
### **运行 GridWeb 的分步指南 Java 演示**
1. 提炼**apache-tomcat-7.0.52.zip**在任何目录中，例如 C:\Tomcat

![待办事项：图像_替代_文本](introduction-of-gridweb_1.png)



以下快照显示了 Apache Tomcat 服务器的提取目录和文件

![待办事项：图像_替代_文本](introduction-of-gridweb_2.png)



您可能还需要设置环境变量**卡塔利娜之家** 

![待办事项：图像_替代_文本](introduction-of-gridweb_3.png)

1. 打开**tomcat-users.xml**文件。

![待办事项：图像_替代_文本](introduction-of-gridweb_4.png)

1. 添加此用户：

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**这里的用户名是tomcat，密码是secret** 

![待办事项：图像_替代_文本](introduction-of-gridweb_5.png)

1. 跑过**启动.bat**文件。
它将运行 Apache Tomcat 服务器。

![待办事项：图像_替代_文本](introduction-of-gridweb_6.png)



**在命令窗口中运行的 Tomcat 服务器** 

![待办事项：图像_替代_文本](introduction-of-gridweb_7.png)

1. 现在打开浏览器并输入**本地主机：8080**.
显示 Apache Tomcat 网页。

   **Apache Tomcat 网页** 

![待办事项：图像_替代_文本](introduction-of-gridweb_8.png)

1. 点击**经理应用程序**并键入用户名和密码。 （如上：tomcat，secret）

![待办事项：图像_替代_文本](introduction-of-gridweb_9.png)

1. 向下滚动到该部分**要部署的 WAR 文件**并浏览**gridwebdemo.war**文件。
1. 点击**部署**. 

![待办事项：图像_替代_文本](introduction-of-gridweb_10.png)

1. 浏览**gridwebdemo.war**文件。

![待办事项：图像_替代_文本](introduction-of-gridweb_11.png)

1. 点击**部署**. 

![待办事项：图像_替代_文本](introduction-of-gridweb_12.png)

1. 部署好后，点击**/网格网络演示**并开始运行演示。

![待办事项：图像_替代_文本](introduction-of-gridweb_13.png)


显示 GridWeb 演示页面。

**GridWeb 演示页面** 

![待办事项：图像_替代_文本](introduction-of-gridweb_14.png)

1. 单击任何演示并运行它。

   **创建内容演示运行** 

![待办事项：图像_替代_文本](introduction-of-gridweb_15.png)



**工作表演示运行** 

![待办事项：图像_替代_文本](introduction-of-gridweb_16.png)



**HeaderBar 和 CommandButton 演示运行** 

![待办事项：图像_替代_文本](introduction-of-gridweb_17.png)
## **Aspose.Cells.GridWeb - 演示**
{{% alert color="primary" %}} 

为了让您快速启动和运行，我们提供了一些代码示例和演示，展示了如何使用 Aspose.Cells.GridWeb API。

请从以下链接下载演示：
[Aspose.Cells.GridWeb 演示](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)

{{% /alert %}} 
## **浏览器功能和 Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb 是一个基于 GUI 的 Web 控件，可以像其他 Web 控件一样嵌入到 JSP 网页中。 Web 控件最重要的是提供跨浏览器支持。 Aspose.Cells.GridWeb 提供跨浏览器支持。
### **比较**
Aspose.Cells.GridWeb 完全支持 Microsoft 的 Internet Explorer (IE)。但是，在其他浏览器上，它有一些小限制。本主题详细比较了不同浏览器支持的功能。

|**客户端功能**|**Microsoft Internet Explorer**|**Google 铬**|**火狐浏览器**|**歌剧**|
|:- |:- |:- |:- |:- |
|Cell的上下文菜单|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|客户端验证|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|双击事件|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|下拉列表 （*组合框模式* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|下拉列表 （*弹出菜单模式* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|公式输入/编辑|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|冻结或解冻行/列|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|超链接 (*单元命令模式* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|超链接 (*网址模式* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|合并或取消合并 Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|多个 Cells 复制/粘贴|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|多个 Cells 输入/编辑，单个回发|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|数字格式|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|工作表分页|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|只读 Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|只读行/列|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|使用正则表达式进行数据验证|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|调整列宽|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|调整行高|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|插入/删除行和列|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|滚动内容|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|滚动工作表标签|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|设置Cells的边框|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|设置Cells的字体设置|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}}单元格的上下文菜单只能通过单击客户端菜单按钮激活。
