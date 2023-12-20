---
title: GridWebのOnAjaxCallFinishedClientFunctionを利用する
type: docs
weight: 20
url: /ja/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---
## **考えられる使用シナリオ**
OnAjaxCallFinishedClientFunction は、ユーザーがデータを GridWeb ワークシートにコピーするときに呼び出されるクライアント側関数です。この関数は、大量のセルが更新され、それらの更新されたセルをクライアント側 (つまり、FireFox、Google Chrome などの Web ブラウザー) で追跡したい場合に役立ちます。
## **GridWebのOnAjaxCallFinishedClientFunctionを利用する**
次のサンプル コードでは、OnAjaxCallFinishedClientFunction クライアント関数を使用する方法について説明します。スクリーンショットは、コードが実行されたときの Google Chrome と FireFox のコンソール出力を示しています。コードを実行したら、GridWeb ワークシート内の複数のセルにまたがるデータをコピーして貼り付け、スクリーンショットに示すように Web ブラウザー コンソールを確認してください。
## **Google Chrome コンソール出力**
![todo:画像_代替_文章](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **FireFox コンソール出力**
![todo:画像_代替_文章](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **サンプルコード**
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
