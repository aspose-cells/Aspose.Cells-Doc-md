---
title: özel yerelleştirme
type: docs
weight: 40
url: /tr/net/aspose-cells-griddesktop/griddesktop-localization/
keywords: GridDesktop,özel,yerelleştirme,çeviri,küreselleştirme
description: Bu makale, GridDesktop ta yerelleştirmeyi nasıl özelleştireceğinizi tanıtır.
---

{{% alert color="primary" %}} 

GridDesktop'ta tüm menüler/mesaj ipuçları vb. için yerelleştirme yapmamız gerekiyorsa, kaynak dosyasını tanımlayabilir ve GridDesktop.SetCustomResourceManager'ı bu kaynağı yüklemek için kullanabiliriz.

{{% /alert %}} 
## **örnek**

Öncelikle yeni bir kaynak dosyası ekleyin: customtest.resx


![custom-resource](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

Yukarıdaki kodu çalıştırdıktan sonra, menü öğeleri gösterilir:

![show menu](managing-griddesktops-show-custom.png)

