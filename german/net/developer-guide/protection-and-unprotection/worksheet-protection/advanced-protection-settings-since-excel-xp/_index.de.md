---
title: Erweiterte Schutzeinstellungen seit Excel XP
type: docs
weight: 30
url: /de/net/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

Seit der Veröffentlichung von Excel 2002 oder XP hat Microsoft viele erweiterte Schutzeinstellungen hinzugefügt.

{{% /alert %}}

## **Einführung**

Diese Schutzeinstellungen beschränken oder erlauben Benutzern:

- Zeilen oder Spalten löschen.
- Inhalte, Objekte oder Szenarien bearbeiten.
- Zellen, Zeilen oder Spalten formatieren.
- Zeilen, Spalten oder Hyperlinks einfügen.
- Gesperrte oder ungesperrte Zellen auswählen.
- Pivot-Tabellen verwenden und vieles mehr.

Aspose.Cells unterstützt alle erweiterten Schutzeinstellungen, die von Excel XP oder späteren Versionen angeboten werden.

### **Erweiterte Schutzeinstellungen mit Excel XP und späteren Versionen verwenden**

Um die Schutzeinstellungen in Excel XP anzuzeigen:

1. Wählen Sie im **Extras**-Menü **Schutz** und danach **Arbeitsblatt schützen** aus. Es wird ein Dialogfeld angezeigt.

Um die Schutzeinstellungen in Excel 2016 anzuzeigen

1. Wählen Sie im **Datei**-Menü **Arbeitsmappe schützen** und danach **Aktuelles Blatt schützen** aus.
1. Wählen Sie **Arbeitsblatt schützen** im **Überprüfen**-Menü aus.

Durch das Befolgen der oben genannten Schritte wird ein Dialogfeld angezeigt, in dem Sie Arbeitsblattfunktionen zulassen oder einschränken oder ein Passwort auf das Arbeitsblatt anwenden können.

### **Erweiterte Schutzeinstellungen mit Aspose.Cells verwenden**

Aspose.Cells unterstützt alle erweiterten Schutzeinstellungen.

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), bereit, die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert.

Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) stellt die Eigenschaft [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) bereit, die verwendet wird, um diese erweiterten Schutzeinstellungen anzuwenden. Die Eigenschaft [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) ist tatsächlich ein Objekt der Klasse [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection), das mehrere boolesche Eigenschaften zur Deaktivierung oder Aktivierung von Einschränkungen umschließt.

Unten finden Sie eine kleine Beispielanwendung. Es öffnet eine Excel-Datei und verwendet die meisten von Excel XP und späteren Versionen unterstützten erweiterten Schutzeinstellungen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

Bitte rufen Sie die Methode [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) nicht auf, wenn Sie die Eigenschaft [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) verwenden. Speichern Sie die Datei auch im Excel97To2003- oder Xlsx-Format, da die erweiterten Schutzeinstellungen nur von Excel XP und späteren Versionen unterstützt werden.

{{% /alert %}}

### **Problem mit Zellsperre**

Wenn Sie Benutzer daran hindern möchten, Zellen zu bearbeiten, müssen die Zellen gesperrt werden, bevor irgendwelche Schutzeinstellungen angewendet werden. Andernfalls können die Zellen bearbeitet werden, auch wenn das Arbeitsblatt geschützt ist. In Microsoft Excel XP können Zellen durch den folgenden Dialog gesperrt werden:

|**Dialog zum Sperren von Zellen in Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Es ist auch möglich, Zellen mithilfe der Aspose.Cells-API zu sperren. Jede Zelle kann ein [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-Format erhalten, das eine boolesche Eigenschaft, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked), enthält. Setzen Sie die [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)-Eigenschaft auf **true** oder **false**, um die Zelle zu sperren oder zu entsperren.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
