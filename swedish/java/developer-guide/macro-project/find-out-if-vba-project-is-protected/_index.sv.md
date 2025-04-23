---
title: Ta reda på om VBA projektet är skyddat
type: docs
weight: 80
url: /sv/java/find-out-if-vba-project-is-protected/
---

## **Möjliga användningsscenario**
Du kan se om VBA (Visual Basic Applications) -projektet i din Excel-fil är skyddat eller inte med Aspose.Cells med hjälp av [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) metoden
## **Exempelkod**
Följande exempelkod skapar en arbetsbok och kontrollerar sedan om dess VBA-projekt är skyddat eller inte. Sedan skyddar den VBA-projektet och kontrollerar igen om dess VBA-projekt är skyddat eller inte. Se dess konsoloutput för en referens. Innan skyddet, returnerar [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) **false** men efter skydd, returnerar den **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **Konsoloutput**
Detta är konsoloutputen av den ovanstående exempelkoden som referens.

{{< highlight java >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
