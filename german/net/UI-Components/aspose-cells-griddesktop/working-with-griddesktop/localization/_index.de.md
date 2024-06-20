---
title: Benutzerdefinierte Lokalisierung
type: docs
weight: 40
url: /de/net/aspose-cells-griddesktop/griddesktop-localization/
keywords: GridDesktop, benutzerdefiniert, Lokalisierung, Übersetzung, Globalisierung
description: Dieser Artikel erläutert, wie Sie die Lokalisierung in GridDesktop anpassen können.
---

{{% alert color="primary" %}} 

Wenn wir die Lokalisierung für alle Menüs/Nachrichtentipps usw. in GridDesktop anpassen müssen, können wir die Ressourcendatei definieren und GridDesktop.SetCustomResourceManager verwenden, um diese Ressource zu laden.

{{% /alert %}} 
## **Beispiel**

fügen Sie zunächst eine neue Ressourcendatei hinzu: customtest.resx


![custom-resource](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

Nach Ausführung des obigen Codes werden die Menüelemente angezeigt:

![show menu](managing-griddesktops-show-custom.png)

