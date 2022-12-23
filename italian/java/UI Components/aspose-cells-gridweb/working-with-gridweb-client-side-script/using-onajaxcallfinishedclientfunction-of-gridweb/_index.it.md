---
title: Utilizzando OnAjaxCallFinishedClientFunction di GridWeb
type: docs
weight: 20
url: /it/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---
## **Possibili scenari di utilizzo**
OnAjaxCallFinishedClientFunction è una funzione lato client che viene chiamata quando l'utente copia alcuni dati nel foglio di lavoro GridWeb. Questa funzione è utile quando la maggior parte delle celle viene aggiornata e si desidera tenere traccia di tali celle aggiornate sul lato client (ad esempio nei browser Web come FireFox, Google Chrome ecc.).
## **Utilizzando OnAjaxCallFinishedClientFunction di GridWeb**
Il seguente codice di esempio spiega come utilizzare la funzione client OnAjaxCallFinishedClientFunction. Gli screenshot mostrano l'output della console in Google Chrome e FireFox quando il codice viene eseguito. Una volta eseguito il codice, copiare/incollare alcuni dati che si estendono su più celle all'interno del foglio di lavoro GridWeb e quindi controllare la console del browser Web come mostrato negli screenshot.
## **Google Uscita console cromata**
![cose da fare:immagine_alt_testo](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **Uscita console FireFox**
![cose da fare:immagine_alt_testo](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Codice d'esempio**
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
