---
title: ノード.jsとC++を使用したシートのパスワード保護の検証
linktitle: ワークシートを保護するために使用されたパスワードの検証
type: docs
weight: 370
url: /ja/nodejs-cpp/verify-password-used-to-protect-the-worksheet/
description: Aspose.Cells for Node.js via C++を使ってシートを保護するために使用したパスワードの検証方法について学習します。
---

{{% alert color="primary" %}}

Aspose.Cells APIは、便利なプロパティとメソッドを導入して[**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection)クラスを強化しました。その一つが[**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-)であり、パスワードを*string*として指定し、同じパスワードがシートの保護に使用されたかどうかを検証します。

{{% /alert %}}

[**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-)メソッドは、指定されたパスワードが対象のワークシートを保護するために使用されたパスワードと一致すれば**true**を返し、一致しなければ**false**を返します。次のコード例は、[**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-)メソッドと[**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--)プロパティを併用してパスワード保護を検出し、パスワードを確認します。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Create an instance of Workbook and load a spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Access the protected Worksheet
const sheet = workbook.getWorksheets().get(0);

// Check if Worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
// Verify the password used to protect the Worksheet
if (sheet.getProtection().verifyPassword("1234")) {
console.log("Specified password has matched");
} else {
console.log("Specified password has not matched");
}
}
```
