---
title: 与GridWeb一起工作
type: docs
weight: 20
url: /zh/java/working-with-gridweb/
---

## **打开Microsoft Excel文件**

Aspose.Cells.GridWeb控件可以打开和加载Microsoft Excel文件-包括数据、格式、图表、图像等。本主题解释了如何操作。

使用GridWeb控件打开Excel文件：

1. 将Aspose.Cells.GridWeb控件添加到Web表单或页面。
1.通过指定文件路径导入Excel文件
1. 运行应用程序或打开页面。

要将Excel文件的内容加载到Aspose.Cells.GridWeb控件中，您必须调用importExcelFile方法以指定Excel文件的路径。之后，GridWeb控件将自动从指定路径找到文件并在其中显示其内容。提供了加载Excel文件内容的代码片段。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

上述代码片段可随意使用。例如，要在Web表单加载时自动加载Excel文件，请将此代码添加到您自己指定的表单的Page_Load事件中。

**Excel文件已加载到GridWeb中**

![todo:image_alt_text](working-with-gridweb_1.png)

## **保存Microsoft Excel文件**

可以在网站上使用Aspose.Cells.GridWeb控件以GUI模式创建新的或操作现有的Microsoft Excel文件。 然后可以将这些文件保存为Excel文件。 Aspose.Cells.GridWeb有效地充当在线电子表格编辑器。 本主题介绍了如何将网格内容保存为Excel文件。

### **保存为文件**

将 Aspose.Cells.GridWeb 控件的内容保存为 Excel 文件：

1. 将Aspose.Cells.GridWeb控件添加到Web表单或页面。
1. 将您的工作保存为指定路径的 Excel 文件。
1. 运行应用程序或打开页面。

下面的代码示例说明了如何将网格内容保存为 Excel 文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

上述代码片段可以以多种方式使用。 一种常见的方法是添加一个按钮，当单击时将网格内容保存到Excel文件。 Aspose.Cells.GridWeb为此任务提供了一种更简便的方法。 Aspose.Cells.GridWeb具有一个名为SaveCommand的事件。 上述代码片段可以添加到SaveCommand事件的事件处理程序中，从而允许用户通过单击Aspose.Cells.GridWeb的内置**保存**按钮保存他们的工作。

## **调整Aspose.Cells.GridWeb及其标题栏的大小**

本文说明了如何在运行时使用Aspose.Cells.GridWeb API调整GridWeb的大小。 还解释了如何调整Aspose.Cells.GridWeb控件的标题栏大小，以使其数据更易于阅读。

### **更改Aspose.Cells.GridWeb的宽度和高度**

更改Aspose.Cells.GridWeb控件的宽度和高度是一项简单但重要的功能。Aspose.Cells.GridWeb控件在API中由GridWeb类表示。要调整GridWeb控件的宽度和高度，只需使用其宽度和高度属性。

{{% alert color="primary" %}}

控件的宽度和高度可以以像素或点数定义。

{{% /alert %}}

以下代码片段的输出如下所示。

**更改GridWeb控件的宽度和高度**

