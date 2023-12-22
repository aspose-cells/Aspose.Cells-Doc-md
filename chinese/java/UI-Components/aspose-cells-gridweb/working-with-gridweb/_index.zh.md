---
title: 使用 GridWeb
type: docs
weight: 20
url: /zh/java/working-with-gridweb/
---
##  **打开 Microsoft Excel 文件**

Aspose.Cells.GridWeb 控件可以打开和加载 Microsoft Excel 文件 - 包含数据、格式、图表、图像等。本主题介绍了如何操作。

要使用 GridWeb 控件打开 Excel 文件：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 表单或页面。
1. 通过指定文件路径导入Excel文件。
1. 运行应用程序或打开页面。

要将Excel文件中的内容加载到Aspose.Cells.GridWeb控件中，您必须调用importExcelFile方法来指定Excel文件的路径。之后，GridWeb控件将自动从指定路径查找该文件并显示其中的内容。下面提供了加载 Excel 文件内容的代码片段。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

上面的代码片段可以按照您想要的任何方式使用。例如，要在加载 Web 表单时自动加载 Excel 文件，请将此代码添加到您自己指定的表单的 Page_Load 事件中。

**Excel 文件被加载到 GridWeb 中**

![待办事项：图像_替代_文本](working-with-gridweb_1.png)

##  **保存 Microsoft Excel 文件**

可以使用 Aspose.Cells.GridWeb 控件在 GUI 模式下的网站上创建新的或操作现有的 Microsoft Excel 文件。然后可以将文件保存为 Excel 文件。 Aspose.Cells.GridWeb 有效地充当在线电子表格编辑器。本主题介绍如何将网格内容保存到 Excel 文件。

###  **另存为文件**

要将 Aspose.Cells.GridWeb 控件的内容保存为 Excel 文件：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 表单或页面。
1. 将您的工作另存为 Excel 文件并保存在指定路径中。
1. 运行应用程序或打开页面。

下面的代码示例说明了如何将网格内容保存到 Excel 文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

上面的代码片段可以通过多种方式使用。一种常见的方法是添加一个按钮，单击该按钮即可将网格内容保存到 Excel 文件中。 Aspose.Cells.GridWeb 提供了一种更简单的方法来完成该任务。 Aspose.Cells.GridWeb 有一个名为 SaveCommand 的事件。上面的代码片段可以添加到 SaveCommand 事件的事件处理程序中，该处理程序允许用户通过单击 Aspose.Cells.GridWeb 的内置来保存他们的工作**节省**按钮。

##  **调整Aspose.Cells.GridWeb及其标题栏的大小**

本文介绍了如何使用 Aspose.Cells.GridWeb API 在运行时调整 GridWeb 的大小。还介绍了如何调整 Aspose.Cells.GridWeb 控件的标题栏的大小以使数据更易于阅读。

###  **更改 Aspose.Cells.GridWeb 的宽度和高度**

更改 Aspose.Cells.GridWeb 控件的宽度和高度是一个简单但重要的功能。 Aspose.Cells.GridWeb 控件由 API 中的 GridWeb 类表示。要调整 GridWeb 控件的宽度和高度，只需使用其 width 和 height 属性即可。

{{% alert color="primary" %}}

控件的宽度和高度可以以像素或点为单位定义。

{{% /alert %}}

接下来的代码片段的输出如下所示。

**更改了 GridWeb 控件的宽度和高度**

