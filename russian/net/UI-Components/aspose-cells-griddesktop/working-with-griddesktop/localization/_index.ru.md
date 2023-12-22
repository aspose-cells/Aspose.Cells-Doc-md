---
title: пользовательская локализация
type: docs
weight: 40
url: /ru/net/griddesktop-localization/
keywords: custom,localization,translation,globalization
---
{{% alert color="primary" %}} 

Если нам нужно выполнить локализацию всех меню/подсказок к сообщениям и т. д. в GridDesktop, мы можем определить файл ресурсов и использовать GridDesktop.SetCustomResourceManager для загрузки этого ресурса.

{{% /alert %}} 
##  **пример**

сначала добавьте новый файл ресурсов: customtest.resx


![пользовательский ресурс](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

После выполнения приведенного выше кода пункты меню отобразят:

![показать меню](managing-griddesktops-show-custom.png)
 