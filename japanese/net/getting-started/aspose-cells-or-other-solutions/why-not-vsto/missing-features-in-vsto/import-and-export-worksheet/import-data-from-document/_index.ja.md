---
title: ドキュメントからデータをインポート
type: docs
weight: 20
url: /ja/net/import-data-from-document/
---

データは、生の事実の集まりであり、これらの生の事実をより意味のある形で提示するためにスプレッドシートドキュメントやレポートを作成します。通常、スプレッドシートにデータを追加しますが、既存のデータリソースを再利用する必要がある場合があります。その際に異なるデータソースからワークシートにデータをインポートする必要があります。このトピックでは、異なるデータソースからワークシートにデータをインポートするためのいくつかの技術について説明します。

**Aspose.Cells**を使用したデータのインポート 
**Aspose.Cells**を使用してExcelファイルを開くと、ファイルのすべてのデータが自動的にインポートされますが、Aspose.Cellsは異なるデータソースからのデータのインポートもサポートしています。いくつかのデータソースのうちいくつかを以下に示します。

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cellsは、Excelファイルを表す**Workbook**クラスを提供しています。Workbookクラスには、Excelファイルの各ワークシートにアクセスすることができるWorksheetsコレクションが含まれています。ワークシートはWorksheetクラスで表されます。WorksheetクラスはCellsコレクションを提供しています。

Cellsコレクションは、異なるデータソースからのデータのインポートに非常に有用なメソッドを提供しています。

このセクションには以下のトピックがあります。

- [配列からのインポート](/cells/ja/net/importing-from-array/)
- [ArrayListからのインポート](/cells/ja/net/importing-from-arraylist/)
- [カスタムオブジェクトからのインポート](/cells/ja/net/importing-from-custom-objects/)
- [DataTableからのインポート](/cells/ja/net/importing-from-datatable/)
{{< app/cells/assistant language="csharp" >}}
