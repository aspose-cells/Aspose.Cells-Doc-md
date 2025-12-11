---  
title: Use Format Painter  
type: docs  
weight: 80  
url: /net/aspose-cells-griddesktop/use-format-painter/  
keywords: GridDesktop,format painter  
description: This article introduces the format painter in GridDesktop.  
ai_search_scope: cells_net  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

The **Format Painter** is a feature of MS Excel that has been adapted in Aspose.Cells.GridDesktop. It's a very useful feature. For users who have not yet used this feature, the Format Painter allows them to apply the formatting settings of a focused cell to another cell. The implementation of this feature is very simple. In this topic, we will cover that as well.  

{{% /alert %}}  

## **Using Format Painter**  

The **Format Painter** feature requires users to select a cell whose formatting settings they want to apply to other cells and then call the **StartFormatPainter** method of **GridDesktop**. There are two modes of the Format Painter as follows:

- **Using Format Painter Once**  
- **Using Format Painter Always**  

### **Using Format Painter Once**  

If developers want to use the Format Painter feature just once to apply the formatting settings of a focused cell to a single cell, they can call the **StartFormatPainter** method and pass a **false** value. This **false** value prevents the Format Painter from remaining active.  

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}  

### **Using Format Painter Always**  

Using the Format Painter always is useful when we need to apply the formatting settings to more than one cell. Developers can achieve this by simply calling the **StartFormatPainter** method and passing a **true** value.  

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}  

This mode of the Format Painter remains active indefinitely until it is stopped. To stop the Format Painter, simply call the **EndFormatPainter** method of **GridDesktop**.  

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
