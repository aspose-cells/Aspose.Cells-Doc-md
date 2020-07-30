---
title : "Using OnAjaxCallFinishedClientFunction of GridWeb" 
description : "" 
weight : 16679 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridwebclientsidescript/using+onajaxcallfinishedclientfunction+of+gridweb/
---

# Aspose.Cells for .NET : Using OnAjaxCallFinishedClientFunction of GridWeb


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Using OnAjaxCallFinishedClientFunction of GridWeb](#using-onajaxcallfinishedclientfunction-of-gridweb)
*   3 [Google Chrome Console Output](#google-chrome-console-output)
*   4 [FireFox Console Output](#firefox-console-output)
*   5 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

`OnAjaxCallFinishedClientFunction` is a client side function which is called when user copies some data to GridWeb worksheet. This function is helpful when bulk of cells are updated and you want to keep the track of those updated cells at client side (i.e. in web browsers like FireFox, Google Chrome etc.).

## Using OnAjaxCallFinishedClientFunction of GridWeb

The following sample code explains how to make use of `OnAjaxCallFinishedClientFunction` client function. The screenshots show the console output in Google Chrome and FireFox when the code is executed. Once, you execute the code, please copy/paste some data spanning multiple cells inside the GridWeb worksheet and then check the Web Browser Console as shown in screenshots.

## Google Chrome Console Output

![](https://docs2.aspose.com/cells/net/attachments/45909138/46465059.png)

## FireFox Console Output

![](https://docs2.aspose.com/cells/net/attachments/45909138/46465058.png)

## Sample Code

{{< code lang="cs" >}}
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
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Using-OnAjaxCallFinishedClientFunction-of-GridWeb-FireFox.png](https://docs2.aspose.com/cells/net/attachments/45909138/46465058.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Using-OnAjaxCallFinishedClientFunction-of-GridWeb-Chrome.png](https://docs2.aspose.com/cells/net/attachments/45909138/46465060.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Using-OnAjaxCallFinishedClientFunction-of-GridWeb-Chrome.png](https://docs2.aspose.com/cells/net/attachments/45909138/46465059.png) (image/png)  

