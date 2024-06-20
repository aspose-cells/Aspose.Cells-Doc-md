---
title: Användning av OnAjaxCallFinishedClientFunction från GridWeb
type: docs
weight: 20
url: /sv/net/aspose-cells-gridweb/using-onajaxcallfinishedclientfunction-of-gridweb/
keywords: GridWeb,ajacall,onajaxcallfinishedclientfunction,OnAjaxCallFinishedClientFunction 
description: Denna artikel introducerar hur man arbetar med OnAjaxCallFinishedClientFunction i GridWeb.
---

## **Möjliga användningsscenario**
OnAjaxCallFinishedClientFunction är en klientfunktion som anropas när användaren kopierar några data till GridWeb-kalkylarket. Denna funktion är användbar när många celler uppdateras och du vill hålla koll på dessa uppdaterade celler på klientsidan (dvs. i webbläsare som FireFox, Google Chrome osv.).
## **Användning av OnAjaxCallFinishedClientFunction från GridWeb**
Följande exempelkod förklarar hur man använder OnAjaxCallFinishedClientFunction-klientfunktionen. Skärmbilderna visar konsoloutput i Google Chrome och FireFox när koden körs. När du har kört koden, vänligen kopiera/klistra in några data som spänner över flera celler i GridWeb-kalkylarket och kontrollera sedan webbläsarkonsolen enligt skärmbilderna.
## **Google Chrome Konsoloutput**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **FireFox Konsoloutput**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Exempelkod**
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
