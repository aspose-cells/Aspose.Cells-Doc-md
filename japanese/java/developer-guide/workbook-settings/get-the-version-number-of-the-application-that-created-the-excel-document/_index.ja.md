---
title: Excelドキュメントを作成したアプリケーションのバージョン番号を取得する
type: docs
weight: 150
url: /ja/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

しばしば、Microsoft Excelドキュメントを作成したアプリケーションのバージョン番号が必要となります。Aspose.Cellsはこのために[**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version)プロパティを提供しています。

{{% /alert %}}

次のサンプルコードでは、[**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version)プロパティの使用方法を示しています。これは、Microsoft Excel 2003、2007、2010、2013で作成したExcelファイルをロードして、これらのExcelドキュメントを作成したアプリケーションのバージョン番号を出力します。

参照のために、以下はサンプルコードのコンソール出力です。

{{< highlight java >}}

Excel 2003 XLS Version: 726502

Excel 2007 XLS Version: 786432

Excel 2010 XLS Version: 917504

Excel 2013 XLS Version: 983040

Excel 2007 XLSX Version: 12.0000

Excel 2010 XLSX Version: 14.0300

Excel 2013 XLSX Version: 15.0300

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetVersionNumberofApplication-GetVersionNumberofApplication.java" >}}
