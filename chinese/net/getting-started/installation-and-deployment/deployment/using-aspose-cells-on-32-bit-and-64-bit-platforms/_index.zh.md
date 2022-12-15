---
title: 在 32 位和 64 位平台上使用 Aspose.Cells
type: docs
weight: 10
url: /zh/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---
{{% alert color="primary" %}} 

Aspose.Cells 是一个纯 .NET 组件，可以通过使用 XCOPY 部署来简化您的部署过程。要安装 Aspose.Cells，您只需将组件程序集 (Aspose.Cells.dll) 复制到您的应用程序的目录中：应用程序可以立即开始使用它。这是可能的，因为 .NET 组件的自描述性质。这种类型的部署对安装过程也有零影响。

{{% /alert %}} 
## **部署**
Aspose.Cells 同时支持 32 位和 64 位环境。当您使用 Aspose.Cells MSI 安装程序安装 Aspose.Cells for .NET 组件时，不同的 DLL 会添加到 Aspose.Cells ${installation_Path} 文件夹中的不同文件夹中。请参阅表中的说明，哪个文件夹包含您需要与特定版本的 .NET Framework 一起使用的程序集。

|**文件夹**|**描述**|
|:- |:- |
|net2.0|包含用于 .NET Framework 2.0、3.0、3.5、4.0 和 Mono 的程序集。这些程序集通常应用于 32 位和 64 位环境。|
|net2.0_AuthenticodeSigned|同上，但程序集使用 Authenticode 进行了数字签名。签名程序集的加载速度可能比没有 Authenticode 时慢|
|net3.5_ClientProfile|包含与 .NET Framework 3.5 或 4.0 客户端配置文件一起使用的程序集。|
|net3.5_客户资料_验证码签名|同上，但程序集使用 Authenticode 进行了数字签名。签名程序集的加载速度可能比没有 Authenticode 时慢。|
|net3.5|包含用于 .NET Framework 3.5 或 4.0 的程序集。|
|net3.5_AuthenticodeSigned|同上，但程序集使用 Authenticode 进行了数字签名。签名程序集的加载速度可能比没有 Authenticode 时慢。|
|net4.0|包含用于 .NET Framework 4.0 和 4.5 的程序集。|
|网络标准|包含与 .Net Standard 2.0 一起使用的程序集|
|netcoreapp2.1|包含与 .Net core 2.1 一起使用的程序集|
|Xamarin.iOS|包含与 Xamarin.iOS 一起使用的程序集|
|Xamarin.Android|包含与 Xamarin.Android 一起使用的程序集|
|net5.0|包含与 .net5.0 一起使用的程序集。|
|net6.0|包含与 .net6.0 一起使用的程序集。|
{{% alert color="primary" %}} 

在 VS.NET（例如 2005、2008、2010、2012 等）项目中，添加对 Aspose.Cells 的引用时，“添加引用”对话框分别引用 net2.0 或 net3.5 文件夹中的 Aspose.Cells.dll 文件。 （要进一步参考，请阅读 Referencing Aspose.Cells from a .NET project。）您可以根据您的环境更改对库的引用。请注意，如果项目的目标框架是 .NET Framework 3.5/4 Client Profile，请使用位于 net_ClientProfile 文件夹中的 Aspose.Cells.dll 组件文件。

{{% /alert %}}
