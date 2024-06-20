---
title: GridWeb de Etkileşimli Kaydırgaç Oluşturma
type: docs
weight: 170
url: /tr/net/aspose-cells-gridweb/render-interactive-scrollbar-in-gridweb/
keywords: GridWeb, kaydırgaç
description: Bu makale, GridWeb de kaydırgaçla çalışmanın nasıl yapılacağını tanıtır.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells for GridWeb, GridWeb elektronik tablosunun içine etkileşimli kaydırgaç kontrolü oluşturabilir. Kullanıcılar, Microsoft Excel'de yaptıkları gibi kaydırgac ile etkileşimde bulunabilir. Etkileşimli kaydırgaç oluşturabilmek için aşağıda gösterildiği gibi **jQuery** ve **jQuery UI** kütüphaneleri için bağlantıları eklemeniz gerekir.

{{< highlight java >}}

 <head runat="server">

	<link rel="stylesheet" href="/Scripts/jquery-ui.css">

	<script src="/Scripts/jquery-2.1.1.js"></script>

	<script src="/Scripts/jquery-ui.js"></script>

</head>

{{< /highlight >}}
## **GridWeb'de Etkileşimli Kaydırgaç Oluşturma**
Aşağıdaki örnek kod, aşağıdaki ekran görüntüsünde gösterilen kaydırgacı içeren [örnek Excel dosyasını](61767764.xlsx) yükler. Diğer ekran görüntüleri, GridWeb'in etkileşimli kaydırgacı oluşturduğunu ve kaydırgacın değerini B3 hücresinde gösterdiğini gösterir. Kaydırgacı sürüklediğinizde, B3 hücresinin değeri elde edilen değeri gösterir.

![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_1.png)

![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_2.png)

![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_3.png)

![todo:image_alt_text](render-interactive-scrollbar-in-gridweb_4.png)
## **Örnek Kod**
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
