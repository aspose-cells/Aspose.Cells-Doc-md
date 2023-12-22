---
title: benutzerdefinierte Lokalisierung
type: docs
weight: 40
url: /de/net/griddesktop-localization/
keywords: custom,localization,translation,globalization
---
{{% alert color="primary" %}} 

Wenn wir alle Menüs/Nachrichtentipps usw. in GridDesktop lokalisieren müssen, können wir die Ressourcendatei definieren und GridDesktop.SetCustomResourceManager verwenden, um diese Ressource zu laden.

{{% /alert %}} 
##  **Beispiel**

Fügen Sie zunächst eine neue Ressourcendatei hinzu: customtest.resx


![benutzerdefinierte Ressource](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

Nach der Ausführung des obigen Codes werden folgende Menüpunkte angezeigt:

![zeige das Menü](managing-griddesktops-show-custom.png)
 