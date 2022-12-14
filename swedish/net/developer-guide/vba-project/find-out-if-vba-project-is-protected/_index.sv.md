---
title: Ta reda på om VBA-projektet är skyddat
type: docs
weight: 20
url: /sv/net/find-out-if-vba-project-is-protected/
---
## **Ta reda på om VBA-projektet är skyddat i C#**

 Du kan se om VBA-projektet (Visual Basic Applications) i din Excel-fil är skyddat eller inte med Aspose.Cells med hjälp av[**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected)fast egendom.

## **Exempelkod**

 Följande exempelkod skapar en arbetsbok och kontrollerar sedan om dess VBA-projekt är skyddat eller inte. Sedan skyddar den VBA-projektet och kontrollerar igen om dess VBA-projekt är skyddat eller inte. Se dess konsolutgång för en referens. Innan skydd,[**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) returnerar**falsk** men efter skydd kommer den tillbaka**Sann**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-FindoutifVBAProjectisProtected.cs" >}}

## **Konsolutgång**

Detta är konsolutgången för ovanstående exempelkod som referens.

{{< highlight "java" >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
