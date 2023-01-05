---
title: VBA プロジェクトが保護されているかどうかを調べる
type: docs
weight: 20
url: /ja/net/find-out-if-vba-project-is-protected/
---
## **VBA プロジェクトが C# で保護されているかどうかを調べる**

ExcelファイルのVBA（Visual Basic Applications）プロジェクトが保護されているかどうかは、Aspose.Cellsを使用して確認できます[**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected)財産。

## **サンプルコード**

次のサンプル コードは、ブックを作成し、その VBA プロジェクトが保護されているかどうかを確認します。次に、VBA プロジェクトを保護し、VBA プロジェクトが保護されているかどうかを再度確認します。コンソール出力を参照してください。保護前に、[**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected)戻り値**間違い**しかし、保護の後、それは戻ってきます**真実**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-FindoutifVBAProjectisProtected.cs" >}}

## **コンソール出力**

これは、参照用の上記のサンプル コードのコンソール出力です。

{{< highlight "java" >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
