---
title: Rendera interaktiv rullningslist i GridWeb
type: docs
weight: 170
url: /sv/net/render-interactive-scrollbar-in-gridweb/
---
## **Möjliga användningsscenarier**
 Aspose.Cells för GridWeb kan återge interaktiv rullningslistkontroll inuti GridWeb-kalkylbladet. Användaren kan interagera med rullningslisten som de gör i Microsoft Excel. För att skapa interaktiv rullningslist måste du lägga till länkarna för**jQuery** och**jQuery UI** bibliotek som visas nedan.

{{< highlight "java" >}}

 <head runat="server">

	<link rel="stylesheet" href="/Scripts/jquery-ui.css">

	<script src="/Scripts/jquery-2.1.1.js"></script>

	<script src="/Scripts/jquery-ui.js"></script>

</head>

{{< /highlight >}}
## **Rendera interaktiv rullningslist i GridWeb**
 Följande exempelkod laddar[exempel på Excel-fil](61767764.xlsx)som innehåller rullningslisten som visas i följande skärmdump. De andra skärmdumparna visar hur GridWeb renderar interaktiv rullningslist och visar värdet på rullningslisten i cell B3. När du rullar rullningslisten visar värdet för cell B3 det resulterande värdet.

![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_1.png)

![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_2.png)

![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_3.png)

![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_4.png)
## **Exempelkod**
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
