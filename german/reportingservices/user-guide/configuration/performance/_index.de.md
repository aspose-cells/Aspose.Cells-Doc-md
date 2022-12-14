---
title: Leistung
type: docs
weight: 30
url: /de/reportingservices/performance/
---
 Um die Leistung zu verbessern, stellen Sie den Performance-Parameter auf ein**AN**.

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="False">

    <Report name="">

    <AutoRowFit value="True"/>

    <SetStyle value="True"/>

    <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}

Die verschiedenen Leistungsparameter sind wie folgt:

- **LimitCellsNumberForMerged** : die maximale Anzahl von Zellen, die zusammengeführt werden können. Der Standardwert 1.000.000. Der Parameterwert wird vom Benutzer eingestellt und wird nicht durch den Leistungsparameterschalter beeinflusst.

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit** : Wenn der Wert der Leistung ist**aus** , ist der Wert von IsAutoRowFit**FALSCH**standardmäßig. Wenn der Wert des Leistungsparameters ist**an** , der Wert ist**Stimmt** standardmäßig. Wenn der Wert der Leistung ist**an** , kann ein Unterelementbericht den Punktbericht auf den AutoRowFit-Wert zurücksetzen.

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="Test">

      <AutoRowFit value="False"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **IsMerged** : Wenn der Wert der Leistung ist**aus** , IsMerged-Standardwert ist**FALSCH** . Wenn der Wert der Leistung ist**an** , der Standardwert ist**Stimmt** . Wenn der Wert Performance-Parameter ist**an** , kann ein Unterelementbericht den Punktbericht auf den AutoRowFit-Wert zurücksetzen.

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="False"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **IsSetStyle** : Wenn der Wert der Leistung ist**aus** , der Standardwert ist**FALSCH** . Wenn Leistung ist**an** , der Standardwert ist**Stimmt** . Auch bei der Leistung**an** , kann ein Unterelementbericht den Punktbericht auf den AutoRowFit-Wert zurücksetzen.

{{< highlight "java" >}}

   <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="False"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **IsConditionalFormatting** : Wenn Leistung ist**aus** , der Standardwert ist**FALSCH** . Wenn Leistung ist**an** , der Standardwert ist**Stimmt** . Auch bei der Leistung**an** , kann ein Unterelementbericht den Punktbericht auf den AutoRowFit-Wert zurücksetzen. Wenn der IsSetStyle-Parameterwert auf festgelegt ist**FALSCH** , ist der Wert der Leistung ungültig.

{{< highlight "java" >}}

   <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="False"/>

      </Report>

   </Performance>

{{< /highlight >}}
