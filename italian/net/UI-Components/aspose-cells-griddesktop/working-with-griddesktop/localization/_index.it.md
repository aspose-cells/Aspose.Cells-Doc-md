---
title: localizzazione personalizzata
type: docs
weight: 40
url: /it/net/griddesktop-localization/
keywords: custom,localization,translation,globalization
---
{{% alert color="primary" %}} 

Se dobbiamo localizzare tutti i menu/suggerimenti sui messaggi ecc. in GridDesktop, possiamo definire il file di risorse e utilizzare GridDesktop.SetCustomResourceManager per caricare questa risorsa.

{{% /alert %}} 
##  **esempio**

aggiungere prima un nuovo file di risorse: customtest.resx


![risorsa-personalizzata](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

Dopo aver eseguito il codice precedente, le voci di menu mostrano:

![mostra il menu](managing-griddesktops-show-custom.png)
 