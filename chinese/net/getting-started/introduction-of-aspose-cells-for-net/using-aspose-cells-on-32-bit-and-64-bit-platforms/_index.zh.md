---
title: 在 32 位和 64 位平台上使用 Aspose.Cells
type: docs
weight: 10
url: /zh/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---

{{% alert color="primary" %}} 

Aspose.Cells 是纯 .NET 组件，可以通过 XCOPY 部署简化部署流程。要安装 Aspose.Cells，只需将组件程序集 (Aspose.Cells.dll) 复制到应用程序的目录中：应用程序可以立即开始使用它。这是因为 .NET 组件的自描述性质所致。这种部署方式也不会对安装过程造成任何影响。

{{% /alert %}} 
## **部署**
Aspose.Cells支持32位和64位环境。使用Aspose.Cells MSI安装程序安装Aspose.Cells for .NET组件时，将不同的DLL添加到Aspose.Cells ${installation_Path}文件夹的不同文件夹中。请查看表中的描述，找出包含您需要与特定版本的.NET Framework一起使用的程序集的文件夹。

|**文件夹**|**描述**|
| :- | :- |
|net2.0| 包含用于 .NET Framework 2.0、3.0、3.5、4.0 和 Mono 的程序集。这些通常是你应该在 32 位和 64 位环境中使用的程序集。|
|net2.0_AuthenticodeSigned| 与上述相同，但这些程序集经过 Authenticode 数字签名。经过签名的程序集可能比没有经过 Authenticode 的加载速度慢。|
|net3.5_ClientProfile| 包含用于 .NET Framework 3.5 或 4.0 客户端配置文件的程序集。|
|net3.5_ClientProfile_AuthenticodeSigned| 与上述相同，但这些程序集经过 Authenticode 数字签名。经过签名的程序集可能比没有经过 Authenticode 的加载速度慢。|
|net3.5| 包含用于 .NET Framework 3.5 或 4.0 的程序集。|
|net3.5_AuthenticodeSigned| 与上述相同，但这些程序集经过 Authenticode 数字签名。经过签名的程序集可能比没有经过 Authenticode 的加载速度慢。|
|net4.0|包含用于 .NET Framework 4.0 和 4.5 的程序集。|
|netStandard|包含用于 .Net Standard 2.0 的程序集|
|netcoreapp2.1|包含用于 .Net core 2.1 的程序集|
|Xamarin.iOS|包含用于 Xamarin.iOS 的程序集|
|Xamarin.Android|包含用于 Xamarin.Android 的程序集|
|net5.0|包含用于 .net5.0 的程序集。|
|net6.0|包含用于 .net6.0 的程序集。|
|net8.0|包含适用于.net8.0的程序集。|
|net9.0|包含适用于.net9.0的程序集。|

{{% alert color="primary" %}} 

在 VS.NET（例如：2005、2008、2010、2012 等）项目中，当向 Aspose.Cells 添加引用时，添加引用对话框会引用 net2.0 或 net3.5 文件夹中的 Aspose.Cells.dll 文件。（若需要进一步参考，请阅读《从 .NET 项目引用 Aspose.Cells》。）您可以根据您的环境更改对库的引用。请注意，如果项目的目标框架是 .NET Framework 3.5/4 Client Profile，请使用位于 net_ClientProfile 文件夹中的 Aspose.Cells.dll 组件文件。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
