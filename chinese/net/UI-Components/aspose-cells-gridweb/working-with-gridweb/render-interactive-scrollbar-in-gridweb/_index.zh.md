---
title: 在 GridWeb 中渲染交互式滚动条
type: docs
weight: 170
url: /zh/net/render-interactive-scrollbar-in-gridweb/
---
## **可能的使用场景**
Aspose.Cells for GridWeb 可以在 GridWeb 工作表内呈现交互式滚动条控件。用户可以像在 Microsoft Excel 中一样与滚动条交互。为了创建交互式滚动条，您必须添加链接**查询**和**用户界面**库如下所示。

{{< highlight "java" >}}

 <head runat="server">

	<link rel="stylesheet" href="/Scripts/jquery-ui.css">

	<script src="/Scripts/jquery-2.1.1.js"></script>

	<script src="/Scripts/jquery-ui.js"></script>

</head>

{{< /highlight >}}
## **在 GridWeb 中渲染交互式滚动条**
下面的示例代码加载[示例 Excel 文件](61767764.xlsx)包含滚动条，如以下屏幕截图所示。其他屏幕截图显示了 GridWeb 如何呈现交互式滚动条并在单元格 B3 中显示滚动条的值。无论何时滚动滚动条，单元格 B3 的值都会显示结果值。

![待办事项：图片_替代_文本](render-interactive-scrollbar-in-gridweb_1.png)

![待办事项：图片_替代_文本](render-interactive-scrollbar-in-gridweb_2.png)

![待办事项：图片_替代_文本](render-interactive-scrollbar-in-gridweb_3.png)

![待办事项：图片_替代_文本](render-interactive-scrollbar-in-gridweb_4.png)
## **示例代码**
{{< highlight "java" >}}

 <%@ Page Language="C#" AutoEventWireup="true" CodeFile="TestGridWeb.aspx.cs" Inherits="TestGridWeb" %>

<%@ Register TagPrefix="acw" Namespace="Aspose.Cells.GridWeb" Assembly="Aspose.Cells.GridWeb" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head runat="server">



	<link rel="stylesheet" href="/Scripts/jquery-ui.css">

	<script src="/Scripts/jquery-2.1.1.js"></script>

	<script src="/Scripts/jquery-ui.js"></script>



    <title>Test GridWeb</title>

</head>

<body>

    <form id="form1" runat="server">

        <div>

            <div>

                <b>GridWeb Version:&nbsp </b>

                <asp:Label ID="lblVersion" runat="server" Text="Label"></asp:Label>

                <br />

            </div>

            <acw:GridWeb ID="GridWeb1" runat="server" XhtmlMode="True" Height="504px" Width="1119px">

            </acw:GridWeb>

        </div>

    </form>

</body>

</html>

\--------------------------------------------

\--------------------------------------------

\--------------------------------------------

using System;

using System.Collections;

using System.Configuration;

using System.Data;

using System.Linq;

using System.Web;

using System.Web.Security;

using System.Web.UI;

using System.Web.UI.HtmlControls;

using System.Web.UI.WebControls;

using System.Web.UI.WebControls.WebParts;

using System.Xml.Linq;

using System.IO;

using Aspose.Cells;

using Aspose.Cells.GridWeb.Data;

using Aspose.Cells.GridWeb;

using System.Globalization;

using System.Threading;

using System.Collections.Generic;

public partial class TestGridWeb : System.Web.UI.Page

{

    protected void Page_Load(object sender, EventArgs e)

    {

        if (Page.IsPostBack == false && this.GridWeb1.IsPostBack == false)

        {

            lblVersion.Text = GridWeb.GetVersion();

            string fileName = "sampleRenderScrollbarInGridWeb.xlsx";

            string filePath = Server.MapPath("~/ExcelFile/" + fileName);

            GridWeb1.ImportExcelFile(filePath);

        }

    }

}


{{< /highlight >}}
