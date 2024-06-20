---
title: Renderizar barra de desplazamiento interactiva en GridWeb
type: docs
weight: 170
url: /es/net/aspose-cells-gridweb/render-interactive-scrollbar-in-gridweb/
keywords: GridWeb, barra de desplazamiento
description: Este artículo presenta cómo trabajar con la barra de desplazamiento en GridWeb.
---

## **Escenarios de uso posibles**
Aspose.Cells for GridWeb puede renderizar el control de barra de desplazamiento interactiva dentro de la hoja de cálculo de GridWeb. El usuario puede interactuar con la barra de desplazamiento como lo hace en Microsoft Excel. Para crear una barra de desplazamiento interactiva, debe agregar los enlaces para las bibliotecas de **jQuery** y **jQuery UI** como se muestra a continuación.

{{< highlight java >}}

 <head runat="server">

	<link rel="stylesheet" href="/Scripts/jquery-ui.css">

	<script src="/Scripts/jquery-2.1.1.js"></script>

	<script src="/Scripts/jquery-ui.js"></script>

</head>

{{< /highlight >}}
## **Renderizar barra de desplazamiento interactiva en GridWeb**
El siguiente código de muestra carga el [archivo Excel de ejemplo](61767764.xlsx) que contiene la barra de desplazamiento como se muestra en la siguiente captura de pantalla. Las demás capturas de pantalla muestran cómo GridWeb renderiza la barra de desplazamiento interactiva y muestra el valor de la barra de desplazamiento en la celda B3. Cada vez que se desplaza la barra de desplazamiento, el valor de la celda B3 muestra el valor resultante.

![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_1.png)

![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_2.png)

![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_3.png)

![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_4.png)
## **Código de muestra**
{{< highlight java >}}

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
