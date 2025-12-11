---
title: custom localization
type: docs
weight: 40
url: /net/aspose-cells-griddesktop/griddesktop-localization/
keywords: GridDesktop,custom,localization,translation,globalization
description: This article introduces how to customize localization in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

If we need to do localization for all the menus, message tips, etc. in GridDesktop, we can define the resource file, and use `GridDesktop.SetCustomResourceManager` to load this resource.

{{% /alert %}} 

## Example

First, add a new resource file: `customtest.resx`

![custom-resource](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
// Suppose your application has the namespace: myapp
ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
gridDesktop1.SetCustomResourceManager(rm);
```

After executing the above code, the menu items show:

![show menu](managing-griddesktops-show-custom.png)
