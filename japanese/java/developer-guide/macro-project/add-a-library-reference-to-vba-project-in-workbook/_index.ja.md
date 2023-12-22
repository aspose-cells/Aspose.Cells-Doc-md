---
title: ワークブック内の VBA プロジェクトへのライブラリ参照を追加します。
type: docs
weight: 10
url: /ja/java/add-a-library-reference-to-vba-project-in-workbook/
description: Aspose.Cells for Java API を通じて、ワークブック内の VBA プロジェクトにライブラリ参照を追加する方法を学習します。
keywords: How to Add a library reference to VBA project in workbook in Java, Insert a library reference to VBA project in workbook using Java, Java Set library reference to VBA project in workbook. 
---
{{% alert color="primary" %}}

 Microsoft Excel では、**[ツール] > [参照...]**手動で。次のダイアログ ボックスが開き、既存の参照から選択するか、自分でライブラリを参照することができます。

![todo:image_alt_text](add-a-library-reference-to-vba-project-in-workbook_1.png)

ただし、場合によっては、コードを通じて VBA プロジェクトにライブラリ参照を追加または登録する必要があります。 Aspose.Cellsを使用して行うことができます[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)） 方法。

{{% /alert %}}

##  **ワークブック内の VBA プロジェクトにライブラリ参照を追加する方法**

次のサンプル コードは、ワークブックの VBA プロジェクトに 2 つのライブラリ参照を追加または登録します。[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
