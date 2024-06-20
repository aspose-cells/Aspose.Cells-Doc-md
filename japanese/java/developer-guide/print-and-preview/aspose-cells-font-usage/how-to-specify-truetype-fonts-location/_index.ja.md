---
title: TrueType フォントの場所を指定する方法
type: docs
weight: 30
url: /ja/java/how-to-specify-truetype-fonts-location/
---

{{% alert color="primary" %}}

この記事では次のことについて説明します:

1. [Aspose.Cells API が TrueType フォントを探す場所](/cells/ja/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows)。
1. [Aspose.Cells API に明示的に TrueType フォントフォルダーを指定する方法](/cells/ja/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder)。
1. [Aspose.Cells API が単一の TrueType フォント位置のみを使用するように制限する方法](/cells/ja/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder)。

{{% /alert %}}

## **フォントの操作**

### **Windows 上で Aspose.Cells が TrueType フォントを探す場所**

Aspose.Cells はフォントを **Windows\Fonts** フォルダーで検索します。このデフォルト設定はほとんどの場合に機能するため、本当に必要な場合にのみ独自のフォントフォルダーを指定してください。

### **Aspose.Cells が Linux で TrueType フォントを検索する場所**

デフォルトでは、Aspose.Cells API は以下のすべての場所でフォントを検索しますが、異なる Linux ディストリビューションは異なるフォルダーにフォントを保存します。

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

このデフォルトの動作はほとんどの Linux ディストリビューションで機能しますが、常に機能するわけではありません。TrueType フォントの場所を明示的に指定する必要がある場合があります。 

{{% /alert %}}

### **フォントフォルダーを明示的に指定する方法**

Aspose.Cells API は、以下に説明するようにフォントまたはフォントフォルダーを指定するための FontConfigs クラスの多くのファクトリメソッドを公開しています。

1. setFontFolder メソッドは、フォントディレクトリの場所を示す String 型の第1パラメータと、Aspose.Cells API にフォントファイルを再帰的に検索するかどうかを指示するための Boolean 型の第2パラメータを受け入れます。
1. setFontFolders メソッドは、String 型の配列を受け入れるため、この方法を使用して多くのフォントディレクトリを指定することができます。第2パラメータに true を指定することで、Aspose.Cells API にフォルダを再帰的に検索させることもできます。
1. setFontSources メソッドは、個々のフォントの場所を指定するための FontSourceBase 型の配列を受け入れます。

{{% alert color="primary" %}}

上記のいずれかの方法を使用してフォントフォルダーを指定する場合、フォントの場所をアプリケーションの開始時に設定することをお勧めします。そうしないと、見栄えの悪い結果が得られる可能性があります。

{{% /alert %}} {{% alert color="primary" %}}

上記の方法を使用してフォントフォルダーを設定しても、Aspose.Cells API がシステムのフォントフォルダーなど、デフォルトの場所でフォントを検索しないことを保証するものではありません。

{{% /alert %}}

### **Aspose.Cells が単一のフォントフォルダーのみを使用するように制限する方法**

Aspose.Cells for Java 8.1.0 以降、JVM 引数を **-DAspose.Cells.FontDirExc="YourFontDir** と設定することで、Aspose.Cells API が指定されたフォントの場所のみを使用することが保証されます。

次のように System.setProperty メソッドを使用して指定の引数を設定してください。

{{< highlight java >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

以下に注意してください。

- 上記の記述はアプリケーションの開始時に配置する必要があります。
- 上記のアプローチを使用する場合、上記で説明したいずれかの FontConfigs メソッドを使用してフォントディレクトリを設定する必要はありません。
- 文字列 "FontDirSet" は、必要なフォントを含むフォルダーの完全なパスである必要があります。

{{% /alert %}}
