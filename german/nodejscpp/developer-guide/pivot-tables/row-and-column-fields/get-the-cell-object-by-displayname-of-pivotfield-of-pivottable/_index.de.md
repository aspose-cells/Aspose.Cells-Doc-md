---
title: Abrufen des Zellenobjekts nach Anzeigenamen des PivotField der Pivot Tabelle
type: docs
weight: 70
url: /de/nodejs-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Wie man die Zellenobjekt mit der DisplayName eines PivotField eines PivotTable mit Aspose.Cells for Node.js via C++ erhält.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js Bibliothek, Das Cell Objekt anhand des DisplayName des PivotField eines PivotTable mit Aspose.Cells for Node.js via C++ abrufen.
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ bietet die [**PivotTable.getCellByDisplayName(string)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getCellByDisplayName-string-)-Methode, mit der Sie auf das Zellobjekt anhand des Anzeigenamens des Pivot-Feldes zugreifen können. Diese Methode ist nützlich, wenn Sie den Kopfbereich des Pivot-Felds hervorheben oder formatieren möchten. Dieser Artikel erklärt, wie Sie das Zell-Objekt anhand des Anzeigenamens des Datenfeldes abrufen und dann eine Formatierung anwenden.

{{% /alert %}}

## **Wie man das Zellenobjekt anhand des Anzeigenamens des PivotField der PivotTable erhält**

Der folgende Code greift auf die erste Pivot-Tabelle des Arbeitsblatts zu und ruft dann die Zelle über den Anzeigenamen des zweiten Datenfelds der Pivot-Tabelle ab. Ehe ändert er die Füllfarbe und Schriftfarbe der Zelle jeweils in Hellblau und Schwarz. Unten sind Screenshots, die zeigen, wie die Pivot-Tabelle vor und nach der Ausführung des Codes aussieht.

|**Pivot-Tabelle - Vorher**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GetCellByDisplayName-GetCellObjectByDisplayName.js" >}}

|**Pivot-Tabelle - Nachher**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="nodejs-cpp" >}}
