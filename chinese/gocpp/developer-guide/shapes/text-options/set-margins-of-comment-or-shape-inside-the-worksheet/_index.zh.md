---  
title: 使用 Golang 通过 C++ 设置工作表内评论或形状的边距  
linktitle: 在工作表内设置评论或形状的边距  
type: docs  
weight: 1500  
url: /zh/go-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: 学习如何使用 Aspose.Cells 通过 C++ 与 Golang 设置工作表内评论或形状的边距。  
---  

## **可能的使用场景**  

Aspose.Cells允许你使用[**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/go-cpp/fontsettingcollection/gettextalignment/)属性设置任何形状或评论的边距。该属性返回一个[**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment)类的对象，该类具有不同的属性例如[**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/)、[**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/)、[**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/)、[**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/)等，用于设置顶部、左侧、底部和右侧边距。  

## **设置工作表内批注或形状的边距**  

请查看以下示例代码。它加载包含两个形状的[示例Excel文件](61767851.xlsx)，代码逐个访问这些形状并设置它们的顶部、左侧、底部和右侧边距。请参阅由代码生成的[输出Excel文件](61767852.xlsx)以及显示代码对输出Excel文件影响的截图。  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **示例代码**  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetMarginsOfCommentOrShapeInsideTheWorksheet.go" >}}  
