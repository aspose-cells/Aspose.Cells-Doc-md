---
title: Überprüfen Sie die Versionsnummer
type: docs
weight: 80
url: /de/python-net/check-version-number/
---
{{% alert color="primary" %}}

Fragen Sie sich, welche Version von Aspose.Cells Sie verwenden? Wir veröffentlichen regelmäßig neue Versionen von Aspose.Cells, sowohl um neue Funktionen einzuführen als auch um Probleme zu beheben. Die Versionsnummer besteht aus der Hauptversionsnummer, der Nebenversionsnummer und der Hotfix-Versionsnummer. Jede Zahl muss eine ganze Zahl von 0 aufwärts sein. Das Format ist wie folgt:

Haupt.Neben.Hotfix

Wenn wir einen neuen Build von Aspose.Cells veröffentlichen, aktualisieren wir die Versionsnummer.

In diesem Artikel wird erläutert, wie Sie manuell und mithilfe der Aspose.Cells API überprüfen können, welche Version von Aspose.Cells auf dem System installiert ist.

{{% /alert %}}

## **Überprüfen Sie die Versionsnummer manuell**

So finden Sie manuell heraus, welche Version von Aspose.Cells Sie verwenden:

1.  Klicken Sie mit der rechten Maustaste auf die Datei Aspose.Cells.dll und wählen Sie sie aus**Eigenschaften**.
1. Klicken Sie auf die Registerkarte Version (oder Details), um die Versionsnummer zu überprüfen.

## **Überprüfen Sie die Versionsnummer mit Aspose.Cells API**

Um herauszufinden, welche Version von Aspose.Cells Sie über API verwenden, verwenden Sie die statische GetVersion-Methode der CellsHelper-Klasse, um die Versionsnummer von Aspose.Cell abzurufen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CheckVersionNumber.py" >}}
