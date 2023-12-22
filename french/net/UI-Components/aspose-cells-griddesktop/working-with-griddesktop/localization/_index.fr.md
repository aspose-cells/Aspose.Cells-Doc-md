---
title: localisation personnalisée
type: docs
weight: 40
url: /fr/net/griddesktop-localization/
keywords: custom,localization,translation,globalization
---
{{% alert color="primary" %}} 

Si nous devons localiser tous les menus/conseils de messages, etc. dans GridDesktop, nous pouvons définir le fichier de ressources et utiliser GridDesktop.SetCustomResourceManager pour charger cette ressource.

{{% /alert %}} 
##  **exemple**

ajoutez d'abord un nouveau fichier de ressources : customtest.resx


![ressource personnalisée](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

Après avoir exécuté le code ci-dessus, les éléments de menu s'affichent :

![Afficher le menu](managing-griddesktops-show-custom.png)
 