---
title: Excelマクロ対応ワークブックのVBAコード管理
linktitle: マクロプロジェクト
type: docs
weight: 200
url: /ja/nodejs-cpp/manage-vba-project/
description: VBAモジュールを追加し、Aspose.Cells for Node.js via C++を使用してVBAやマクロを変更します。
---

## **Node.jsでVBAモジュールを追加**
{{% alert color="primary" %}}

Aspose.Cellsを使用すると、Aspose.Cells for Node.js via C++を使って新しいVBAモジュールとマクロコードを追加できます。[**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#add-worksheet-)メソッドを使用して、ワークブック内に新しいVBAモジュールを追加してください。

{{% /alert %}}

以下のサンプルコードは、新しいワークブックを作成し、新しいVBAモジュールとマクロコードを追加して、XLSM形式で保存します。出力されたXLSMファイルをMicrosoft Excelで開き、「開発」>「Visual Basic」をクリックすると、「TestModule」と名前付けられたモジュールと、その中のマクロコードが表示されます。

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}

VBAモジュールとマクロコードを含む出力XLSMファイルを生成するサンプルコードです。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add VBA Module
const idx = workbook.getVbaProject().getModules().add(worksheet);

// Access the VBA Module, set its name and codes
const module = workbook.getVbaProject().getModules().get(idx);
module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```

## **Node.jsでVBAやマクロを修正**

{{% alert color="primary" %}} 

Aspose.Cells for Node.js via C++を使用してVBAやマクロコードを修正できます。Aspose.Cellsには、ExcelファイルのVBAプロジェクトを読み取り、修正するためのモジュールとクラスが追加されています。

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

この記事では、Aspose.Cellsを使用してソースExcelファイル内のVBAまたはマクロコードを変更する方法を説明します。

{{% /alert %}} 

以下のサンプルコードは、内包されているVBAまたはマクロコードを持つソースExcelファイルを読み込みます。

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

Aspose.Cellsのサンプルコードの実行後、VBAまたはマクロコードは次のように変更されます。

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

提供されたリンクから [ソースExcelファイル](5112508.xlsm) と [出力Excelファイル](5112511.xlsm) をダウンロードできます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsm"));

// Change the VBA Module Code
const modules = workbook.getVbaProject().getModules();
const moduleCount = modules.getCount();
for (let i = 0; i < moduleCount; i++) {
const module = modules.get(i);
const code = module.getCodes();
if (code.includes("This is test message.")) 
{
code = code.replace("This is test message.", "This is Aspose.Cells message.");
module.setCodes(code);
}
}


// Save the output Excel file
workbook.save(path.join(dataDir, "output_out.xlsm"));
```

## **高度なトピック**
- [ワークブック内のVBAプロジェクトにライブラリ参照を追加する](/cells/ja/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [フォームコントロールにマクロを割り当てる](/cells/ja/nodejs-cpp/assign-macro-to-form-control/)
- [VBAコードのデジタル署名が有効かどうかをチェックする](/cells/ja/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [VBAコードが署名されているかを確認する](/cells/ja/nodejs-cpp/check-if-vba-code-is-signed/)
- [WorkbookのVBAプロジェクトが署名されているかを確認する](/cells/ja/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [VBAプロジェクトが保護されており、閲覧用にロックされているかを確認する](/cells/ja/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [テンプレートからターゲットワークブックへのVBAマクロUserForm DesignerStorageのコピー](/cells/ja/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [証明書でVBAコードプロジェクトにデジタル署名する](/cells/ja/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [VBA証明書をファイルまたはストリームにエクスポートする](/cells/ja/nodejs-cpp/export-vba-certificate-to-file-or-stream/)
- [ワークブックの読み込み時にVBAプロジェクトをフィルタリングする](/cells/ja/nodejs-cpp/filter-vba-project-while-loading-a-workbook/)
- [VBAプロジェクトが保護されているかを調べる](/cells/ja/nodejs-cpp/find-out-if-vba-project-is-protected/)
- [ExcelワークブックのVBAプロジェクトをパスワードで保護する](/cells/ja/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="nodejs-cpp" >}}
