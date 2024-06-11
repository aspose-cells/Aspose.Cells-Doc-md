---
title: 与 GridWeb 一起工作
type: docs
weight: 20
url: /zh/java/working-with-gridweb/
---

## **打开 Microsoft Excel 文件**

Aspose.Cells.GridWeb 控件可以打开和加载 Microsoft Excel 文件 - 包括数据，格式，图表，图片等。本主题解释了如何操作。

使用 GridWeb 控件打开 Excel 文件：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 表单或页面。
1. 通过指定文件路径导入 Excel 文件。
1. 运行应用程序或打开页面。

要将 Excel 文件内容加载到 Aspose.Cells.GridWeb 控件中，必须调用 importExcelFile 方法来指定 Excel 文件的路径。之后，GridWeb 控件将自动在指定路径找到文件并显示其中的内容。下面提供了加载 Excel 文件内容的代码段。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

上述代码段可以按您的需求使用。例如，要在 Web 表单加载时自动加载 Excel 文件，请将此代码添加到您自己指定的表单的 Page_Load 事件中。

**将 Excel 文件加载到 GridWeb 中**

![todo:image_alt_text](working-with-gridweb_1.png)

## **保存 Microsoft Excel 文件**

可以使用 Aspose.Cells.GridWeb 控件在网站上以 GUI 模式创建新的或操作现有的 Microsoft Excel 文件。然后可以将文件保存为 Excel 文件。Aspose.Cells.GridWeb 有效地充当在线电子表格编辑器。本主题描述了如何将网格内容保存为 Excel 文件。

### **另存为文件**

要将 Aspose.Cells.GridWeb 控件的内容另存为 Excel 文件：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 表单或页面。
1. 将您的工作保存为指定路径的 Excel 文件。
1. 运行应用程序或打开页面。

下面的代码示例说明了如何将网格内容保存为 Excel 文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

以上的代码片段可以以多种方式使用。一种常见的方式是添加一个按钮，当点击按钮时，将网格内容保存到Excel文件中。Aspose.Cells.GridWeb为此任务提供了更简单的方法。Aspose.Cells.GridWeb具有一个名为SaveCommand的事件。可以将以上的代码片段添加到SaveCommand事件的事件处理程序中，这样用户就可以通过点击Aspose.Cells.GridWeb内置的**保存**按钮来保存他们的工作。

## **调整Aspose.Cells.GridWeb及其标题栏的大小**

本文介绍如何使用Aspose.Cells.GridWeb API在运行时调整GridWeb的大小。同时，还解释了如何调整Aspose.Cells.GridWeb控件的标题栏大小，以使它们的数据更易于阅读。

### **更改Aspose.Cells.GridWeb的宽度和高度**

更改Aspose.Cells.GridWeb控件的宽度和高度是一个简单但重要的功能。Aspose.Cells.GridWeb控件在API中由GridWeb类表示。要调整GridWeb控件的宽度和高度，只需使用其width和height属性。

{{% alert color="primary" %}}

控件的宽度和高度可以以像素或点的形式定义。

{{% /alert %}}

以下是代码片段的输出结果。

**更改了GridWeb控件的宽度和高度**

