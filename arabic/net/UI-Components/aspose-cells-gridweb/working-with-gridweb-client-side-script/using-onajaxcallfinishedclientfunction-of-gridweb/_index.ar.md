---
title: استخدام OnAjaxCallFinishedClientFunction من GridWeb
type: docs
weight: 20
url: /ar/net/aspose-cells-gridweb/using-onajaxcallfinishedclientfunction-of-gridweb/
keywords: GridWeb,ajacall,onajaxcallfinishedclientfunction,OnAjaxCallFinishedClientFunction 
description: يقدم هذا المقال كيفية العمل مع OnAjaxCallFinishedClientFunction في GridWeb.
---

## **سيناريوهات الاستخدام المحتملة**
OnAjaxCallFinishedClientFunction هو وظيفة جانب العميل يتم استدعاؤها عندما يقوم المستخدم بنسخ بعض البيانات إلى ورقة عمل GridWeb. تكون هذه الوظيفة مفيدة عندما يتم تحديث الخلايا بكميات كبيرة وترغب في تتبع تلك الخلايا المحدثة في الجانب العميل (على سبيل المثال في متصفحات الويب مثل FireFox و Google Chrome وما إلى ذلك).
## **استخدام OnAjaxCallFinishedClientFunction من GridWeb**
الرمز البرمجي المعروض أدناه يشرح كيفية الاستفادة من وظيفة العميل OnAjaxCallFinishedClientFunction. تظهر اللقطات الشاشة لمخرجات الكونسول في Google Chrome و FireFox عند تنفيذ الكود. بمجرد تنفيذ الكود ، يرجى نسخ / لصق بعض البيانات تمتد عبر عدة خلايا داخل ورقة العمل GridWeb ثم التحقق من كونسول متصفح الويب كما هو موضح في اللقطات.
## **مخرجات كونسول Google Chrome**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **مخرجات كونسول FireFox**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **الكود المثالي**
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
