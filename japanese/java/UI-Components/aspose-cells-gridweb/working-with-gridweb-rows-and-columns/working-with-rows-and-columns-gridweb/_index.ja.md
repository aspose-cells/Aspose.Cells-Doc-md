---
title: 行と列の操作
type: docs
weight: 20
url: /ja/java/working-with-rows-and-columns-gridweb/
---
## **行と列の挿入**
このトピックでは、Aspose.Cells.GridWeb API を使用して新しい行と列をワークシートに挿入する方法について説明します。行または列は、ワークシートの任意の位置に挿入できます。
### **行の挿入**
ワークシートの任意の位置に行を挿入するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームまたはページに追加します。
1. 行を追加するワークシートにアクセスします。
1. 行が挿入される行インデックスを指定して、行を挿入します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **列の挿入**
ワークシートの任意の位置に列を挿入するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームまたはページに追加します。
1. 列を追加するワークシートにアクセスします。
1. 列が挿入される列インデックスを指定して、列を挿入します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

また、insertRows()/insertColumns() メソッドを使用して、ワークシートに複数の行/列を挿入することもできます。

{{% /alert %}} 
## **行と列の削除**
このトピックでは、Aspose.Cells.GridWeb API を使用してワークシートから行と列を削除する方法を示します。この機能を利用して、開発者は実行時に行または列を削除できます。
### **行の削除**
ワークシートから行を削除するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームまたはページに追加します。
1. 行を削除するワークシートにアクセスします。
1. 行インデックスを指定して、ワークシートから行を削除します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **列の削除**
ワークシートから列を削除するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームまたはページに追加します。
1. 列を削除するワークシートにアクセスします。
1. 列インデックスを指定して、ワークシートから列を削除します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **行の高さと列の幅の設定**
セルの値が、セルの幅よりも広い場合や、複数の行にある場合があります。このような値は、行と列の高さと幅を変更しない限り、ユーザーに完全には表示されません。 Aspose.Cells.GridWeb は、行の高さと列の幅の設定を完全にサポートしています。このトピックでは、例を使用してこれらの機能について詳しく説明します。
### **行の高さと列の幅の操作**
#### **行の高さの設定**
行の高さを設定するには:

1. Aspose.Cells.GridWeb コントロールを Web フォーム/ページに追加します。
1. ワークシートの GridCells コレクションにアクセスします。
1. 指定した行のすべてのセルの高さを設定します。

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb は、行の高さと列の幅をポイント、インチ、ピクセルなどで測定できます。

{{% /alert %}} 

**出力: 1 行目の高さは 50 ポイントに設定されています** 

![todo:画像_代替_文章](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **列幅の設定**
列の幅を設定するには:

1. Aspose.Cells.GridWeb コントロールを Web フォーム/ページに追加します。
1. ワークシートの GridCells コレクションにアクセスします。
1. 指定された列のすべてのセルの幅を設定します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **行ヘッダーと列ヘッダーのカスタマイズ**
Microsoft Excel と同様に、Aspose.Cells.GridWeb も行 (1、2、3 などの数字) と列 (A、B、C などのアルファベット) に標準のヘッダーまたはキャプションを使用します。 Aspose.Cells.GridWeb ではキャプションのカスタマイズも可能です。このトピックでは、Aspose.Cells.GridWeb API を使用して、実行時に行ヘッダーと列ヘッダーをカスタマイズする方法について説明します。
### **行ヘッダーのカスタマイズ**
行のヘッダーまたはキャプションをカスタマイズするには:

1. Aspose.Cells.GridWeb コントロールを Web フォーム/ページに追加します。
1. GridWorksheetCollection でワークシートにアクセスします。
1. 指定した行のキャプションを設定します。

**行 1 と 2 のヘッダーはカスタマイズされています** 

![todo:画像_代替_文章](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **列ヘッダーのカスタマイズ**
列のヘッダーまたはキャプションをカスタマイズするには:

1. Aspose.Cells.GridWeb コントロールを Web フォーム/ページに追加します。
1. GridWorksheetCollection でワークシートにアクセスします。
1. 指定された列のキャプションを設定します。

**列 1 と 2 のヘッダーはカスタマイズされています** 

![todo:画像_代替_文章](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **行と列の固定と固定解除**
このトピックでは、行と列を固定および固定解除する方法について説明します。列または行を固定すると、ユーザーはワークシートの他の部分にスクロールしている間、列見出しまたは行タイトルを表示したままにすることができます。この機能は、大量のデータを含むワークシートを操作する場合に非常に役立ちます。ユーザーがスクロールすると、データのみが下にスクロールされ、見出しがそのまま残るため、日付が読みやすくなります。フリーズ ペイン機能は、Internet Explorer 6.0 以降でのみサポートされています。
### **行と列の固定**
特定の数の行と列を固定するには:

1. Aspose.Cells.GridWeb コントロールを Web フォーム/ページに追加します。
1. ワークシートにアクセスします。
1. 行と列の数を固定します。

{{% alert color="primary" %}} 

インターフェイスを使用して、特定の数の行と列を固定することもできます。行と列を固定するセルを右クリックして選択します**氷結**リストから。

{{% /alert %}} 

**固定状態の行と列** 

![todo:画像_代替_文章](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **行と列の解凍**
行と列を固定解除するには:

1. Aspose.Cells.GridWeb コントロールを Web フォーム/ページに追加します。
1. ワークシートにアクセスします。
1. 行と列の固定を解除します。

**解凍後のワークシート** 

![todo:画像_代替_文章](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **行と列の保護**
このトピックでは、エンド ユーザーが実行するあらゆる種類のアクションから行と列のセルを保護するためのいくつかの手法について説明します。開発者は、行と列のセルを読み取り専用にするか、GridWeb のコンテキスト メニュー オプションを制限するという 2 つの手法を使用して、この保護を実装できます。
### **コンテキスト メニュー オプションの制限**
GridWeb は、エンド ユーザーがコントロールで操作を実行するために使用できるコンテキスト メニューを提供します。このメニューには、セル、行、および列を操作するための多くのオプションが用意されています。

**完全なコンテキスト オプション** 

![todo:画像_代替_文章](working-with-rows-and-columns-gridweb_6.png)

コンテキスト メニューで使用できるオプションを制限することで、行と列に対するあらゆる種類のクライアント側操作を制限することができます。これは、GridWeb コントロールの EnableClientColumnOperations および EnableClientRowOperations 属性を false に設定することで実行できます。 GridWeb コントロールの EnableClientFreeze 属性を false に設定することで、ユーザーが行と列をフリーズするのを制限することもできます。

**行と列のオプションを制限した後のコンテキスト メニュー** 

![todo:画像_代替_文章](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
