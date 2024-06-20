---
title: локализация по заказу
type: docs
weight: 40
url: /ru/net/aspose-cells-griddesktop/griddesktop-localization/
keywords: GridDesktop,пользовательская,локализация,перевод,глобализация
description: В этой статье представлено, как настраивать локализацию в GridDesktop.
---

{{% alert color="primary" %}} 

Если нам нужно выполнить локализацию для всех меню/подсказок сообщений и т. д. в GridDesktop, мы можем определить файл ресурсов и использовать GridDesktop.SetCustomResourceManager для загрузки этого ресурса.

{{% /alert %}} 
## **пример**

сначала добавьте новый файл ресурсов: customtest.resx


![custom-resource](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

После выполнения приведенного выше кода пункты меню показывают:

![show menu](managing-griddesktops-show-custom.png)

