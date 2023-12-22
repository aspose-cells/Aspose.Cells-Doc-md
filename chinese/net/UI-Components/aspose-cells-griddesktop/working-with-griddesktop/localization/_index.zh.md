---
title: 定制本地化
type: docs
weight: 40
url: /zh/net/griddesktop-localization/
keywords: custom,localization,translation,globalization
---
{{% alert color="primary" %}} 

如果我们需要对GridDesktop中的所有菜单/消息提示等进行本地化，我们可以定义资源文件，并使用GridDesktop.SetCustomResourceManager来加载该资源。

{{% /alert %}} 
##  **例子**

首先添加一个新的资源文件：customtest.resx


![自定义资源](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

执行上述代码后，菜单项显示：

![显示菜单](managing-griddesktops-show-custom.png)
 