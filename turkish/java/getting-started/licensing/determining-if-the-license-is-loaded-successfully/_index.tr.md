---
title: Lisansın Başarıyla Yüklendiğini Belirleme
type: docs
weight: 210
url: /tr/java/determining-if-the-license-is-loaded-successfully/
---

{{% alert color="primary" %}}

Aspose.Cells, lisansın başarılı bir şekilde yüklenip yüklenmediğini belirlemeniz için kullanabileceğiniz [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) özelliğini sağlar. Lisansı ayarlamadan önce bu yöntemi çağırırsanız false dönecek ve lisansı ayarladıktan sonra bu yöntemi çağırırsanız lisansın başarılı bir şekilde yüklendiğini gösteren true dönecektir.

{{% /alert %}}

## **Lisansın başarılı bir şekilde yüklendiğini belirleme**

Aşağıdaki kod, lisansı ayarlamadan önce [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) yöntemine erişir ve false döndürür. Daha sonra lisansı yükler ve tekrar özelliğe erişir, bu sefer true döndürür.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı aşağıdaki gibidir

{{< highlight java >}}

false

true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
