---
title: Speichern Sie ODS Dateien in den Spezifikationen ODF 1.1, 1.2 und 1.3
type: docs
weight: 170
url: /de/java/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Speichern (**OpenDocument Spreadsheet**) ODS-Dateien im (**OpenDocument Format**) ODF 1.1, 1.2 und ODF 1.3 Spezifikationen. Aspose.Cells hat die [**OdsSaveOptions.setOdfStrictVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/odssaveoptions/#setOdfStrictVersion-int-) Eigenschaft hinzugefügt, um die ODF-Version zum Speichern von ODS-Dateien zu verwenden. Der Standardwert dieser Eigenschaft ist [**OpenDocumentFormatVersionType.ODF_12**](https://reference.aspose.com/cells/java/com.aspose.cells/opendocumentformatversiontype/#ODF-12), sodass eine ODS-Datei, die ohne diese Sonder-Einstellungen gespeichert wird, die Spezifikation 1.2 verwendet.

{{% /alert %}}

Das folgende Beispielcode erstellt das Arbeitsbuch-Objekt, fügt einen Wert in Zelle A1 des ersten Arbeitsblatts hinzu und speichert dann die ODS-Datei in den Spezifikationen ODF 1.1 und 1.2. Standardmäßig wird die ODS-Datei in der ODF 1.2-Spezifikation gespeichert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveODSfile-SaveODSfile.java" >}}
{{< app/cells/assistant language="java" >}}