![todo:image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **更改标题栏的宽度和高度**

Aspose.Cells.GridWeb控件包含以下两个标题栏:

- 顶部标题栏，该标题栏表示列为A，B，C，D等。
- 左侧标题栏，该标题栏表示行为1，2，3，4等。

下面显示了这两个标题栏。

**标题栏**

![todo:image_alt_text](working-with-gridweb_3.png)

使用GridWeb控件的HeaderBarHeight和HeaderBarWidth属性分别更改顶部标题栏和左侧标题栏的高度和宽度。下图显示了以下代码示例的输出。

**更改了标题栏的宽度和高度**

![todo:image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **使用Aspose.Cells.GridWeb事件**

所有开发人员必须熟悉事件及其用途。事件用于发送控件或类中可能发生的更改通知。Aspose.Cells.GridWeb具有几个事件，可用于在控件发生特定更改时执行特定任务。

本主题介绍了Aspose.Cells.GridWeb控件支持的所有事件的概述，以及如何处理这些事件的一些细节。

### **Grid事件简介**

Aspose.Cells.GridWeb 控件支持多个事件，这些事件在控件中触发特定事件时提供更多操作控制。以下是 Aspose.Cells.GridWeb 控件支持的完整事件列表。

|**事件**|**描述**|
| :- | :- |
|CellCommand| 当单元格的命令超链接被点击时触发。当触发此事件时，其参数 e.Argument 提供命令的名称。
|CellDoubleClick| 当双击单元格时触发。
|ColumnDeleted| 当用户使用客户端菜单从工作表中删除列时触发。
|ColumnDeleting| 当用户尝试使用客户端菜单从工作表中删除列时触发。
|ColumnDoubleClick| 当双击列标题时触发。
|ColumnInserted| 当用户使用客户端菜单在工作表中插入列时触发。
|CustomCommand| 当用户点击自定义命令按钮时触发。
|LoadCustomData| 当控件的 EnableSession 属性设置为 false 并且需要加载工作表数据时触发。您可以在无会话模式下处理此事件，以从文件或数据库加载工作表数据。
|PageIndexChanged| 当控件的工作表页索引更改时触发。
|RowDeleted| 当用户使用客户端菜单从工作表中删除行时触发。
|RowDeleting| 用户尝试使用客户端菜单从工作表中删除行时触发。
|RowDoubleClick| 当双击行标题时触发。
|RowInserted| 当用户使用客户端菜单在工作表中插入行时触发。
|SaveCommand| 当点击**保存**按钮时触发。
|SheetTabClick| 当单击工作表标签时触发。
|SubmitCommand| 当单击**提交**按钮时触发。
|UndoCommand| 当单击**撤销**按钮时触发。
|AjaxCallFinished| 当控件的 AJAX 更新完成时触发。(EnableAJAX 必须设置为 true)。
|CellModifiedOnAjax|当AJAX调用中的单元格被修改时触发。
|AfterColumnFilter|当对列应用筛选器时触发。

### **处理网格事件**

为了在触发特定事件时执行特定操作，我们必须创建一个事件处理程序。事件处理程序在触发某个特定事件时执行所需的任务。以下示例展示了如何处理简单的网格事件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **处理双击事件**

Aspose.Cells.GridWeb包含三种类型的双击事件:

- CellDoubleClick，当双击单元格时触发。
- ColumnDoubleClick，当双击列标题时触发。
- RowDoubleClick，当双击行标题时触发。

本主题讨论如何在Aspose.Cells.GridWeb中启用双击事件。它还讨论了为这些事件创建事件处理程序。

### **启用双击事件**

通过将GridWeb控件的EnableDoubleClickEvent属性设置为true可以在客户端启用所有类型的双击事件。

{{% alert color="primary" %}}

默认情况下，EnableDoubleClickEvent属性设置为false。这意味着默认情况下未启用双击事件。要实现这些事件，首先要启用该功能。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

一旦启用双击事件，就可以为任何双击事件创建事件处理程序。这些事件处理程序在触发给定的双击事件时执行特定任务。

### **处理双击事件**

#### **双击单元格**

CellDoubleClick事件处理程序提供CellEventArgs类型的参数，该参数提供双击的单元格的完整信息。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **双击列标题**

ColumnDoubleClick事件处理程序提供RowColumnEventArgs类型的参数，该参数提供双击列标题的列的索引号和其他信息。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **双击行标题**

RowDoubleClick事件的事件处理程序提供了RowColumnEventArgs类型的参数，该参数提供了双击的标题行的索引号和其他相关信息。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **设置Aspose.Cells.GridWeb的样式或外观**

Aspose.Cells.GridWeb有自己的默认外观，但可以更改其外观。Aspose.Cells.GridWeb提供了多个属性，让开发人员完全控制其外观。本主题讨论了其中一些属性。

### **设置Aspose.Cells.GridWeb的样式或外观**

#### **预设样式**

为了节省开发人员的工作，Aspose.Cells.GridWeb提供了一些预设样式。只需从列表中选择样式以应用该样式。

|**样式**|**颜色方案**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
当选择特定样式时，它会改变GridWeb控件的整体外观。开发人员可以使用Aspose.Cells.GridWeb灵活的API在运行时选择要应用的预设样式。

GridWeb控件提供了PresetStyle属性，开发人员可以将任何所需的预设样式分配给它。

下面代码片段的输出显示如下。

**GridWeb控件应用了Colorful1样式**

![todo:image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **标题栏样式**

如果您看一看GridWeb控件，您会注意到有两个标题栏。一个用于列（即A、B、C、D等），另一个用于行（即1、2、3、4等）。Aspose.Cells.GridWeb允许开发人员控制这些标题栏的外观。开发人员可以在运行时设置标题栏的样式。

{{% alert color="primary" %}}

GridWeb控件提供了HeaderBarStyle属性，该属性应用于控件的两个标题栏。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **选项卡栏样式**

也可以设置选项卡栏的样式。请参阅以下代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **加载样式文件**

要将现有样式文件中的样式设置应用到GridWeb控件，开发人员可以将样式文件的路径设置为控件的CustomStyleFileName属性。但在这样做之前，必须将控件的PresetStyle属性设置为Custom。因为样式文件包含开发人员已经定义的自定义样式信息。

请参见以下图片，显示了应用到GridWeb的自定义样式。

![todo:image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

重要提示：将样式文件加载到GridWeb控件中不会影响控件的单元格格式设置。

{{% /alert %}}

#### **示例自定义样式模板**

这是示例自定义样式模板。您可以根据您的需求进行修改。

{{< highlight java >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **在 Web 表单上创建控件**

本文将指导您如何在 JSP（Java 服务器页）上创建具有 GridWeb 控件的简单 Web 表单。

**步骤 1 - 创建目录结构**

您需要在 Tomcat 服务器的 **webapps** 目录下创建以下目录结构

![todo:image_alt_text](working-with-gridweb_7.png)

这些是您需要创建的目录和文件。请阅读注释并按照其指示操作。您可以从[此链接](https://downloads.aspose.com/cells/java)获取最新的 Aspose.Cells.GridWeb for Java 发行版存档。

{{< highlight java >}}

 SamplePageGridWebJava

SamplePageGridWebJava\grid

//Get acwclient directory from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\acwclient

SamplePageGridWebJava\WEB-INF

SamplePageGridWebJava\WEB-INF\lib

//Get aspose-gridweb-x.x.x.jar file from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\WEB-INF\aspose-gridweb-x.x.x.jar

SamplePageGridWebJava\WEB-INF\web.xml

SamplePageGridWebJava\head.jsp

//Create this excel file using Microsoft Excel or you can use any excel file and rename it SampleExcel.xlsx

SamplePageGridWebJava\SampleExcel.xlsx

SamplePageGridWebJava\SamplePage.jsp

{{< /highlight >}}

**步骤 2 - 在创建的文件中添加代码**

此部分显示了上述目录结构中各个文件的代码。请获取这些代码，并通过在记事本中打开文件并复制/粘贴来添加到您的文件中。

**Web.xml**

{{< highlight java >}}

 <?xml version="1.0" encoding="UTF-8"?>

<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://java.sun.com/xml/ns/javaee" xmlns:web="http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" id="WebApp_ID" version="2.5">

  <display-name>testGridWeb</display-name>

  <welcome-file-list>

    <welcome-file>SamplePage.jsp</welcome-file>

  </welcome-file-list>

  <servlet>

    <display-name>GridWebServlet</display-name>

    <servlet-name>GridWebServlet</servlet-name>

    <servlet-class>com.aspose.gridweb.GridWebServlet</servlet-class>

  </servlet>

  <servlet-mapping>

    <servlet-name>GridWebServlet</servlet-name>

    <url-pattern>/GridWebServlet</url-pattern>

  </servlet-mapping>

</web-app>

{{< /highlight >}}

**head.jsp**

{{< highlight java >}}

 <%

String path = request.getContextPath();

String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";

%>

<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9"/>

<base href="<%=basePath%>">

<script type="text/javascript" language="javascript"

	src="grid/acw_client/acwmain.js"></script>

<script type="text/javascript" language="javascript"

	src="grid/acw_client/lang_en.js"></script>

<link href="grid/acw_client/menu.css" rel="stylesheet" type="text/css" />

<style>

span.acwxc {

	overflow: hidden;

	border: none;

	display: block;

	white-space: pre;

}

</style>

<style>

span.rotation90 {

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(-90deg);

	-moz-transform: rotate(-90deg);

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3 );

	display: block

}

</style>

<style>

span.rotation-90 {

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1 );

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(90deg);

	-moz-transform: rotate(90deg);

	display: block

}

</style>

<style>

span.wrap {

	white-space: pre-wrap;

	white-space: -moz-pre-wrap;

	white-space: -pre-wrap;

	white-space: -o-pre-wrap;

	word-wrap: break-word;

	-ms-word-break: break-all;

}

</style>

{{< /highlight >}}

**SamplePage.jsp**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-SamplePage-SamplePage.jsp" >}}

**步骤 3 - 运行您的示例 JSP 网页**

现在您已经完成所有操作。是时候运行网页了。请启动您的 Tomcat 服务器，然后在网络浏览器中粘贴以下 URL。

{{< highlight java >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

您将看到类似以下屏幕截图的内容。恭喜，您已成功在您的 JSP 页面上使用了 GridWeb 控件。

![todo:image_alt_text](working-with-gridweb_8.png)

## **打印 GridWeb**

开发人员有时需要在不保存 Microsoft Excel 文件的情况下从网页中打印 GridWeb 内容。Aspose.Cells.GridWeb 控件支持此功能。

### **打印 GridWeb**

要在不保存单独文件的情况下打印，可以在客户端调用 GridWeb 类的 print() 方法来打印表格。您还可以选择一些适当的事件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

由于您是从客户端调用它，所以您首先要获取 gridweb 的客户端 ID。您可以使用 gridweb.getClientID() 方法获取客户端 ID。

### **客户端示例代码**

请参阅以下链接，从客户端调用gridweb.print()方法。

**HTML**

{{< highlight java >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **不同网格模式介绍**

本文描述Aspose.Cells.GridWeb的不同模式。这些模式在逻辑上由于其不同的特性和行为而有所区别。我们已经确定了不同类型的模式：

- 编辑模式
- 查看模式

所有这些模式都有其自己的特点。开发人员可以根据自己的需求在任何模式下使用Aspose.Cells.GridWeb。我们将逐个查看每种模式。

### **编辑模式**

默认情况下，Aspose.Cells.GridWeb控件处于编辑模式。在编辑模式下，您可以使用Aspose.Cells.GridWeb控件提供的所有功能完全编辑或修改网格内容。这些功能包括：

- 将网格内容保存为Microsoft Excel文件。
- 将数据提交到服务器。
- 计算公式。
- 撤消或放弃之前的操作。
- 管理行和列。
- 剪切、复制或粘贴数据。
- 格式化单元格等。

**编辑模式下的GridWeb控件**

![todo:image_alt_text](working-with-gridweb_9.png)

开发人员还可以通过将GridWeb控件的EditMode属性设置为true来以编程方式切换到编辑模式。

### **代码示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **查看模式**

当GridWeb控件处于查看模式时，用户无法编辑或修改网格内容，这意味着用户只能查看网格内容。这就是为什么这个模式被称为查看模式。在查看模式下，一些按钮（**提交**、**保存**和**撤消**）是隐藏的，右键单击时出现的菜单只包含**复制**和**查找**选项。

**GridWeb控件的查看模式** 

![todo:image_alt_text](working-with-gridweb_10.png)

如果开发人员希望他们的用户只能查看数据，那么他们可以通过将GridWeb控件的EditMode属性设置为**false**来以编程方式切换到查看模式。

### **代码示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

即使在查看模式下，用户也可以更改行和列的高度和宽度。

{{% /alert %}}
