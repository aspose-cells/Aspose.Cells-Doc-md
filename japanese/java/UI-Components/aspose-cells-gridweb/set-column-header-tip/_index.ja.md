---
title: 列ヘッダーのヒントを設定する
type: docs
weight: 90
url: /ja/java/set-column-header-tip/
---
##  **考えられる使用シナリオ**
ワークシートにテーブルを作成するときに、カスタム列のツールチップを設定することが必要になる場合があります。 Aspose.Cells.GridWeb では、列のキャプションの名前を変更したり、ツールチップを列に設定したりできるため、ユーザーはその列が何のためのものかを簡単に理解できます。
##  **列ヘッダーのヒントの設定**
列のキャプションを変更し、ツールチップ テキストを適用する方法を示す完全な例を以下に示します。サンプル コードを実行した後、指定された列のヘッダーの上にマウス カーソルを置くと、ツールヒント テキストがポップアップ表示されます。

##  **サンプルコード**
のサンプルコードは次のとおりです**テスト.jsp**ファイル。

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
