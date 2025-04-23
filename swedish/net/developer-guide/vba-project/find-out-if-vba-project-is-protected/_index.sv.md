---
title: Ta reda på om VBA projektet är skyddat
type: docs
weight: 20
url: /sv/net/find-out-if-vba-project-is-protected/
---

## **Ta reda på om VBA-projektet är skyddat i C#**

Du kan kontrollera om VBA (Visual Basic Applications)-projektet i din Excel-fil är skyddat eller inte med Aspose.Cells genom att använda [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) egenskap.

## **Exempelkod**

Följande exempelkod skapar en arbetsbok och kontrollerar sedan om dess VBA-projekt är skyddat eller inte. Sedan skyddar den VBA-projektet och kontrollerar igen om dess VBA-projekt är skyddat eller inte. Vänligen se dess konsoloutput som referens. Innan skyddet, [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) returnerar **false** men efter skyddet returnerar den **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-FindoutifVBAProjectisProtected.cs" >}}

## **Konsoloutput**

Detta är konsoloutputen av den ovanstående exempelkoden som referens.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
