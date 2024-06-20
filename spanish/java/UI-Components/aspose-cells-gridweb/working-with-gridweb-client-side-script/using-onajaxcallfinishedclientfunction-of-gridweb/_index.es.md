---
title: Usando OnAjaxCallFinishedClientFunction de GridWeb
type: docs
weight: 20
url: /es/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---

## **Escenarios de uso posibles**
OnAjaxCallFinishedClientFunction es una función del lado del cliente que se llama cuando el usuario copia algunos datos a la hoja de cálculo de GridWeb. Esta función es útil cuando se actualiza un montón de celdas y se quiere realizar un seguimiento de esas celdas actualizadas en el lado del cliente (es decir, en navegadores web como FireFox, Google Chrome, etc.).
## **Usando OnAjaxCallFinishedClientFunction de GridWeb**
El siguiente código de muestra explica cómo usar la función del lado del cliente de OnAjaxCallFinishedClientFunction. Las capturas de pantalla muestran la salida en la consola de Google Chrome y FireFox cuando se ejecuta el código. Una vez que hayas ejecutado el código, por favor, copia/pega algunos datos que abarquen múltiples celdas dentro de la hoja de cálculo de GridWeb y luego revisa la consola del navegador web como se muestra en las capturas de pantalla.
## **Salida de la Consola de Google Chrome**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **Salida de la Consola de FireFox**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Código de muestra**
{{< highlight java >}}

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
