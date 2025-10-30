---
title: Versionsnummer überprüfen
type: docs
weight: 80
url: /de/python-net/check-version-number/
---

{{% alert color="primary" %}}

Sie fragen sich, welche Version von Aspose.Cells Sie verwenden? Wir veröffentlichen regelmäßig neue Versionen von Aspose.Cells, sowohl um neue Funktionen einzuführen als auch um Probleme zu beheben. Die Versionsnummer besteht aus der Hauptversionsnummer, der Nebenversionsnummer und der Hotfix-Versionsnummer. Jede Nummer muss eine ganze Zahl von 0 nach oben sein. Das Format ist wie folgt:

major.minor.hotfix

Wenn wir eine neue Version von Aspose.Cells veröffentlichen, aktualisieren wir die Versionsnummer.

Dieser Artikel erklärt, wie Sie manuell überprüfen können, welche Version von Aspose.Cells auf dem System installiert ist, und wie Sie die Aspose.Cells-API verwenden.

{{% /alert %}}

## **Versionsnummer manuell überprüfen**

Um manuell herauszufinden, welche Version von Aspose.Cells Sie verwenden:

1. Klicken Sie mit der rechten Maustaste auf die Datei Aspose.Cells.dll und wählen Sie **Eigenschaften**.
1. Klicken Sie auf die Version (oder Details) Registerkarte, um die Versionsnummer zu überprüfen.

## **Versionsnummer mit der Aspose.Cells API überprüfen**

Um herauszufinden, welche Version von Aspose.Cells Sie über die API verwenden, verwenden Sie die GetVersion-Statikmethode der CellsHelper-Klasse, um die Versionsnummer von Aspose.Cell zu erhalten.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CheckVersionNumber.py" >}}
{{< app/cells/assistant language="python-net" >}}
