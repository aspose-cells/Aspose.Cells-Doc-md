---
title: GridWeb Cell の Hyperlink オブジェクトにアクセスする
type: docs
weight: 100
url: /ja/net/access-hyperlink-object-of-the-gridweb-cell/
---
## **考えられる使用シナリオ**
次の 2 つの方法を使用して、セルにハイパーリンクが含まれているかどうかを確認できます。これらのメソッドは、セルにハイパーリンクが含まれていない場合は null を返し、ハイパーリンクが含まれている場合は GridHyperlink オブジェクトを返します。

- GridHyperlinkCollection.GetHyperlink(GridCell セル)
- GridHyperlinkCollection.GetHyperlink(int 行、int 列)
## **新規または既存のウィンドウでハイパーリンクを開く**
Excelファイルに、次のようなURLにリンクするハイパーリンクが含まれている場合<http://wwww.aspose.com/>それを GridWeb にロードすると、ハイパーリンクは target 属性が設定された状態でレンダリングされます。_空欄。つまり、GridWeb セルのハイパーリンクをクリックすると、既存のウィンドウではなく新しいウィンドウで開きます。次のデバッグ ウィンドウで GridHyperlink.Target プロパティを確認してください。また、ハイパーリンクを既存のウィンドウで開きたい場合は、GridHyperlink.Target を次のように設定してください。_自己。

![todo:画像_代替_文章](access-hyperlink-object-of-the-gridweb-cell_1.png)
## **GridWeb Cell の Hyperlink オブジェクトにアクセスする**
次のサンプル コードは、セル A1 のハイパーリンクにアクセスします。セル A1 にハイパーリンクが含まれている場合は GridHyperlink オブジェクトが返され、それ以外の場合は null が返されます。
### **サンプルコード**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCellHyperlink.aspx-AccessHyperlink.cs" >}}
