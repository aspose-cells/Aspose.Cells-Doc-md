---
title: Radbrytningar och textomslag med Golang via C++
description: Hur man implementerar textomslag och ordwrap i C++ med Aspose.Cells biblioteket. Genom att använda Aspose.Cells kan du enkelt infoga text i celler och ställa in metod för textomslag, såsom manuell ordwrap, ordwrap osv. Detta dokument beskriver hur du implementerar dessa funktioner och ger exempel på kod för din referens.
keywords: Aspose.Cells, radbrytningar, textomslag, textlayout
type: docs
weight: 60
url: /sv/go-cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

För att säkerställa att texten i en cell kan läsas, kan explicita radbrytningar och textomslag appliceras. Textomslag gör att en rad blir flera i en cell, medan explicita radbrytningar sätts in precis där du vill ha dem.

{{% /alert %}}

## **För att omsluta text i en cell**

För att omsluta text i en cell, använd egenskapen [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping.go" >}}
## **För att använda explicita radbrytningar**

Du kan använda '\n' i C++ för att infoga ett explicit radbrytning i en cell.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping-1.go" >}}
