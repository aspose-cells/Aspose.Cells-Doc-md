---
title: カスタムローカリゼーション
type: docs
weight: 40
url: /ja/net/griddesktop-localization/
keywords: custom,localization,translation,globalization
---
{{% alert color="primary" %}} 

GridDesktop のすべてのメニュー/メッセージ ヒントなどのローカライズを行う必要がある場合は、リソース ファイルを定義し、GridDesktop.SetCustomResourceManager を使用してこのリソースをロードします。

{{% /alert %}} 
##  **例**

まず新しいリソース ファイルcustomtest.resx を追加します。


![カスタムリソース](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

上記のコードを実行すると、メニュー項目に次が表示されます。

![メニューを表示](managing-griddesktops-show-custom.png)
 