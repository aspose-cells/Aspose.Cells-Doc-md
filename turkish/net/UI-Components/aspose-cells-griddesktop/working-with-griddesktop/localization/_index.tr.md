---
title: özel yerelleştirme
type: docs
weight: 40
url: /tr/net/griddesktop-localization/
keywords: custom,localization,translation,globalization
---
{{% alert color="primary" %}} 

GridDesktop'taki tüm menüler/mesaj ipuçları vb. için yerelleştirme yapmamız gerekiyorsa, kaynak dosyasını tanımlayabiliriz ve bu kaynağı yüklemek için GridDesktop.SetCustomResourceManager'ı kullanabiliriz.

{{% /alert %}} 
##  **örnek**

önce yeni bir kaynak dosyası ekleyin:customtest.resx


![özel kaynak](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

Yukarıdaki kodu çalıştırdıktan sonra menü öğeleri şunu gösterir:

![menüyü göster](managing-griddesktops-show-custom.png)
 