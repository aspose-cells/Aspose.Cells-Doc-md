---
title: GridWebのデフォルトのアイコンの代わりに独自のアイコンを使用する
type: docs
weight: 10
url: /ja/net/aspose-cells-gridweb/use-your-own-icons-instead-of-the-default-icons/
keywords: GridWeb、icon、icons
description: この記事では、GridWebでアイコンを使用する方法について説明しています。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWebコントロールのデフォルトのアイコンではなく、独自のアイコン（画像）を使用したい場合があります。この記事では、その方法について説明します。

{{% /alert %}} 

デフォルトのアイコンはURLパス"/acw_client/"にあります。ファイルパスはデフォルトで"C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client"になります。そのフォルダには、submit.gif、save.gifなどのファイルが含まれます。これらの画像を独自の画像で置き換えたい場合、Webアプリケーションのweb.configファイルにconfigセクションを追加します。

**XML**

{{< highlight csharp >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

この構成は、ライセンスされたコントロールのみが有効になります。
**XML**

{{< highlight csharp >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

"Aspose.Cells for Python via Javaを使用してExcelに背景画像を挿入する方法"

{{% /alert %}}
