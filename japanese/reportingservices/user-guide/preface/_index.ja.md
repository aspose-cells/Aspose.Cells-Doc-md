---
title: 序文
type: docs
weight: 20
url: /ja/reportingservices/preface/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services は主に Aspose.Cells.Report.Designer と Aspose.Cells.Renderer for Reporting Services の 2 つのコンポーネントで構成されています。前者は Microsoft Excel で直接レポートを設計するために使用され、後者は RDL レポートを Microsoft Excel にレンダリングする責務を持っています。 

{{% /alert %}} 
### **レポートデザイナーを使用したレポートの設計**
Aspose.Cells.Report.Designer を使用してレポートを設計する主要なステップは次のとおりです：

1. データソースとクエリを作成します。
   Microsoft Query は Aspose.Cells.Report.Designer と統合され、データソースとクエリを作成するためのグラフィックツールとして使用されます。ユーザーは既存のデータソースとクエリが操作可能な RDL ファイルも使用できます。
1. パラメータをマップします。
   クエリの SQL ステートメントにパラメータが含まれる場合、ユーザーはレポートパラメーターを作成し、SQL パラメーターをレポートパラメーターにマッピングする必要があります。Aspose.Cells.Report.Designer では、レポートパラメーターの有効な値を指定することができます。
1. Microsoft Excel レポートテンプレートのコンテンツ、スタイル、フォーマットを設計します。
   Aspose.Cells レポートテンプレートには、次のタイプのレポートアイテムを任意の数含めることができます： 
   1. 表
   1. ピボットテーブル
   1. チャート
   1. テキストボックス
   1. マトリックス
      通常、クエリ（つまり、DataSet）はレポートアイテムのデータソースとして使用されます。一部のレポートアイテムに対しては、Reporting Services のパラメーターや式、グローバル変数をデータソースとして使用することもできます。レポートアイテムのスタイルとフォーマットは、単純にレポートアイテムを構成するセルのスタイルとフォーマットを設定することで指定されます。
1. レポートを公開します。
   上記の手順を経て、レポートは公開の準備が整いました。ユーザーはレポートを公開するフォルダを指定することができます。必要に応じて、レポートのデータソースとして Report Server 上の共有データソースを割り当てることができます。
1. レポートをプレビューします。
   Report Server 上でレポートをプレビューする際には、エクスポートするファイル形式（たとえば Microsoft Excel 97-2003 バイナリ XLS 形式、SpreadsheetML、Microsoft Excel 2007 XLSX 形式）と、レポート設計中に作成された入力レポートパラメーターを指定する必要があります。その後、Reporting Services によって提供されるデータでレポートが埋め込まれます。
