---
title: Leistung
type: docs
weight: 30
url: /de/reportingservices/performance/
---

Um die Leistung zu verbessern, setzen Sie den Leistungsparameter auf **AN**.

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="False">

    <Report name="">

    <AutoRowFit value="True"/>

    <SetStyle value="True"/>

    <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}

Die verschiedenen Leistungsparameter lauten wie folgt:

- **LimitCellsNumberForMerged**: die maximale Anzahl von Zellen, die zusammengeführt werden können. Der Standardwert beträgt 1.000.000. Der Parameterwert wird vom Benutzer festgelegt und wird nicht vom Leistungsparameterschalter beeinflusst. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit**: Wenn der Wert von Leistung auf **aus** gesetzt ist, ist der Standardwert für IsAutoRowFit standardmäßig **falsch**. Wenn der Wert des Leistungsparameters **an** ist, ist der Wert standardmäßig **wahr**. Wenn der Wert des Leistungsparameters **an** ist, kann ein Unterelementbericht den Punktbericht auf den AutoRowFit-Wert zurücksetzen. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="Test">

      <AutoRowFit value="False"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **IsMerged**: Wenn der Wert von Leistung auf **aus** gesetzt ist, ist der Standardwert für IsMerged **falsch**. Wenn der Wert von Leistung auf **an** gesetzt wird, ist der Standardwert **wahr**. Wenn der Wert des Leistungsparameters **an** ist, kann ein Unterelementbericht den Punktbericht auf den AutoRowFit-Wert zurücksetzen. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="False"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **IsSetStyle**: Wenn der Wert von Leistung auf **aus** gesetzt ist, ist der Standardwert **falsch**. Wenn Leistung **an** ist, ist der Standardwert **wahr**. Auch wenn Leistung **an** ist, kann ein Unterelementbericht den Punktbericht auf den AutoRowFit-Wert zurücksetzen. 

{{< highlight java >}}

   <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="False"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **IsConditionalFormatting**: Wenn die Leistung **aus** ist, ist der Standardwert **falsch**. Ist die Leistung **an**, ist der Standardwert **wahr**. Zudem kann bei aktivierter Leistung ein untergeordneter Berichtselement den Punktbericht auf den Wert AutoRowFit zurücksetzen. Wenn der Parameterwert von IsSetStyle auf **falsch** gesetzt ist, ist der Wert von Performance ungültig. 

{{< highlight java >}}

   <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="False"/>

      </Report>

   </Performance>

{{< /highlight >}}
