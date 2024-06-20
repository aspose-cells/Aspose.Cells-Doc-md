---
title: localización personalizada
type: docs
weight: 40
url: /es/net/aspose-cells-griddesktop/griddesktop-localization/
keywords: GridDesktop, personalizado, localización, traducción, globalización
description: Este artículo presenta cómo personalizar la localización en GridDesktop.
---

{{% alert color="primary" %}} 

Si necesitamos realizar la localización de todos los menús/consejos de mensajes, etc. en GridDesktop, podemos definir el archivo de recursos y usar GridDesktop.SetCustomResourceManager para cargar este recurso.

{{% /alert %}} 
## **ejemplo**

primero agregue un nuevo archivo de recursos: customtest.resx


![custom-resource](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

Después de ejecutar el código anterior, los elementos del menú muestran:

![show menu](managing-griddesktops-show-custom.png)

