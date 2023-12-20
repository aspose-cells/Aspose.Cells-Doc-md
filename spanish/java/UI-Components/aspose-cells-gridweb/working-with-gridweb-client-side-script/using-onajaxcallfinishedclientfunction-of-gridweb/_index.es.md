---
title: Usando OnAjaxCallFinishedClientFunction de GridWeb
type: docs
weight: 20
url: /es/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---
## **Posibles escenarios de uso**
OnAjaxCallFinishedClientFunction es una función del lado del cliente que se llama cuando el usuario copia algunos datos en la hoja de trabajo de GridWeb. Esta función es útil cuando se actualiza la mayor parte de las celdas y desea realizar un seguimiento de esas celdas actualizadas en el lado del cliente (es decir, en navegadores web como FireFox, Google Chrome, etc.).
## **Usando OnAjaxCallFinishedClientFunction de GridWeb**
El siguiente código de ejemplo explica cómo utilizar la función de cliente OnAjaxCallFinishedClientFunction. Las capturas de pantalla muestran la salida de la consola en Google Chrome y FireFox cuando se ejecuta el código. Una vez que ejecute el código, copie/pegue algunos datos que abarquen varias celdas dentro de la hoja de trabajo de GridWeb y luego verifique la consola del navegador web como se muestra en las capturas de pantalla.
## **Google Salida de consola cromada**
![todo:imagen_alternativa_texto](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **Salida de la consola FireFox**
![todo:imagen_alternativa_texto](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Código de muestra**
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
