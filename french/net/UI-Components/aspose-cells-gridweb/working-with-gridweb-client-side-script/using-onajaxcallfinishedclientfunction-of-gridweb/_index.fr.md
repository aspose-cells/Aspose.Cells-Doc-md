---
title: Utilisation de la fonction OnAjaxCallFinishedClient de GridWeb
type: docs
weight: 20
url: /fr/net/using-onajaxcallfinishedclientfunction-of-gridweb/
---
## **Scénarios d'utilisation possibles**
OnAjaxCallFinishedClientFunction est une fonction côté client qui est appelée lorsque l'utilisateur copie des données dans la feuille de calcul GridWeb. Cette fonction est utile lorsque la plupart des cellules sont mises à jour et que vous souhaitez conserver la trace de ces cellules mises à jour côté client (c'est-à-dire dans les navigateurs Web tels que FireFox, Google Chrome, etc.).
## **Utilisation de la fonction OnAjaxCallFinishedClient de GridWeb**
L'exemple de code suivant explique comment utiliser la fonction client OnAjaxCallFinishedClientFunction. Les captures d'écran montrent la sortie de la console dans Google Chrome et FireFox lorsque le code est exécuté. Une fois que vous avez exécuté le code, veuillez copier/coller des données couvrant plusieurs cellules à l'intérieur de la feuille de calcul GridWeb, puis vérifiez la console du navigateur Web, comme indiqué dans les captures d'écran.
## **Google Sortie de console chromée**
![tâche : image_autre_texte](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **Sortie de la console Firefox**
![tâche : image_autre_texte](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Exemple de code**
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
