---
title: Ta reda på om VBA projektet är skyddat
type: docs
weight: 20
url: /sv/python-net/find-out-if-vba-project-is-protected/
---

## **Ta reda på om VBA-projekt är skyddat i Python**

Du kan ta reda på om VBA (Visual Basic for Applications)-projektet i din Excel-fil är skyddat eller ej med Aspose.Cells för Python via .NET med hjälp av [**VbaProject.is_protected**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_protected)-egenskapen.

## **Exempelkod**

Följande exempelkod skapar en arbetsbok och kontrollerar sedan om dess VBA-projekt är skyddat eller inte. Sedan skyddar den VBA-projektet och kontrollerar igen om dess VBA-projekt är skyddat eller inte. Vänligen se dess konsoloutput som referens. Innan skyddet, [**VbaProject.is_protected**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_protected) returnerar **false** men efter skyddet returnerar den **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FindoutifVBAProjectisProtected.py" >}}

## **Konsoloutput**

Detta är konsoloutputen av den ovanstående exempelkoden som referens.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
