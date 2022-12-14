---
title: Hinzufügen von Cell-Schutz im Arbeitsblatt
type: docs
weight: 130
url: /de/net/adding-cell-protection-in-worksheet/
---
{{% alert color="primary" %}} 

Aspose.Cells für GridDesktop ermöglicht es Ihnen, Ihre Zellen in einem Arbeitsblatt zu schützen. Sie müssen zuerst Ihr Arbeitsblatt schützen, dann können Sie Ihre gewünschten Zellen in einem Arbeitsblatt schützen. Um das Arbeitsblatt zu schützen, bitte einstellen**Arbeitsblatt.Geschützt** Eigenschaft auf true, dann verwenden**Arbeitsblatt.SetProtected()** Methode zum Schutz des Zellbereichs.

{{% /alert %}} 
## **Schützen Sie Cell mit Aspose.Cells.GridDesktop**
 Der folgende Beispielcode schützt alle Zellen im Bereich**A1:B1** des aktiven Arbeitsblatts von GridDesktop. Wenn Sie auf eine beliebige Zelle in diesem Bereich doppelklicken, können Sie sie nicht bearbeiten. Dadurch werden diese Zellen schreibgeschützt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
