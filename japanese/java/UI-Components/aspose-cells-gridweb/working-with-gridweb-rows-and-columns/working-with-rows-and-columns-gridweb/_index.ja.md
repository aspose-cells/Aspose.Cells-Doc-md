---
title: GridWebの行と列との作業
type: docs
weight: 20
url: /ja/java/working-with-rows-and-columns-gridweb/
---

## **行と列の挿入**
このトピックでは、Aspose.Cells.GridWeb APIを使用してワークシートに新しい行や列を挿入する方法について説明します。行または列はワークシートの任意の位置に挿入できます。
### **行の挿入**
ワークシートの任意の位置に行を挿入するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームまたはページに追加します。
1. 行を追加するワークシートにアクセスします。
1. 行が挿入される行インデックスを指定して行を挿入します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **列の挿入**
ワークシートの任意の位置に列を挿入するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームまたはページに追加します。
1. 列を追加するワークシートにアクセスします。
1. 列が挿入される列インデックスを指定して列を挿入します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

挿入Rows()/insertColumns() メソッドを使用して、ワークシートに複数の行/列を適切に挿入することもできます。

{{% /alert %}} 
## **行と列の削除**
このトピックでは、Aspose.Cells.GridWeb API を使用してワークシートから行や列を削除する方法について説明します。この機能のおかげで、開発者は実行時に行や列を削除できます。
### **行の削除**
ワークシートから行を削除するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームまたはページに追加します。
1. 行を削除するワークシートにアクセスします。
1. 行のインデックスを指定してワークシートから行を削除します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **列の削除**
ワークシートから列を削除するには:

1. Aspose.Cells.GridWeb コントロールを Web フォームまたはページに追加します。
1. 列を削除したいワークシートにアクセスします。
1. 列のインデックスを指定してワークシートから列を削除します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **行の高さと列の幅の設定**
セルの値がセルの幅を超える場合や複数行に渡る場合があります。そのような値は、行と列の高さと幅を変更しない限り、ユーザーに完全に表示されません。Aspose.Cells.GridWeb は行の高さと列の幅の設定を完全にサポートしています。このトピックでは、これらの機能について、例を挙げて詳しく説明します。
### **行の高さと列の幅の設定**
#### **行の高さの設定**
行の高さを設定するには:

1. Web フォーム/ページに Aspose.Cells.GridWeb コントロールを追加します。
1. ワークシートの GridCells コレクションにアクセスします。
1. 指定された行内のすべてのセルの高さを設定します。

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb は、ポイント、インチ、ピクセルなどの単位で行の高さと列の幅の測定を受け入れます。

{{% /alert %}} 

**出力: 第1行の高さが50ポイントに設定されました** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **列の幅の設定**
列の幅を設定するには:

1. Web フォーム/ページに Aspose.Cells.GridWeb コントロールを追加します。
1. ワークシートの GridCells コレクションにアクセスします。
1. 指定された列内のすべてのセルの幅を設定します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **行と列ヘッダーのカスタマイズ**
Microsoft Excel のように、Aspose.Cells.GridWeb は行（1、2、3 などの数字）と列（A、B、C などのアルファベット）に標準のヘッダーまたは見出しを使用します。Aspose.Cells.GridWeb は見出しをカスタマイズすることも可能にします。このトピックでは、Aspose.Cells.GridWeb API を使用して実行時に行と列のヘッダーをカスタマイズする方法について説明します。
### **行ヘッダーのカスタマイズ**
行のヘッダーやキャプションをカスタマイズするには:

1. Web フォーム/ページに Aspose.Cells.GridWeb コントロールを追加します。
1. GridWorksheetCollection内のワークシートにアクセスします。
1. 指定した行のキャプションを設定します。

**行1および2のヘッダーがカスタマイズされました** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **列ヘッダーのカスタマイズ**
列のヘッダーやキャプションをカスタマイズするには:

1. Web フォーム/ページに Aspose.Cells.GridWeb コントロールを追加します。
1. GridWorksheetCollection内のワークシートにアクセスします。
1. 指定した列のキャプションを設定します。

**列1および2のヘッダーがカスタマイズされました** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **行と列の固定、解除**
このトピックでは、行や列を凍結および解凍する方法について説明します。列や行を凍結すると、ユーザーはワークシートの他の部分にスクロールする際にも、列の見出しや行のタイトルを表示した状態で保持することができます。この機能は、大量のデータを含むワークシートで作業する際に非常に役立ちます。ユーザーがスクロールする際にも、見出しはそのままでデータのみがスクロールし、データを見やすくします。凍結の機能は、Internet Explorer 6.0 以降でのみサポートされています。
### **行と列の凍結**
特定の行数と列数を凍結するには:

1. Web フォーム/ページに Aspose.Cells.GridWeb コントロールを追加します。
1. ワークシートにアクセスします。
1. 行数と列数を凍結します。

{{% alert color="primary" %}} 

インターフェースを使用して特定の行数と列数を凍結することも可能です。行数と列数を凍結したいセルを右クリックし、リストから **凍結** を選択します。

{{% /alert %}} 

**凍結状態の行と列** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **行と列の凍結を解除**
行と列を解凍するには:

1. Web フォーム/ページに Aspose.Cells.GridWeb コントロールを追加します。
1. ワークシートにアクセスします。
1. 行と列を解凍します。

**解凍後のワークシート** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **行と列の保護**
このトピックでは、エンドユーザーによる行と列内のセルのいかなるアクションからも保護するためのいくつかの技術について説明します。開発者は、行と列内のセルを読み取り専用にすること、または GridWeb のコンテキストメニューオプションを制限することで、この保護を実装することができます。
### **コンテキストメニューオプションの制限**
GridWebは、コントロール上で操作を実行するためにエンドユーザーが使用できるコンテキストメニューを提供します。このメニューにはセル、行、列を操作するための多くのオプションがあります。

**完全なコンテキストオプション** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

コンテキストメニューで利用可能なオプションを制限することで、行や列に対する任意のクライアントサイド操作を制限することが可能です。これは、GridWebコントロールのEnableClientColumnOperationsおよびEnableClientRowOperations属性をfalseに設定することで行えます。また、GridWebコントロールのEnableClientFreeze属性をfalseに設定することで、ユーザーが行や列を固定することも制限することが可能です。

**行と列のオプションを制限した後のコンテキストメニュー** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
