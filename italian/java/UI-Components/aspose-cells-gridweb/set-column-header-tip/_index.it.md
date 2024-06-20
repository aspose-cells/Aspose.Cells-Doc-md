---
title: Imposta Suggerimento Intestazione Colonna
type: docs
weight: 90
url: /it/java/set-column-header-tip/
---

## **Possibili Scenari di Utilizzo**
Potresti avere bisogno di impostare il suggerimento per la tua colonna personalizzata durante la creazione della tabella nel foglio di lavoro. Aspose.Cells.GridWeb ti consente di rinominare la didascalia di una colonna e puoi impostare il suggerimento della colonna, in modo che gli utenti possano capire facilmente a cosa serve la colonna.
## **Impostazione Suggerimento Intestazione Colonna**
Di seguito è fornito un esempio completo per dimostrare come modificare le didascalie delle colonne e applicare il testo del suggerimento. Dopo l'esecuzione del codice di esempio, il testo del suggerimento verrà visualizzato quando si posiziona il cursore del mouse sull'intestazione della colonna specificata.

## **Codice di Esempio**
Ecco il codice sorgente del file **test.jsp**.

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
