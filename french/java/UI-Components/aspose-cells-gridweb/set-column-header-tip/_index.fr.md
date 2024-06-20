---
title: Définir l astuce de l en tête de colonne
type: docs
weight: 90
url: /fr/java/set-column-header-tip/
---

## **Scénarios d'utilisation possibles**
Vous pourriez avoir besoin de définir une info-bulle pour votre colonne personnalisée lors de la création du tableau dans la feuille de calcul. Aspose.Cells.GridWeb vous permet de renommer la légende d'une colonne et vous pouvez définir une info-bulle pour la colonne, afin que les utilisateurs puissent facilement comprendre à quoi sert la colonne.
## **Définition de l'astuce de l'en-tête de colonne**
Un exemple complet est donné ci-dessous pour démontrer comment modifier les légendes des colonnes et appliquer du texte d'info-bulle. Après l'exécution du code d'exemple, le texte d'info-bulle apparaîtrait lorsque vous placez le curseur de la souris sur l'en-tête de la colonne spécifiée.

## **Code d'exemple**
Voici le code d'exemple du fichier **test.jsp**.

{{< highlight java >}}

 <%@ page language="java" contentType="text/html; charset=UTF-8"

 import="com.aspose.gridweb.*" pageEncoding="UTF-8"%>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">

<head>

<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9"/>

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<title>Setting Column Header ToolTip</title>

<%

ExtPage BeanManager=ExtPage.getInstance();

GridWebBean gridweb=BeanManager.getBean(request);

out.println(gridweb.getHTMLHead());

%>

</head>

<BODY>



<%

gridweb.setReqRes(request, response);

gridweb.setEnableAsync(false);

//Access the first worksheet

GridWorksheet gridSheet = gridweb.getWorkSheets().get(0);

//Input data into the cells of the first worksheet.

gridSheet.getCells().get("A1").putValue("Product1");

gridSheet.getCells().get("A2").putValue("Product2");

gridSheet.getCells().get("A3").putValue("Product3");

gridSheet.getCells().get("A4").putValue("Product4");

gridSheet.getCells().get("B1").putValue(100);

gridSheet.getCells().get("B2").putValue(200);

gridSheet.getCells().get("B3").putValue(300);

gridSheet.getCells().get("B4").putValue(400);

//Set the caption of the first two columns.

gridSheet.setColumnCaption(0, "Product Name");

gridSheet.setColumnCaption(1, "Price");

//Set the column width of the first column.

gridSheet.getCells().setColumnWidth(0, 20);

//Set the second column header's tip.

gridSheet.setColumnHeaderToolTip(1, "Unit Price of Products");

gridweb.prepareRender();

out.println(gridweb.getHTMLBody());

%>

<br>



</BODY>

</html>

{{< /highlight >}}
