---
title: VBAプロジェクトが保護されているかどうかを調べる
type: docs
weight: 20
url: /ja/python-net/find-out-if-vba-project-is-protected/
---

## **PythonでVBAプロジェクトの保護状態を確認する**

Aspose.Cells for Python via .NETを使用して、Excelファイル内のVBA（Visual Basic Applications）プロジェクトが保護されているかどうかを[**VbaProject.is_protected**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_protected)プロパティで判定可能です。

## **サンプルコード**

以下のサンプルコードは、ワークブックを作成し、そのVBAプロジェクトが保護されているかどうかを確認し、保護を設定し、再度そのVBAプロジェクトが保護されているかどうかを確認します。参照のためにコンソール出力をご覧ください。保護前に[**VbaProject.is_protected**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_protected)は**false**を返し、保護後に**true**を返します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FindoutifVBAProjectisProtected.py" >}}

## **コンソール出力**

上記サンプルコードのコンソール出力の参考情報です。

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}

