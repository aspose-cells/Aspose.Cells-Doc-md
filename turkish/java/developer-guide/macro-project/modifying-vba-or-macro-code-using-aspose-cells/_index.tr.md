---
title: Aspose.Cells kullanarak VBA veya Makro Kodunu Değiştirme
type: docs
weight: 90
url: /tr/java/modifying-vba-or-macro-code-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells kullanarak VBA veya Makro Kodunu Değiştirebilirsiniz. Aspose.Cells, Excel dosyasındaki VBA projesini okumak ve değiştirmek için aşağıdaki sınıfları eklemiştir.

- VbaProject
- VbaModuleCollection
- VbaModule

Bu makale, Aspose.Cells kullanarak kaynak Excel dosyasındaki VBA veya Makro Kodunu değiştirmeyi gösterecektir.

{{% /alert %}} 
## **Örnek**
Aşağıdaki örnek kod, içinde belirtilen VBA veya Makro kodu bulunan kaynak Excel dosyasını yükler

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

Aspose.Cells örnek kodunun yürütülmesinden sonra, VBA veya Makro kodu bu şekilde değiştirilmiş olacaktır

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

[Kaynak Excel dosyasını](5472596.xlsm) ve [çıkış Excel dosyasını](5472597.xlsm) verilen bağlantılardan indirebilirsiniz.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






{{< app/cells/assistant language="java" >}}
