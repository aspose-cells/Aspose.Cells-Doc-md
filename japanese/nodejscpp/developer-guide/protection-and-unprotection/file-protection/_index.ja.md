---  
title: Node.js経由のC++を使ったExcelファイルの暗号化と復号化  
linktitle: Excelファイルの暗号化および復号化  
type: docs  
weight: 10  
url: /ja/nodejs-cpp/encrypt-and-decrypt-excel-files/  
description: Node.js経由のC++を使ったExcelファイルの暗号化と復号化方法。Excelファイルのロックと解除。  
---  

{{% alert color="primary" %}}  
Microsoft Excel (97 - 365)を使用して、スプレッドシートを暗号化およびパスワード保護することができます。暗号化には、暗号化サービスプロバイダー（CSP）によって提供されるアルゴリズムが使用されます。暗号化キーの長さを適切に選択することが重要です。一部のCSPは40ビットまたは56ビットを超える長さをサポートしていません。これは弱い暗号化と見なされます。強力な暗号化には、最小128ビットのキー長が必要です。Microsoft Windowsには、強力な暗号化タイプを提供するCSPも含まれています。例えば、「Microsoft Strong Cryptographic Provider」などです。128ビットの暗号化は、銀行がインターネットバンキングシステムとの接続を暗号化する際に使用するものです。  

Aspose.Cellsを使用すると、任意の暗号化タイプでMicrosoft Excelファイルを暗号化およびパスワード保護することができます。  
{{% /alert %}}  

## **Microsoft Excel の使用**  

Microsoft Excel（ここではMicrosoft Excel 2003）でファイルの暗号化設定を行うには：  

1. **ツール**メニューから**オプション**を選択します。ダイアログが表示されます。  
2. **セキュリティ**タブを選択。  
3. パスワードを入力し、**詳細設定**をクリック。  
4. 暗号化タイプを選択し、パスワードを確認。  

## **Aspose.Cells for Node.js via C++を使ったExcelファイルの暗号化**  

次の例は、Aspose.Cells APIを使用してExcelファイルを暗号化し、パスワード保護する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify XOR encryption type.
workbook.setEncryptionOptions(AsposeCells.EncryptionType.XOR, 40);

// Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password protect the file.
workbook.getSettings().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```  

### **変更用パスワードの指定オプション**  

次の例は、Aspose.Cells APIを使用して既存のファイルの**修正パスワード**Microsoft Excelオプションを設定する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```  


## **Aspose.Cells for Node.js via C++を使ったExcelファイルの復号化**  
次のコード例のように、Aspose.Cells APIを使用してパスワード保護されたExcelファイルを容易に開き、復号することができます。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open encrypted file with password.
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("password");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);

// Remove password.
workbook.getSettings().setPassword(null);

// Save the file.
workbook.save(filePath);
```  


## **高度なトピック**  
- [ODSファイルの暗号化および復号化](/cells/ja/nodejs-cpp/encrypt-and-decrypt-ods-files/)  
- [強力な暗号化タイプの設定](/cells/ja/nodejs-cpp/setting-strong-encryption-type/)  
- [ブックを書き込み保護する際に著者を指定する](/cells/ja/nodejs-cpp/specify-author-while-write-protecting-workbook/)  
- [暗号化されたファイルのパスワードの検証](/cells/ja/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
