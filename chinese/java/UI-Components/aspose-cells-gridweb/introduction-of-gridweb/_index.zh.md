---
title: GridWeb简介
type: docs
weight: 10
url: /zh/java/introduction-of-gridweb/
---
##  **GridWeb 基础知识**
Aspose.Cells.GridWeb是一个基于GUI的Web控件，可以嵌入JSP网页或java服务器中的任何html页面。
{{% alert color="primary" %}} 

它使用起来简单方便。

它可以帮助您快速构建电子表格文件的在线网页编辑器。

它还支持导入和导出各种电子表格格式文件，与MS Excel文件100%兼容。

##  **Aspose.Cells.GridWeb - 演示**
{{% alert color="primary" %}} 

为了让您快速启动并运行，我们提供了许多代码示例和演示，展示如何使用 Aspose.Cells.GridWeb API。

请从以下链接下载演示：
[Aspose.Cells.GridWeb 演示](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


##  **如何为 GridWeb Java 演示运行 Aspose.Cells**
{{% alert color="primary" %}} 

 Aspose.Cells for GridWeb Java 演示很容易运行。您只需要部署**gridwebdemo.war**在您的网络服务器中。请从这里下载演示[关联](https://forum.aspose.com/uploads/discourse_instance3/22292).

本文介绍如何在 Apache Tomcat 服务器中运行 GridWeb Java 演示的 Aspose.Cells。

{{% /alert %}} 
###  **运行 GridWeb 的分步指南 Java 演示**
1. 提炼**apache-tomcat-7.0.52.zip**在任何目录中，例如 C:\Tomcat

![待办事项：图像_替代_文本](introduction-of-gridweb_1.png)



以下快照显示了 Apache Tomcat 服务器的解压目录和文件

![待办事项：图像_替代_文本](introduction-of-gridweb_2.png)



您可能还需要设置环境变量**CATALINA_HOME** 

![待办事项：图像_替代_文本](introduction-of-gridweb_3.png)

1. 打开**tomcat-用户.xml**文件。

![待办事项：图像_替代_文本](introduction-of-gridweb_4.png)

1. 添加该用户：

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**这里用户名是tomcat，密码是secret** 

![待办事项：图像_替代_文本](introduction-of-gridweb_5.png)

1. 跑过**启动.bat**文件。
它将运行 Apache Tomcat 服务器。

![待办事项：图像_替代_文本](introduction-of-gridweb_6.png)



**Tomcat 服务器在命令窗口中运行** 

![待办事项：图像_替代_文本](introduction-of-gridweb_7.png)

1. 现在打开浏览器并输入 *localhost:8080**。
将显示 Apache Tomcat 网页。

   **Apache Tomcat 网页** 

![待办事项：图像_替代_文本](introduction-of-gridweb_8.png)

1. 点击**经理应用程序**并输入用户名和密码。 （如上：tomcat、secret）

![待办事项：图像_替代_文本](introduction-of-gridweb_9.png)

1. 向下滚动到该部分**要部署的 WAR 文件**并浏览**gridwebdemo.war**文件。
1. 单击*部署**。

![待办事项：图像_替代_文本](introduction-of-gridweb_10.png)

1. 浏览**gridwebdemo.war**文件。

![待办事项：图像_替代_文本](introduction-of-gridweb_11.png)

1. 单击*部署**。

![待办事项：图像_替代_文本](introduction-of-gridweb_12.png)

1. 部署完成后，单击**/gridwebdemo**并开始运行演示。

![待办事项：图像_替代_文本](introduction-of-gridweb_13.png)


将显示 GridWeb 演示页面。

**GridWeb 演示页面** 

![待办事项：图像_替代_文本](introduction-of-gridweb_14.png)

1. 单击任意演示并运行它。

   **创建内容演示运行** 

![待办事项：图像_替代_文本](introduction-of-gridweb_15.png)



**工作表演示运行** 

![待办事项：图像_替代_文本](introduction-of-gridweb_16.png)



**正在运行的 HeaderBar 和 CommandButton 演示** 

![待办事项：图像_替代_文本](introduction-of-gridweb_17.png)


{{% /alert %}} 
##  **浏览器功能和 Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb是一个基于GUI的Web控件，可以像其他Web控件一样嵌入JSP网页中。 Web 控制最重要的是提供跨浏览器支持。 Aspose.Cells.GridWeb提供跨浏览器支持。
###  **比较**
Aspose.Cells.GridWeb 在 Microsoft 的 Internet Explorer (IE) 上得到完全支持。然而，在其他浏览器上，它有一些小的限制。本主题详细比较了不同浏览器支持的功能。

|**客户端功能**|**Microsoft 互联网浏览器**|**Google 铬**|**火狐浏览器**|**歌剧**|
| :- | :- | :- | :- | :- |
|Cell 的右键菜单|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|客户端验证|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|双击事件|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|下拉列表 （*组合框模式* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|下拉列表 （*弹出菜单模式* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|公式输入/编辑|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|冻结或解冻行/列|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|超链接（*单元命令模式* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|超链接（*网址模式* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
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
|滚动工作表选项卡|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|设置 Cells 的边框|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|设置Cells的字体设置|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}}单元格的上下文菜单只能通过单击客户端菜单按钮来激活。
