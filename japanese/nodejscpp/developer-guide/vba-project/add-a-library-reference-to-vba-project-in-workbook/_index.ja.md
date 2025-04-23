---  
title: Node.js 経由で C++を使用してワークブックのVBAプロジェクトにライブラリ参照を追加する方法  
linktitle: ワークブックのVBAプロジェクトにライブラリの参照を追加  
type: docs  
weight: 80  
url: /ja/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/  
---  

{{% alert color="primary" %}}  

時折、コードを通じてVBAプロジェクトにライブラリ参照を追加または登録する必要があります。Aspose.Cellsの[**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-)メソッドを使用して行うことができます。  

{{% /alert %}}  

## **Microsoft ExcelのVBAプロジェクトにライブラリ参照を追加する**  

Microsoft Excelでは、**ツール > 参照設定...**をクリックしてVBAプロジェクトにライブラリ参照を追加できます。  

## **Aspose.Cells for Node.js via C++を使用してワークブックのVBAプロジェクトにライブラリ参照を追加**  

以下のサンプルコードは、[**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-)メソッドを使用してワークブックのVBAプロジェクトに2つのライブラリ参照を追加または登録します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputPath = path.join(dataDir, "Output_out.xlsm");

const workbook = new AsposeCells.Workbook();

const vbaProj = workbook.getVbaProject();
vbaProj.getReferences().addRegisteredReference("stdole", "*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\\Windows\\system32\\stdole2.tlb#OLE Automation");
vbaProj.getReferences().addRegisteredReference("Office", "*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.0#0#C:\\Program Files\\Common Files\\Microsoft Shared\\OFFICE14\\MSO.DLL#Microsoft Office 14.0 Object Library");

workbook.save(outputPath);
```  

