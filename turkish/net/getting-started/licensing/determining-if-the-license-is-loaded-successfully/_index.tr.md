---
title: Lisansın başarıyla yüklenip yüklenmediğini belirleme
type: docs
weight: 260
url: /tr/net/determining-if-the-license-is-loaded-successfully/
description: NET API'leri için Lisansın Aspose.Cells aracılığıyla başarıyla yüklenip yüklenmediğini nasıl tespit edeceğinizi öğrenin.
keywords: How to Detect if the License is loaded successfully in C#, Determine if the License is loaded successfully using C#, Check if the License is loaded successfully via C#, check the status of license.
---
{{% alert color="primary" %}}

 Aspose.Cells sağlar[**Çalışma Kitabı.Lisanslıdır**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) Lisansın başarıyla yüklenip yüklenmediğini belirlemek için kullanabileceğiniz özellik. Lisansı ayarlamadan önce bu özelliğe erişirseniz,**YANLIŞ** ve lisansı ayarladıktan sonra bu özelliği çağırırsanız geri dönecektir**doğru** Lisansın başarıyla yüklendiğini gösterir.

{{% /alert %}}

##  Lisansın başarıyla yüklenip yüklenmediğini belirlemek için C# kodu

 Aşağıdaki kod erişim sağlar[**Çalışma Kitabı.Lisanslıdır**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)Bir lisans ayarlamadan önce özellik kullanılır ve *false** değeri döndürülür. Daha sonra lisansı yükler ve özelliğe yeniden erişir; bu özellik artık *true** değerini döndürür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

##  **Konsol Çıkışı**

Yukarıdaki örnek kodun konsol (hata ayıklama) çıktısı aşağıdadır

{{< highlight "java" >}}

False

True

{{< /highlight >}}
