---
title: anpassad lokalisering
type: docs
weight: 40
url: /sv/net/griddesktop-localization/
keywords: custom,localization,translation,globalization
---
{{% alert color="primary" %}} 

Om vi behöver göra lokalisering för alla menyer/meddelandetips etc. i GridDesktop, kan vi definiera resursfilen och använda GridDesktop.SetCustomResourceManager för att ladda denna resurs.

{{% /alert %}} 
##  **exempel**

lägg först till en ny resursfil: customtest.resx


![anpassad resurs](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

Efter att ha kört ovanstående kod visar menyalternativen:

![visa menyn](managing-griddesktops-show-custom.png)
 