---
title: Kopieren Sie ein Arbeitsblatt
type: docs
weight: 50
url: /de/net/copy-a-worksheet/
---
{{% alert color="primary" %}} 

[Arbeitsblätter hinzufügen](/cells/de/net/add-worksheets/) beschreibt, wie man neue Arbeitsblätter zu Aspose.Cells.GridWeb hinzufügt. Es ist auch möglich, dem Aspose.Cells.GridWeb-Steuerelement eine Kopie (oder ein Replikat) eines anderen Arbeitsblatts hinzuzufügen. Diese Funktion kann nützlich sein, wenn identische oder ähnliche Daten in einem Arbeitsblatt auch in einem anderen Arbeitsblatt benötigt werden. In diesem Fall ist es einfacher, ein vorhandenes Arbeitsblatt zu kopieren und es als neues Arbeitsblatt zu Aspose.Cells.GridWeb hinzuzufügen, anstatt es von Grund auf neu zu erstellen.

{{% /alert %}} 
## **Kopieren eines Arbeitsblatts**
### **Blattindex verwenden**
Der folgende Beispielcode zeigt, wie dem GridWeb-Steuerelement eine Kopie eines Arbeitsblatts hinzugefügt wird, indem der Index des Arbeitsblatts in der AddCopy-Methode der GridWorksheetCollection angegeben wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingIndex.cs" >}}
### **Blattname verwenden**
Der folgende Beispielcode zeigt, wie dem GridWeb-Steuerelement eine Kopie eines Arbeitsblatts hinzugefügt wird, indem der Name des Arbeitsblatts in der AddCopy-Methode der GridWorksheetCollection angegeben wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-CopyWorksheets.aspx-CopyWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

 Die Methode AddCopy gibt den Index des neu hinzugefügten Arbeitsblatts zurück, der für den Zugriff auf die Arbeitsblattinstanz verwendet werden kann. Weitere Informationen zum Zugriff auf Arbeitsblätter finden Sie unter[Greifen Sie auf Arbeitsblätter zu](/cells/de/net/access-worksheets/).

{{% /alert %}}
