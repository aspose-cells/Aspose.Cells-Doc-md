---  
title: VBA Projesinin Korunup Körlenmediğini Golang ile C++ kullanarak öğrenin  
linktitle: VBA Projesinin Korunup Korunmadığını Bul  
type: docs  
weight: 20  
url: /tr/go-cpp/find-out-if-vba-project-is-protected/  
description: Aspose.Cells kullanarak Golang ile C++ aracılığıyla Excel dosyasının VBA projesinin korunduğunu kontrol edin.  
---  

## **C++ kullanarak VBA Projesinin Korunduğunu Kontrol Edin**

Excel dosyanızdaki VBA (Visual Basic Applications) Projesinin korunan olup olmadığını Aspose.Cells kullanarak [**VbaProject.IsProtected**](https://reference.aspose.com/cells/go-cpp/vbaproject/isprotected/) özelliği ile öğrenebilirsiniz.

## **Örnek Kod**

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve ardından VBA projesinin korunup korunmadığını kontrol eder. Ardından VBA projesini korur ve tekrar kontrol eder. Lütfen referans olarak konsol çıkışını inceleyin. Koruma öncesinde, [**VbaProject.IsProtected**](https://reference.aspose.com/cells/go-cpp/vbaproject/isprotected/) **false** döner, ancak korumadan sonra **true** döner.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindOutIfVbaProjectIsProtected.go" >}}
## **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı referans için görüntülenmiştir.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
