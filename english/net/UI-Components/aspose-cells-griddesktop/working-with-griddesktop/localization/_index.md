---
title: custom localization
type: docs
weight: 40
url: /net/griddesktop-localization/
keywords: custom,localization,translation,globalization
---

{{% alert color="primary" %}} 

If we need to do localization for all the menus/message tips etc. in GridDesktop,We can define the resource file ,and use GridDesktop.SetCustomResourceManager to load this resource.

{{% /alert %}} 
## **example**

first add a new resource file: customtest.resx


![custom-resource](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

After executing the above code,   menu items shows:

![show menu](managing-griddesktops-show-custom.png)
 