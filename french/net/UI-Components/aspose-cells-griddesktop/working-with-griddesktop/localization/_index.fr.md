---
title: localisation personnalisée
type: docs
weight: 40
url: /fr/net/aspose-cells-griddesktop/griddesktop-localization/
keywords: GridDesktop, personnalisé, localisation, traduction, mondialisation
description: Cet article présente comment personnaliser la localisation dans GridDesktop.
---

{{% alert color="primary" %}} 

Si nous devons effectuer la localisation pour tous les menus/messages etc. dans GridDesktop, nous pouvons définir le fichier de ressources et utiliser GridDesktop.SetCustomResourceManager pour charger ce fichier de ressources.

{{% /alert %}} 
## **exemple**

d'abord, ajoutez un nouveau fichier de ressources : customtest.resx


![custom-resource](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

Après l'exécution du code ci-dessus, les éléments de menu s'affichent :

![show menu](managing-griddesktops-show-custom.png)

