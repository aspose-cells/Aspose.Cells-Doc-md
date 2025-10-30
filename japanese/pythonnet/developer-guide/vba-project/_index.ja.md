---
title: Excel Macro EnabledワークブックのVBAコードを管理する
linktitle: マクロプロジェクト
type: docs
weight: 200
url: /ja/python-net/manage-vba-project/
description: VBAモジュールを追加し、VBAまたはマクロをAspose.Cells for Python via .NETライブラリで編集します。
---

## **PythonでVBAモジュールを追加する**
{{% alert color="primary" %}}

Aspose.Cellsを使用すると、Aspose.Cells for Python via .NETを使って新しいVBAモジュールとマクロコードを追加できます。[**Workbook.vba_project.modules.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add/)メソッドを使用して、ワークブック内に新しいVBAモジュールを追加してください。

{{% /alert %}}

次のサンプルコードは、新しいワークブックを作成し、新しいVBAモジュールとマクロコードを追加し、出力をXLSM形式で保存します。作業結果のXLSMファイルをMicrosoft Excelで開いて**開発者 > Visual Basic**メニューコマンドをクリックすると、「TestModule」というモジュールが表示され、その中に次のマクロコードが表示されます。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

VBAモジュールとマクロコードを含む出力XLSMファイルを生成するためのサンプルコードは次のとおりです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AddVBAModuleOrCode.py" >}}

## **PythonでVBAまたはマクロを修正する**

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET を使用してVBAまたはマクロコードを修正できます。Aspose.Cells for Python via .NETには、Excelファイル内のVBAプロジェクトを読み取り修正するための名前空間とクラスが追加されています。

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

この記事では、Aspose.Cells for Python via .NETを使用してソースExcelファイル内のVBAまたはマクロコードを変更する方法を説明します。

{{% /alert %}} 

次のサンプルコードは、次のようなVBAまたはマクロコードが含まれているソースExcelファイルをロードします。

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Aspose.Cells for Python via .NETのサンプルコードを実行した後、VBAまたはマクロコードはこのように修正されます。

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

提供されたリンクから [ソースExcelファイル](5112508.xlsm) と [出力Excelファイル](5112511.xlsm) をダウンロードできます。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-ModifyingVBAOrMacroCode.py" >}}

## **高度なトピック**
- [ワークブック内のVBAプロジェクトにライブラリ参照を追加する](/cells/ja/python-net/add-a-library-reference-to-vba-project-in-workbook/)
- [VBAコードのデジタル署名が有効かどうかをチェックする](/cells/ja/python-net/check-if-digital-signature-of-vba-code-is-valid/)
- [VBAコードが署名されているかを確認する](/cells/ja/python-net/check-if-vba-code-is-signed/)
- [WorkbookのVBAプロジェクトが署名されているかを確認する](/cells/ja/python-net/check-if-vba-project-in-a-workbook-is-signed/)
- [VBAプロジェクトが保護されており、閲覧用にロックされているかを確認する](/cells/ja/python-net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [証明書でVBAコードプロジェクトにデジタル署名する](/cells/ja/python-net/digitally-sign-a-vba-code-project-with-certificate/)
- [VBA証明書をファイルまたはストリームにエクスポートする](/cells/ja/python-net/export-vba-certificate-to-file-or-stream/)
- [ワークブックの読み込み時にVBAプロジェクトをフィルタリングする](/cells/ja/python-net/filter-vba-project-while-loading-a-workbook/)
- [VBAプロジェクトが保護されているかを調べる](/cells/ja/python-net/find-out-if-vba-project-is-protected/)
- [ExcelワークブックのVBAプロジェクトをパスワードで保護する](/cells/ja/python-net/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="python-net" >}}
