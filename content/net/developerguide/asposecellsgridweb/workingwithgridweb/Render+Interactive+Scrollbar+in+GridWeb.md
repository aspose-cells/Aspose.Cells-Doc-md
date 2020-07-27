+++
title = "Render Interactive Scrollbar in GridWeb" 
description = "" 
weight = 16676 
+++

Aspose.Cells for .NET : Render Interactive Scrollbar in GridWeb  

# Aspose.Cells for .NET : Render Interactive Scrollbar in GridWeb


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#RenderInteractiveScrollbarinGridWeb-PossibleUsageScenarios)
*   2 [Render Interactive Scrollbar in GridWeb](#RenderInteractiveScrollbarinGridWeb-RenderInteractiveScrollbarinGridWeb)
*   3 [Sample Code](#RenderInteractiveScrollbarinGridWeb-SampleCode)
{{< /panel >}}
 

## Possible Usage Scenarios

Aspose.Cells for GridWeb can render interactive scroll bar control inside the GridWeb worksheet. User can interact with the scroll bar like they do in Microsoft Excel. In order to create interactive scroll bar, you must add the links for **jQuery** and **jQuery UI** libraries as shown below.

{{< code lang="cs" >}}
<head runat="server">
	<link rel="stylesheet" href="/Scripts/jquery-ui.css">
	<script src="/Scripts/jquery-2.1.1.js"></script>
	<script src="/Scripts/jquery-ui.js"></script>
</head>
{{< /code >}}

## Render Interactive Scrollbar in GridWeb

The following sample code loads the [sample Excel file](https://docs2.aspose.com/cells/net/attachments/61540702/61767764.xlsx) containing the scroll bar as shown in the following screenshot. The other screenshots show how the GridWeb renders interactive scroll bar and displays the value of scroll bar in cell B3. Whenever you scroll the scroll bar, the value of cell B3 shows the resulting value.

![](https://docs2.aspose.com/cells/net/attachments/61540702/61767763.png)

![](https://docs2.aspose.com/cells/net/attachments/61540702/61767760.png)

![](https://docs2.aspose.com/cells/net/attachments/61540702/61767761.png)

![](https://docs2.aspose.com/cells/net/attachments/61540702/61767762.png)

## Sample Code

{{< code lang="cs" >}}
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

--------------------------------------------
--------------------------------------------
--------------------------------------------

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

{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Render-Scrollbar-in-GridWeb-1.png](https://docs2.aspose.com/cells/net/attachments/61540702/61767834.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Render-Scrollbar-in-GridWeb-3.png](https://docs2.aspose.com/cells/net/attachments/61540702/61767836.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Render-Scrollbar-in-GridWeb-2.png](https://docs2.aspose.com/cells/net/attachments/61540702/61767835.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Render-Scrollbar-in-GridWeb-4.png](https://docs2.aspose.com/cells/net/attachments/61540702/61767833.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sampleRenderScrollbarInGridWeb.xlsx](https://docs2.aspose.com/cells/net/attachments/61540702/61767837.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Render-Scrollbar-in-GridWeb-4.png](https://docs2.aspose.com/cells/net/attachments/61540702/61767763.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Render-Scrollbar-in-GridWeb-1.png](https://docs2.aspose.com/cells/net/attachments/61540702/61767760.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Render-Scrollbar-in-GridWeb-2.png](https://docs2.aspose.com/cells/net/attachments/61540702/61767761.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Render-Scrollbar-in-GridWeb-3.png](https://docs2.aspose.com/cells/net/attachments/61540702/61767762.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sampleRenderScrollbarInGridWeb.xlsx](https://docs2.aspose.com/cells/net/attachments/61540702/61767764.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

