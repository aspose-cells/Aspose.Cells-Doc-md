---
title: Excel Macro EnabledワークブックのVBAコードを管理する
linktitle: マクロプロジェクト
type: docs
weight: 200
url: /ja/net/manage-vba-project/
description: Aspose.Cellsライブラリを使用してVBAモジュールを追加し、VBAまたはマクロを変更します。
---

## **C#でVBAモジュールを追加**
{{% alert color="primary" %}}

Aspose.Cellsを使用して新しいVBAモジュールとマクロコードを追加することができます。新しいVBAモジュールをワークブック内に追加するには、[**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index)メソッドを使用してください。

{{% /alert %}}

次のサンプルコードは、新しいワークブックを作成し、新しいVBAモジュールとマクロコードを追加し、出力をXLSM形式で保存します。作業結果のXLSMファイルをMicrosoft Excelで開いて**開発者 > Visual Basic**メニューコマンドをクリックすると、「TestModule」というモジュールが表示され、その中に次のマクロコードが表示されます。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

VBAモジュールとマクロコードを含む出力XLSMファイルを生成するためのサンプルコードは次のとおりです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **C#でVBAまたはマクロを変更する**

{{% alert color="primary" %}} 

Aspose.Cellsを使用してVBAまたはマクロコードを変更できます。Aspose.Cellsは、Excelファイル内のVBAプロジェクトを読み取り、変更するための次の名前空間とクラスを追加しました。

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

この記事では、Aspose.Cellsを使用してソースExcelファイル内のVBAまたはマクロコードを変更する方法を説明します。

{{% /alert %}} 

次のサンプルコードは、次のようなVBAまたはマクロコードが含まれているソースExcelファイルをロードします。

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Aspose.Cellsのサンプルコードの実行後、VBAまたはマクロコードは次のように変更されます。

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

提供されたリンクから [ソースExcelファイル](5112508.xlsm) と [出力Excelファイル](5112511.xlsm) をダウンロードできます。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **高度なトピック**
- [ワークブック内のVBAプロジェクトにライブラリ参照を追加する](/cells/ja/net/add-a-library-reference-to-vba-project-in-workbook/)
- [フォームコントロールにマクロを割り当てる](/cells/ja/net/assign-macro-to-form-control/)
- [VBAコードのデジタル署名が有効かどうかをチェックする](/cells/ja/net/check-if-digital-signature-of-vba-code-is-valid/)
- [VBAコードが署名されているかを確認する](/cells/ja/net/check-if-vba-code-is-signed/)
- [WorkbookのVBAプロジェクトが署名されているかを確認する](/cells/ja/net/check-if-vba-project-in-a-workbook-is-signed/)
- [VBAプロジェクトが保護されており、閲覧用にロックされているかを確認する](/cells/ja/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [テンプレートからターゲットワークブックへのVBAマクロUserForm DesignerStorageのコピー](/cells/ja/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [証明書でVBAコードプロジェクトにデジタル署名する](/cells/ja/net/digitally-sign-a-vba-code-project-with-certificate/)
- [VBA証明書をファイルまたはストリームにエクスポートする](/cells/ja/net/export-vba-certificate-to-file-or-stream/)
- [ワークブックの読み込み時にVBAプロジェクトをフィルタリングする](/cells/ja/net/filter-vba-project-while-loading-a-workbook/)
- [VBAプロジェクトが保護されているかを調べる](/cells/ja/net/find-out-if-vba-project-is-protected/)
- [ExcelワークブックのVBAプロジェクトをパスワードで保護する](/cells/ja/net/password-protect-the-vba-project-of-excel-workbook/)

