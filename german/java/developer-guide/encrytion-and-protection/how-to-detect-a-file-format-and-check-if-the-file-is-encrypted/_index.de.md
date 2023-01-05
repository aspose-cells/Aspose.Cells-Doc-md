---
title: So erkennen Sie ein Dateiformat und prüfen, ob die Datei verschlüsselt ist
type: docs
weight: 2000
url: /de/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 Manchmal müssen Sie das Format einer Datei erkennen, bevor Sie sie öffnen, da die Dateierweiterung nicht garantiert, dass der Dateiinhalt angemessen ist. Die Datei ist möglicherweise verschlüsselt (eine passwortgeschützte Datei), sodass sie nicht direkt gelesen werden kann, oder wir sollten sie nicht lesen. Aspose.Cells bietet die[**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat(java.io.InputStream)statische Methode und einige relevante APIs, die Sie zum Verarbeiten von Dokumenten verwenden können.

{{% /alert %}}

## **Java-Code zum Erkennen des Dateiformats und zum Überprüfen, ob die Datei verschlüsselt ist**

Der folgende Beispielcode veranschaulicht, wie ein Dateiformat (unter Verwendung des Dateipfads) erkannt und seine Erweiterung überprüft wird. Sie können auch feststellen, ob die Datei verschlüsselt ist.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
