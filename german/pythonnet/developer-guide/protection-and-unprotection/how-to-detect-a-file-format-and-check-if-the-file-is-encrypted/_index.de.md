---
title: Wie man ein Dateiformat erkennt und überprüft, ob die Datei verschlüsselt ist
type: docs
weight: 2700
url: /de/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

Manchmal muss man das Format einer Datei erkennen, bevor man sie öffnet, da die Dateierweiterung nicht garantiert, dass der Inhalt der Datei geeignet ist. Die Datei könnte verschlüsselt sein (passwortgeschützt), sodass sie nicht direkt gelesen werden kann, oder wir sollten sie nicht lesen. Aspose.Cells für Python via .NET bietet die statische Methode [**FileFormatUtil.detect_file_format()**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/detect_file_format) und andere relevante APIs, die Sie zum Verarbeiten von Dokumenten verwenden können.

{{% /alert %}}

Der folgende Beispielcode veranschaulicht, wie man ein Dateiformat (unter Verwendung des Dateipfads) erkennt und ihre Erweiterung überprüft. Sie können auch feststellen, ob die Datei verschlüsselt ist.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DetectFileFormatAndEncryption.py" >}}

{{< app/cells/assistant language="python-net" >}}
