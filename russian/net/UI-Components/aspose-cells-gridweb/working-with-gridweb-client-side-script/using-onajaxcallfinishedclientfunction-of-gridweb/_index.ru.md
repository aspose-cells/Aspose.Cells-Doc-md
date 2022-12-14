---
title: Использование OnAjaxCallFinishedClientFunction GridWeb
type: docs
weight: 20
url: /ru/net/using-onajaxcallfinishedclientfunction-of-gridweb/
---
## **Возможные сценарии использования**
OnAjaxCallFinishedClientFunction — это функция на стороне клиента, которая вызывается, когда пользователь копирует некоторые данные на лист GridWeb. Эта функция полезна, когда обновляется большое количество ячеек, и вы хотите отслеживать эти обновленные ячейки на стороне клиента (например, в веб-браузерах, таких как FireFox, Google Chrome и т. д.).
## **Использование OnAjaxCallFinishedClientFunction GridWeb**
В следующем примере кода показано, как использовать клиентскую функцию OnAjaxCallFinishedClientFunction. На снимках экрана показан вывод консоли в Google Chrome и FireFox при выполнении кода. После выполнения кода скопируйте/вставьте некоторые данные, охватывающие несколько ячеек, на листе GridWeb, а затем проверьте консоль веб-браузера, как показано на снимках экрана.
## **Google Вывод консоли Chrome**
![дело:изображение_альтернативный_текст](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **Вывод консоли FireFox**
![дело:изображение_альтернативный_текст](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Образец кода**
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
