---
title: Wie man ein Dateiformat erkennt und überprüft, ob die Datei verschlüsselt ist
type: docs
weight: 2000
url: /de/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

Manchmal müssen Sie das Format einer Datei erkennen, bevor Sie sie öffnen, weil die Dateierweiterung nicht garantiert, dass der Dateiinhalt geeignet ist. Die Datei könnte verschlüsselt sein (eine passwortgeschützte Datei), sodass sie nicht direkt gelesen werden kann, oder wir sollten sie nicht lesen. Aspose.Cells bietet die statische Methode [**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat-java.io.InputStream-) und einige relevante APIs, die Sie zum Verarbeiten von Dokumenten verwenden können.

{{% /alert %}}

## **Java-Code zum Erkennen des Dateiformats und Überprüfen, ob die Datei verschlüsselt ist**

Der folgende Beispielcode veranschaulicht, wie man ein Dateiformat (unter Verwendung des Dateipfads) erkennt und ihre Erweiterung überprüft. Sie können auch feststellen, ob die Datei verschlüsselt ist.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
{{< app/cells/assistant language="java" >}}
