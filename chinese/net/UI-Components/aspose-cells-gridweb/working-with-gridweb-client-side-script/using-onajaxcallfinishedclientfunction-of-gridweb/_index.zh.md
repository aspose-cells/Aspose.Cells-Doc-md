---
title: 使用 GridWeb 的 OnAjaxCallFinishedClientFunction
type: docs
weight: 20
url: /zh/net/using-onajaxcallfinishedclientfunction-of-gridweb/
---
## **可能的使用场景**
OnAjaxCallFinishedClientFunction 是一个客户端函数，当用户将一些数据复制到 GridWeb 工作表时调用它。当大量单元格更新并且您希望在客户端跟踪这些更新的单元格时（即在 FireFox、Google Chrome 等网络浏览器中），此功能很有用。
## **使用 GridWeb 的 OnAjaxCallFinishedClientFunction**
以下示例代码解释了如何使用 OnAjaxCallFinishedClientFunction 客户端函数。屏幕截图显示了执行代码时 Google Chrome 和 FireFox 中的控制台输出。执行代码后，请在 GridWeb 工作表中复制/粘贴一些跨越多个单元格的数据，然后检查 Web 浏览器控制台，如屏幕截图所示。
## **Google Chrome 控制台输出**
![待办事项：图片_替代_文本](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **FireFox 控制台输出**
![待办事项：图片_替代_文本](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **示例代码**
{{< highlight "java" >}}

 //-------------------------------------------------------

//------TestGridWeb.aspx---------------------------------

//-------------------------------------------------------

//

<%@ Page Language="C#" AutoEventWireup="true" CodeFile="TestGridWeb.aspx.cs" Inherits="TestGridWeb" %>

<%@ Register TagPrefix="acw" Namespace="Aspose.Cells.GridWeb" Assembly="Aspose.Cells.GridWeb" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head runat="server">

    <title>Test GridWeb</title>

    <script type="text/javascript">



    var updateCells = new Array();



    function TestAjaxCallFinish()

    {

        for (var i = 0; i < updateCells.length; i++) {

            console.log("updated:" + toString(this,updateCells[i]));

        }

        updateCells = [];

    }

    function CellUpdate(cell) {

        var id = updateCells.length;

        updateCells[id++] = cell;

    }

    function toString(gridweb,cell) {

        return gridweb.getCellName(cell) +

            ",value is:" +

            gridweb.getCellValueByCell(cell) +

            " ,row:" +

            gridweb.getCellRow(cell) +

            ",col:" +

            gridweb.getCellColumn(cell);

    }

</script>

</head>

<body>

    <form id="form1" runat="server">

        <div>

            <div>

                <b>GridWeb Version:&nbsp </b>

                <asp:Label ID="lblVersion" runat="server" Text="Label"></asp:Label>

                <br />

            </div>

            <acw:GridWeb ID="GridWeb1" runat="server" XhtmlMode="True" Height="504px" Width="1119px" EnableAJAX="true" OnAjaxCallFinishedClientFunction="TestAjaxCallFinish" OnCellUpdatedClientFunction="CellUpdate">

            </acw:GridWeb>

        </div>

    </form>

</body>

</html>

//-------------------------------------------------------

//------TestGridWeb.aspx.cs------------------------------

//-------------------------------------------------------

//

using System;

using System.Web.UI;

using Aspose.Cells.GridWeb;

public partial class TestGridWeb : System.Web.UI.Page

{

    protected void Page_Load(object sender, EventArgs e)

    {

        if (Page.IsPostBack == false && this.GridWeb1.IsPostBack == false)

        {

            lblVersion.Text = GridWeb.GetVersion();

        }

    }

}

{{< /highlight >}}
