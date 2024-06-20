---
title: ワークブックのVBAプロジェクトにライブラリの参照を追加
type: docs
weight: 10
url: /ja/java/add-a-library-reference-to-vba-project-in-workbook/
description: Aspose.Cells for Java APIを介してワークブックのVBAプロジェクトにライブラリの参照を追加する方法を学ぶ。
keywords: ワークブックにVBAプロジェクトへのライブラリの参照を追加する方法、Javaを使用してワークブックにVBAプロジェクトへのライブラリの参照を追加する方法、Javaを使用してVBAプロジェクトにライブラリの参照を設定する方法。 
---

{{% alert color="primary" %}}

Microsoft Excelでは、**ツール > 参照設定**をクリックして、VBAプロジェクトにライブラリの参照を追加することができます。手動で行うことにより、既存の参照から選択したり、独自のライブラリを参照したりすることができます。

![todo:image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

ただし、時々、コードを使用してVBAプロジェクトにライブラリの参照を追加または登録する必要があります。Aspose.Cellsの[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String))メソッドを使用して行うことができます。

{{% /alert %}}

## **ブック内のVBAプロジェクトへのライブラリの参照の追加方法**

次のサンプルコードは、ブックのVBAプロジェクトに2つのライブラリ参照を追加または登録します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
