---
title: 自定义本地化
type: docs
weight: 40
url: /zh/net/aspose-cells-griddesktop/griddesktop-localization/
keywords: GridDesktop,自定义,本地化,翻译,全球化
description: 本文介绍了如何在 GridDesktop 中自定义本地化。
---

{{% alert color="primary" %}} 

如果我们需要为 GridDesktop 中的所有菜单/提示信息等进行本地化，我们可以定义资源文件，并使用 GridDesktop.SetCustomResourceManager 来加载这个资源。

{{% /alert %}} 
## **示例**

首先添加一个新的资源文件：customtest.resx


![custom-resource](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

执行上述代码后，菜单项显示：

![show menu](managing-griddesktops-show-custom.png)

