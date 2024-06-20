---
title: GridWebのOnAjaxCallFinishedClientFunctionの使用
type: docs
weight: 20
url: /ja/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---

## **可能な使用シナリオ**
OnAjaxCallFinishedClientFunctionは、ユーザーがデータをGridWebのワークシートにコピーするときに呼び出されるクライアント側の関数です。この関数は、大量のセルが更新され、それらの更新されたセルをクライアント側（たとえばFireFox、Google ChromeなどのWebブラウザ）で追跡したいときに役立ちます。
## **GridWebのOnAjaxCallFinishedClientFunctionの使用**
次のサンプルコードは、OnAjaxCallFinishedClientFunctionクライアント関数を使用する方法を説明しています。スクリーンショットでは、コードを実行したときにGoogle ChromeとFireFoxでコンソール出力が表示されています。コードを実行した後、GridWebワークシート内に複数のセルにわたるデータをコピー/貼り付けし、その後、スクリーンショットに表示されているようにWebブラウザのコンソールをチェックしてください。
## **Google Chromeのコンソール出力**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **FireFoxのコンソール出力**
![todo:image_alt_text](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **サンプルコード**
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
