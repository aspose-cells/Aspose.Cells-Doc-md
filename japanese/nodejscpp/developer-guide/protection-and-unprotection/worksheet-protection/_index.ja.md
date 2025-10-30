---  
title: Node.js経由のC++を使ったワークシートの保護・解除  
linktitle: ワークシートの保護と保護解除  
type: docs  
weight: 40  
url: /ja/nodejs-cpp/protect-and-unprotect-worksheets/  
description: ExcelファイルのワークシートをAspose.Cells for Node.js via C++で保護・解除します。  
---  

{{% alert color="primary" %}}  
ワークシート上のデータの変更、移動、または削除を他のユーザーが誤ってまたは意図的に防ぐために、Excelワークシートのセルをロックし、その後シートをパスワードで保護できます。  
{{% /alert %}}  

## **MS Excelでのワークシートの保護と保護解除**  

**![ワークシートの保護と保護解除](protect-and-unprotect-worksheet.png)**  

1. **レビュー > ワークシートの保護** をクリックします。  
1. **パスワードボックス** にパスワードを入力します。  
1. **許可** オプションを選択します。  
1. **OK** を選択し、パスワードを再入力して確認し、その後再度 **OK** を選択します。  

## **Aspose.Cells for Node.js via C++を使用したワークシートの保護**  
Excelファイルのワークシートの構造を保護するためには、次の簡単なコード行のみが必要です。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.protect(AsposeCells.ProtectionType.Contents);
// Protect worksheet with password.
sheet.getProtection().setPassword("test");
// Save as Excel file.
workbook.save("Book1.xlsx");
```  

## **Aspose.Cells for Node.js via C++を使用したワークシートの解除**  
ワークシートの解除は、Aspose.Cells APIを使えば簡単です。ワークシートがパスワード保護されている場合、正しいパスワードが必要です。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook(filePath);
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.unprotect("password");
// Save Excel file.
workbook.save("Book1.xlsx");
```  

## **高度なトピック**  
- [Excel XP以降の高度な保護設定](/cells/ja/nodejs-cpp/advanced-protection-settings-since-excel-xp/)  
- [ワークシートがパスワードで保護されているかどうかを検出する](/cells/ja/nodejs-cpp/detect-if-worksheet-is-password-protected/)  
- [ワークシートの保護](/cells/ja/nodejs-cpp/protecting-worksheets/)  
- [ワークシートの保護を解除する](/cells/ja/nodejs-cpp/unprotect-a-worksheet/)  
- [ワークシートを保護するために使用されたパスワードの検証](/cells/ja/nodejs-cpp/verify-password-used-to-protect-the-worksheet/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
