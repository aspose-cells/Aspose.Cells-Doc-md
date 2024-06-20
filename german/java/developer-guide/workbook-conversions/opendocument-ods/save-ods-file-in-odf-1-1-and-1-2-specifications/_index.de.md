---
title: ODS Datei in ODF 1.1 und 1.2 Spezifikationen speichern
type: docs
weight: 170
url: /de/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Speichern von (**OpenDocument Spreadsheet**) ODS-Dateien in den Spezifikationen (**OpenDocument Format**) ODF 1.1 und ODF 1.2. Aspose.Cells hat die [**OdsSaveOptions.setStrictSchema11()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions#IsStrictSchema11)-Eigenschaft hinzugefügt, um die ODF 1.1-Spezifikation zur Speicherung von ODS-Dateien zu verwenden. Der Standardwert dieser Eigenschaft ist **false**, sodass ODS-Dateien ohne diese spezielle Einstellung die 1.2-Spezifikation verwenden.

{{% /alert %}}

Das folgende Beispielcode erstellt das Arbeitsbuch-Objekt, fügt einen Wert in Zelle A1 des ersten Arbeitsblatts hinzu und speichert dann die ODS-Datei in den Spezifikationen ODF 1.1 und 1.2. Standardmäßig wird die ODS-Datei in der ODF 1.2-Spezifikation gespeichert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
