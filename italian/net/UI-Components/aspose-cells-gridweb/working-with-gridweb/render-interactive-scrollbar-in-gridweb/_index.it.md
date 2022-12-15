---
title: Renderizza la barra di scorrimento interattiva in GridWeb
type: docs
weight: 170
url: /it/net/render-interactive-scrollbar-in-gridweb/
---
## **Possibili scenari di utilizzo**
 Aspose.Cells per GridWeb può eseguire il rendering del controllo interattivo della barra di scorrimento all'interno del foglio di lavoro GridWeb. L'utente può interagire con la barra di scorrimento come in Microsoft Excel. Per creare una barra di scorrimento interattiva, è necessario aggiungere i collegamenti per**jQuery** e**interfaccia utente jQuery** librerie come mostrato di seguito.

{{< highlight "java" >}}

 <head runat="server">

	<link rel="stylesheet" href="/Scripts/jquery-ui.css">

	<script src="/Scripts/jquery-2.1.1.js"></script>

	<script src="/Scripts/jquery-ui.js"></script>

</head>

{{< /highlight >}}
## **Renderizza la barra di scorrimento interattiva in GridWeb**
 Il codice di esempio seguente carica il file[esempio di file Excel](61767764.xlsx)contenente la barra di scorrimento come mostrato nello screenshot seguente. Gli altri screenshot mostrano come GridWeb esegue il rendering della barra di scorrimento interattiva e visualizza il valore della barra di scorrimento nella cella B3. Ogni volta che si scorre la barra di scorrimento, il valore della cella B3 mostra il valore risultante.

![cose da fare:immagine_alt_testo](render-interactive-scrollbar-in-gridweb_1.png)

![cose da fare:immagine_alt_testo](render-interactive-scrollbar-in-gridweb_2.png)

![cose da fare:immagine_alt_testo](render-interactive-scrollbar-in-gridweb_3.png)

![cose da fare:immagine_alt_testo](render-interactive-scrollbar-in-gridweb_4.png)
## **Codice di esempio**
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
