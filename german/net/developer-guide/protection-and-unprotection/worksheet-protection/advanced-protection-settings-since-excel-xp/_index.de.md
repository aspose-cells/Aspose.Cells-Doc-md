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

Diese Schutzeinstellungen beschränken oder erlauben Benutzern Folgendes:

- Zeilen oder Spalten löschen.
- Bearbeiten Sie Inhalte, Objekte oder Szenarien.
- Zellen, Zeilen oder Spalten formatieren.
- Zeilen, Spalten oder Hyperlinks einfügen.
- Wählen Sie gesperrte oder entsperrte Zellen aus.
- Verwenden Sie Pivot-Tabellen und vieles mehr.

Aspose.Cells unterstützt alle erweiterten Schutzeinstellungen, die von Excel XP oder späteren Versionen angeboten werden.

### **Erweiterte Schutzeinstellungen mit Excel XP und späteren Versionen**

So zeigen Sie die in Excel XP verfügbaren Schutzeinstellungen an:

1.  Von dem**Werkzeug** Menü, auswählen**Schutz** gefolgt von**Schutzblatt**. Ein Dialogfeld wird angezeigt.

So zeigen Sie die in Excel 2016 verfügbaren Schutzeinstellungen an

1.  Von dem**Datei** Menü, auswählen**Arbeitsmappe schützen** gefolgt von**Aktuelles Blatt schützen**.
1.  Wähle aus**Schutzblatt** in dem**Überprüfung** Speisekarte.

Wenn Sie den oben genannten Schritten folgen, wird ein Dialogfeld angezeigt, in dem Sie Arbeitsblattfunktionen zulassen oder einschränken oder ein Kennwort auf das Arbeitsblatt anwenden können.

### **Erweiterte Schutzeinstellungen mit Aspose.Cells**

Aspose.Cells unterstützt alle erweiterten Schutzeinstellungen.

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse.

 Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet die[**Schutz**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) -Eigenschaft, die zum Anwenden dieser erweiterten Schutzeinstellungen verwendet wird. Das[**Schutz**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) Eigentum ist in der Tat ein Objekt der[**Schutz**](https://reference.aspose.com/cells/net/aspose.cells/protection)Klasse, die mehrere boolesche Eigenschaften zum Deaktivieren oder Aktivieren von Einschränkungen kapselt.

Unten ist eine kleine Beispielanwendung. Es öffnet eine Excel-Datei und verwendet die meisten erweiterten Schutzeinstellungen, die von Excel XP und späteren Versionen unterstützt werden.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

 Bitte nicht anrufen[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse'[**Beschützen**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) Methode bei Verwendung der[**Schutz**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)Eigentum. Speichern Sie die Datei außerdem im Excel97To2003- oder Xlsx-Format, da die erweiterten Schutzeinstellungen nur von Excel XP und höheren Versionen unterstützt werden.

{{% /alert %}}

### **Cell Sperrproblem**

Wenn Sie verhindern möchten, dass Benutzer Zellen bearbeiten, müssen die Zellen gesperrt werden, bevor Schutzeinstellungen angewendet werden. Andernfalls können die Zellen auch dann bearbeitet werden, wenn das Arbeitsblatt geschützt ist. In Microsoft Excel XP können Zellen über den folgenden Dialog gesperrt werden:

|**Dialog zum Sperren von Zellen in Excel XP**|
|:- |
|![todo: Bild_alt_Text](advanced-protection-settings-since-excel-xp_1.png)|

Es ist auch möglich, Zellen unter der Nummer Aspose.Cells API zu sperren. Jede Zelle kann bekommen[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Formatierung, die eine boolesche Eigenschaft enthält,[**Ist gesperrt**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Stellen Sie die ein[**Ist gesperrt**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) Eigentum zu**wahr** oder**FALSCH** um die Zelle zu sperren oder zu entsperren.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
