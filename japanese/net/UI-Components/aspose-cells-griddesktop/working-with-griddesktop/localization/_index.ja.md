---
title: カスタムローカリゼーション
type: docs
weight: 40
url: /ja/net/aspose-cells-griddesktop/griddesktop-localization/
keywords: GridDesktop、custom、ローカリゼーション、翻訳、グローバリゼーション
description: この記事では、GridDesktopでのローカリゼーションのカスタマイズ方法について紹介しています。
---

{{% alert color="primary" %}} 

GridDesktopのメニューやメッセージのローカリゼーションを行う必要がある場合は、リソースファイルを定義し、GridDesktop.SetCustomResourceManagerを使用してこのリソースを読み込むことができます。

{{% /alert %}} 
## **例**

最初に新しいリソースファイル 'customtest.resx' を追加します


![custom-resource](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

上記のコードを実行した後、メニューアイテムが表示されます：

![show menu](managing-griddesktops-show-custom.png)

