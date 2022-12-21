---
title: データの検索または検索
type: docs
weight: 120
url: /ja/java/find-or-search-data/
---
{{% alert color="primary" %}} 

 Microsoft Excel では、ユーザーは特定のデータを含むセルを検索できます。たとえば、**編集**その後**探す**検索ダイアログを開きます。ユーザーが値を入力してクリック**わかった**それを検索します。 Excel で一致するフィールドが強調表示されます。

**検索ダイアログを使用して特定の値を含むセルを検索する** 

![todo:画像_代替_文章](find-or-search-data_1.png)

この例では、検索値は「オレンジ」です。

Aspose.Cells を使用すると、開発者はワークシート内のセルを検索して、特定の値を含むセルを見つけることができます。

{{% /alert %}} 
## **特定のデータを含む Cells の検索**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)、Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスが含まれています[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)、Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。

の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスが提供する[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)、ワークシート内のすべてのセルを表すコレクション。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection には、ユーザー指定のデータを含むワークシート内のセルを検索するためのメソッドがいくつか用意されています。これらの方法のいくつかについて、以下で詳しく説明します。

すべての検索メソッドは、指定された検索値を含むセルのセル参照を返します。
## **数式を含む検索**
開発者は、を呼び出してワークシート内の指定された数式を見つけることができます。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの[探す](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\) メソッド、設定[FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType)に[LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS)にパラメータとして渡します。[探す](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)） 方法。

通常、[探す](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) メソッドは 2 つ以上のパラメーターを受け入れます。

- 検索するオブジェクト: ワークシートで検索する必要があるオブジェクトを表します。
- 前の Cell: は、同じ数式を持つ前のセルを表します。最初から検索する場合、このパラメーターを null に設定できます。
- 検索オプション: 検索条件を表します。以下の例では、次のワークシート データを使用してメソッドの検索を練習します。

**サンプル ワークシート データ** 

![todo:画像_代替_文章](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **文字列の検索**
文字列値を含むセルの検索は、簡単かつ柔軟です。検索にはさまざまな方法があります。たとえば、特定の文字または文字セットで始まる文字列を含むセルを検索します。
### **特定の文字で始まる文字列を検索する**
文字列の最初の文字を検索するには、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの[探す](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) メソッドで、[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType)に[LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH)にパラメータとして渡します。[探す](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **特定の文字で終わる文字列を検索する**
Aspose.Cells は、特定の文字で終わる文字列も検索できます。文字列の最後の文字を検索するには、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの[探す](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) メソッドで、[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType)に[LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH)にパラメータとして渡します。[探す](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **正規表現による検索: RegEx 機能**
正規表現は、特定の文字、単語、またはパターンなどのテキストの文字列を照合 (指定および認識) するための簡潔で柔軟な手段を提供します。

たとえば、正規表現パターン abc-* ~~xyz~~ は、文字列「abc-123-xyz」、「abc-985-xyz」、および「abc-pony-xyz」に一致します。*はワイルドカードであるため、途中の文字に関係なく、パターンは「abc」で始まり「-xyz」で終わるすべての文字列に一致します。

Aspose.Cells は正規表現で検索できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **先行トピック**
- [特定のスタイルのセルを見つける](/cells/ja/java/find-cells-with-specific-style/)
- [元の値を使用してデータを検索する](/cells/ja/java/search-data-using-original-values/)
