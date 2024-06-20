---
title: リストオブジェクトの書式設定  テーブル
type: docs
weight: 50
url: /ja/java/format-a-list-object-table/
---

{{% alert color="primary" %}}

関連するデータのグループを管理および分析するには、セル範囲をリストオブジェクト（またはExcelテーブルとも呼ばれる）に変換することができます。 テーブルは、他の行や列のデータから独立して管理される関連データを含む行と列のシリーズです。 テーブルの各列には、ヘッダー行でフィルタリングが有効になっており、リストオブジェクトデータを迅速にフィルタリングまたは並べ替えることができます。 リストオブジェクトには特別な行（数値データで作業するために有用な集計関数の選択を提供するリスト内の特別な行）を追加することができます。 Aspose.Cellsには、リスト（またはテーブル）の作成と管理のためのオプションが用意されています。

{{% /alert %}}

## **リストオブジェクトの書式設定**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには、Excelファイルの各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスで表されます。 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)クラスには、ワークシートを管理するための多くのプロパティとメソッドが提供されています。 ワークシート内に[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)を作成するには、ワークシートクラスの[**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects)コレクションプロパティを使用します。 各[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)は実際には[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)クラスのオブジェクトであり、さらにはリストオブジェクトを追加し、リストオブジェクトの範囲を指定するためのaddメソッドを提供しています。 指定したセル範囲に応じて、Aspose.Cellsによって[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)がワークシートに作成されます。 テーブルをコントロールするための[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)クラスの属性（たとえば、[**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType)）を使用して、テーブルを独自の要件に応じて書式設定します。

以下の例では、ワークシートにサンプルデータを追加し、[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)を追加し、そのデフォルトスタイルを適用します。 Microsoft Excel 2007/2010でサポートされる[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)スタイルがサポートされます。

コードを実行すると、以下の出力が生成されます。

**ワークシートにフォーマットされたテーブルが作成されます** 

![todo:image_alt_text](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
