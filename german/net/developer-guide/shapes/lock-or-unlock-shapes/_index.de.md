---
title: Formen sperren oder freigeben
linktitle: Formen sperren oder freigeben
type: docs
weight: 200
url: /de/net/lock-or-unlock-shapes/
description: Dieser Artikel zeigt Code, der erklärt, wie man Formen sperrt oder entsperrt, um sie mit der Aspose.Cells Bibliothek zu schützen.
keywords: C# Formen sperren, um sie zu schützen, wie man Formen in C# sperrt oder entsperrt.
---

## **Mögliche Verwendungsszenarien**

Manchmal müssen Sie alle Formen in bestimmten Tabellenblättern schützen, um zu verhindern, dass sie durch unerwünschte Situationen zerstört werden. In diesem Fall müssen Sie alle Formen im angegebenen Tabellenblatt sperren. 

Das Sperren von Formen in einer Tabelle oder einem Dokument kann aus mehreren Gründen vorteilhaft sein:
1. Vermeidung versehentlicher Änderungen: Das Sperren von Formen stellt sicher, dass sie nicht versehentlich verschoben, in der Größe verändert oder gelöscht werden. Besonders in komplexen Dokumenten, in denen Formen für Anmerkungen, Illustrationen oder als Teil des Designs verwendet werden.
1. Layout und Design beibehalten: Formen spielen oft eine entscheidende Rolle im Layout und der visuellen Gestaltung eines Dokuments. Das Sperren bewahrt das beabsichtigte Erscheinungsbild und sorgt dafür, dass das Dokument professionell und visuell ansprechend bleibt.
1. Datenintegrität: In Tabellen können Formen verwendet werden, um wichtige Datenpunkte hervorzuheben, Kommentare hinzuzufügen oder visuelle Erklärungen zu liefern. Das Sperren dieser Formen stellt sicher, dass die kontextbezogenen Informationen richtig und intakt bleiben.
1. Konsistenz bei gemeinsam genutzten Dokumenten: Bei der Zusammenarbeit an Dokumenten haben verschiedene Benutzer unterschiedliche Fachkenntnisse. Das Sperren von Formen hilft, die Konsistenz im gesamten Dokument zu wahren, indem unbeabsichtigte Änderungen verhindert werden.
1. Sicherheit: In sensiblen Dokumenten kann das Sperren von Formen ein Teil einer umfassenderen Strategie zum Schutz von Informationen sein. Beispielsweise in Finanzberichten oder rechtlichen Dokumenten, wo gesperrte Formen verwendet werden können, um bestimmte Anmerkungen oder Hervorhebungen zu sichern, die kritischen Kontext liefern.

Manchmal müssen Sie in bestimmten geschützten Arbeitsblättern bestimmte Formen bearbeiten können, in diesem Fall müssen Sie diese Formen entsperren. Dieser Artikel wird detailliert erklären, wie man bestimmte Formen sperrt und entsperrt.

## **Wie sperrt man Formen in Excel zum Schutz**

So sperren Sie Zellen in Microsoft Excel:

1. Öffnen Sie Ihre Excel-Datei: Öffnen Sie die Excel-Datei, die die Formen enthält, die Sie sperren möchten.

1. Wählen Sie die Form aus: Klicken Sie auf die Form, die Sie sperren möchten. Sie können auch mehrere Formen auswählen, indem Sie die Strg-Taste gedrückt halten und auf jede Form klicken.

1. Öffnen Sie das Formatieren-Formen-Paneel: Klicken Sie mit der rechten Maustaste auf die ausgewählte(n) Form(en) und wählen Sie „Größe und Eigenschaften“. Alternativ können Sie im Ribbon auf die Registerkarte „Format“ gehen und in der Gruppe „Größe“ den Dialogstarter (kleiner Pfeil) anklicken, um das „Form formatieren“-Fenster zu öffnen.
1. Sperren Sie die Form: Im „Form formatieren“-Paneel gehen Sie auf die Registerkarte „Größe & Eigenschaften“ (das Symbol sieht aus wie ein Quadrat mit Pfeilen). Unter dem Abschnitt „Eigenschaften“ setzen Sie das Häkchen bei „Gesperrt“.
<br>
<img src="1.png" width=60% />
1. Arbeitsblatt schützen: Gehen Sie auf die Registerkarte "Überprüfen" im Menüband. Klicken Sie auf "Blatt schützen". Legen Sie ein Passwort fest (optional) und wählen Sie die Berechtigungen, die Sie zulassen möchten (z. B. geschützte Zellen auswählen, Zellen formatieren usw.). Klicken Sie auf "OK."
<br>
<img src="2.png" width=60% />

## **So sperren Sie alle Formen in einem bestimmten Arbeitsblatt**

Um alle Formen in einem angegebenen Arbeitsblatt zu schützen, verwenden Sie die Methode [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect), wie im folgenden Beispielcode gezeigt.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **So entsperren Sie bestimmte Formen in einem geschützten Arbeitsblatt**

Um eine bestimmte Form in einem geschützten Arbeitsblatt zu entsperren, verwenden Sie [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), wie im folgenden Beispielcode gezeigt.

Hinweis: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) ist nur sinnvoll, wenn das Arbeitsblatt geschützt ist.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

{{< app/cells/assistant language="csharp" >}}
