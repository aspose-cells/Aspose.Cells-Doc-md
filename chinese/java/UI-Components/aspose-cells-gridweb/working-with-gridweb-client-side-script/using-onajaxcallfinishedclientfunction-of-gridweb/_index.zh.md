---
title: 使用GridWeb的OnAjaxCallFinishedClientFunction
type: docs
weight: 20
url: /zh/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---

## **可能的使用场景**
OnAjaxCallFinishedClientFunction是一个客户端函数，在用户将一些数据复制到GridWeb工作表时调用。当更新了大量的单元格，并且您希望在客户端跟踪这些更新的单元格时（即在像FireFox、Google Chrome等的Web浏览器中），此函数很有帮助。
## **使用GridWeb的OnAjaxCallFinishedClientFunction**
以下示例代码解释了如何使用 OnAjaxCallFinishedClientFunction 客户端函数。当执行代码时，屏幕截图显示了在Google Chrome和FireFox中执行代码时的控制台输出。一旦执行代码，请在GridWeb工作表中复制/粘贴一些跨多个单元格的数据，然后检查Web浏览器控制台，如屏幕截图所示。
## **Google Chrome控制台输出**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **FireFox控制台输出**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **示例代码**
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
