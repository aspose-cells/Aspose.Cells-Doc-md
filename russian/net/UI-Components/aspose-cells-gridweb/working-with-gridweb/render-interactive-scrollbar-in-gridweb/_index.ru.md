---
title: Визуализация интерактивной полосы прокрутки в GridWeb
type: docs
weight: 170
url: /ru/net/render-interactive-scrollbar-in-gridweb/
---
## **Возможные сценарии использования**
 Aspose.Cells для GridWeb может отображать интерактивный элемент управления полосой прокрутки внутри рабочего листа GridWeb. Пользователь может взаимодействовать с полосой прокрутки, как в Microsoft Excel. Чтобы создать интерактивную полосу прокрутки, необходимо добавить ссылки для**jQuery** и**jQuery-интерфейс** библиотеки, как показано ниже.

{{< highlight "java" >}}

 <head runat="server">

	<link rel="stylesheet" href="/Scripts/jquery-ui.css">

	<script src="/Scripts/jquery-2.1.1.js"></script>

	<script src="/Scripts/jquery-ui.js"></script>

</head>

{{< /highlight >}}
## **Визуализация интерактивной полосы прокрутки в GridWeb**
 Следующий пример кода загружает[образец файла Excel](61767764.xlsx)содержащий полосу прокрутки, как показано на следующем снимке экрана. На других снимках экрана показано, как GridWeb отображает интерактивную полосу прокрутки и отображает значение полосы прокрутки в ячейке B3. Всякий раз, когда вы прокручиваете полосу прокрутки, значение ячейки B3 показывает результирующее значение.

![дело:изображение_альтернативный_текст](render-interactive-scrollbar-in-gridweb_1.png)

![дело:изображение_альтернативный_текст](render-interactive-scrollbar-in-gridweb_2.png)

![дело:изображение_альтернативный_текст](render-interactive-scrollbar-in-gridweb_3.png)

![дело:изображение_альтернативный_текст](render-interactive-scrollbar-in-gridweb_4.png)
## **Образец кода**
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
