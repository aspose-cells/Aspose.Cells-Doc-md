---
title: GridWeb'in OnAjaxCallFinishedClientFunction'ını Kullanma
type: docs
weight: 20
url: /tr/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---
## **Olası Kullanım Senaryoları**
OnAjaxCallFinishedClientFunction, kullanıcı bazı verileri GridWeb çalışma sayfasına kopyaladığında çağrılan bir istemci tarafı işlevidir. Bu işlev, hücrelerin büyük bir kısmı güncellendiğinde ve bu güncellenen hücrelerin izini istemci tarafında tutmak istediğinizde (örn. FireFox, Google Chrome vb. web tarayıcılarında) yararlıdır.
## **GridWeb'in OnAjaxCallFinishedClientFunction'ını Kullanma**
Aşağıdaki örnek kod, OnAjaxCallFinishedClientFunction istemci işlevinin nasıl kullanılacağını açıklar. Ekran görüntüleri, kod yürütüldüğünde Google Chrome ve FireFox'ta konsol çıktısını gösterir. Kodu çalıştırdıktan sonra, lütfen birden çok hücreye yayılan bazı verileri GridWeb çalışma sayfasına kopyalayın/yapıştırın ve ardından ekran görüntülerinde gösterildiği gibi Web Tarayıcı Konsolunu kontrol edin.
## **Google Chrome Konsol Çıkışı**
![yapılacaklar:resim_alternatif_metin](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **FireFox Konsol Çıkışı**
![yapılacaklar:resim_alternatif_metin](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Basit kod**
{{< highlight "java" >}}

 <%@page language="java" contentType="text/html; charset=UTF-8" import="com.aspose.gridweb.*"  pageEncoding="UTF-8"%>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">

<head>

<%

String path = request.getContextPath();

String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";

%>

<base href="<%=basePath%>">

<script type="text/javascript" language="javascript" src="grid/acw_client/acwmain.js"></script>

<script type="text/javascript" language="javascript" src="grid/acw_client/lang_en.js"></script>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

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

<title>Aspose.Cells.GridWeb for Java - Sample JSP Page</title>

<%

//Print GridWeb version on Console

System.out.println("Aspose.Cells.GridWeb for Java Version: " + GridWebBean.getVersion());

ExtPage BeanManager=ExtPage.getInstance();

GridWebBean gridweb=BeanManager.getBean(request);

out.println(gridweb.getHTMLHead());

%>

</head>

<body>

<%

gridweb.setReqRes(request, response);

gridweb.setEnableAJAX(true);

gridweb.setOnAjaxCallFinishedClientFunction("TestAjaxCallFinish");

gridweb.setOnCellUpdatedClientFunction("CellUpdate");

gridweb.setWidth(Unit.Pixel(600));

gridweb.setHeight(Unit.Pixel(400));

gridweb.prepareRender();

out.print(gridweb.getHTMLBody());

%>

</body>

</html>

{{< /highlight >}}
