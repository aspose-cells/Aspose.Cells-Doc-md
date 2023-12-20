---
title: GridWeb Cell の Hyperlink オブジェクトにアクセスする
type: docs
weight: 60
url: /ja/java/access-hyperlink-object-of-the-gridweb-cell/
---
## **考えられる使用シナリオ**
次の 2 つの方法を使用して、セルにハイパーリンクが含まれているかどうかを確認できます。これらのメソッドは、セルにハイパーリンクが含まれていない場合は null を返し、ハイパーリンクが含まれている場合は GridHyperlink オブジェクトを返します。

- GridHyperlinkCollection.getHyperlink(GridCell セル)
- GridHyperlinkCollection.getHyperlink(int 行、int 列)
## **新規または既存のウィンドウでハイパーリンクを開く**
Excelファイルに、次のようなURLにリンクするハイパーリンクが含まれている場合<http://wwww.aspose.com/>それを GridWeb にロードすると、ハイパーリンクは target 属性が設定された状態でレンダリングされます。_空欄。つまり、GridWeb セル内のハイパーリンクをクリックすると、既存のウィンドウではなく新しいウィンドウで開きます。また、ハイパーリンクを既存のウィンドウで開きたい場合は、GridHyperlink.Target を次のように設定してください。_自己。
## **GridWeb Cell の Hyperlink オブジェクトにアクセスする**
次のサンプル コードは、セル A1 のハイパーリンクにアクセスします。セル A1 にハイパーリンクが含まれている場合は GridHyperlink オブジェクトが返され、それ以外の場合は null が返されます。
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}
