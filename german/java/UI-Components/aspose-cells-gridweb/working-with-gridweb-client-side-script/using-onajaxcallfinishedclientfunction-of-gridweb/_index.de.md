---
title: Verwendung der OnAjaxCallFinishedClientFunction von GridWeb
type: docs
weight: 20
url: /de/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---

## **Mögliche Verwendungsszenarien**
OnAjaxCallFinishedClientFunction ist eine clientseitige Funktion, die aufgerufen wird, wenn ein Benutzer einige Daten in das GridWeb-Arbeitsblatt kopiert. Diese Funktion ist hilfreich, wenn eine Vielzahl von Zellen aktualisiert wird und Sie den Überblick über diese aktualisierten Zellen auf der Client-Seite behalten möchten (z. B. in Webbrowsern wie FireFox, Google Chrome usw.).
## **Verwendung der OnAjaxCallFinishedClientFunction von GridWeb**
Der folgende Beispielcode erläutert, wie die OnAjaxCallFinishedClientFunction-Clientfunktion genutzt werden kann. Die Screenshots zeigen die Konsolenausgabe in Google Chrome und FireFox, wenn der Code ausgeführt wird. Nachdem Sie den Code ausgeführt haben, kopieren/einfügen Sie bitte einige Daten, die mehrere Zellen im GridWeb-Arbeitsblatt umfassen, und überprüfen Sie dann die Webbrowserkonsole wie in den Screenshots dargestellt.
## **Konsolenausgabe in Google Chrome**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **Konsolenausgabe in FireFox**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Beispielcode**
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
