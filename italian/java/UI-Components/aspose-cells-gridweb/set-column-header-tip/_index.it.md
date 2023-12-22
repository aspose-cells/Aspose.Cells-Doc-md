---
title: Imposta il suggerimento dell'intestazione della colonna
type: docs
weight: 90
url: /it/java/set-column-header-tip/
---
##  **Possibili scenari di utilizzo**
Potrebbe essere necessario impostare la descrizione comando per la colonna personalizzata durante la creazione della tabella nel foglio di lavoro. Aspose.Cells.GridWeb ti consente di rinominare la didascalia di una colonna e puoi impostare la descrizione comando sulla colonna, in modo che gli utenti possano facilmente capire a cosa serve la colonna.
##  **Impostazione del suggerimento per l'intestazione della colonna**
Di seguito viene fornito un esempio completo per dimostrare come modificare le didascalie delle colonne e applicare il testo della descrizione comando. Dopo aver eseguito il codice di esempio, il testo della descrizione comando verrà visualizzato quando si posiziona il cursore del mouse sull'intestazione della colonna specificata.

##  **Codice d'esempio**
Ecco il codice di esempio di**prova.jsp** file.

{{< highlight "java" >}}

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
