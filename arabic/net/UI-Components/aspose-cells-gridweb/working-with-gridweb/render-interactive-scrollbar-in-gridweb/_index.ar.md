---
title: تقديم شريط التمرير التفاعلي في GridWeb
type: docs
weight: 170
url: /ar/net/render-interactive-scrollbar-in-gridweb/
---
## **سيناريوهات الاستخدام الممكنة**
 يمكن لـ Aspose.Cells لـ GridWeb تقديم تحكم شريط التمرير التفاعلي داخل ورقة عمل GridWeb. يمكن للمستخدم التفاعل مع شريط التمرير كما يفعل في Microsoft Excel. لإنشاء شريط تمرير تفاعلي ، يجب إضافة روابط لـ**مسج** و**jQuery UI** المكتبات كما هو موضح أدناه.

{{< highlight "java" >}}

 <head runat="server">

	<link rel="stylesheet" href="/Scripts/jquery-ui.css">

	<script src="/Scripts/jquery-2.1.1.js"></script>

	<script src="/Scripts/jquery-ui.js"></script>

</head>

{{< /highlight >}}
## **تقديم شريط التمرير التفاعلي في GridWeb**
 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](61767764.xlsx)تحتوي على شريط التمرير كما هو موضح في لقطة الشاشة التالية. تُظهر لقطات الشاشة الأخرى كيف يعرض GridWeb شريط التمرير التفاعلي ويعرض قيمة شريط التمرير في الخلية B3. كلما قمت بالتمرير في شريط التمرير ، تعرض قيمة الخلية B3 القيمة الناتجة.

![ما يجب القيام به: image_بديل_نص](render-interactive-scrollbar-in-gridweb_1.png)

![ما يجب القيام به: image_بديل_نص](render-interactive-scrollbar-in-gridweb_2.png)

![ما يجب القيام به: image_بديل_نص](render-interactive-scrollbar-in-gridweb_3.png)

![ما يجب القيام به: image_بديل_نص](render-interactive-scrollbar-in-gridweb_4.png)
## **عينة من الرموز**
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
