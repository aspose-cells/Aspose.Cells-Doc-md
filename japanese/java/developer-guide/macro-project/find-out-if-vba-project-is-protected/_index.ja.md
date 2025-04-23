---
title: VBAプロジェクトが保護されているかどうかを調べる
type: docs
weight: 80
url: /ja/java/find-out-if-vba-project-is-protected/
---

## **可能な使用シナリオ**
Aspose.Cellsを使用してExcelファイルのVBA（Visual Basic Applications）プロジェクトが保護されているかどうかを確認できます。[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) メソッドを使用します。
## **サンプルコード**
次のサンプルコードは、ワークブックを作成し、そのVBAプロジェクトが保護されているかどうかを確認し、VBAプロジェクトを保護し、再度そのVBAプロジェクトが保護されているかどうかを確認します。参考のためにコンソール出力をご覧ください。保護前には[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) は**false**を返しますが、保護後は**true**を返します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **コンソール出力**
上記サンプルコードのコンソール出力の参考情報です。

{{< highlight java >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
