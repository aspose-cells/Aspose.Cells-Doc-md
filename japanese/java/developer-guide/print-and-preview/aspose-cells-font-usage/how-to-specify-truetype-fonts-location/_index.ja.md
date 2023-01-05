---
title: TrueType フォントの場所を指定する方法
type: docs
weight: 30
url: /ja/java/how-to-specify-truetype-fonts-location/
---
{{% alert color="primary" %}}

この記事では、次のことについて説明します。

1. [Aspose.Cells API が TrueType フォントを探す場所](/cells/ja/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [Aspose.Cells API の TrueType フォント フォルダーを明示的に指定する方法](/cells/ja/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [Aspose.Cells API で TrueType フォントの場所を 1 つだけ使用するように制限する方法](/cells/ja/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **フォントの操作**

### **Aspose.Cells が Windows の TrueType フォントを検索する場所**

Aspose.Cells は、**Windows\フォント**フォルダ。ほとんどの場合、このデフォルト設定が機能するため、本当に必要な場合にのみ独自のフォント フォルダーを指定してください。

### **Linux で Aspose.Cells が TrueType フォントを検索する場所**

デフォルトでは、Aspose.Cells API は次のすべての場所でフォントを検索しますが、Linux ディストリビューションが異なればフォントは別のフォルダーに保存されます。

1. /usr/share/フォント
1. /usr/ローカル/共有/フォント

{{% alert color="primary" %}}

このデフォルトの動作はほとんどの Linux ディストリビューションで機能しますが、常に機能するとは限りません。 TrueType フォントの場所を明示的に指定する必要がある場合があります。

{{% /alert %}}

### **フォント フォルダーを明示的に指定する方法**

Aspose.Cells 以下で説明するように、API は FontConfigs クラスの多くのファクトリ メソッドを公開して、フォントまたはフォント フォルダーを指定します。

1. setFontFolder メソッドは、String 型の最初のパラメーターをフォント ディレクトリの場所とともに受け入れます。一方、Boolean 型の 2 番目のパラメーターは、Aspose.Cells AP がフォルダーを再帰的に検索してフォント ファイルを検索するように指示します。
1. setFontFolders メソッドは String 型の配列を受け入れるため、このアプローチを使用して多くのフォント ディレクトリを指定できます。 2 番目のパラメーターとして true を指定して、Aspose.Cells AP にフォルダーを再帰的に検索するように指示することもできます。
1. setFontSources メソッドは、個々のフォントの場所のリストを指定するために、FontSourceBase 型の配列を受け入れます。

{{% alert color="primary" %}}

上記の方法のいずれかを使用してフォント フォルダーを指定する場合、アプリケーションの開始時にフォントの場所を設定することをお勧めします。

{{% /alert %}} {{% alert color="primary" %}}

上記の方法のいずれかを使用してフォント フォルダーを設定しても、Aspose.Cells API がシステムのフォント フォルダーなどの既定の場所でフォントを検索しないという保証はありません。

{{% /alert %}}

### **Aspose.Cells が 1 つのフォント フォルダーのみを使用するように制限する方法**

Aspose.Cells for Java 8.1.0 以降、JVM 引数を次のように設定します。**-DAspose.Cells.FontDirExc="あなたのフォントディレクトリ**Aspose.Cells API が指定されたフォントの場所のみを使用するようにします。

以下に示すように、System.setProperty メソッドを使用して、指定された引数を設定します。

{{< highlight "java" >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

次の点に注意してください：

- 上記のステートメントは、アプリケーションの最初にある必要があります。
- 上記のアプローチを使用する場合、上記で説明した FontConfigs メソッドのいずれかを使用してフォント ディレクトリを設定する必要はありません。
- 文字列「FontDirSet」は、必要なフォントを含むフォルダーへの完全なパスである必要があります。

{{% /alert %}}
