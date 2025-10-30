---  
title: Ta reda på om VBA projektet är skyddat med Golang via C++  
linktitle: Ta reda på om VBA projektet är skyddat  
type: docs  
weight: 20  
url: /sv/go-cpp/find-out-if-vba-project-is-protected/  
description: Kontrollera om VBA projektet i en Excel fil är skyddat med Aspose.Cells med Golang via C++.  
---  

## **Ta reda på om VBA-projektet är skyddat i C++**

Du kan avgöra om VBA (Visual Basic Applications) projektet för din Excel-fil är skyddat eller inte med Aspose.Cells med [**VbaProject.IsProtected**](https://reference.aspose.com/cells/go-cpp/vbaproject/isprotected/)-egenskapen.

## **Exempelkod**

Följande exempel skapar en arbetsbok och kontrollerar om dess VBA-projekt är skyddat eller inte. Sedan skyddar den VBA-projektet och kontrollerar igen. Se dess konsolutdata för referens. Innan skyddet returnerar [**VbaProject.IsProtected**](https://reference.aspose.com/cells/go-cpp/vbaproject/isprotected/) **false**, men efter skyddet returnerar det **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindOutIfVbaProjectIsProtected.go" >}}
## **Konsoloutput**

Detta är konsoloutputen av den ovanstående exempelkoden som referens.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
