---
title: ノード.jsとC++を使用したワークシートの保護解除
linktitle: ワークシートの保護解除
type: docs
weight: 20
url: /ja/nodejs-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

開発者が保護されたワークシートから保護を解除してファイルに変更を加える必要がある場合は？ Aspose.Cells を使用して簡単に行うことができます。

{{% /alert %}}

## **ワークシートの保護を解除する**

### **Microsoft Excel の使用**

ワークシートから保護を解除するには：

**ツール**メニューから**保護**を選択し、その後**シートの保護解除**を選びます。ワークシートがパスワード保護されていなければ、保護は解除されます。パスワード保護されている場合は、ダイアログでパスワードの入力を求められます。パスワードを入力すれば、シートの保護が解除されます。

### **Aspose.Cells を使用して単純に保護されたワークシートの保護解除**

ワークシートは、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスの[**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--)メソッドを呼び出すことで保護解除できます。パスワードなしの単純な保護されたシートは、パスワードで保護されていないシートです。このようなシートは、パラメータを渡さずに[**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--)メソッドを呼び出すことで解除可能です。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet without a password
worksheet.unprotect();

// Saving the Workbook
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Aspose.Cells を使用してパスワードで保護されたワークシートの保護解除**

パスワード保護されたワークシートは、パスワードで保護されたシートです。そのようなシートは、パスワードを引数に取るオーバーロードされた[**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--)メソッドを呼び出すことで解除できます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet with a password
worksheet.unprotect("");

// Save Workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
