---
title: So erkennen Sie ein Dateiformat und prüfen, ob die Datei verschlüsselt ist
type: docs
weight: 2700
url: /de/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 Manchmal müssen Sie das Format einer Datei erkennen, bevor Sie sie öffnen, da die Dateierweiterung nicht garantiert, dass der Dateiinhalt angemessen ist. Die Datei ist möglicherweise verschlüsselt (eine passwortgeschützte Datei), sodass sie nicht direkt gelesen werden kann, oder wir sollten sie nicht lesen. Aspose.Cells bietet die[**FileFormatUtil.DetectFileFormat()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) statische Methode und einige relevante APIs, die Sie zum Verarbeiten von Dokumenten verwenden können.

{{% /alert %}}

Der folgende Beispielcode veranschaulicht, wie ein Dateiformat (unter Verwendung des Dateipfads) erkannt und seine Erweiterung überprüft wird. Sie können auch feststellen, ob die Datei verschlüsselt ist.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
