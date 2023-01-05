---
title: 実行時エラー 429
type: docs
weight: 60
url: /ja/reportingservices/runtime-error-429/
---
##### **説明**
実行時エラー: '429'
 ActiveX コンポーネントはオブジェクトを作成できません
エラーの原因となっている行は次のとおりです。
 AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient") を設定します。
##### **解決**
{{% alert color="primary" %}} 

再登録**Aspose.Cells.ReportingServices.Client.dll**を使用して**Regasm.exe**効用：

1. cmd.exe を管理者として実行します。
1. cd $(Aspose.Cells for Reporting Services インストール フォルダー)。
1. 実行する**regasm.exe**登録するために**Aspose.Cells.ReportingServices.Client.dll**手動で。

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

システムの実行環境を確認してください。例えば：

-  Microsoft Office が x64 の場合は、次のコマンドを実行します

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

- Microsoft Office が x86 の場合は、次のコマンドを実行します

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

次の例/コマンドを参照してください。

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
