---  
title: Sätt marginaler för kommentar eller form inom kalkbladet med Golang via C++  
linktitle: Ställ in marginaler för kommentar eller shape i kalkylbladet  
type: docs  
weight: 1500  
url: /sv/go-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Lär dig hur du sätter marginaler för kommentarer eller former inom ett kalkblad med Aspose.Cells med Golang via C++.  
---  

## **Möjliga användningsscenario**  

Aspose.Cells tillåter dig att ställa in marginaler för vilken form eller kommentar som helst med hjälp av [**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/go-cpp/fontsettingcollection/gettextalignment/)-egenskapen. Denna egenskap returnerar objekt av [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment)-klassen som har olika egenskaper, t.ex. [**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/), [**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/), [**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/), [**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/), etc., vilka kan användas för att ställa in topp-, vänster-, botten- och högermarginaler.  

## **Ställ in marginaler för kommentar eller shape i kalkylbladet**  

Se följande exempel. Den laddar [exempel-Excel-fil](61767851.xlsx) som innehåller två former. Koden går in i varje form och ställer in deras topp-, vänster-, botten- och högermarginaler. Se [utdata Excel-fil](61767852.xlsx) som genererats av koden och en skärmbild som visar kodens effekt på utdatafilen.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Exempelkod**  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetMarginsOfCommentOrShapeInsideTheWorksheet.go" >}}  