![todo:image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **更改标题栏的宽度和高度**

Aspose.Cells.GridWeb控件包含两个标题栏，如下所示:

- 顶部标题栏，该标题栏代表列，如A、B、C、D等。
- 左侧标题栏，该标题栏代表行，如1、2、3、4等。

这两个标题栏如下所示。

**标题栏**

![todo:image_alt_text](working-with-gridweb_3.png)

使用GridWeb控件的HeaderBarHeight和HeaderBarWidth属性分别更改顶部标题栏和左侧标题栏的高度。下面的图片展示了接下来的代码示例的输出。

**已更改的标题栏宽度和高度**

![todo:image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **处理Aspose.Cells.GridWeb事件**

所有开发人员都必须熟悉事件及其目的。 事件用于发送可能发生在控件或类中的更改的通知。 Aspose.Cells.GridWeb具有几个事件，可用于在控件中发生特定更改时执行特定任务。

本主题介绍了 Aspose.Cells.GridWeb 控件支持的所有事件以及如何处理这些事件的一些细节。

### **网格事件简介**

Aspose.Cells.GridWeb 控件支持多个事件，可以在控件中触发特定事件时提供更多控制以执行操作。您可以在下面找到 Aspose.Cells.GridWeb 控件支持的事件的完整列表。

|**事件**|**描述**|
| :- | :- |
|CellCommand|当单元格的超链接命令被点击时触发。当此事件被触发时，其参数e.Argument提供该命令的名称。|
|CellDoubleClick|当双击单元格时发生。|
|ColumnDeleted|用户使用客户端菜单从工作表中删除列时发生。|
|ColumnDeleting|当用户尝试使用客户端菜单从工作表中删除列时发生。|
|ColumnDoubleClick|当双击列标题时发生。|
|ColumnInserted|当用户使用客户端菜单在工作表中插入列时发生。|
|CustomCommand|当用户点击自定义命令按钮时发生。|
|LoadCustomData|当控件的EnableSession属性设置为false且需要加载工作表数据时发生。您可以在无会话模式下处理此事件以从文件或数据库加载工作表数据。|
|PageIndexChanged|当控件的工作表页索引更改时发生。|
|RowDeleted|当用户使用客户端菜单从工作表中删除行时发生。|
|RowDeleting|当用户尝试使用客户端菜单从工作表中删除行时发生。|
|RowDoubleClick|当双击行标题时发生。|
|RowInserted|当用户使用客户端菜单在工作表中插入行时发生。|
|SaveCommand|单击“保存”按钮时发生。|
|SheetTabClick|单击工作表选项卡时发生。|
|SubmitCommand|单击“提交”按钮时发生。|
|UndoCommand|单击“撤消”按钮时发生。|
|AjaxCallFinished|控件的AJAX更新完成后触发。(EnableAJAX应设置为true)。|
|CellModifiedOnAjax|AJAX调用中修改单元格时触发。|
|AfterColumnFilter|在列上应用过滤器时触发。|

### **处理网格事件**

要在触发特定事件时执行特定操作，我们必须创建一个事件处理程序。事件处理程序在特定事件触发时执行所需的任务。以下示例显示了如何处理简单网格事件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **处理双击事件**

Aspose.Cells.GridWeb 包含三种类型的双击事件：

- 当双击单元格时触发 CellDoubleClick。
- 当双击列标题时触发 ColumnDoubleClick。
- 当双击行标题时触发 RowDoubleClick。

本主题讨论如何在 Aspose.Cells.GridWeb 中启用双击事件。它还讨论了为这些事件创建事件处理程序。

### **启用双击事件**

可以通过设置 GridWeb 控件的 EnableDoubleClickEvent 属性为 true 在客户端启用所有类型的双击事件。

{{% alert color="primary" %}}

默认情况下，EnableDoubleClickEvent 属性设置为 false。这意味着默认情况下未启用双击事件。要实现这些事件，首先要启用该功能。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

一旦启用双击事件，就可以为任何双击事件创建事件处理程序。这些事件处理程序在触发给定双击事件时执行特定任务。

### **处理双击事件**

#### **双击单元格**

CellDoubleClick 事件处理程序提供了 CellEventArgs 类型的参数，提供了双击的单元格的完整信息。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **双击列标题**

ColumnDoubleClick 事件处理程序提供了 RowColumnEventArgs 类型的参数，该参数提供了双击的列标题的索引号以及其他信息。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **双击行标题**

RowDoubleClick 事件处理程序提供了 RowColumnEventArgs 类型的参数，该参数提供了双击的行标题的索引号以及其他相关信息。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **设置 Aspose.Cells.GridWeb 的样式或外观**

Aspose.Cells.GridWeb 有自己的默认外观，但可以更改外观。Aspose.Cells.GridWeb 提供多个属性，让开发人员完全控制其外观。本主题讨论了其中一些属性。

### **设置 Aspose.Cells.GridWeb 的样式或外观**

#### **预设样式**

为了节省开发人员的精力，Aspose.Cells.GridWeb 提供了一些预设样式。只需从列表中选择一个样式即可应用该样式。

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
选择特定样式后，会更改 GridWeb 控件的整体外观。开发人员可以使用 Aspose.Cells.GridWeb 灵活的 API 在运行时选择要应用的预设样式。

GridWeb 控件提供 PresetStyle 属性，开发人员可以将任何所需的预设样式分配给它。

以下代码片段的输出如下所示。

**应用 Colorful1 样式的 GridWeb 控件**

![todo:image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **标题栏样式**

如果查看 GridWeb 控件，您会注意到两个标题栏。一个用于列（即 A、B、C、D 等），另一个用于行（即 1、2、3、4 等）。Aspose.Cells.GridWeb 允许开发人员控制这些标题栏的外观。开发人员可以在运行时设置标题栏的样式。

{{% alert color="primary" %}}

GridWeb控件提供了HeaderBarStyle属性，可应用于控件的两个标题栏。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **选项卡栏样式**

也可以设置标签栏的样式。请参阅以下代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **加载样式文件**

要将现有样式文件中的样式设置应用于GridWeb控件，开发人员可以将样式文件的路径设置为控件的CustomStyleFileName属性。但在此之前，必须将控件的PresetStyle属性设置为Custom。这是因为样式文件包含已由开发人员定义的自定义样式信息。

请查看以下图片，显示了应用于GridWeb的自定义样式

![todo:image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

重要提示：将样式文件加载到GridWeb控件中不会影响控件的单元格格式设置。

{{% /alert %}}

#### **示例自定义样式模板**

这是一个示例自定义样式模板。您可以根据需要进行修改。

{{< highlight java >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **在Web表单上创建控件**

本文将指导您如何在一个简单的Web表单JSP（Java Server Page）上创建一个带有GridWeb控件的控件。

**步骤1-创建目录结构**

您需要在Tomcat服务器的**webapps**目录中创建以下目录结构

![todo:image_alt_text](working-with-gridweb_7.png)

这些是您需要创建的目录和文件。请阅读注释并遵循它们。您可以从[此链接](https://downloads.aspose.com/cells/java)获取最新的Aspose.Cells.GridWeb for Java发行存档。

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

**步骤2-在已创建的文件中添加代码**

此部分显示了上述目录结构中创建的各个文件的代码。请获取这些代码，并通过在记事本中打开文件并复制/粘贴它们的方式将它们添加到您的文件中。

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

**步骤3-运行您的示例JSP Web页面**

现在您已经完成一切。是时候运行web页面了。请启动Tomcat服务器，然后在Web浏览器中粘贴以下URL。

{{< highlight java >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

您将看到类似以下截屏的内容。恭喜，您已成功在JSP页面上使用了GridWeb控件。

![todo:image_alt_text](working-with-gridweb_8.png)

## **打印GridWeb**

有时候开发人员需要打印包含在网页中的GridWeb内容，而不是保存为Microsoft Excel文件。Aspose.Cells.GridWeb控件支持此功能

### **打印GridWeb**

要打印而不保存单独的文件，请在客户端调用GridWeb类的print()方法来打印表格。您也可以选择适当的事件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

由于您是从客户端调用的，所以您首先需要获取gridweb客户端ID。您可以使用gridweb.getClientID()方法获取客户端ID。

### **客户端代码示例**

请查看下面的链接，从客户端调用gridweb.print()方法。

**HTML**

{{< highlight java >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **不同网格模式简介**

本文描述了Aspose.Cells.GridWeb的不同模式。这些模式在逻辑上由于其不同的特性和行为而有所区别。我们已经确定了不同类型的模式如下:

- 编辑模式
- 查看模式

所有这些模式都有其特点。开发人员可以根据自己的需求在任何模式下使用Aspose.Cells.GridWeb。我们将在下面介绍每种模式。

### **编辑模式**

默认情况下，Aspose.Cells.GridWeb控件处于编辑模式。在编辑模式下，您可以完全编辑或修改网格内容，使用Aspose.Cells.GridWeb控件提供的所有功能。这些功能包括:

- 将网格内容保存到Microsoft Excel文件中。
- 将数据提交到服务器。
- 计算公式。
- 撤销或放弃以前的操作。
- 管理行和列。
- 剪切、复制或粘贴数据。
- 设置单元格格式等。

**编辑模式中的GridWeb控件**

![todo:image_alt_text](working-with-gridweb_9.png)

开发人员还可以通过将GridWeb控件的EditMode属性设置为true来以编程方式切换到编辑模式。

### **代码示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **查看模式**

当GridWeb控件处于查看模式时，用户无法编辑或修改网格内容，这意味着用户只能查看网格内容。这就是为什么这个模式称为查看模式。在查看模式下，一些按钮（**提交**、**保存**和**撤消**）被隐藏，右键单击时出现的菜单只包含**复制**和**查找**选项。

**GridWeb 控件处于查看模式** 

![todo:image_alt_text](working-with-gridweb_10.png)

如果开发人员希望他们的用户只能查看数据，则可以通过将GridWeb控件的EditMode属性设置为**false**来以编程方式切换到查看模式。

### **代码示例**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

即使在查看模式下，用户也可以更改行和列的高度和宽度。

{{% /alert %}}
