---
title: Excel マクロ有効ブックの VBA コードを管理します。
linktitle: マクロプロジェクト
type: docs
weight: 200
url: /ja/net/manage-vba-project/
description: VBA モジュールを追加し、VBA またはマクロを Aspose.Cells ライブラリで変更します。
---
## **C# に VBA モジュールを追加します。**
{{% alert color="primary" %}}

Aspose.Cells を使用すると、Aspose.Cells を使用して新しい VBA モジュールとマクロ コードを追加できます。[**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index)ワークブック内に新しい VBA モジュールを追加するメソッド

{{% /alert %}}

次のサンプル コードは、新しいワークブックを作成し、新しい VBA モジュールとマクロ コードを追加して、出力を XLSM 形式で保存します。一度、出力された XLSM ファイルを Microsoft Excel で開き、**開発者 > Visual Basic**メニュー コマンドを実行すると、"TestModule" という名前のモジュールが表示され、その中に次のマクロ コードが表示されます。

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

VBA モジュールとマクロ コードを使用して出力 XLSM ファイルを生成するサンプル コードを次に示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **C# の VBA またはマクロを変更します。**

{{% alert color="primary" %}} 

Aspose.Cells を使用して VBA またはマクロ コードを変更できます。

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- Vbaモジュール

この記事では、Aspose.Cells を使用して、ソース Excel ファイル内の VBA またはマクロ コードを変更する方法について説明します。

{{% /alert %}} 

次のサンプル コードは、次の VBA またはマクロ コードを含むソース Excel ファイルを読み込みます。

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Aspose.Cells サンプルコードを実行すると、VBA またはマクロコードは次のように変更されます。

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

ダウンロードできます[ソースの Excel ファイル](5112508.xlsm)そしてその[出力エクセルファイル](5112511.xlsm)指定されたリンクから。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **先行トピック**
- [ワークブックの VBA プロジェクトへのライブラリ参照を追加する](/cells/ja/net/add-a-library-reference-to-vba-project-in-workbook/)
- [フォーム コントロールへのマクロの割り当て](/cells/ja/net/assign-macro-to-form-control/)
- [VBA コードのデジタル署名が有効かどうかを確認する](/cells/ja/net/check-if-digital-signature-of-vba-code-is-valid/)
- [VBA コードが署名されているかどうかを確認する](/cells/ja/net/check-if-vba-code-is-signed/)
- [ワークブック内の VBA プロジェクトが署名されているかどうかを確認する](/cells/ja/net/check-if-vba-project-in-a-workbook-is-signed/)
- [VBA プロジェクトが保護され、表示用にロックされているかどうかを確認する](/cells/ja/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [VBA マクロ UserForm DesignerStorage をテンプレートからターゲット ワークブックにコピーする](/cells/ja/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [証明書を使用して VBA コード プロジェクトにデジタル署名する](/cells/ja/net/digitally-sign-a-vba-code-project-with-certificate/)
- [VBA 証明書をファイルまたはストリームにエクスポートする](/cells/ja/net/export-vba-certificate-to-file-or-stream/)
- [ワークブックの読み込み中に VBA プロジェクトをフィルター処理する](/cells/ja/net/filter-vba-project-while-loading-a-workbook/)
- [VBA プロジェクトが保護されているかどうかを調べる](/cells/ja/net/find-out-if-vba-project-is-protected/)
- [Excel ワークブックの VBA プロジェクトをパスワードで保護する](/cells/ja/net/password-protect-the-vba-project-of-excel-workbook/)

