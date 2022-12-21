---
title: 32 ビットおよび 64 ビットのプラットフォームで Aspose.Cells を使用する
type: docs
weight: 10
url: /ja/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---
{{% alert color="primary" %}} 

Aspose.Cells は純粋な .NET コンポーネントであり、XCOPY 展開を使用して展開プロセスを簡素化できます。 Aspose.Cells をインストールするには、コンポーネント アセンブリ (Aspose.Cells.dll) をアプリケーションのディレクトリにコピーするだけです。アプリケーションはすぐに使用を開始できます。これが可能なのは、.NET コンポーネントの自己記述的な性質によるものです。このタイプの展開は、インストール プロセスにも影響しません。

{{% /alert %}} 
## **展開**
Aspose.Cells は、32 ビット環境と 64 ビット環境の両方をサポートします。 Aspose.Cells MSI インストーラーを使用して Aspose.Cells for .NET コンポーネントをインストールすると、Aspose.Cells ${installation_Path} フォルダー内の異なるフォルダーに異なる DLL が追加されます。 .NET フレームワークの特定のバージョンで使用する必要があるアセンブリが含まれるフォルダーの表の説明を参照してください。

|**フォルダ**|**説明**|
|:- |:- |
|net2.0|.NET Framework 2.0、3.0、3.5、4.0、および Mono で使用するアセンブリが含まれています。これらは、32 ビット環境と 64 ビット環境の両方で通常使用するアセンブリです。|
|net2.0_AuthenticodeSigned|上記と同じですが、アセンブリは Authenticode でデジタル署名されています。署名されたアセンブリは、Authenticode がない場合よりも読み込みが遅くなる場合があります|
|net3.5_ClientProfile|.NET Framework 3.5 または 4.0 Client Profile で使用するアセンブリが含まれています。|
|net3.5_クライアントプロファイル_AuthenticodeSigned|上記と同じですが、アセンブリは Authenticode でデジタル署名されています。署名されたアセンブリは、Authenticode がない場合よりも読み込みが遅くなる場合があります。|
|net3.5|.NET Framework 3.5 または 4.0 で使用するアセンブリが含まれています。|
|net3.5_AuthenticodeSigned|上記と同じですが、アセンブリは Authenticode でデジタル署名されています。署名されたアセンブリは、Authenticode がない場合よりも読み込みが遅くなる場合があります。|
|net4.0|.NET Framework 4.0 および 4.5 で使用するアセンブリが含まれています。|
|netStandard|.Net Standard 2.0 で使用するアセンブリが含まれています|
|netcoreapp2.1|.Net コア 2.1 で使用するアセンブリが含まれています|
|Xamarin.iOS|Xamarin.iOS で使用するアセンブリが含まれています|
|Xamarin.Android|Xamarin.Android で使用するアセンブリが含まれています|
|net5.0|.net5.0 で使用するアセンブリが含まれています。|
|net6.0|.net6.0 で使用するアセンブリが含まれています。|
{{% alert color="primary" %}} 

VS.NET (たとえば、2005、2008、2010、2012 など) プロジェクトでは、Aspose.Cells への参照を追加すると、[参照の追加] ダイアログはそれぞれ net2.0 または net3.5 フォルダー内の Aspose.Cells.dll ファイルを参照します。 (詳細については、.NET プロジェクトからの参照 Aspose.Cells を参照してください。) 環境に応じて、ライブラリへの参照を変更できます。プロジェクトのターゲット フレームワークが .NET Framework 3.5/4 Client Profile の場合は、net_ClientProfile フォルダーにある Aspose.Cells.dll コンポーネント ファイルを使用してください。

{{% /alert %}}
