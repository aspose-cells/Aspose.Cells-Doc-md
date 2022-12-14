---
title: Aspose.Cells kullanarak VBA veya Makro Kodunu değiştirme
type: docs
weight: 90
url: /tr/java/modifying-vba-or-macro-code-using-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells'i kullanarak VBA veya Makro Kodunu değiştirebilirsiniz. Aspose.Cells, VBA projesini Excel dosyasında okumak ve değiştirmek için aşağıdaki sınıfları ekledi.

- Vba Projesi
- VbaModül Koleksiyonu
- Vba Modülü

Bu makale, Aspose.Cells kullanarak kaynak Excel dosyası içindeki VBA veya Makro Kodunu nasıl değiştireceğinizi gösterecektir.

{{% /alert %}} 
## **Örnek**
Aşağıdaki örnek kod, içinde aşağıdaki VBA veya Makro kodu bulunan kaynak Excel dosyasını yükler.

{{< highlight "java" >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

Aspose.Cells örnek kodunun yürütülmesinden sonra, VBA veya Makro kodu bu şekilde değiştirilecektir.

{{< highlight "java" >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

 indirebilirsiniz[kaynak Excel dosyası](5472596.xlsm) ve[çıktı excel dosyası](5472597.xlsm) verilen linklerden







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






