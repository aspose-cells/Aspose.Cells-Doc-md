---
title: 32 ビットおよび 64 ビットのプラットフォームで Aspose.Cells を使用する
type: docs
weight: 10
url: /ja/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---

{{% alert color="primary" %}} 

Aspose.Cells は純粋な .NET コンポーネントで、XCOPY デプロイメントを使用して展開プロセスを簡素化できます。Aspose.Cells をインストールするには、単純にコンポーネントアセンブリ (Aspose.Cells.dll) をアプリケーションのディレクトリにコピーするだけで、そのアプリケーションはすぐにそれを使用できます。これは .NET コンポーネントの自己記述的な性質によるものです。この種の展開はインストールプロセスにもゼロの影響を与えます。

{{% /alert %}} 
## **デプロイメント**
Aspose.Cellsは32ビット環境と64ビット環境の両方をサポートしています。 Aspose.Cells MSIインストーラーを使用してAspose.Cells for .NETコンポーネントをインストールすると、異なるフォルダに異なるDLLがAspose.Cells ${installation_Path}フォルダに追加されます。特定の.NET Frameworkのバージョンと使用する必要のあるアセンブリを確認するために、テーブルの説明を参照してください。

|**フォルダー**|**説明**|
| :- | :- |
|net2.0|.NET Framework 2.0、3.0、3.5、4.0 および Mono で使用するアセンブリを含みます。これらは通常、32 ビットおよび 64 ビット環境の両方で使用する必要のあるアセンブリです。
|net2.0_AuthenticodeSigned|上記と同様ですが、アセンブリに Authenticode でデジタル署名がされています。署名されたアセンブリは非署名のアセンブリよりも遅く読み込む場合があります。
|net3.5_ClientProfile|.NET Framework 3.5 または 4.0 クライアントプロファイルで使用するアセンブリを含みます。
|net3.5_ClientProfile_AuthenticodeSigned|上記と同様ですが、アセンブリに Authenticode でデジタル署名がされています。署名されたアセンブリは非署名のアセンブリよりも遅く読み込む場合があります。
|net3.5|.NET Framework 3.5 または 4.0 で使用するアセンブリを含みます。
|net3.5_AuthenticodeSigned|上記と同様ですが、アセンブリに Authenticode でデジタル署名がされています。署名されたアセンブリは非署名のアセンブリよりも遅く読み込む場合があります。
|net4.0|.NET Framework 4.0 および 4.5 で使用するアセンブリを含みます。
|netStandard|.Net Standard 2.0を使用するためのアセンブリが含まれています。
|netcoreapp2.1|.Net Core 2.1を使用するためのアセンブリが含まれています。
|Xamarin.iOS|Xamarin.iOSを使用するためのアセンブリが含まれています。
|Xamarin.Android|Xamarin.Androidを使用するためのアセンブリが含まれています。
|net5.0|.net5.0を使用するためのアセンブリが含まれています。
|net6.0|.net6.0を使用するためのアセンブリが含まれています。
|net8.0|net8.0 と共に使用するアセンブリを含む|
|net9.0|net9.0 と共に使用するアセンブリを含む|

{{% alert color="primary" %}} 

VS.NETでは（たとえば2005年、2008年、2010年、2012年など）、Aspose.Cellsへの参照を追加する場合、参照の追加ダイアログはそれぞれnet2.0またはnet3.5フォルダ内のAspose.Cells.dllファイルを参照します。（詳細は[.NETプロジェクトからAspose.Cellsへの参照付与](https://blog.aspose.com/2008/03/17/complete-excel-export-capabilities-using-apis/)を参照してください。）プロジェクトのターゲットフレームワークが.NET Framework 3.5/4 Client Profileである場合は、net_ClientProfileフォルダ内のAspose.Cells.dllコンポーネントファイルを使用してください。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
