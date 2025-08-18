---
title: GridWeb简介
type: docs
weight: 10
url: /zh/java/introduction-of-gridweb/
---
## **GridWeb基础知识**
Aspose.Cells.GridWeb是一个基于GUI的Web控件，可以嵌入到JSP Web页面或任何java服务器中的html页面中。 
 

使用它很简单且易上手。

它可帮助您快速构建在线电子表格文件编辑器。

还支持导入和导出所有种类的电子表格格式文件，100%兼容MS Excel文件。

## **Aspose.Cells.GridWeb - 演示**
 

为了让您快速上手，我们提供了许多代码示例和演示，展示了如何使用Aspose.Cells.GridWeb API。

请从以下链接下载演示:
[Aspose.Cells.GridWeb 演示](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


## **如何运行Aspose.Cells for GridWeb Java演示**
{{% alert color="primary" %}}  

Aspose.Cells for GridWeb Java演示易于运行。您只需要在您的Web服务器上部署**gridwebdemo.war**。请从此[链接](https://forum.aspose.com/uploads/discourse_instance3/22292)下载演示。

本文描述了如何在Apache Tomcat服务器中运行Aspose.Cells for GridWeb Java演示。

{{% /alert %}} 
### **运行GridWeb Java演示的逐步指南**
1. 在任何目录中解压**apache-tomcat-7.0.52.zip**，例如C:\Tomcat 

![todo:image_alt_text](introduction-of-gridweb_1.png)



下图显示了Apache Tomcat服务器的解压目录和文件。 

![todo:image_alt_text](introduction-of-gridweb_2.png)



您可能还需要设置环境变量**CATALINA_HOME** 

![todo:image_alt_text](introduction-of-gridweb_3.png)

1. 打开**tomcat-users.xml**文件。 

![todo:image_alt_text](introduction-of-gridweb_4.png)

1. 添加此用户:

{{< highlight java >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**这里的用户名是tomcat，密码是secret** 

![todo:image_alt_text](introduction-of-gridweb_5.png)

1. 运行**startup.bat**文件。
   它将运行Apache Tomcat服务器。 

![todo:image_alt_text](introduction-of-gridweb_6.png)



**Tomcat服务器在命令窗口中运行** 

![todo:image_alt_text](introduction-of-gridweb_7.png)

1. 现在打开浏览器，输入**localhost:8080**。
   将显示Apache Tomcat网页。 

   **Apache Tomcat 网页** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1. 点击**管理应用**并输入用户名和密码。（如上图：tomcat, secret） 

![todo:image_alt_text](introduction-of-gridweb_9.png)

1. 向下滚动到**要部署的WAR文件**部分，然后浏览**gridwebdemo.war**文件。
1. 点击**部署**。 

![todo:image_alt_text](introduction-of-gridweb_10.png)

1. 浏览**gridwebdemo.war**文件。 

![todo:image_alt_text](introduction-of-gridweb_11.png)

1. 点击**部署**。 

![todo:image_alt_text](introduction-of-gridweb_12.png)

1. 部署完成后，点击**/gridwebdemo**并开始运行演示。 

![todo:image_alt_text](introduction-of-gridweb_13.png)


GridWeb 演示页面显示。 

**GridWeb 演示页面** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1. 点击任意演示并运行。 

   **创建内容演示正在运行** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**工作表演示正在运行** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**HeaderBar 和 CommandButton 演示正在运行** 

![todo:image_alt_text](introduction-of-gridweb_17.png)



## **浏览器功能和 Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb是基于GUI的Web控件，可以像其他Web控件一样嵌入到JSP网页中。Web控件最重要的一点是提供跨浏览器支持。Aspose.Cells.GridWeb提供了跨浏览器支持。
### **比较**
Aspose.Cells.GridWeb完全支持微软的Internet Explorer (IE)。然而，在其他浏览器上，它有一些较小的限制。本主题详细比较了不同浏览器支持的功能。

|**客户端功能**|**微软Internet Explorer**|**Google Chrome**|**Mozilla Firefox**|**Opera**|
| :- | :- | :- | :- | :- |
|单元格的上下文菜单|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|客户端验证|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|双击事件|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|下拉列表（*ComboBox模式*）|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|下拉列表（*弹出菜单模式*）|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|公式输入/编辑|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|冻结或取消冻结行/列|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|超链接（*CellCommand模式*）|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|超链接（*URL模式*）|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|合并或取消合并单元格|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|多个单元格复制/粘贴|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|多个单元格输入/编辑，单一回发|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
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
