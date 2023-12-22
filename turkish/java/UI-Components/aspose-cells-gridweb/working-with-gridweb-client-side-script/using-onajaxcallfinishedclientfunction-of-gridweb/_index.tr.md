---
title: GridWeb'in OnAjaxCallFinishedClientFunction'ını Kullanma
type: docs
weight: 20
url: /tr/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---
##  **Olası Kullanım Senaryoları**
OnAjaxCallFinishedClientFunction, kullanıcı bazı verileri GridWeb çalışma sayfasına kopyaladığında çağrılan istemci tarafı bir işlevdir. Bu işlev, çok sayıda hücre güncellendiğinde ve istemci tarafında (ör. FireFox, Google Chrome vb. gibi web tarayıcılarında) güncellenen hücrelerin takibini yapmak istediğinizde faydalıdır.
##  **GridWeb'in OnAjaxCallFinishedClientFunction'ını Kullanma**
Aşağıdaki örnek kod, OnAjaxCallFinishedClientFunction istemci işlevinin nasıl kullanılacağını açıklamaktadır. Ekran görüntüleri, kod yürütüldüğünde Google Chrome ve FireFox'taki konsol çıktısını gösteriyor. Kodu çalıştırdıktan sonra, lütfen GridWeb çalışma sayfasının içindeki birden fazla hücreye yayılan bazı verileri kopyalayıp yapıştırın ve ardından ekran görüntülerinde gösterildiği gibi Web Tarayıcı Konsolunu kontrol edin.
##  **Google Krom Konsol Çıkışı**
![yapılacak şey:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
##  **FireFox Konsol Çıkışı**
![yapılacak şey:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
##  **Basit kod**
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
