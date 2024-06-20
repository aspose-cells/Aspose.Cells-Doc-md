---
title: GridWebのOnAjaxCallFinishedClientFunctionの使用
type: docs
weight: 20
url: /ja/net/aspose-cells-gridweb/using-onajaxcallfinishedclientfunction-of-gridweb/
keywords: GridWeb,ajacall,onajaxcallfinishedclientfunction,OnAjaxCallFinishedClientFunction 
description: この記事では、GridWebでOnAjaxCallFinishedClientFunctionを使用する方法について紹介します。
---

## **可能な使用シナリオ**
OnAjaxCallFinishedClientFunctionは、ユーザーがデータをGridWebのワークシートにコピーするときに呼び出されるクライアント側の関数です。この関数は、大量のセルが更新され、それらの更新されたセルをクライアント側（たとえばFireFox、Google ChromeなどのWebブラウザ）で追跡したいときに役立ちます。
## **GridWebのOnAjaxCallFinishedClientFunctionの使用**
次のサンプルコードは、OnAjaxCallFinishedClientFunctionクライアント関数を使用する方法を説明しています。スクリーンショットでは、コードを実行したときにGoogle ChromeとFireFoxでコンソール出力が表示されています。コードを実行した後、GridWebワークシート内に複数のセルにわたるデータをコピー/貼り付けし、その後、スクリーンショットに表示されているようにWebブラウザのコンソールをチェックしてください。
## **Google Chromeのコンソール出力**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **FireFoxのコンソール出力**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **サンプルコード**
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
