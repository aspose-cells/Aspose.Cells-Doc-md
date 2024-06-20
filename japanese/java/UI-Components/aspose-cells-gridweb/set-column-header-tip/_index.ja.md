---
title: 列ヘッダーチップを設定する
type: docs
weight: 90
url: /ja/java/set-column-header-tip/
---

## **可能な使用シナリオ**
ワークシートでテーブルを作成する際に、カスタムカラムのツールヒントを設定する必要があるかもしれません。Aspose.Cells.GridWebを使用すると、列の見出しを変更し、ツールヒントを設定することができます。これにより、ユーザーがカラムの用途を簡単に理解できます。
## **列見出しヒントの設定**
下記の完全な例は、列のキャプションを変更し、ツールヒントテキストを適用する方法を示しています。例のコードを実行すると、指定された列のヘッダーにマウスカーソルを置くとツールヒントテキストが表示されます。

## **サンプルコード**
以下は **test.jsp** ファイルのサンプルコードです。

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
