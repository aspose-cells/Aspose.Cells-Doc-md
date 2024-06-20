---
title: anpassad lokalisering
type: docs
weight: 40
url: /sv/net/aspose-cells-griddesktop/griddesktop-localization/
keywords: GridDesktop,anpassad,lokalisering,översättning,globalisering
description: Den här artikeln introducerar hur man anpassar lokaliseringen i GridDesktop.
---

{{% alert color="primary" %}} 

Om vi behöver göra lokalisering för alla menyer/meddelandetips osv. i GridDesktop kan vi definiera en resursfil och använda GridDesktop.SetCustomResourceManager för att ladda denna resurs.

{{% /alert %}} 
## **exempel**

börja med att lägga till en ny resursfil: customtest.resx


![custom-resource](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

Efter att ovanstående kod har exekverats, kommer menyobjekten att visas:

![show menu](managing-griddesktops-show-custom.png)

