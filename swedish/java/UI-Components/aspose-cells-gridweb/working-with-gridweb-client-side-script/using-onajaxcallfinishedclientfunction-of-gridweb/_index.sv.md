---
title: Använda OnAjaxCallFinishedClientFunction av GridWeb
type: docs
weight: 20
url: /sv/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---
## **Möjliga användningsscenarier**
OnAjaxCallFinishedClientFunction är en funktion på klientsidan som anropas när användaren kopierar vissa data till GridWeb-kalkylbladet. Den här funktionen är användbar när en stor del av cellerna uppdateras och du vill hålla koll på de uppdaterade cellerna på klientsidan (dvs i webbläsare som FireFox, Google Chrome etc.).
## **Använda OnAjaxCallFinishedClientFunction av GridWeb**
Följande exempelkod förklarar hur du använder OnAjaxCallFinishedClientFunction-klientfunktionen. Skärmbilderna visar konsolutgången i Google Chrome och FireFox när koden exekveras. När du har kört koden, kopiera/klistra in lite data som spänner över flera celler i GridWeb-arbetsbladet och kontrollera sedan webbläsarkonsolen som visas i skärmdumpar.
## **Google Chrome Console-utgång**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **FireFox-konsolutgång**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Exempelkod**
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
