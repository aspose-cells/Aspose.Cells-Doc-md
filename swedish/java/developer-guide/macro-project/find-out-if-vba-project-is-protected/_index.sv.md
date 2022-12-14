---
title: Ta reda på om VBA-projektet är skyddat
type: docs
weight: 80
url: /sv/java/find-out-if-vba-project-is-protected/
---
## **Möjliga användningsscenarier**
 Du kan se om VBA-projektet (Visual Basic Applications) i din Excel-fil är skyddat eller inte med Aspose.Cells med hjälp av[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected)metod
## **Exempelkod**
 Följande exempelkod skapar en arbetsbok och kontrollerar sedan om dess VBA-projekt är skyddat eller inte. Sedan skyddar den VBA-projektet och kontrollerar igen om dess VBA-projekt är skyddat eller inte. Se dess konsolutgång för en referens. Innan skydd,[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) returnerar**falsk** men efter skydd kommer den tillbaka**Sann**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **Konsolutgång**
Detta är konsolutgången för ovanstående exempelkod som referens.

{{< highlight "java" >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
