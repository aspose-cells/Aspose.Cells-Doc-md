---
title: データの検索または検索
type: docs
weight: 120
url: /ja/java/find-or-search-data/
---

{{% alert color="primary" %}} 

Microsoft Excel では、特定のデータを含むセルを検索できます。たとえば、**編集** をクリックして**検索**をクリックすると、検索ダイアログが開きます。ユーザーは値を入力し、**OK** をクリックして検索できます。Excel は一致するフィールドを強調表示します。

**特定の値を含むセルを検索するための検索ダイアログを使用する方法** 

![todo:image_alt_text](find-or-search-data_1.png)

この例では、検索値は「オレンジ」です。

Aspose.Cells は、ワークシート内のセルを検索して特定の値を含むものを検索することができます。

{{% /alert %}} 
## **特定のデータを含むセルを検索する**
Aspose.Cells はExcelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) クラスを提供します。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) クラスには、Excelファイル内の各ワークシートにアクセスできるコレクションである[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) が含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスで表されます。

[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスは、ワークシート内のすべてのセルを表す[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションを提供します。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションには、ワークシート内の特定のデータを含むセルを検索するためのいくつかのメソッドがあります。これらのメソッドのうちいくつかについて以下で詳しく説明します。

すべての検索メソッドは、指定された検索値を含むセルの参照を返します。
## **数式を含むセルを検索**
開発者は[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションの[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) メソッドを呼び出し、[FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) を[LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS) に設定し、それを[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) メソッドのパラメータとして渡すことで、ワークシート内の指定された数式を検索できます。

通常、[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) メソッドは、2つ以上のパラメータを受け入れます:

- 検索するオブジェクト: ワークシート内で検索するオブジェクトを表します。
- 前のセル: 同じ数式を持つ以前のセルを表します。このパラメータは、開始位置から検索する場合はnullに設定できます。
- オプションの検索：検索条件を表します。以下の例では、次のワークシートデータが検索メソッドの練習に使用されます。

**サンプルのワークシートデータ** 

![todo:image_alt_text](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **文字列を検索**
文字列値を含むセルを検索することは簡単で柔軟です。例えば、特定の文字または文字列で始まる文字列を含むセルを検索する方法など、さまざまな検索方法があります。
### **特定の文字で始まる文字列を検索する**
文字列内の最初の文字を検索するには、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))メソッドを呼び出し、[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType)を[LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH)に設定して、そのパラメータを[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))メソッドに渡します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **特定の文字で終わる文字列を検索**
Aspose.Cellsでは、特定の文字で終わる文字列も検索できます。文字列内の最後の文字を検索するには、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))メソッドを呼び出し、[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType)を[LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH)に設定して、そのパラメータを[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))メソッドに渡します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **正規表現を使用した検索：RegEx機能**
正規表現は、特定の文字、単語、またはパターンなどの文字列を簡潔かつ柔軟にマッチング（指定および認識）する手段を提供します。

例えば、正規表現パターンabc-*~~xyz~~は、"abc-123-xyz"、"abc-985-xyz"、"abc-pony-xyz"の文字列とマッチします。*はワイルドカードなので、このパターンは"abc"で始まり"-xyz"で終わる任意の文字列にマッチします。

Aspose.Cellsを使用して正規表現で検索できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **高度なトピック**
- [特定のスタイルを持つセルを検索](/cells/ja/java/find-cells-with-specific-style/)
- [元の値を使用したデータの検索](/cells/ja/java/search-data-using-original-values/)
