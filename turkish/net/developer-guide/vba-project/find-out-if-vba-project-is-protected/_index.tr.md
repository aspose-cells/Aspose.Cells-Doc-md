---
title: VBA Projesinin Korunup Korunmadığını Bul
type: docs
weight: 20
url: /tr/net/find-out-if-vba-project-is-protected/
---

## **VBA Projesinin C# kullanarak korunup korunmadığını bul**

Aspose.Cells kullanarak, Excel dosyanızın VBA (Görsel Temel Uygulamalar) Projesinin korunup korunmadığını [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) özelliğini kullanarak bulabilirsiniz.

## **Örnek Kod**

Aşağıdaki örnek kod bir çalışma kitabı oluşturur ve ardından VBA projesinin korunup korunmadığını kontrol eder. Daha sonra VBA projesini korur ve tekrar korunup korunmadığını kontrol eder. Bir referans için konsol çıktısına bakınız. Koruma öncesi [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) **false** döndürürken, koruma sonrası **true** döndürür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-FindoutifVBAProjectisProtected.cs" >}}

## **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı referans için görüntülenmiştir.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
