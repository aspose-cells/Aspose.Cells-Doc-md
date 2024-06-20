---
title: Использование OnAjaxCallFinishedClientFunction в GridWeb
type: docs
weight: 20
url: /ru/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---

## **Возможные сценарии использования**
OnAjaxCallFinishedClientFunction - это клиентская функция, которая вызывается, когда пользователь копирует некоторые данные в рабочий лист GridWeb. Эта функция полезна, когда обновляется большое количество ячеек, и вы хотите отслеживать эти обновленные ячейки на стороне клиента (т. е. в веб-браузерах, таких как FireFox, Google Chrome и т. д.).
## **Использование OnAjaxCallFinishedClientFunction в GridWeb**
В следующем примере кода показано, как использовать клиентскую функцию OnAjaxCallFinishedClientFunction. Снимки экрана показывают вывод консоли в Google Chrome и FireFox при выполнении кода. После выполнения кода скопируйте/вставьте некоторые данные, охватывающие несколько ячеек в рабочем листе GridWeb, и затем проверьте консоль веб-браузера, как показано на скриншотах.
## **Вывод консоли Google Chrome**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **Вывод консоли FireFox**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Образец кода**
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
