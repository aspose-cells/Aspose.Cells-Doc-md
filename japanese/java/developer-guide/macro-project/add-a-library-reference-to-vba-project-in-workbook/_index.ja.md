---
title: ワークブックの VBA プロジェクトへのライブラリ参照を追加する
type: docs
weight: 10
url: /ja/java/add-a-library-reference-to-vba-project-in-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel では、**ツール > 参照...**手動で。次のダイアログ ボックスが開き、既存の参照から選択したり、自分のライブラリを参照したりできます。

![todo:画像_代替_文章](add-a-library-reference-to-vba-project-in-workbook_1.png)

ただし、場合によっては、コードを使用してライブラリ参照を VBA プロジェクトに追加または登録する必要があります。 Aspose.Cellsを使用して行うことができます[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)） 方法。

{{% /alert %}}

## **ワークブックの VBA プロジェクトへのライブラリ参照を追加する**

次のサンプル コードは、ワークブックの VBA プロジェクトに 2 つのライブラリ参照を追加または登録します。[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
