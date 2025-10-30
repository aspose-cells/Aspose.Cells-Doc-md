---
title: VBAプロジェクトが保護されているかどうかをNode.js経由でC++を使用して確認
linktitle: VBAプロジェクトが保護されているかどうかを調べる
type: docs
weight: 20
url: /ja/nodejs-cpp/find-out-if-vba-project-is-protected/
---

## **Node.jsでVBAプロジェクトが保護されているかどうかを調べる**

Aspose.Cellsを使用して[**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--)プロパティでExcelファイルのVBA（Visual Basic Applications）プロジェクトが保護されているかどうかを確認できます。

## **サンプルコード**

次のサンプルコードは、ブックを作成し、そのVBAプロジェクトが保護されているかどうかを確認します。そしてVBAプロジェクトを保護し、再び保護されているかどうかを確認します。コンソール出力も参照してください。保護前は[**VbaProject.isProtected()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isProtected--)は**false**を返し、保護後は**true**を返します。

```javascript
const AsposeCells = require("aspose.cells.node");

// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access the VBA project of the workbook.
const vbaProj = wb.getVbaProject();

// Find out if VBA Project is Protected using isProtected method.
console.log("IsProtected - Before Protecting VBA Project: " + vbaProj.isProtected());

// Protect the VBA project.
vbaProj.protect(true, "11");

// Find out if VBA Project is Protected using isProtected method.
console.log("IsProtected - After Protecting VBA Project: " + vbaProj.isProtected());
```

## **コンソール出力**

上記サンプルコードのコンソール出力の参考情報です。

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
