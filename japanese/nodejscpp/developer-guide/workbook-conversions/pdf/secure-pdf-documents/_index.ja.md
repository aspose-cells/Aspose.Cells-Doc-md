---
title: Node.js経由のC++でPDFドキュメントを安全にする
linktitle: セキュアなPDFドキュメント
type: docs
weight: 120
url: /ja/nodejs-cpp/secure-pdf-documents/
description: 所有者パスワードとユーザーパスワードを使用し、PDFファイルの許可設定を行ってPDFドキュメントの保護方法を学びます（Aspose.Cells for Node.js via C++を使用）。
---

{{% alert color="primary" %}}

開発者は、暗号化されたPDFファイルと作業する必要がある場合があります。

- ドキュメントをオーナーパスワードとユーザーパスワードでセキュリティ保護して、誰もがそれを開けなくする。
- ドキュメントを開いた後にドキュメントに制限や権限を設定します。例: ドキュメントの内容を印刷または抽出できるかどうかを制限します。

この記事では、スプレッドシートをPDFに保存する際にPDFセキュリティオプションを渡す方法について説明します。

{{% /alert %}}

Aspose.Cellsはセキュリティを扱うための[**PdfSecurityOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/)を提供します。PDFに保存する際に所有者パスワードとユーザーパスワードを設定できます。暗号化されたPDFドキュメントを開くには、所有者またはユーザーパスワードが必要です。

- ユーザーパスワードは null または空文字列に設定可能です。この場合、PDFを開くときにパスワードは必要ありません。
- 正しい所有者パスワードを使ってPDFドキュメントを開くと、アクセス制限なしでドキュメントに完全にアクセスできます。
- 正しいユーザーパスワードでPDFドキュメントを開く（またはユーザーパスワードのないドキュメントを開く）と、指定された権限に応じて限定されたアクセスが可能です。

以下のサンプルコードは、Aspose.CellsでPDFをセキュアにする方法を説明しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const saveOption = new AsposeCells.PdfSaveOptions();
saveOption.setSecurityOptions(new AsposeCells.PdfSecurityOptions());

saveOption.getSecurityOptions().setUserPassword("user");
saveOption.getSecurityOptions().setOwnerPassword("owner");
saveOption.getSecurityOptions().setExtractContentPermission(false);
saveOption.getSecurityOptions().setPrintPermission(false);

workbook.save(path.join(dataDir, "securepdf_test.out.pdf"), saveOption);
```

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、スプレッドシートをPDFにレンダリングする直前に[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)を呼び出すことが最善です。これにより、数式に依存した値が再計算され、正しい値がPDFに表示されます。

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
