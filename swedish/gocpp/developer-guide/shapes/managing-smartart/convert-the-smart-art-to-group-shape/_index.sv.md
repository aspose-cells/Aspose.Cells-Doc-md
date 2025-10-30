---
title: Konvertera Smart Art till gruppform med Golang via C++
linktitle: Konvertera Smart Art till gruppform
type: docs
weight: 200
url: /sv/go-cpp/convert-the-smart-art-to-group-shape/
description: Lär dig hur man konverterar Smart Art Shape till Gruppform med Aspose.Cells for C++ och får tillgång till enskilda delar av gruppformen.
---

## **Möjliga användningsscenario**

Du kan konvertera Smart Art Shape till gruppform med hjälp av [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/go-cpp/shape/getresultofsmartart/)-metoden. Det gör att du kan hantera Smart Art Shape som en gruppform. Som följd kommer du att ha tillgång till de enskilda delarna eller formarna i gruppformen.

## **Konvertera SmartArt till gruppform**

Följande exempel kod laddar [exempel-Excelfil](55541793.xlsx) som innehåller en smart art form som visas i denna skärmdump. Den konverterar sedan smart art formen till gruppform och skriver ut Shape::IsGroup-egenskapen. Se konsolutmatningen av koden nedan.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertTheSmartArtToGroupShape.go" >}}
## **Konsoloutput**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
