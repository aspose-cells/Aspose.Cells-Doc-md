---
title: VBA プロジェクトが保護されているかどうかを調べる
type: docs
weight: 80
url: /ja/java/find-out-if-vba-project-is-protected/
---
## **考えられる使用シナリオ**
ExcelファイルのVBA（Visual Basic Applications）プロジェクトが保護されているかどうかは、Aspose.Cellsを使用して確認できます[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected)方法
## **サンプルコード**
次のサンプル コードは、ブックを作成し、その VBA プロジェクトが保護されているかどうかを確認します。次に、VBA プロジェクトを保護し、VBA プロジェクトが保護されているかどうかを再度確認します。コンソール出力を参照してください。保護前に、[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected)戻り値**間違い**しかし、保護の後、それは戻ってきます**真実**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **コンソール出力**
これは、参照用の上記のサンプル コードのコンソール出力です。

{{< highlight "java" >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
