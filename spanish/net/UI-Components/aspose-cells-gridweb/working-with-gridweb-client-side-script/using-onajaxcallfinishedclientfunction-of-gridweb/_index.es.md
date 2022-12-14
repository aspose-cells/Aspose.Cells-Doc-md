---
title: Usando OnAjaxCallFinishedClientFunction de GridWeb
type: docs
weight: 20
url: /es/net/using-onajaxcallfinishedclientfunction-of-gridweb/
---
## **Posibles escenarios de uso**
OnAjaxCallFinishedClientFunction es una función del lado del cliente que se llama cuando el usuario copia algunos datos en la hoja de trabajo de GridWeb. Esta función es útil cuando se actualiza la mayor parte de las celdas y desea realizar un seguimiento de esas celdas actualizadas en el lado del cliente (es decir, en navegadores web como FireFox, Google Chrome, etc.).
## **Usando OnAjaxCallFinishedClientFunction de GridWeb**
El siguiente código de ejemplo explica cómo utilizar la función de cliente OnAjaxCallFinishedClientFunction. Las capturas de pantalla muestran la salida de la consola en Google Chrome y FireFox cuando se ejecuta el código. Una vez que ejecute el código, copie/pegue algunos datos que abarquen varias celdas dentro de la hoja de trabajo de GridWeb y luego verifique la consola del navegador web como se muestra en las capturas de pantalla.
## **Google Salida de consola cromada**
![todo:imagen_alternativa_texto](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **Salida de la consola FireFox**
![todo:imagen_alternativa_texto](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Código de muestra**
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
