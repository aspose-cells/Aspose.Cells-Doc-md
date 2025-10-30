---  
title: Node.js経由のC++を使ったブック構造の保護・解除  
linktitle: ブック構造の保護と保護解除  
type: docs  
weight: 40  
url: /ja/nodejs-cpp/protect-and-unprotect-workbook-structure/  
description: Excelファイルのブック構造をNode.js経由のC++を使って保護または解除します。  
---  


{{% alert color="primary" %}}  
他のユーザーによる隠しワークシートの表示、追加、移動、削除、または非表示、およびワークシートの名前の変更を防ぐために、Excelブックの構造をパスワードで保護できます。  
{{% /alert %}}  


## **MS Excelでのブック構造の保護と保護解除**  

**![ブック構造の保護と保護解除](protect-and-unprotect-workbook-structure.png)**  

1. **レビュー > ブックの保護** をクリックします。  
1. **パスワードボックス** にパスワードを入力します。  
1. **OK** を選択し、パスワードを再入力して確認し、その後再度 **OK** を選択します。  


## **Aspose.Cells for Node.js via C++を使用したブック構造の保護**  
Excelファイルのワークシートの構造を保護するためには、次の簡単なコード行のみが必要です。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Protect workbook structure.
workbook.protect(AsposeCells.ProtectionType.Structure, "password");
// Save Excel file.
workbook.save(filePath);
```  

## **Aspose.Cells for Node.js via C++を使用したブック構造の解除**  
Aspose.Cells APIを使用してワークブック構造を保護解除するのは簡単です。正しいパスワードが必要です。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open an Excel file which workbook structure is protected.
const workbook = new AsposeCells.Workbook(filePath);
// Unprotect workbook structure.
workbook.unprotect("password");
// Save Excel file.
workbook.save(filePath);
```  

{{% alert color="primary" %}}  
注意：正しいパスワードが必要です。  
{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
