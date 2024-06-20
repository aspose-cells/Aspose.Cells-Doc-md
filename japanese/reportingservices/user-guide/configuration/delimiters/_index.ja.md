---
title: デリミタ
type: docs
weight: 20
url: /ja/reportingservices/delimiters/
---

Aspose.Cells for Reporting Services は TXT や CSV フォーマットでの指定されたデリミタのサポートを提供します。Aspose.Cells for Reporting Services では、2つの設定が Aspose.Cells for Reporting Services のフィールドデリミタを制御します。

1. **rsreportserver.config** のフィールドデリミタパラメータは特定のレンダリング拡張子を制御できます。 

{{< highlight java >}}

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




1. **Aspose.Cells.ReportingServices.xml** のフィールドデリミタパラメータはすべての TXT 型のレンダリング拡張子を制御できます。 

{{< highlight java >}}



<CSVRender Mode="Default">

    <encode value="Default"/>

    <Delimiters value=","/>

    <RenderTableList value ="False"/>

    <report name="" Mode="" encode="" Delimiters="" RenderTableList=""/>

    <NoOutPutIsValid ALL="False"/>

  </CSVRender>


{{< /highlight >}}

**rsreportserver.config**のフィールド区切り記号パラメーターは、**Aspose.Cells.ReportingServices.xml**のフィールド区切り記号パラメーターよりも優先されます。**rsreportserver.config**のフィールド区切り記号パラメーターがnullまたはデフォルト値の場合、**Aspose.Cells.ReportingServices.xml**のフィールド区切り記号パラメーターが使用されます。
