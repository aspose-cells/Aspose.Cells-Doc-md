---
title: ランタイムエラー429
type: docs
weight: 60
url: /ja/reportingservices/runtime-error-429/
---

##### **説明**
実行時エラー: '429' 
ActiveXコンポーネントを作成できません 
エラーを引き起こしている行は: 
Set AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient"). 
##### **解決策**
{{% alert color="primary" %}} 

Regasm.exeユーティリティを使用して、『Aspose.Cells.ReportingServices.Client.dll』を再登録してください。 

1. 管理者としてcmd.exeを実行します。
1. cd $(Aspose.Cells for Reporting Services installation folder).
1. **Aspose.Cells.ReportingServices.Client.dll**を手動で登録するために**regasm.exe**を実行してください。 

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

システムの実行環境を確認してください。たとえば: 

- Microsoft Officeがx64の場合、次のコマンドを実行します 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

- Microsoft Officeがx86の場合、次のコマンドを実行します 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

次の例/コマンドを参照してください:

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
