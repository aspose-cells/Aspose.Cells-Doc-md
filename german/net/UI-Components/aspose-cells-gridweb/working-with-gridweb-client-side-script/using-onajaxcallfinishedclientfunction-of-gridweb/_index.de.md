---
title: Verwendung der OnAjaxCallFinishedClientFunction von GridWeb
type: docs
weight: 20
url: /de/net/aspose-cells-gridweb/using-onajaxcallfinishedclientfunction-of-gridweb/
keywords: GridWeb,ajacall,onajaxcallfinishedclientfunction,OnAjaxCallFinishedClientFunction 
description: Dieser Artikel zeigt, wie man mit OnAjaxCallFinishedClientFunction in GridWeb arbeitet.
---

## **Mögliche Verwendungsszenarien**
OnAjaxCallFinishedClientFunction ist eine clientseitige Funktion, die aufgerufen wird, wenn ein Benutzer einige Daten in das GridWeb-Arbeitsblatt kopiert. Diese Funktion ist hilfreich, wenn eine Vielzahl von Zellen aktualisiert wird und Sie den Überblick über diese aktualisierten Zellen auf der Client-Seite behalten möchten (z. B. in Webbrowsern wie FireFox, Google Chrome usw.).
## **Verwendung der OnAjaxCallFinishedClientFunction von GridWeb**
Der folgende Beispielcode erläutert, wie die OnAjaxCallFinishedClientFunction-Clientfunktion genutzt werden kann. Die Screenshots zeigen die Konsolenausgabe in Google Chrome und FireFox, wenn der Code ausgeführt wird. Nachdem Sie den Code ausgeführt haben, kopieren/einfügen Sie bitte einige Daten, die mehrere Zellen im GridWeb-Arbeitsblatt umfassen, und überprüfen Sie dann die Webbrowserkonsole wie in den Screenshots dargestellt.
## **Konsolenausgabe in Google Chrome**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **Konsolenausgabe in FireFox**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Beispielcode**
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
