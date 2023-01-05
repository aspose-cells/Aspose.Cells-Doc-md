---
title: Utilizzando OnAjaxCallFinishedClientFunction di GridWeb
type: docs
weight: 20
url: /it/net/using-onajaxcallfinishedclientfunction-of-gridweb/
---
## **Possibili scenari di utilizzo**
OnAjaxCallFinishedClientFunction è una funzione lato client che viene chiamata quando l'utente copia alcuni dati nel foglio di lavoro GridWeb. Questa funzione è utile quando la maggior parte delle celle viene aggiornata e si desidera tenere traccia di tali celle aggiornate sul lato client (ad esempio nei browser Web come FireFox, Google Chrome ecc.).
## **Utilizzando OnAjaxCallFinishedClientFunction di GridWeb**
Il seguente codice di esempio spiega come utilizzare la funzione client OnAjaxCallFinishedClientFunction. Gli screenshot mostrano l'output della console in Google Chrome e FireFox quando il codice viene eseguito. Una volta eseguito il codice, copiare/incollare alcuni dati che si estendono su più celle all'interno del foglio di lavoro GridWeb e quindi controllare la console del browser Web come mostrato negli screenshot.
## **Google Uscita console cromata**
![cose da fare:immagine_alt_testo](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **Uscita console FireFox**
![cose da fare:immagine_alt_testo](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Codice d'esempio**
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
