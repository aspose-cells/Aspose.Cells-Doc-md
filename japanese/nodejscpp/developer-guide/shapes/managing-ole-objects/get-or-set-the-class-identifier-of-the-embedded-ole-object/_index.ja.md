---  
title: Node.js経由でC++を使用して埋め込みOLEオブジェクトのクラス識別子を取得または設定する  
linktitle: 埋め込みOLEオブジェクトのクラス識別子を取得または設定する  
type: docs  
weight: 200  
url: /ja/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/  
description: Aspose.CellsをC++経由で使用して、Node.js内で埋め込みOLEオブジェクトのクラス識別子を取得または設定する方法を学びます。  
---  

## **可能な使用シナリオ**  
Aspose.Cellsは、[OleObject.getClassIdentifier()](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getClassIdentifier--)」プロパティを提供しており、これを使用して埋め込みOLEオブジェクトのクラス識別子を取得または設定できます。OLEオブジェクトのクラス識別子は、実際にはGUID（グローバル一意識別子）です。GUIDは常に16バイト長で、クラス識別子も16バイト長です。これらはWindowsレジストリ内にあり、クライアントアプリケーション内の埋め込みリソースを開く方法に関する情報をホストアプリに提供します。

## **埋め込まれたOLEオブジェクトのクラス識別子を取得または設定する**  
次のスクリーンショットは、PowerPointの埋め込みOLEオブジェクトを含む[サンプルExcelファイル](5115190.xls)から読み取ったOLEオブジェクトのクラス識別子（GUID）を示しています。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **サンプルコード**  
次のサンプルコードとそのコンソール出力を参照してください。これはOLEオブジェクトのクラス識別子（GUID）を表示します。出力されたGUIDは、スクリーンショットに表示されているものと完全に一致します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your sample workbook which contains embedded PowerPoint ole object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xls"));

// Access its first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first ole object inside the worksheet
const oleObject = worksheet.getOleObjects().get(0);

// Convert 16-bytes array into GUID
const guid = new Uint8Array(oleObject.getClassIdentifier()).reduce((acc, byte) => acc + String.fromCharCode(byte), '');

// Print the GUID
console.log(guid.toUpperCase());
```  
### **コンソール出力**  
上記のサンプルコードのコンソール出力は、[サンプルExcelファイル](5115190.xls)で実行したときのものです。

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
