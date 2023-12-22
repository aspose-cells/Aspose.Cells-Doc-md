---
title: 使用 GridWeb 的 OnAjaxCallFinishedClientFunction
type: docs
weight: 20
url: /zh/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---
##  **可能的使用场景**
OnAjaxCallFinishedClientFunction 是一个客户端函数，当用户将某些数据复制到 GridWeb 工作表时调用。当大量单元格更新并且您希望在客户端（即在 FireFox、Google Chrome 等网络浏览器中）跟踪这些更新的单元格时，此功能非常有用。
##  **使用 GridWeb 的 OnAjaxCallFinishedClientFunction**
以下示例代码说明了如何使用 OnAjaxCallFinishedClientFunction 客户端函数。屏幕截图显示了执行代码时 Google Chrome 和 FireFox 中的控制台输出。执行代码后，请复制/粘贴 GridWeb 工作表内多个单元格的一些数据，然后检查 Web 浏览器控制台，如屏幕截图所示。
##  **Google Chrome 控制台输出**
![待办事项：图像_替代_文本](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
##  **FireFox 控制台输出**
![待办事项：图像_替代_文本](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
##  **示例代码**
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
