---
title: localizzazione personalizzata
type: docs
weight: 40
url: /it/net/aspose-cells-griddesktop/griddesktop-localization/
keywords: GridDesktop, personalizzato, localizzazione, traduzione, globalizzazione
description: Questo articolo illustra come personalizzare la localizzazione in GridDesktop.
---

{{% alert color="primary" %}} 

Se abbiamo bisogno di localizzare tutti i menu/suggerimenti dei messaggi etc. in GridDesktop, possiamo definire il file di risorse e utilizzare GridDesktop.SetCustomResourceManager per caricare questa risorsa.

{{% /alert %}} 
## **esempio**

aggiungi prima un nuovo file di risorse: customtest.resx


![custom-resource](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

Dopo aver eseguito il codice precedente, gli elementi di menu mostrano:

![show menu](managing-griddesktops-show-custom.png)

