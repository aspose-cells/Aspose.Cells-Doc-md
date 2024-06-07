---
title: 使用GridWeb的OnAjaxCallFinishedClientFunction
type: docs
weight: 20
url: /zh/net/aspose-cells-gridweb/using-onajaxcallfinishedclientfunction-of-gridweb/
keywords: GridWeb,ajacall,onajaxcallfinishedclientfunction,OnAjaxCallFinishedClientFunction 
description: 本文介绍了如何在GridWeb中使用OnAjaxCallFinishedClientFunction。
---

## **可能的使用场景**
OnAjaxCallFinishedClientFunction是客户端函数，当用户将一些数据复制到GridWeb工作表时调用。当大量单元格被更新时，使用此函数会帮助您在客户端（如FireFox、Google Chrome等Web浏览器）上跟踪这些更新的单元格。
## **使用GridWeb的OnAjaxCallFinishedClientFunction**
以下示例代码解释了如何使用OnAjaxCallFinishedClientFunction客户端函数。当代码执行时，屏幕截图展示了在Google Chrome和FireFox中的控制台输出。执行代码后，请复制/粘贴一些跨多个单元格的数据到GridWeb工作表中，然后检查屏幕截图中所示的Web浏览器控制台。
## **Google Chrome控制台输出**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **FireFox控制台输出**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **示例代码**
{{< highlight java >}}

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
