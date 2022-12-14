---
title: GridWeb'in OnAjaxCallFinishedClientFunction'ını Kullanma
type: docs
weight: 20
url: /tr/net/using-onajaxcallfinishedclientfunction-of-gridweb/
---
## **Olası Kullanım Senaryoları**
OnAjaxCallFinishedClientFunction, kullanıcı bazı verileri GridWeb çalışma sayfasına kopyaladığında çağrılan bir istemci tarafı işlevidir. Bu işlev, hücrelerin büyük bir kısmı güncellendiğinde ve bu güncellenen hücrelerin izini istemci tarafında tutmak istediğinizde (örn. FireFox, Google Chrome vb. web tarayıcılarında) yararlıdır.
## **GridWeb'in OnAjaxCallFinishedClientFunction'ını Kullanma**
Aşağıdaki örnek kod, OnAjaxCallFinishedClientFunction istemci işlevinin nasıl kullanılacağını açıklar. Ekran görüntüleri, kod yürütüldüğünde Google Chrome ve FireFox'ta konsol çıktısını gösterir. Kodu çalıştırdıktan sonra, lütfen birden çok hücreye yayılan bazı verileri GridWeb çalışma sayfasına kopyalayın/yapıştırın ve ardından ekran görüntülerinde gösterildiği gibi Web Tarayıcı Konsolunu kontrol edin.
## **Google Chrome Konsol Çıkışı**
![yapılacaklar:resim_alternatif_Metin](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **FireFox Konsol Çıkışı**
![yapılacaklar:resim_alternatif_Metin](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Basit kod**
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
