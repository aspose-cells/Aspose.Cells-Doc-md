---
title: 区切り記号
type: docs
weight: 20
url: /ja/reportingservices/delimiters/
---
Aspose.Cells for Reporting Services は、TXT または CSV 形式をレンダリングするときに指定された区切り文字をサポートします。 2 つの設定で、Aspose.Cells for Reporting Services のフィールド区切り文字を制御します。

1. のフィールド区切り文字パラメーター**rsreportserver.config**指定された表示拡張機能のみを制御できます。

{{< highlight "java" >}}

 <Extension Name="ACTXT" Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer,Aspose.Cells.ReportingServices" >

<Configuration>

<DeviceInfo>

<FieldDelimiter>,</FieldDelimiter>

</DeviceInfo>

</Configuration>

</Extension>

Specified field delimiters configuration reference:

----blank delimiter

<Extension Name="ACTXT" Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer,Aspose.Cells.ReportingServices" >

<Configuration>

<DeviceInfo>

<FieldDelimiter>blank</FieldDelimiter>

</DeviceInfo>

</Configuration>

</Extension>

---- tab delimiter

<Extension Name="ACTXT" Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer,Aspose.Cells.ReportingServices" >

<Configuration>

<DeviceInfo>

<FieldDelimiter>tab</FieldDelimiter>

</DeviceInfo>

</Configuration>

</Extension>


{{< /highlight >}}




1. のフィールド区切り文字パラメーター**Aspose.Cells.ReportingServices.xml**すべての TXT タイプのレンダリング拡張機能を制御できます。

{{< highlight "java" >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

のフィールド区切り文字パラメーター**rsreportserver.config**のフィールド区切り文字パラメーターよりも優先されます。**Aspose.Cells.ReportingServices.xml**.フィールド区切りパラメータが**rsreportserver.config**null またはデフォルト値、フィールド区切り文字パラメータ**Aspose.Cells.ReportingServices.xml**使用されている。
