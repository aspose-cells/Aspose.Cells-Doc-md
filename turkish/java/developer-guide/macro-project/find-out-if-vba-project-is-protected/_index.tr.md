---
title: VBA Projesinin Korunup Korunmadığını Bul
type: docs
weight: 80
url: /tr/java/find-out-if-vba-project-is-protected/
---

## **Olası Kullanım Senaryoları**
Excel dosyanızın VBA (Görsel Temel Uygulamalar) Projesinin Aspose.Cells kullanarak korunup korunmadığını [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) yöntemi ile kontrol edebilirsiniz
## **Örnek Kod**
Aşağıdaki örnek kod, bir çalışma kitabı oluşturur ve ardından VBA projesinin korunup korunmadığını kontrol eder. Ardından VBA projesini korur ve tekrar VBA projesinin korunup korunmadığını kontrol eder. Bir referans için konsol çıktısına bakınız. Koruma öncesi, [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) **false** döndürür ancak koruma sonrası **true** döndürür.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun konsol çıktısı referans için görüntülenmiştir.

{{< highlight java >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
