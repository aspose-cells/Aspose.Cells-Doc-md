---
title: VBAプロジェクトが保護されているかどうかを調べる
type: docs
weight: 20
url: /ja/net/find-out-if-vba-project-is-protected/
---

## **C#でVBAプロジェクトが保護されているかどうかを確認する**

Aspose.Cellsを使用して、ExcelファイルのVBA（Visual Basic Applications）プロジェクトが保護されているかどうかを確認できます。[**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected)プロパティを使用します。

## **サンプルコード**

以下のサンプルコードは、ワークブックを作成し、そのVBAプロジェクトが保護されているかどうかを確認し、保護を設定し、再度そのVBAプロジェクトが保護されているかどうかを確認します。参照のためにコンソール出力をご覧ください。保護前に[**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected)は**false**を返し、保護後に**true**を返します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-FindoutifVBAProjectisProtected.cs" >}}

## **コンソール出力**

上記サンプルコードのコンソール出力の参考情報です。

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
