---  
title: Line Breaks and Text Wrapping
linktitle: Line Breaks and Text Wrapping  
description: How to implement text wrapping and word wrap using the Aspose.Cells library in Node.js via C++. By using the Aspose.Cells library, you can easily insert text in cells and set the text wrapping method, such as manual word wrap, word wrap, etc. This document details how to implement these features and provides sample code for your reference.  
keywords: Aspose.Cells, line breaks, text wraps, text layout Node.js via C++  
type: docs  
weight: 60  
url: /nodejs-cpp/line-breaks-and-text-wrapping/  
---  

{{% alert color="primary" %}}  
To ensure that text in a cell can be read, explicit line breaks and text wrapping can be applied. Text wrapping turns one line into several in a cell, which explicit line breaks put in breaks exactly where you want them.  
{{% /alert %}}  

## **To Wrap Text in a Cell**  
To wrap text in a cell, use the [**Aspose.Cells.Style.setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-) method.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapTextInCell.js" >}}


## **To Use Explicit Line Breaks**  
You can use ‘\n’ in JavaScript to insert explicit line breaks in a cell.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-UseExplicitLineBreaks.js" >}}


  
{{< app/cells/assistant language="nodejs-cpp" >}}