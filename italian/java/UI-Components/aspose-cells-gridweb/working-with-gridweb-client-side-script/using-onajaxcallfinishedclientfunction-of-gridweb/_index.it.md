---
title: Utilizzo di OnAjaxCallFinishedClientFunction di GridWeb
type: docs
weight: 20
url: /it/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---

## **Possibili Scenari di Utilizzo**
OnAjaxCallFinishedClientFunction è una funzione sul lato client che viene chiamata quando l'utente copia alcuni dati nel foglio di calcolo di GridWeb. Questa funzione è utile quando vengono aggiornate moltissime celle e si desidera tenere traccia di queste celle aggiornate sul lato client (ad es. nei browser web come FireFox, Google Chrome, ecc.).
## **Utilizzo di OnAjaxCallFinishedClientFunction di GridWeb**
Il seguente codice di esempio spiega come utilizzare la funzione client OnAjaxCallFinishedClientFunction. Le schermate mostrano l'output della console in Google Chrome e FireFox quando il codice viene eseguito. Una volta eseguito il codice, si prega di copiare/incollare alcuni dati che si estendono su più celle all'interno del foglio di calcolo di GridWeb e quindi controllare la Console del browser web come mostrato nelle schermate.
## **Output della Console di Google Chrome**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **Output della Console di FireFox**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Codice di Esempio**
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
