---  
title: Node.js と C++ を使用したコメントのフォントカラーの変更方法  
linktitle: コメントのフォントの色を変更する方法  
type: docs  
weight: 180  
url: /ja/nodejs-cpp/how-to-change-the-comment-font-color/  
---  

{{% alert color="primary" %}}  
Microsoft Excel では、セルにコメントを追加して追加情報やデータのハイライトを行うことができます。開発者は、コメントの整列設定、テキスト方向、フォントカラーなどをカスタマイズする必要があります。Aspose.Cells for Node.js via C++ はこれを行うAPIを提供します。  
{{% /alert %}}  

Aspose.Cells for Node.js via C++はコメントのフォントカラーを設定する [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) プロパティを提供します。以下のサンプルコードは、[**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) プロパティを使用してコメントのフォントカラーを設定する例です。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add some text in cell A1
worksheet.getCells().get("A1").putValue("Here");

// Add a comment to A1 cell
const commentIndex = worksheet.getComments().add("A1");
const comment = worksheet.getComments().get(commentIndex);

// Set its vertical alignment setting            
comment.getCommentShape().setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Set the Comment note
comment.setNote("This is my Comment Text. This is Test.");

const shape = worksheet.getComments().get("A1").getCommentShape();

shape.getFill().getSolidFill().setColor(AsposeCells.Color.Black);
const font = shape.getFont();
font.setColor(AsposeCells.Color.White);
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setFontColor(true);
shape.getTextBody().format(0, shape.getText().length, font, styleFlag);

// Save the Excel file
workbook.save(path.join(outputDir, "outputChangeCommentFontColor.xlsx"));
```  

上記のコードによって生成された[出力ファイル](102662195.xlsx)を参照してください。  