![待办事项：图像_替代_文本](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

###  **更改标题栏的宽度和高度**

Aspose.Cells.GridWeb控件包含两个标题栏，如下所示：

- 顶部标题栏，该标题栏表示列为 A、B、C、D 等。
- 左侧标题栏，此标题栏表示行为 1、2、3、4 等。

这两个标题栏如下所示。

**标题栏**

![待办事项：图像_替代_文本](working-with-gridweb_3.png)

分别使用 GridWeb 控件的 HeaderBarHeight 和 HeaderBarWidth 属性更改顶部标题栏的高度和左侧标题栏的宽度。下图显示了后续代码示例的输出。

**更改了标题栏的宽度和高度**

![待办事项：图像_替代_文本](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

##  **使用 Aspose.Cells.GridWeb 事件**

所有开发人员都必须熟悉事件及其目的。事件用于发送控件或类中可能发生的更改的通知。 Aspose.Cells.GridWeb 有几个事件，可用于在控件中发生某些更改时执行特定任务。

本主题介绍 Aspose.Cells.GridWeb 控件支持的所有事件以及有关如何处理这些事件的一些详细信息。

###  **网格事件简介**

Aspose.Cells.GridWeb 控件支持多个事件，这些事件可以在控件中触发特定事件时提供更多的控制来执行操作。下面可以找到 Aspose.Cells.GridWeb 控件支持的事件的完整列表。

|**活动**|**描述**|
| :- | :- |
|细胞命令|单击单元格的命令超链接时发生。当此事件被触发时，其参数 e.Argument 提供命令的名称。|
|单元格双击|双击单元格时发生。|
|列已删除|当用户使用客户端菜单从工作表中删除列时发生。|
|删除列|当用户尝试使用客户端菜单从工作表中删除列时发生。|
|列双击|双击列标题时发生。|
|已插入列|当用户使用客户端菜单将列插入工作表时发生。|
|自定义命令|当用户单击自定义命令按钮时发生。|
|加载自定义数据|当控件的 EnableSession 属性设置为 false 并且需要加载工作表数据时发生。您可以在无会话模式下处理此事件，以从文件或数据库加载工作表数据。|
|页面索引已更改|当控件的工作表页面索引更改时发生。|
|已删除行|当用户使用客户端菜单从工作表中删除行时发生。|
|行删除|当用户尝试使用客户端菜单从工作表中删除行时发生。|
|行双击|双击行标题时发生。|
|插入行|当用户使用客户端菜单将行插入工作表时发生。|
|保存命令|发生在**节省**单击按钮。|
|工作表选项卡单击|单击工作表选项卡时发生。|
|提交命令|发生在**提交**单击按钮。|
|撤消命令|发生在**撤消**单击按钮。|
|AjaxCallFinished|当控件的 AJAX 更新完成时触发。 （EnableAJAX 应设置为 true）。|
|CellModifiedOnAjax|在 AJAX 调用中修改单元格时触发。|
|列过滤后|当过滤器应用于列时触发。|

###  **处理网格事件**

要执行触发特定事件的特定操作，我们必须创建一个事件处理程序。当触发某个事件时，事件处理程序将执行所需的任务。下面的示例显示如何处理简单的网格事件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

##  **使用双击事件**

Aspose.Cells.GridWeb包含三种类型的双击事件：

- CellDoubleClick，双击单元格时触发。
- ColumnDoubleClick，双击列标题时触发。
- RowDoubleClick，双击行标题时触发。

本主题讨论如何在 Aspose.Cells.GridWeb 中启用双击事件。它还讨论了为这些事件创建事件处理程序。

###  **启用双击事件**

通过将 GridWeb 控件的 EnableDoubleClickEvent 属性设置为 true，可以在客户端启用所有类型的双击事件。

{{% alert color="primary" %}}

默认情况下，EnableDoubleClickEvent 属性设置为 false。这意味着默认情况下不启用双击事件。要实现此类事件，请首先启用该功能。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

启用双击事件后，就可以为任何双击事件创建事件处理程序。当触发给定的双击事件时，这些事件处理程序执行特定任务。

###  **处理双击事件**

####  **双击Cell**

CellDoubleClick 事件的事件处理程序提供 CellEventArgs 类型的参数，该参数提供双击单元格的完整信息。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

####  **双击列标题**

ColumnDoubleClick 事件的事件处理程序提供 RowColumnEventArgs 类型的参数，该参数提供双击标题的列的索引号和其他信息。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

####  **双击行标题**

RowDoubleClick 事件的事件处理程序提供 RowColumnEventArgs 类型的参数，该参数提供双击标题的行索引号和其他相关信息。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

##  **设置Aspose.Cells.GridWeb的样式或外观**

Aspose.Cells.GridWeb 有自己的默认外观和感觉，但可以更改其外观。 Aspose.Cells.GridWeb提供了几个属性来让开发人员完全控制其外观。本主题讨论其中一些属性。

###  **设置Aspose.Cells.GridWeb的样式或外观**

####  **预设风格**

为了节省开发人员的精力，Aspose.Cells.GridWeb提供了一些预设的样式。只需从列表中选择一种样式即可应用该样式。

|**风格**|**配色方案**|
| :- | :- |
|标准|银|
|多彩1|玫瑰|
|多彩2|蓝色的|
|专业1|青色|
|专业2|再次青色|
|传统1|黑暗的|
|传统2|灰色的|
|风俗|定制|
当选择特定样式时，它会更改 GridWeb 控件的整体外观。开发人员可以使用 Aspose.Cells.GridWeb 的灵活 API 选择要在运行时应用的预设样式。

GridWeb 控件提供 PresetStyle 属性，开发人员可以向该属性分配任何所需的预设样式。

以下代码片段的输出如下所示。

**应用了Colorful1风格的GridWeb控件**

![待办事项：图像_替代_文本](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

####  **标题栏样式**

如果您查看 GridWeb 控件，您会注意到两个标题栏。一种用于列（即 A、B、C、D 等），另一种用于行（即 1、2、3、4 等）。 Aspose.Cells.GridWeb 允许开发人员控制这些标题栏的外观。开发者可以在运行时设置标题栏的样式。

{{% alert color="primary" %}}

GridWeb 控件提供 HeaderBarStyle 属性，该属性可在控件的两个标题栏上应用样式。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

####  **标签栏样式**

也可以设置选项卡栏的样式。请看下面的代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

####  **加载样式文件**

要将现有样式文件中的样式设置应用到 GridWeb 控件，开发人员可以将样式文件的路径设置为控件的 CustomStyleFileName 属性。但是，在执行此操作之前，必须将控件的 PresetStyle 属性设置为 Custom。这是因为该样式文件包含开发人员已定义的自定义样式信息。

请参阅下图，该图显示了应用了自定义样式的 GridWeb。

![待办事项：图像_替代_文本](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

重要信息：将样式文件加载到 GridWeb 控件中不会影响控件单元格的格式设置。

{{% /alert %}}

####  **自定义样式模板示例**

这是自定义样式模板示例。您可以根据您的要求进行修改。

{{< highlight "java" >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

##  **在 Web 窗体上创建控件**

本文将指导您如何创建一个带有 GridWeb 控件的简单 Web 表单 JSP（Java 服务器页）。

**第 1 步 - 创建目录结构**

您需要在目录中创建以下目录结构**网络应用程序**Tomcat服务器目录

![待办事项：图像_替代_文本](working-with-gridweb_7.png)

这些是您需要创建的目录和文件。请阅读评论并关注它们。您可以从以下位置获取最新的 Aspose.Cells.GridWeb for Java 发布档案[这个链接](https://downloads.aspose.com/cells/java).

{{< highlight "java" >}}

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

**第 2 步 - 在创建的文件中添加代码**

本节显示了在上述目录结构中创建的各种文件的代码。请获取这些代码并将其添加到您的文件中，方法是在记事本中打开它们并复制/粘贴。

**网页.xml**

{{< highlight "java" >}}

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

**头.jsp**

{{< highlight "java" >}}

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

**示例页面.jsp**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-SamplePage-SamplePage.jsp" >}}

**第 3 步 - 运行示例 JSP 网页**

现在你已经完成了一切。现在是运行网页的时候了。请启动 Tomcat 服务器，然后将以下 URL 粘贴到 Web 浏览器中。

{{< highlight "java" >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

您将看到类似以下屏幕截图的内容。恭喜，您已经在 JSP 页面上成功使用了 GridWeb 控件。

![待办事项：图像_替代_文本](working-with-gridweb_8.png)

##  **打印网格网页**

有时，开发人员需要打印网页中包含的 GridWeb 内容而不保存 Microsoft Excel 文件。 Aspose.Cells.GridWeb 控件支持此功能。

###  **打印网格网页**

要在不保存单独文件的情况下进行打印，请在客户端调用 GridWeb 类的 print() 方法来打印网格。您也可以选择一些合适的活动。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

由于您是从客户端调用它，因此您必须首先获取 gridweb 客户端 id。您可以使用 gridweb.getClientID() 方法获取客户端 ID。

###  **客户端示例代码**

请参阅以下从客户端调用 gridweb.print() 方法的链接。

**HTML**

{{< highlight "java" >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

##  **不同网格模式简介**

本文介绍了Aspose.Cells.GridWeb的不同模式。这些模式由于其不同的特征和行为而在逻辑上有所区别。我们将不同类型的模式确定为：

- 编辑模式
- 查看模式

所有这些模式都有各自的特点。开发者可以根据自己的需求以任意模式使用Aspose.Cells.GridWeb。我们将在下面看看每种模式。

###  **编辑模式**

默认情况下，Aspose.Cells.GridWeb 控件处于编辑模式。在编辑模式下，您可以使用 Aspose.Cells.GridWeb 控件提供的所有功能完全编辑或修改网格内容。这些功能包括：

- 将网格内容保存到 Microsoft Excel 文件。
- 向服务器提交数据。
- 计算公式。
- 撤消或放弃之前的操作。
- 管理行和列。
- 剪切、复制或粘贴数据。
- 格式化单元格等

**编辑模式下的 GridWeb 控件**

![待办事项：图像_替代_文本](working-with-gridweb_9.png)

开发人员还可以通过将 GridWeb 控件的 EditMode 属性设置为 true，以编程方式切换到编辑模式。

###  **代码示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

###  **查看模式**

当GridWeb控件处于查看模式时，用户无法编辑或修改网格内容，这意味着用户只能查看网格内容。这就是为什么这种模式被称为“查看”模式。在查看模式下，有几个按钮（**提交**、**节省**和**撤消**）被隐藏，右键单击时出现的菜单仅包含**复制**和**寻找**选项。

**查看模式下的 GridWeb 控件** 

![待办事项：图像_替代_文本](working-with-gridweb_10.png)

如果开发人员希望用户仅查看数据，那么他们可以通过将 GridWeb 控件的 EditMode 属性设置为 *false** 以编程方式切换到“查看”模式。

###  **代码示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

即使在“查看”模式下，用户也可以更改行和列的高度和宽度。

{{% /alert %}}
