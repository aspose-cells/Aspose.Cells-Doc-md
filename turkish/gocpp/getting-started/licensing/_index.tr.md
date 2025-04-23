---
title: Lisanslama
type: docs
weight: 50
url: /tr/go-cpp/licensing/
---

## **Değerlendirme Sürümü Kısıtlamaları**

A free evaluation version of Aspose.Cells for Go via C++ can be downloaded from the downloads section of Aspose's web site at: <//<https://releases.aspose.com/cells/go-cpp/>>.

## **Dosyadan Lisans Yükleme**

{{% alert color="primary" %}}

SetLicense metodunu çağırdığınızda, pasladığınız lisans adının lisans dosyasına ait olması gerekir. Örneğin, lisans dosyasının adını "Aspose.Cells.lic.xml" olarak değiştirirseniz, bu dosya adını License->SetLicense_String(…) metoduna geçirin.

{{% /alert %}}

**Go**

{{< highlight csharp >}}
 lic, _:= NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

{{< /highlight >}}
