---  
title: 行尾和文本换行
linktitle: 行尾和文本换行  
description: 如何在Node.js中通过C++使用Aspose.Cells库实现文本换行和自动换行。使用Aspose.Cells库，可以轻松在单元格中插入文本并设置换行方式，例如手动换行、自动换行等。本文详细介绍如何实现这些功能，并提供示例代码供参考。  
keywords: Aspose.Cells，换行符，文本换行，文本布局，Node.js via C++  
type: docs  
weight: 60  
url: /zh/nodejs-cpp/line-breaks-and-text-wrapping/  
---  

{{% alert color="primary" %}}  
为了确保单元格中的文本可以被读取，可以应用明确的行尾和文本换行。文本换行将单元格中的一行变成了多行，而明确的行尾则将文本换行放在您想要的确切位置。  
{{% /alert %}}  

## **将单元格中的文本自动换行**  
要在单元格中换行，使用 [**Aspose.Cells.Style.setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-) 方法。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapTextInCell.js" >}}


## **使用显式换行符**  
你可以在 JavaScript 中使用 '\n' 在单元格中插入显式换行符。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-UseExplicitLineBreaks.js" >}}



{{< app/cells/assistant language="nodejs-cpp" >}}
