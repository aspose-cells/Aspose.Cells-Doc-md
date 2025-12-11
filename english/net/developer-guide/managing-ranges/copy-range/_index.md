---  
title: Copy Ranges of Excel  
linktitle: Copy Ranges  
type: docs  
weight: 105  
url: /net/copy-ranges-of-Excel/  
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Introduction**  

In Excel, you can select a range, copy the range, then paste it with specific options to the same worksheet, other worksheets, or other files.  

## **Copy Ranges Using Aspose.Cells**  

Aspose.Cells provides several overloaded [Range.Copy](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) methods to copy a range. It also offers [Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) to copy only the style of a range and [Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) to copy only the values of a range.  

## **Copy Range**  

Create two ranges—the source range and the target range—and then copy the source range to the target range using the `Range.Copy` method.  

See the following code:  

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}  

## **Paste Range With Options**  

Aspose.Cells supports pasting a range with specific types.  

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}  

## **Only Copy Data of the Range**  

You can also copy only the data using the `Range.CopyData` method, as shown in the following code:  

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}  

## **Advanced topics**  

- [Copy Row Heights of Source Range to Destination Range](/cells/net/copy-row-heights-of-source-range-to-destination-range/)  

{{< app/cells/assistant language="csharp" >}}
