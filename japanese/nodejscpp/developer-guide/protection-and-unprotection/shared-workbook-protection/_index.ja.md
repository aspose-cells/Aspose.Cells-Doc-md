---
title: Node.js経由のC++を使った共有ブックの保護・解除
linktitle: 共有ブックをパスワードで保護または保護解除
type: docs
weight: 10
url: /ja/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **可能な使用シナリオ**

次のスクリーンショットのように、Microsoft Excelを使って共有ブックを保護または解除できます。Aspose.Cells for Node.js via C++もこの機能を[**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#protectSharedWorkbook-string-)および[**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#unprotectSharedWorkbook-string-)メソッドでサポートしています。

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **共有ワークブックのパスワード保護または保護解除**

次のサンプルコードは、ブックを作成し、共有を有効にした状態で保護し、[出力Excelファイル](55541777.xlsx)として保存します。スクリーンショットに示すように、保護を解除しようとすると、Microsoft Excelがパスワードの入力を要求します。

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **サンプルコード**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty Excel file
const workbook = new AsposeCells.Workbook();

// Protect the Shared Workbook with Password
workbook.protectSharedWorkbook("1234");

// Uncomment this line to Unprotect the Shared Workbook
// workbook.unprotectSharedWorkbook("1234");

// Save the output Excel file
workbook.save("outputProtectSharedWorkbook.xlsx");
```
