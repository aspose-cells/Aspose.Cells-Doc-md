---
title: localización personalizada
type: docs
weight: 40
url: /es/net/griddesktop-localization/
keywords: custom,localization,translation,globalization
---
{{% alert color="primary" %}} 

Si necesitamos localizar todos los menús/sugerencias de mensajes, etc. en GridDesktop, podemos definir el archivo de recursos y usar GridDesktop.SetCustomResourceManager para cargar este recurso.

{{% /alert %}} 
##  **ejemplo**

Primero agregue un nuevo archivo de recursos: customtest.resx


![recurso personalizado](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

Después de ejecutar el código anterior, los elementos del menú muestran:

![Muestrame el menu](managing-griddesktops-show-custom.png)
 