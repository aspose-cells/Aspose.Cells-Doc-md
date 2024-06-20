---
title: GridWeb in OnAjaxCallFinishedClientFunction ını Kullanma
type: docs
weight: 20
url: /tr/net/aspose-cells-gridweb/using-onajaxcallfinishedclientfunction-of-gridweb/
keywords: GridWeb,ajacall,onajaxcallfinishedclientfunction,OnAjaxCallFinishedClientFunction 
description: Bu makale, GridWeb de OnAjaxCallFinishedClientFunction ile nasıl çalışılacağını tanıtır.
---

## **Olası Kullanım Senaryoları**
OnAjaxCallFinishedClientFunction, kullanıcı GridWeb çalışma sayfasına veri kopyaladığında çağrılan bir client side fonksiyonudur. Bu fonksiyon, birden fazla hücre güncellendiğinde ve bu güncellenen hücrelerin izinini web tarayıcılarında (FireFox, Google Chrome vb.) tutmak istediğinizde (yani client side'da) faydalıdır.
## **GridWeb'in OnAjaxCallFinishedClientFunction'ını Kullanma**
Aşağıdaki örnek kod, OnAjaxCallFinishedClientFunction client fonksiyonundan nasıl yararlanılacağını açıklar. Ekran görüntüleri, kodun çalıştırıldığında Google Chrome ve FireFox'ta konsol çıktısını göstermektedir. Kodu çalıştırdıktan sonra, lütfen GridWeb çalışma sayfasında birden fazla hücreyi kapsayan bazı verileri kopyalayıp yapıştırın ve ardından ekran görüntülerinde gösterildiği gibi Web Tarayıcı Konsolunu kontrol edin.
## **Google Chrome Konsol Çıktısı**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **FireFox Konsolu Çıktısı**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Örnek Kod**
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
