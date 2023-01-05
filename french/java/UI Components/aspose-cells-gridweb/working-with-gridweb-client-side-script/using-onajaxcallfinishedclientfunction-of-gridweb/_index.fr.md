---
title: Utilisation de la fonction OnAjaxCallFinishedClient de GridWeb
type: docs
weight: 20
url: /fr/java/using-onajaxcallfinishedclientfunction-of-gridweb/
---
## **Scénarios d'utilisation possibles**
OnAjaxCallFinishedClientFunction est une fonction côté client qui est appelée lorsque l'utilisateur copie des données dans la feuille de calcul GridWeb. Cette fonction est utile lorsque la plupart des cellules sont mises à jour et que vous souhaitez conserver la trace de ces cellules mises à jour côté client (c'est-à-dire dans les navigateurs Web tels que FireFox, Google Chrome, etc.).
## **Utilisation de la fonction OnAjaxCallFinishedClient de GridWeb**
L'exemple de code suivant explique comment utiliser la fonction client OnAjaxCallFinishedClientFunction. Les captures d'écran montrent la sortie de la console dans Google Chrome et FireFox lorsque le code est exécuté. Une fois que vous avez exécuté le code, veuillez copier/coller des données couvrant plusieurs cellules à l'intérieur de la feuille de calcul GridWeb, puis vérifiez la console du navigateur Web, comme indiqué dans les captures d'écran.
## **Google Sortie de console chromée**
![tâche : image_autre_texte](using-onajaxcallfinishedclientfunction-of-gridweb_1.png)
## **Sortie de la console Firefox**
![tâche : image_autre_texte](using-onajaxcallfinishedclientfunction-of-gridweb_2.png)
## **Exemple de code**
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
