---
title: ワークブックのAutoRecoverプロパティを設定する方法
type: docs
weight: 160
url: /ja/java/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してワークブックのAutoRecoverプロパティを設定できます。このプロパティのデフォルト値は**true**です。ワークブックで**false**に設定すると、Microsoft ExcelはそのExcelファイルのAutorecover（Autosave）を無効にします。

Aspose.Cellsは、このオプションを有効または無効にするための[**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover)プロパティを提供しています。

{{% /alert %}}

ワークブックのAutoRecoverプロパティの設定に関するJavaコード

次のコードは、ワークブックの[**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover)プロパティの使用方法を説明しています。コードはまず、これが**true**であるデフォルト値を読み取り、**false**として設定してワークブックを保存します。その後、ワークブックを再度読み取り、この時点でのこのプロパティの値、つまりfalseを読み取ります。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

サンプルコードによって生成された出力

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
